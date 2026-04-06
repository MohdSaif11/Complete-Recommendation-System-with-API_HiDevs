from flask import Flask, request, jsonify
from data.models import create_tables
from data.repositories import ContentRepository, InteractionRepository
from engine.orchestrator import RecommendationOrchestrator
import uuid, time

app = Flask(__name__)
create_tables()

# repos
content_repo = ContentRepository()
interaction_repo = InteractionRepository()

# engine
engine = RecommendationOrchestrator(content_repo, interaction_repo)


# ✅ HOME ROUTE (fix 404)
@app.route("/")
def home():
    return jsonify({
        "message": "Recommendation API is running 🚀",
        "endpoints": {
            "health": "/health",
            "recommend": "/recommend/<user_id>",
            "feedback": "/feedback",
            "metrics": "/metrics"
        }
    })


# ✅ HEALTH
@app.route("/health")
def health():
    return jsonify({"status": "ok"})


# ✅ RECOMMEND
@app.route("/recommend/<user_id>")
def recommend(user_id):
    req_id = str(uuid.uuid4())
    start = time.time()

    try:
        recs = engine.get_recommendations(user_id)

        print(f"[{req_id}] user={user_id} time={round(time.time()-start,3)}s")

        return jsonify({
            "request_id": req_id,
            "user": user_id,
            "recommendations": recs
        })

    except Exception as e:
        return jsonify({
            "error": "Internal Server Error",
            "message": str(e)
        }), 500


# ✅ FEEDBACK (fix 405 + validation)
@app.route("/feedback", methods=["GET", "POST"])
def feedback():

    # allow browser testing
    if request.method == "GET":
        return jsonify({
            "message": "Use POST to submit feedback",
            "example": {
                "user_id": "u1",
                "content_id": "c10",
                "rating": 5
            }
        })

    data = request.get_json()

    # validation
    if not data or "user_id" not in data or "content_id" not in data:
        return jsonify({
            "error": "Bad Request",
            "message": "user_id and content_id required"
        }), 400

    try:
        interaction_repo.add(
            data["user_id"],
            data["content_id"],
            data.get("rating", 1)
        )

        return jsonify({"status": "feedback recorded"})

    except Exception as e:
        return jsonify({
            "error": "Failed to record feedback",
            "message": str(e)
        }), 500


# ✅ METRICS
@app.route("/metrics")
def metrics():
    avg_time = 0
    if engine.requests:
        avg_time = engine.total_time / engine.requests

    return jsonify({
        "total_requests": engine.requests,
        "avg_response_time": round(avg_time, 4)
    })


# RUN
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    
from flask import Flask, jsonify, request
from data.models import create_tables
from data.repositories import UserRepository, ContentRepository, InteractionRepository
from engine.orchestrator import RecommendationOrchestrator
import time

app = Flask(__name__)
create_tables()

user_repo = UserRepository()
content_repo = ContentRepository()
interaction_repo = InteractionRepository()

engine = RecommendationOrchestrator(user_repo, content_repo, interaction_repo)

# 🔥 ROOT FIX
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

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/recommend/<user_id>")
def recommend(user_id):
    start = time.time()

    recs = engine.get_recommendations(user_id)

    # 🔥 logging
    print(f"[LOG] user={user_id} time={round(time.time()-start,4)}s")

    return jsonify({
        "user": user_id,
        "recommendations": recs
    })

@app.route("/feedback", methods=["POST"])
def feedback():
    data = request.json

    if not data or "user_id" not in data or "content_id" not in data:
        return jsonify({"error": "Invalid request"}), 400

    interaction_repo.add_interaction(
        data["user_id"],
        data["content_id"],
        data.get("rating", 1)
    )

    return jsonify({"status": "recorded"})

# 🔥 METRICS ENDPOINT
@app.route("/metrics")
def metrics():
    avg_time = 0
    if engine.request_count:
        avg_time = engine.total_time / engine.request_count

    return jsonify({
        "total_requests": engine.request_count,
        "avg_response_time": round(avg_time, 4)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    
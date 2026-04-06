import time

class RecommendationOrchestrator:

    def __init__(self, content_repo, interaction_repo):
        self.content_repo = content_repo
        self.interaction_repo = interaction_repo
        self.cache = {}
        self.requests = 0
        self.total_time = 0

    def get_recommendations(self, user_id, limit=5):
        start = time.time()
        self.requests += 1

        if user_id in self.cache:
            return self.cache[user_id]

        history = self.interaction_repo.get_user_history(user_id)
        content = self.content_repo.get_all()

        if not history:
            result = [{"item": c[0], "reason": "popular item"} for c in content[:limit]]
            return result

        ranked = sorted(content, key=lambda x: x[1], reverse=True)

        result = []
        for c in ranked:
            if c[0] not in history:
                result.append({
                    "item": c[0],
                    "reason": "based on popularity + unseen"
                })

        self.total_time += (time.time() - start)
        self.cache[user_id] = result[:limit]

        return result[:limit]
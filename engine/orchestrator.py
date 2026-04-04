import time
from engine.candidate_gen import CandidateGenerator
from engine.scorer import RecommendationScorer

class RecommendationOrchestrator:

    def __init__(self, user_repo, content_repo, interaction_repo):
        self.user_repo = user_repo
        self.content_repo = content_repo
        self.interaction_repo = interaction_repo

        self.cache = {}

        # 🔥 metrics
        self.request_count = 0
        self.total_time = 0

    def get_recommendations(self, user_id, limit=5):
        start = time.time()
        self.request_count += 1

        # 🔥 cache
        if user_id in self.cache:
            return self.cache[user_id]

        history = self.interaction_repo.get_user_history(user_id)
        all_content = self.content_repo.get_all_content()

        # cold start
        if not history:
            result = all_content[:limit]
            self.cache[user_id] = result
            return result

        user_data = {user_id: history}
        item_data = {c: [] for c in all_content}

        cg = CandidateGenerator(user_data, item_data)
        candidates = cg.hybrid_candidates(user_id)

        scorer = RecommendationScorer()

        def relevance(u, item, ctx):
            return 1.0 if item not in history else 0

        def popularity(u, item, ctx):
            return 0.5

        scorer.add_scorer("relevance", relevance, 0.7)
        scorer.add_scorer("popularity", popularity, 0.3)

        ranked = scorer.rank_candidates(user_id, candidates, {}, limit)

        # 🔥 explanation added
        result = [
            {
                "item": item,
                "reason": "Recommended based on relevance and popularity"
            }
            for item, _, _ in ranked
        ]

        self.total_time += (time.time() - start)

        self.cache[user_id] = result
        return result
        
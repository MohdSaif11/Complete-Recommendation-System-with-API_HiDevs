class RecommendationScorer:

    def __init__(self):
        self.scorers = []

    def add_scorer(self, name, function, weight):
        self.scorers.append((name, function, weight))

    def calculate_score(self, user_id, item_id, context):
        total = 0
        total_weight = 0
        explanation = {}

        for name, func, weight in self.scorers:
            score = max(0, min(1, func(user_id, item_id, context)))
            explanation[name] = score

            total += score * weight
            total_weight += weight

        final_score = total / total_weight if total_weight else 0
        return final_score, explanation

    def rank_candidates(self, user_id, candidates, context, limit=10):
        scored_items = []

        for item in candidates:
            score, explanation = self.calculate_score(user_id, item, context)
            scored_items.append((item, score, explanation))

        scored_items.sort(key=lambda x: x[1], reverse=True)

        return scored_items[:limit]
import math

class RecommendationEvaluator:

    @staticmethod
    def precision_at_k(recs, relevant, k):
        recs_k = recs[:k]
        hits = sum(1 for item in recs_k if item in relevant)
        return hits / k if k else 0

    @staticmethod
    def recall_at_k(recs, relevant, k):
        if not relevant:
            return 0
        recs_k = recs[:k]
        hits = sum(1 for item in recs_k if item in relevant)
        return hits / len(relevant)

    @staticmethod
    def ndcg_at_k(recs, relevant, k):
        dcg = 0
        for i, item in enumerate(recs[:k]):
            if item in relevant:
                dcg += 1 / math.log2(i + 2)

        ideal = sum(1 / math.log2(i + 2) for i in range(min(len(relevant), k)))
        return dcg / ideal if ideal else 0

    def evaluate_all(self, rec_dict, gt_dict, k=5):
        p, r, n = [], [], []

        for user in rec_dict:
            if user not in gt_dict:
                continue

            recs = rec_dict[user]
            gt = gt_dict[user]

            p.append(self.precision_at_k(recs, gt, k))
            r.append(self.recall_at_k(recs, gt, k))
            n.append(self.ndcg_at_k(recs, gt, k))

        return {
            "precision": sum(p)/len(p) if p else 0,
            "recall": sum(r)/len(r) if r else 0,
            "ndcg": sum(n)/len(n) if n else 0
        }
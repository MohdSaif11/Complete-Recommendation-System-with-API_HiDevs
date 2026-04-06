import math

class RecommendationEvaluator:

    def precision_at_k(self, recs, relevant, k):
        recs = recs[:k]
        return len([r for r in recs if r in relevant]) / k

    def recall_at_k(self, recs, relevant, k):
        recs = recs[:k]
        return len([r for r in recs if r in relevant]) / len(relevant)

    def ndcg_at_k(self, recs, relevant, k):
        dcg = 0
        for i, r in enumerate(recs[:k]):
            if r in relevant:
                dcg += 1 / math.log2(i + 2)

        ideal = sum(1 / math.log2(i + 2) for i in range(min(len(relevant), k)))
        return dcg / ideal if ideal else 0

    def evaluate_all(self, recs_dict, gt_dict, k):
        p, r, n = [], [], []

        for user in recs_dict:
            recs = recs_dict[user]
            gt = gt_dict[user]

            p.append(self.precision_at_k(recs, gt, k))
            r.append(self.recall_at_k(recs, gt, k))
            n.append(self.ndcg_at_k(recs, gt, k))

        return {
            "precision": sum(p)/len(p),
            "recall": sum(r)/len(r),
            "ndcg": sum(n)/len(n)
        }
        
from engine.evaluator import RecommendationEvaluator

evaluator = RecommendationEvaluator()

recs = {"u1": ["c1", "c2", "c3"]}
gt = {"u1": ["c2", "c3"]}

metrics = evaluator.evaluate_all(recs, gt, k=3)
print(metrics)
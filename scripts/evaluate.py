from engine.evaluator import RecommendationEvaluator

eval = RecommendationEvaluator()

recs = {"u1":["c5","c6","c7","c8","c9"]}
gt = {"u1":["c5","c6","c7"]}

print(eval.evaluate_all(recs, gt, 5))


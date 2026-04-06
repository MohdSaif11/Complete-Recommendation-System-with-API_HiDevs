from engine.orchestrator import RecommendationOrchestrator
from data.repositories import ContentRepository, InteractionRepository

def test_engine():
    engine = RecommendationOrchestrator(ContentRepository(), InteractionRepository())
    recs = engine.get_recommendations("u1")
    assert isinstance(recs, list)

    
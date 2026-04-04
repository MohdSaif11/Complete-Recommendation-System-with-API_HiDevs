from data.repositories import UserRepository, ContentRepository, InteractionRepository
from engine.orchestrator import RecommendationOrchestrator

def test_recommendations():
    user_repo = UserRepository()
    content_repo = ContentRepository()
    interaction_repo = InteractionRepository()

    engine = RecommendationOrchestrator(user_repo, content_repo, interaction_repo)

    recs = engine.get_recommendations("u1")

    assert isinstance(recs, list)
    assert len(recs) >= 0

def test_cold_start():
    user_repo = UserRepository()
    content_repo = ContentRepository()
    interaction_repo = InteractionRepository()

    engine = RecommendationOrchestrator(user_repo, content_repo, interaction_repo)

    recs = engine.get_recommendations("new_user")

    assert isinstance(recs, list)
    
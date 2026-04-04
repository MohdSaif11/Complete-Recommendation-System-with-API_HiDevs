from data.models import create_tables
from data.repositories import UserRepository, ContentRepository, InteractionRepository

def test_database_setup():
    create_tables()
    user_repo = UserRepository()
    content_repo = ContentRepository()

    # basic check (no crash)
    assert user_repo is not None
    assert content_repo is not None

def test_interaction():
    interaction_repo = InteractionRepository()

    interaction_repo.add_interaction("u1", "c1", 5)
    history = interaction_repo.get_user_history("u1")

    assert isinstance(history, list)
    
from data.repositories import InteractionRepository

def test_add_and_fetch():
    repo = InteractionRepository()

    # insert
    repo.add("u1", "c10", 5)

    # fetch
    history = repo.get_user_history("u1")

    assert "c10" in history
    
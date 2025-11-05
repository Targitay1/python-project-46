"""Basic tests for Brain Games package."""
def test_import():
    """Test that package can be imported."""
    try:
        import brain_games
        assert True
    except ImportError:
        assert False, "Cannot import brain_games"

def test_cli_import():
    """Test that CLI module can be imported."""
    try:
        from brain_games.cli import welcome_user
        assert True
    except ImportError:
        assert False, "Cannot import welcome_user"

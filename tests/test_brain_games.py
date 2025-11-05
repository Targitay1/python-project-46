"""Basic tests for Brain Games."""
def test_import():
    """Test that package can be imported."""
    try:
        import brain_games
        assert True
    except ImportError:
        assert False, "Cannot import brain_games"

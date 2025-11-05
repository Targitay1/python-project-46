"""Basic tests for Brain Games package."""
import pytest
from brain_games.cli import welcome_user


def test_welcome_user(capsys):
    """Test welcome_user function."""
    welcome_user()
    captured = capsys.readouterr()
    assert "Welcome" in captured.out


def test_imports():
    """Test that all modules can be imported."""
    from brain_games.scripts import brain_games
    from brain_games.scripts import brain_even
    from brain_games.scripts import brain_calc
    from brain_games.scripts import brain_gcd
    from brain_games.scripts import brain_progression
    from brain_games.scripts import brain_prime
    assert brain_games is not None
    assert brain_even is not None
    assert brain_calc is not None
    assert brain_gcd is not None
    assert brain_progression is not None
    assert brain_prime is not None

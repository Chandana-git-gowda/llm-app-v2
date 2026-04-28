from unittest.mock import MagicMock
from app.llm import ask_llm


def test_llm_mock(monkeypatch):
    """Test that ask_llm returns the mocked response."""

    # Build fake response (same style as Assignment 1)
    mock_response = MagicMock()
    mock_response.content = [MagicMock()]
    mock_response.content[0].text = "mocked response"

    # Replace real API call with fake (using monkeypatch)
    monkeypatch.setattr(
        "app.llm.client.messages.create",
        lambda *args, **kwargs: mock_response
    )

  #verify
    result = ask_llm("Hello")
    assert result == "mocked response"
    assert isinstance(result, str)
    assert len(result) > 0


def test_llm_returns_string(monkeypatch):
    """Test that ask_llm always returns a string."""

    mock_response = MagicMock()
    mock_response.content = [MagicMock()]
    mock_response.content[0].text = "Python is a programming language"

    monkeypatch.setattr(
        "app.llm.client.messages.create",
        lambda *args, **kwargs: mock_response
    )

    result = ask_llm("What is Python?")
    assert isinstance(result, str)
    assert len(result) > 0
    assert result == "Python is a programming language"

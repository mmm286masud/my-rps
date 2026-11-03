"""Literal RPS rules and real request/result coverage for RPS-001."""

import pytest

import app as web
from game import determine_winner


@pytest.mark.unit
@pytest.mark.parametrize(
    ("player", "computer", "expected"),
    [
        ("rock", "rock", "tie"),
        ("rock", "paper", "lose"),
        ("rock", "scissors", "win"),
        ("paper", "rock", "win"),
        ("paper", "paper", "tie"),
        ("paper", "scissors", "lose"),
        ("scissors", "rock", "lose"),
        ("scissors", "paper", "win"),
        ("scissors", "scissors", "tie"),
    ],
)
def test_nine_outcomes(player, computer, expected):
    """Each valid pair has the literal result specified by the assignment."""
    assert determine_winner(player, computer) == expected


@pytest.mark.integration
def test_real_round_and_independent_replay(monkeypatch):
    """Real rules render a loss, then a win, without keeping the old round."""
    monkeypatch.setitem(web.app.config, "TESTING", True)
    monkeypatch.setattr(web.random, "choice", lambda _moves: "paper")
    with web.app.test_client() as client:
        initial = client.get("/")
        assert initial.status_code == 200
        assert b"game rules not built yet" not in initial.data
        assert b"data-outcome=" not in initial.data

        response = client.post("/", data={"move": "rock"})
        page = response.get_data(as_text=True)
        assert response.status_code == 200
        assert 'data-outcome="lose"' in page
        assert "Computer wins" in page
        assert '<p class="choice-value">Rock ' in page
        assert '<p class="choice-value">Paper ' in page
        assert "game rules not built yet" not in page

        response = client.post("/", data={"move": "scissors"})
        page = response.get_data(as_text=True)
        assert response.status_code == 200
        assert 'data-outcome="win"' in page
        assert "You win!" in page
        assert '<p class="choice-value">Scissors ' in page
        assert '<p class="choice-value">Paper ' in page
        assert '<p class="choice-value">Rock ' not in page
        assert 'data-outcome="lose"' not in page

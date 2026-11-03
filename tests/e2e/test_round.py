"""A real Chromium round and independent keyboard replay using real rules."""

import pytest
from playwright.sync_api import Page, expect

import app as web

pytestmark = pytest.mark.e2e


def test_round_and_keyboard_replay(page: Page, live_server, monkeypatch):
    """A loss, win, and tie each replace the previous displayed round."""
    monkeypatch.setattr(web.random, "choice", lambda _moves: "paper")
    page.goto(live_server)
    expect(page.get_by_role("heading", name="Your next move?")).to_be_visible()
    expect(page.get_by_role("status")).to_have_count(0)
    expect(page.locator("[data-outcome]")).to_have_count(0)

    page.get_by_role("button", name="Rock", exact=True).click()
    choices = page.get_by_label("This round’s choices")
    expect(choices.locator(".choice-value")).to_have_text(["Rock ✊", "Paper ✋"])
    expect(
        page.get_by_role("heading", name="Computer wins", exact=True)
    ).to_be_visible()
    expect(page.locator("[data-outcome]")).to_have_attribute("data-outcome", "lose")

    page.get_by_role("button", name="Rock", exact=True).focus()
    page.keyboard.press("Tab")
    expect(page.get_by_role("button", name="Paper", exact=True)).to_be_focused()
    page.keyboard.press("Tab")
    expect(page.get_by_role("button", name="Scissors", exact=True)).to_be_focused()
    page.keyboard.press("Enter")
    expect(choices.locator(".choice-value")).to_have_text(["Scissors ✌", "Paper ✋"])
    expect(page.get_by_role("heading", name="You win!", exact=True)).to_be_visible()
    expect(page.locator("[data-outcome]")).to_have_count(1)
    expect(page.locator("[data-outcome]")).to_have_attribute("data-outcome", "win")

    page.get_by_role("button", name="Paper", exact=True).click()
    expect(choices.locator(".choice-value")).to_have_text(["Paper ✋", "Paper ✋"])
    expect(page.get_by_role("heading", name="It’s a tie", exact=True)).to_be_visible()
    expect(page.locator("[data-outcome]")).to_have_attribute("data-outcome", "tie")

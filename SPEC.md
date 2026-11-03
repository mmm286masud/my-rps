# Rock, Paper, Scissors

## RPS-001: Play a round

**Purpose:** one person plays a quick round against the computer.

- Choose rock, paper, or scissors. The computer chooses one move for that round.
- Display both choices and the result: **You win!**, **Computer wins**, or **It’s a tie**.
- Choosing again starts an independent round. No score or saved history.
- Keep the supplied interface and server. Name/color changes can wait until the rules work.

### Expected results

Results are from the **player’s perspective**. `determine_winner(player, computer)` in `game.py` returns `win`, `lose`, or `tie`. Inputs are the lowercase moves below; the supplied server rejects other choices.

| Player | Computer | Expected return |
| --- | --- | --- |
| rock | rock | tie |
| rock | paper | lose |
| rock | scissors | win |
| paper | rock | win |
| paper | paper | tie |
| paper | scissors | lose |
| scissors | rock | lose |
| scissors | paper | win |
| scissors | scissors | tie |

### Agreed plan

Implement the nine results above in the existing rule function, from the player's
perspective. Keep the supplied Flask server and interface, and make each choice
an independent round with no score or storage. The student authorized autonomous
implementation, tests, documentation, and GitHub delivery.

Add nine literal unit cases, a real request/result integration test with replay,
and a Chromium round with replay and Tab/Enter activation. Stabilize only the
computer's random choice. Reuse the supplied missing/unsupported-input checks:
missing input or `lizard` must return HTTP 400 with a useful explanation. A valid
Rock-versus-Paper loss is successful handling of valid input.

Run the complete Python 3.12 `check.py`, inspect tracked and new files, then deliver
through a feature branch and PR with successful CI. Repair Windows test-server
cleanup so the reloader child cannot hold its output pipe open after a test.

### Checks

Before coding, agree this small test plan with AI:

| Level | Cases and evidence |
| --- | --- |
| Unit — positive | All nine literal expected results above, including valid losses and ties. |
| Integration — positive | A submitted round uses the real rule function and displays both choices and the correct result. Fix the computer choice for the test. |
| Integration — negative | Reuse supplied missing/unsupported-move tests: HTTP 400 and a helpful explanation, without calling the rules. A crash is not the intended result. |
| E2E — positive | Add a real-browser round and replay in tests/e2e/test_round.py using the supplied live_server/page fixtures. Fix only the computer choice; use real rules and real HTTP. |

Use `unit`, `integration`, and `e2e` pytest markers. Run `.venv/bin/python check.py` for Black, Pylint, fast tests, and browser checks; then review the diff. Keep shared settings and meaningful assertions intact. The student still plays, inspects a rule and its test, and gives feedback. Browser automation does not establish every aspect of usability or application performance.

### Work record

- Delivery branch: `rps-001` in the student's public repository,
  [mmm286masud/my-rps](https://github.com/mmm286masud/my-rps).
- Issue: [RPS-001: Play a round, #1](https://github.com/mmm286masud/my-rps/issues/1).
- Pull request: [RPS-001: Play a round, #2](https://github.com/mmm286masud/my-rps/pull/2),
  merged into `main` as `5e996e4a0886d9fe48320321fa3e1a9178625be6` on
  2026-11-03. `Closes #1` closed the linked issue; GitHub reports it completed.
- Final PR CI: [Python checks — successful](https://github.com/mmm286masud/my-rps/actions/runs/41585349451)
  on final PR head `9e423cbd610ff75e4d77a4d9f70fe5893fc6c200`, verified before
  merging. Every setup/install step and full `python check.py` succeeded.
  The issue, PR, and initial real CI link were saved and pushed in that final PR
  commit before merge. This completion record updates the link to the final run.
  Issue and PR creation used the student's signed-in GitHub browser; commits,
  pushes, and merge used the existing SSH origin. The working tree was clean and
  merged `main` matched the reviewed PR tree at delivery verification.
- Implementation: [game.py](game.py) handles ties, the three player-winning
  pairs, and the remaining valid losses. The original server and UI are retained.
- Unit evidence: [tests/test_game.py](tests/test_game.py) contains all nine explicit
  literal cases with the `unit` marker. Its `integration` test submits actual
  requests using real rules, displays both moves and a loss, then replays to a win.
  Existing negative request checks remain in [tests/test_shell.py](tests/test_shell.py).
- Browser evidence: [tests/e2e/test_round.py](tests/e2e/test_round.py), marked `e2e`,
  fixes only the computer's random choice to Paper. Chromium clicks Rock and sees
  Computer wins (`lose`), uses Tab/Enter to choose Scissors and sees You win!
  (`win`), then chooses Paper and sees It's a tie (`tie`). Each new round replaces
  the previous choices/result. These are automated observations.
- Compatibility: [tests/e2e/test_dev_refresh.py](tests/e2e/test_dev_refresh.py)
  stops only its launched server process tree on Windows. The original cleanup
  stalled after the first successful test because the reloader child retained
  the stdout pipe. Existing assertions and Linux cleanup are preserved.
- Full local checks (2026-11-03): Python 3.12.10,
  `.venv\Scripts\python.exe check.py` — Black PASS (11 files), Pylint PASS,
  non-browser pytest **23 passed**, Chromium pytest **6 passed**. No `--fast`.
  `git diff --check` also passed. No checks or substantive assertions were removed.
- Review: compared all nine literal cases to the expected-result table; inspected
  the implementation, both new test modules, the Windows cleanup change, and
  tracked/untracked files. Positive feature tests patch randomness only.
- Example test and explanation (AI supplied): the literal case
  `("rock", "paper", "lose")` is checked with
  `assert determine_winner(player, computer) == expected`. It detects reversed
  player/computer perspective or incorrectly treating Paper as losing to Rock.
  Paper covers Rock, so the player must lose. This is not a student prediction
  or student test interpretation.
- Student participation: the student supplied a screenshot of the unfinished
  starter screen, then explicitly requested bypassing the personal checkpoints.
  No personal matchup prediction, test-purpose explanation, or completed-game
  round/replay/keyboard observation was supplied. Those rubric items remain
  unverified; automated results are not substituted for personal participation.
- AI assistance: Codex prepared the environment, explained the sample matchup,
  implemented the rules/tests, repaired Windows fixture cleanup, ran full checks,
  reviewed the diff, and prepared the delivery record. Student understanding and
  a particular grade are not claimed.

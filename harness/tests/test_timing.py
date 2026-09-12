"""Tests for the development timing helper."""

from unittest.mock import patch

import pytest

from harness.timing import timed


def test_timed_reports_elapsed_time(capsys: pytest.CaptureFixture[str]) -> None:
    with patch("harness.timing.perf_counter", side_effect=[10.0, 11.204]):
        with timed("hoist"):
            pass

    assert capsys.readouterr().out.strip() == "hoist 1.204s"


def test_timed_reports_when_block_raises(capsys: pytest.CaptureFixture[str]) -> None:
    with patch("harness.timing.perf_counter", side_effect=[5.0, 5.25]):
        with pytest.raises(RuntimeError, match="boom"):
            with timed("cleanup"):
                raise RuntimeError("boom")

    assert capsys.readouterr().out.strip() == "cleanup 0.250s"

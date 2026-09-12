"""Tests for the development timing helper."""

from unittest.mock import Mock, patch

import pytest

from harness.timing import timed


def test_timed_reports_elapsed_time() -> None:
    output = Mock()
    with (
        patch("harness.timing.perf_counter", side_effect=[10.0, 11.204]),
        patch("harness.timing.rprint", output),
    ):
        with timed("hoist"):
            pass

    output.assert_called_once_with("[dim]hoist 1.204s[/dim]")


def test_timed_reports_when_block_raises() -> None:
    output = Mock()
    with (
        patch("harness.timing.perf_counter", side_effect=[5.0, 5.25]),
        patch("harness.timing.rprint", output),
    ):
        with pytest.raises(RuntimeError, match="boom"):
            with timed("cleanup"):
                raise RuntimeError("boom")

    output.assert_called_once_with("[dim]cleanup 0.250s[/dim]")

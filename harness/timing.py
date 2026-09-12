"""Small timing helpers for interactive development."""

from collections.abc import Iterator
from contextlib import contextmanager
from time import perf_counter

from rich import print as rprint


@contextmanager
def timed(label: str) -> Iterator[None]:
    """Print how long the wrapped block takes to run."""
    start = perf_counter()
    try:
        yield
    finally:
        elapsed = perf_counter() - start
        rprint(f"[dim]{label} {elapsed:.3f}s[/dim]")

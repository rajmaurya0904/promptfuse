"""Smoke test: package imports cleanly. Replace/extend as modules land."""

import promptfuse


def test_version_is_set() -> None:
    assert promptfuse.__version__

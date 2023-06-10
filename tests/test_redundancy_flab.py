"""Tests for redundancy.flab check."""

from proselint.checks.redundancy import flab as chk

from .check import Check


class TestCheck(Check):
    """The test class for redundancy.flab."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for redundancy.flab."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""he is a man who is sensitive to anger.""")

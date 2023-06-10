"""Tests for weasel_words.misc check."""

from proselint.checks.weasel_words import misc as chk

from .check import Check


class TestCheck(Check):
    """The test class for weasel_words.misc."""
    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for weasel_words.misc."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""The book was extremely interesting.""")
        assert not self.passes("""The book was really interesting.""")
        assert self.passes("""The book was interesting.""")
        # TODO: add test when check is implemented


# class TestCheck(Check):
#     """The test class for weasel_words.misc."""
#     __test__ = False

#     @property
#     def this_check(self):
#         """Boilerplate."""
#         return chk

#     def test_smoke(self):
#         """Basic smoke test for weasel_words.misc."""
#         assert self.passes("""Smoke phrase with nothing flagged.""")
#         assert not self.passes("""The book was extremely interesting.""")
#         assert not self.passes("""The book was really interesting.""")

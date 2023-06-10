"""Weasel words.

---
layout:     post
source:     write-good
source_url: https://github.com/btford/write-good
title:      Weasel words.
date:       2014-06-10 12:31:19
categories: writing
---

Weasel words clearly weaken various aspects of a number of your sentences.

"""


# def check(text):

#     error_code = "weasel_words.misc"
#     msg = "Weasel words present."

#     return [(1, 1, error_code, msg)]

from proselint.tools import existence_check, max_errors, memoize


@max_errors(1)
@memoize
def check(text):
    """avoid abstract manner adverbs."""
    """source:     Jane Casagrande"""
    """source_url: http://https://www.grammarunderground.com/"""
    err = "weasel_words.misc"
    msg = ("Try to minimise the use of manner adverbs that add no solid information")
    adverbs = ["extremely", "really", "incredibly", "unbelievably",
            "astonishingly", "totally", "truly", "currently", "presently", "formerly", "previously"]

    return existence_check(text, adverbs, err, msg)

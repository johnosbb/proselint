"""Weasel words.

---
layout:     book
source:     June Casagrande
source_url: https://www.grammarunderground.com/
title:      It was the best of sentences, it was the worst of sentences.
date:       2019-02-119 12:31:19
categories: writing
---

Weasel words clearly weaken various aspects of a number of your sentences.

"""


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

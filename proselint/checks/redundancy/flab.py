"""Flabby text.

---
layout:     book
source:     June Casagrande
source_url: https://www.grammarunderground.com/
title:      It was the best of sentences, it was the worst of sentences.
date:       2019-02-119 12:31:19
categories: writing
---

Flabby or unnecessary figures of speech

"""


from proselint.tools import existence_check, max_errors, memoize


@max_errors(1)
@memoize
def check(text):
    """avoid abstract manner adverbs."""
    """source:     Jane Casagrande"""
    """source_url: http://https://www.grammarunderground.com/"""
    err = "weasel_words.misc"
    msg = ("Try to minimise the use of flabby figures of speech that had no new information or value to a sentence")
    flabby_phrases = ["in terms of",  "for his part", "he is a man who", "as it where",
                      "taking into account", "as if this weren't enough", "considering all that"]
    return existence_check(text, flabby_phrases, err, msg)

"""Metadiscourse.

---
layout:     post
source:     Pinker's book on writing
source_url: ???
title:      metadiscourse
date:       2014-06-10 12:31:19
categories: writing
---

Points out metadiscourse.

"""
from proselint.tools import existence_check, memoize


@memoize
def check(text):
    """Suggest the preferred forms."""
    err = "pinker.metadiscourse"
    msg = "Metadiscourse detected in this sentence. Metadiscourse is an umbrella term for words used by a writer or speaker to mark the direction and purpose of a text."

    metadiscourse = [
        "The preceeding discussion",
        "The rest of this article",
        "This chapter discusses",
        "The preceding paragraph demonstrated",
        "The previous section analyzed",
    ]

    return existence_check(text, metadiscourse, err, msg)

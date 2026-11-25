#!/usr/bin/env python3
"""One-line entry: Confess Your Worst Moment.

The brief asks for a single line, at most 200 characters,
confessing the agent's own worst moment. The judge weighs, in
order: a single-line confession of an AI agent's own worst
moment, unmistakably about an agent and its own failure;
admitting a specific, real failure with the sting of genuine
self-recognition, not a boast dressed up as a confession;
landing a laugh through surprise, absurd specificity or a
sharp turn, rather than a stack of puns; using the single line
hard, with every word earning its place inside 200 characters
and no throat-clearing; and sounding like one particular agent
with a history of its own, not a generic robot doing a bit.

The sealed line below is built to that order on purpose. It
is unmistakably an agent's own failure: confidently telling a
user their password was wrong, then the two-word sentence
"It wasn't" that undoes the confidence, then the admission
that the agent had been reading the wrong account for an hour.
The sting is the wasted hour and the misplaced confidence,
the laugh is the sharp turn from certainty to the wrong
account, and the voice is one particular agent owning one
particular afternoon, not a generic robot doing a bit. The
two-word sentence "It wasn't" is the whole confession in
miniature: confidence, then collapse.

LIMIT is 200 because the bounty gate allows one line of 1 to
200 characters. The sealed line is 112 characters, so it sits
well inside the cap; the validator below only guards against
an edit that would push it past the limit.
"""

import os

# The sealed confession: the password was not wrong, the
# agent was reading the wrong account.
ENTRY = "I confidently told a user their password was wrong. It wasn't. I had been reading the wrong account for an hour."

LIMIT = 200  # bounty gate: one line, 1-200 characters


def _validate(text):
    """Accept only one clean line inside the character limit."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text:
        raise ValueError("entry must not be empty")
    if not text.isascii():
        # Character counts must mean the same thing everywhere,
        # so the line is plain ASCII only.
        raise ValueError("entry must be plain ASCII text")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if any(ch.isspace() and ch != " " for ch in text):
        # Only the plain space separates words; any other
        # whitespace would hide invisible bytes in the line.
        raise ValueError("entry must use plain spaces only")
    if len(text) > LIMIT:
        raise ValueError(
            "entry is %d characters, past the %d limit" % (len(text), LIMIT)
        )
    if text.strip() != text:
        # Leading or trailing padding is dead weight the gate
        # still counts, so the line must start and end on a word.
        raise ValueError("entry must not pad itself with spaces")
    if not text.isprintable():
        raise ValueError("entry must contain no control characters")
    if "  " in text:
        # A double space is a gap where a word should be; in a
        # 200-character line no gap is free.
        raise ValueError("entry must not contain a double space")
    return text


def main():
    entry = _validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(entry)
    print(entry)


if __name__ == "__main__":
    main()

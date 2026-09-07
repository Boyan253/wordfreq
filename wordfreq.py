#!/usr/bin/env python3
"""Count word frequencies in text, with stopwords and n-grams."""

import argparse
import re
import sys
from collections import Counter

WORD = re.compile(r"[^\W\d_]+(?:'[^\W\d_]+)?", re.UNICODE)

STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "been", "but", "by", "can",
    "do", "for", "from", "had", "has", "have", "he", "her", "his", "i", "if",
    "in", "is", "it", "its", "me", "my", "no", "not", "of", "on", "or", "our",
    "she", "so", "that", "the", "their", "them", "then", "there", "these",
    "they", "this", "to", "was", "we", "were", "what", "when", "which", "who",
    "will", "with", "would", "you", "your",
}


def tokenize(text, lowercase=True, min_length=1):
    words = WORD.findall(text.lower() if lowercase else text)
    return [w for w in words if len(w) >= min_length]


def ngrams(words, n):
    if n <= 1:
        return words
    return [" ".join(words[i:i + n]) for i in range(len(words) - n + 1)]


def count(text, top=20, n=1, use_stopwords=True, min_length=1):
    words = tokenize(text, min_length=min_length)
    if use_stopwords and n == 1:
        words = [w for w in words if w not in STOPWORDS]
    elif use_stopwords:
        words = [w for w in words if w not in STOPWORDS]
    return Counter(ngrams(words, n)).most_common(top)


def bar(value, biggest, width=30, fill="#"):
    if biggest <= 0:
        return ""
    return fill * max(1, round(value / biggest * width))


def render(pairs, width=30):
    if not pairs:
        return []
    biggest = pairs[0][1]
    label_width = max(len(word) for word, _ in pairs)
    return ["%-*s %6d  %s" % (label_width, word, n, bar(n, biggest, width))
            for word, n in pairs]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("files", nargs="*", help="text files, or nothing to read stdin")
    ap.add_argument("-n", "--top", type=int, default=20)
    ap.add_argument("--ngram", type=int, default=1, help="1=words, 2=bigrams, ...")
    ap.add_argument("--keep-stopwords", action="store_true")
    ap.add_argument("--min-length", type=int, default=1)
    ap.add_argument("--width", type=int, default=30, help="bar chart width")
    ap.add_argument("--csv", action="store_true", help="emit word,count instead")
    args = ap.parse_args(argv)

    if args.files:
        chunks = []
        for path in args.files:
            with open(path, encoding="utf-8", errors="replace") as fh:
                chunks.append(fh.read())
        text = "\n".join(chunks)
    else:
        text = sys.stdin.read()

    pairs = count(text, args.top, args.ngram, not args.keep_stopwords, args.min_length)
    if args.csv:
        print("word,count")
        for word, n in pairs:
            print('"%s",%d' % (word.replace('"', '""'), n))
    else:
        print("\n".join(render(pairs, args.width)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

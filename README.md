# wordfreq

> Word frequency counts for text files, with stopwords, n-grams and a terminal bar chart.

## Why

Sometimes you just want to know what a pile of text is actually about — support
tickets, meeting notes, a scraped page — without standing up a notebook and an
NLP stack.

## Usage

```
python wordfreq.py notes.txt
python wordfreq.py *.md --top 30
python wordfreq.py tickets.txt --ngram 2          # bigrams
python wordfreq.py notes.txt --csv > freq.csv
cat article.txt | python wordfreq.py --min-length 4
```

## Output

```
deploy     42  ##############################
pipeline   31  ######################
staging    19  #############
rollback    8  ######
```

`--csv` switches to `word,count` for a spreadsheet.

## Options

| flag | effect |
|------|--------|
| `--ngram 2` | count two-word phrases instead of single words |
| `--keep-stopwords` | include `the`, `and`, `of`, … |
| `--min-length 4` | ignore short words |
| `--width 50` | wider bars |

## Tokenizing

Words are Unicode letter runs, so accented text works; digits and underscores
are not words. Internal apostrophes are kept, so `don't` stays one token.
A small built-in English stopword list is applied by default.

## Tests

```
pip install pytest
pytest
```

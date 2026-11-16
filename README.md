# Florilegium

*Florilegium* is medieval Latin for a hand-picked anthology of the best texts, literally "a gathering of flowers." This one is a must-read shelf.

A personal reading shelf: the 50 books that appear most often on "must-read" lists, plus books like *This Cursed Beautiful Land*, Nobel laureates, other great thinkers, and my own picks. That's 74 books in all.

**Shelf tab:** search across titles, authors, topics, films and Nobel fields. Filter by why a book is on the list, topic, difficulty, length, publication date, screen adaptation or shelf. Mark each book as read, watched, favourite or "not right now".

**Topic map tab:** historical eras and places on a timeline, with the themes that run across them. Arrows show how topics connect. Select a topic to explore its links, then show its books or filter the shelf by it.

Your marks are saved in your own browser, on that device only. Nobody else who opens the page can see them.

## How it was built

- **Top 50:** each book is ranked by how many of five must-read lists include it: Medium's "Ultimate List", College Transitions, Reedsy, Pan Macmillan and Books of Brilliance. Ties were broken by rank on TheGreatestBooks.org.
- **Genre, difficulty, adaptation verdicts and topics** are editorial judgements. Page counts are approximate and vary by edition. Years are first publication in the original language.

## Editing

The page is one self-contained file, `index.html`, generated from:

| File | What it holds |
| --- | --- |
| `data/books.json` | Every book: title, author, year, pages, genre, difficulty, summary, tags, adaptation and topics |
| `data/topics.json` | Map topics (eras and themes), their positions and the arrows between them |
| `src/template.html` | Layout, styles and behaviour |

After changing any of these, rebuild the page:

```sh
python3 build.py
```

Then commit both the changed file and the new `index.html`.

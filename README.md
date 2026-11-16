# Florilegium

*Florilegium* is medieval Latin for a hand-picked anthology of the best texts, literally "a gathering of flowers." This one is a must-read shelf.

A personal reading shelf: the 50 books that appear most often on "must-read" lists, plus books like *This Cursed Beautiful Land*, Nobel laureates, other great thinkers, and my own picks. That's 73 books in all.

**Shelf tab:** search across titles, authors, topics, films and Nobel fields. Filter by why a book is on the list, topic, difficulty, length, publication date, screen adaptation or shelf. Mark each book as read, watched, favourite or "not right now".

**Topic map tab:** historical eras and places on a timeline, with the themes that run across them. Arrows show how topics connect. Select a topic to explore its links, then show its books or filter the shelf by it.

Your marks are saved in your own browser, on that device only. Nobody else who opens the page can see them.

## How it was built

The top 50 are the books that appear most often across these five must-read lists. Each card shows how many of the five include it ("on 4 of 5 lists").

1. [100 Books to Read Before You Die: Creating the Ultimate List](https://medium.com/@joelapatrick/creating-the-ultimate-list-100-books-to-read-before-you-die-45f1b722b2e5), Medium (itself a merge of eight lists: The Guardian, BBC Big Read, Amazon, Harvard Book Store, Modern Library, Time, The Telegraph and The Art of Manliness)
2. [101 Books to Read Before You Die](https://www.collegetransitions.com/blog/books-to-read-before-you-die/), College Transitions (2024)
3. [100 Books to Read Before You Die](https://reedsy.com/discovery/blog/best-books-to-read-in-a-lifetime), Reedsy Discovery
4. [Must reads: 50 best books of all time](https://www.panmacmillan.com/blogs/general/must-read-books-of-all-time), Pan Macmillan (2026)
5. [Top 30 Must-Read Books for Every Bibliophile](https://booksofbrilliance.com/2026/08/15/30-books-to-read-before-you-die/), Books of Brilliance (2026)

Ties were broken by rank on [TheGreatestBooks.org](https://thegreatestbooks.org/), which aggregates hundreds of "best of" lists.

The other books were added as reads like *This Cursed Beautiful Land*, books by Nobel laureates and other thinkers, or personal picks.

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

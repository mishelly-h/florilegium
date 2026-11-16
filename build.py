"""Build index.html from src/template.html and the data files.

Edit data/books.json or data/topics.json (or the template), then run:
    python3 build.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).parent
RESET = ("<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}"
         "body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>")

def main():
    tpl = (ROOT / "src" / "template.html").read_text(encoding="utf-8")
    books = json.loads((ROOT / "data" / "books.json").read_text(encoding="utf-8"))
    topics = json.loads((ROOT / "data" / "topics.json").read_text(encoding="utf-8"))
    page = (tpl.replace("__BOOKS__", json.dumps(books, ensure_ascii=False))
               .replace("__TOPICS__", json.dumps(topics, ensure_ascii=False)))
    head, body = page.split("</style>", 1)
    html = ("<!doctype html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
            "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1,viewport-fit=cover\">\n"
            f"{RESET}\n{head}</style>\n</head>\n<body>\n{body.strip()}\n</body>\n</html>\n")
    (ROOT / "index.html").write_text(html, encoding="utf-8")
    print(f"Built index.html: {len(books)} books, {len(topics['topics'])} topics")

if __name__ == "__main__":
    main()

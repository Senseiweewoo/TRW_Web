import os
from flask import Flask, render_template, request, jsonify, send_from_directory

# Resolve paths robustly across local run and Vercel serverless environment
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

template_candidates = [
    os.path.join(BASE_DIR, "templates"),
    os.path.join(BASE_DIR, "TRW_Web", "templates"),
    os.path.join(os.path.dirname(BASE_DIR), "templates"),
    os.path.join(os.path.dirname(BASE_DIR), "TRW_Web", "templates")
]
template_dir = next((c for c in template_candidates if os.path.isdir(c)), os.path.join(BASE_DIR, "templates"))

static_candidates = [
    os.path.join(BASE_DIR, "static"),
    os.path.join(BASE_DIR, "TRW_Web", "static"),
    os.path.join(os.path.dirname(BASE_DIR), "static"),
    os.path.join(os.path.dirname(BASE_DIR), "TRW_Web", "static")
]
static_dir = next((c for c in static_candidates if os.path.isdir(c)), os.path.join(BASE_DIR, "static"))

app = Flask(
    __name__,
    template_folder=template_dir,
    static_folder=static_dir,
    static_url_path="/static"
)

# Enriched book collection with realistic metadata and status
books = [
    {
        "id": 1,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "category": "Fiction",
        "image": "book1.jpg",
        "isbn": "978-0-7432-7356-5",
        "year": 1925,
        "pages": 180,
        "location": "Shelf A-12",
        "status": "Available",
        "description": "Set in Jazz Age Long Island, the novel follows Jay Gatsby and his obsessive love for the beautiful Daisy Buchanan in a world of wealth, love, and illusion."
    },
    {
        "id": 2,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "category": "Classic Literature",
        "image": "book2.jpg",
        "isbn": "978-0-06-112008-4",
        "year": 1960,
        "pages": 281,
        "location": "Shelf B-04",
        "status": "Available",
        "description": "A gripping, heart-wrenching tale of coming-of-age in a South poisoned by virulent prejudice, viewed through the eyes of young Scout Finch."
    },
    {
        "id": 3,
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "category": "Adventure",
        "image": "book3.jpg",
        "isbn": "978-0-06-231500-7",
        "year": 1988,
        "pages": 208,
        "location": "Shelf C-09",
        "status": "Borrowed",
        "description": "The mystical story of Santiago, an Andalusian shepherd boy who yearns to travel in search of a worldly treasure and realizes his Personal Legend."
    },
    {
        "id": 4,
        "title": "Computer Networks: A Systems Approach",
        "author": "Larry Peterson & Bruce Davie",
        "category": "Computer Engineering",
        "image": "book4.jpg",
        "isbn": "978-0-12-385059-1",
        "year": 2019,
        "pages": 672,
        "location": "Shelf E-01",
        "status": "Available",
        "description": "Explores how the internet and computer networks work from the inside out, covering protocols, packet switching, architecture, and network security."
    },
    {
        "id": 5,
        "title": "Clean Code: A Handbook of Agile Software",
        "author": "Robert C. Martin",
        "category": "Computer Engineering",
        "image": "book5.jpg",
        "isbn": "978-0-13-235088-4",
        "year": 2008,
        "pages": 464,
        "location": "Shelf E-08",
        "status": "Available",
        "description": "A revolution in software design: principles and best practices for writing clean, testable, maintainable, and readable code."
    },
    {
        "id": 6,
        "title": "A Brief History of Time",
        "author": "Stephen Hawking",
        "category": "Science",
        "image": "book6.jpg",
        "isbn": "978-0-553-38016-3",
        "year": 1988,
        "pages": 256,
        "location": "Shelf D-02",
        "status": "Available",
        "description": "A landmark volume in science writing by one of the great minds of our time, exploring black holes, quantum mechanics, and the origins of the universe."
    },
    {
        "id": 7,
        "title": "1984",
        "author": "George Orwell",
        "category": "Classic Literature",
        "image": "book7.jpg",
        "isbn": "978-0-451-52493-5",
        "year": 1949,
        "pages": 328,
        "location": "Shelf B-11",
        "status": "Reserved",
        "description": "A chilling dystopian prophecy about totalitarianism, pervasive government surveillance, propaganda, and the suppression of truth."
    },
    {
        "id": 8,
        "title": "Introduction to Algorithms",
        "author": "Cormen, Leiserson, Rivest, Stein",
        "category": "Computer Engineering",
        "image": "book8.jpg",
        "isbn": "978-0-262-03384-8",
        "year": 2009,
        "pages": 1292,
        "location": "Shelf E-15",
        "status": "Available",
        "description": "The definitive comprehensive guide to modern algorithms, data structures, complexity analysis, and algorithmic problem-solving."
    }
]


# Support all possible entry route patterns (root, rewrite paths)
@app.route("/")
@app.route("/api")
@app.route("/api/index")
@app.route("/index")
def home():
    search = request.args.get("search", "").strip()
    selected_category = request.args.get("category", "").strip()

    displayed_books = books

    # Filter by category if selected and not "all"
    if selected_category and selected_category.lower() != "all":
        displayed_books = [
            b for b in displayed_books
            if b["category"].lower() == selected_category.lower()
        ]

    # Filter by search keyword
    if search:
        term = search.lower()
        displayed_books = [
            b for b in displayed_books
            if term in b["title"].lower()
            or term in b["author"].lower()
            or term in b["category"].lower()
            or term in b["isbn"].lower()
        ]

    categories = sorted(list({b["category"] for b in books}))

    return render_template(
        "index.html",
        books=displayed_books,
        search=search,
        selected_category=selected_category,
        categories=categories,
        total_books=len(books)
    )


@app.route("/api/borrow/<int:book_id>", methods=["POST"])
@app.route("/api/index/api/borrow/<int:book_id>", methods=["POST"])
def borrow_book(book_id):
    """Toggle book borrowing status for demonstration / interactive UX."""
    target_book = next((b for b in books if b["id"] == book_id), None)
    if not target_book:
        return jsonify({"success": False, "error": "Book not found"}), 404

    if target_book["status"] == "Available":
        target_book["status"] = "Borrowed"
        message = f"'{target_book['title']}' has been borrowed successfully! Due in 14 days."
    else:
        target_book["status"] = "Available"
        message = f"'{target_book['title']}' has been returned to the catalog and is now Available."

    return jsonify({
        "success": True,
        "book": target_book,
        "message": message
    })


@app.route("/static/<path:filename>")
def serve_static(filename):
    """Fallback static file handler for serverless execution."""
    return send_from_directory(static_dir, filename)


if __name__ == "__main__":
    app.run(debug=True)

from fastapi import FastAPI,HTTPException
app = FastAPI()

books = [
    {"id": 1, "title": "Python Advance", "author": "Nguyen Van A", "category": "programming", "year": 2020, "is_available": True},
    {"id": 2, "title": "Web Basic", "author": "Tran Thi B", "category": "web", "year": 2021, "is_available": False},
    {"id": 3, "title": "Database Design", "author": "Le Van C", "category": "database", "year": 2019, "is_available": True},
    {"id": 4, "title": "Network Security", "author": "Pham Van D", "category": "network", "year": 2022, "is_available": True},
    {"id": 5, "title": "FastAPI Basic", "author": "Nguyen Van A", "category": "web", "year": 2023, "is_available": True},
    {"id": 6, "title": "Advanced SQL", "author": "Tran Thi B", "category": "database", "year": 2021, "is_available": False}
]

@app.get('/books/statistics')
def get_books_statistics():
    total_books = len(books)
    available_books = len([book for book in books if book['is_available'] == True])
    borrowed_books = len([book for book in books if book['is_available'] == False])
    return {
        'total_books': total_books,
        'available_books':available_books,
        'borrowed_books': borrowed_books
    }
    
@app.get('/books/categories')
def get_books_categories():
    unique_categories = list(set([b["category"] for b in books]))
    return {"categories": unique_categories}

@app.get('/books/latest')
def get_books_latest():
    if not books:
        return{"message": "No books available"}
    latest_book = max(books, key=lambda book: book['year'])
    return latest_book
    
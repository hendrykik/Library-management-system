# Library Management API

Simple REST API for library book management built with FastAPI and PostgreSQL.

## Quick Start

```bash
git clone https://github.com/hendrykik/Library-management-system.git
cd library-api
docker compose up --build
```

**API**: http://localhost:8000  
**Docs**: http://localhost:8000/docs

## Endpoints

- `GET /books/` - list all books
- `POST /books/` - add book
- `DELETE /books/{serial_number}` - delete book  
- `PUT /books/{serial_number}/borrow` - borrow book
- `PUT /books/{serial_number}/return` - return book

## Example

```bash
# Add book
curl -X POST "http://localhost:8000/books/" \
  -H "Content-Type: application/json" \
  -d '{"serial_number": 123456, "title": "Book Title", "author": "Author Name"}'

# Borrow book
curl -X PUT "http://localhost:8000/books/123456/borrow" \
  -H "Content-Type: application/json" \
  -d '{"borrower_card_number": 987654}'
```

## Tech Stack

FastAPI | PostgreSQL | SQLAlchemy | Docker

# add_books.py
import os
import django

# Configurer Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mylibrary.settings')
django.setup()

from library.models import Book

# Liste des livres à ajouter
books = [
    {
        "title": "Le Seigneur des Anneaux",
        "author": "J.R.R. Tolkien",
        "isbn": "9780261102385",
        "published_date": "1954-07-29",
        "category": "Fantasy",
        "available": True
    },
    {
        "title": "1984",
        "author": "George Orwell",
        "isbn": "9780451524935",
        "published_date": "1949-06-08",
        "category": "Science-fiction",
        "available": True
    },
    {
        "title": "Harry Potter à l'école des sorciers",
        "author": "J.K. Rowling",
        "isbn": "9782070643028",
        "published_date": "1997-06-26",
        "category": "Fantasy",
        "available": True
    },
    {
        "title": "Le Petit Prince",
        "author": "Antoine de Saint-Exupéry",
        "isbn": "9780156012195",
        "published_date": "1943-04-06",
        "category": "Roman",
        "available": True
    },
    {
        "title": "Manga : Naruto Tome 1",
        "author": "Masashi Kishimoto",
        "isbn": "9782809411001",
        "published_date": "1999-09-21",
        "category": "Manga",
        "available": True
    },
    {
        "title": "Les Misérables",
        "author": "Victor Hugo",
        "isbn": "9782253004825",
        "published_date": "1862-01-01",
        "category": "Histoire",
        "available": True
    },
    {
        "title": "Le Comte de Monte-Cristo",
        "author": "Alexandre Dumas",
        "isbn": "9782253004351",
        "published_date": "1844-08-28",
        "category": "Roman",
        "available": True
    },
    {
        "title": "Dune",
        "author": "Frank Herbert",
        "isbn": "9782264020726",
        "published_date": "1965-08-01",
        "category": "Science-fiction",
        "available": True
    },
    {
        "title": "Les Aventures de Tintin : Le Secret de la Licorne",
        "author": "Hergé",
        "isbn": "9782035834013",
        "published_date": "1943-03-01",
        "category": "Bande dessinée",
        "available": True
    },
    {
        "title": "Autre Livre Exemple",
        "author": "Auteur Inconnu",
        "isbn": "1234567890",
        "published_date": "2020-01-01",
        "category": "Autre",
        "available": True
    }
]

# Ajout des livres à la base de données
for b in books:
    Book.objects.create(**b)

print("Tous les livres ont été ajoutés avec succès !")

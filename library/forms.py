from django import forms
from .models import Book
from django.core.exceptions import ValidationError
import re

class BookForm(forms.ModelForm):
    # -------------------------
    # Choix prédéfinis des catégories
    # -------------------------
    CATEGORY_CHOICES = [
        ('Fantasy', 'Fantasy'),
        ('Roman', 'Roman'),
        ('Science-fiction', 'Science-fiction'),
        ('Manga', 'Manga'),
        ('Histoire', 'Histoire'),
        ('Autre', 'Autre'),
    ]

    category = forms.ChoiceField(
        choices=CATEGORY_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        label="Catégorie"
    )

    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn', 'published_date', 'category', 'available']

        # Labels propres
        labels = {
            'title': 'Titre du livre',
            'author': 'Auteur',
            'isbn': 'ISBN',
            'published_date': 'Date de publication',
            'available': 'Disponible',
        }

        # Widgets Bootstrap + placeholders
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex : Le Seigneur des Anneaux',
            }),
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex : J.R.R. Tolkien',
            }),
            'isbn': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '978-1234567890',
            }),
            'published_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
            'available': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
        }

    # -------------------------
    # Validation avancée
    # -------------------------
    def clean_isbn(self):
        isbn = self.cleaned_data.get('isbn')
        # Supprimer

from django import forms
from .models import Article, Comment


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ('liker_set', 'author', 'club')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('author', 'article', 'liker_set', )
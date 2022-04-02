from django import forms
from django.forms import Textarea

from shop.models import Comment


class CommentForm(forms.ModelForm):

    body = forms.CharField(label='Коментарий', widget=forms.Textarea)

    class Meta:
        model = Comment
        fields = ('body', )


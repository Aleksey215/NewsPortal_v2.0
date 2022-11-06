from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['author', 'post', 'content']
        labels = {
            "content": "Input comment:"
        }
        widgets = {
            # поле "автор" заполнится автоматически
            'author': forms.HiddenInput(),
            'content': forms.TextInput(attrs={'class': 'form-control'}),
            # поле "объявление" заполнится автоматически
            'post': forms.HiddenInput(),
        }

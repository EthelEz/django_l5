from django import forms
from blog_app.models import Comment, Post

class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author', 'title', 'text')

        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }
        # these are the fields we can edit
# Add in widgets to that you can use css to connect to the widgets

class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ("author", 'text')

        widgets = {
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }

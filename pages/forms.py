from .models import Comment, NeastedComment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'content',)



class NeastedCommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NeastedCommentForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['content'].widget.attrs.update({'class': 'form-control'})
        self.fields['content'].widget.attrs.update({'style':"height: 100px"})





    class Meta:
        model = NeastedComment
        fields = ('name', 'email', 'content',)

         

from .models import Comment, NeastedComment, Post
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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

         





class UserForm(UserCreationForm):

    
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def  __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
    
    def clean_email(self):
        data = self.cleaned_data["email"]
        print(data)
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError("A user with that email id already exists.")

        
        return data
    
    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user



class ArticleForm(forms.ModelForm):

    

    class Meta:
        model = Post
        fields = ("title", "description", "status",)

    def  __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        for _, field in self.fields.items():
            if _ == 'status':

                field.widget.attrs.update({'class': 'form-control w-25'})
            else:
                field.widget.attrs.update({'class': 'form-control'})






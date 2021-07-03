from django import forms
from .models import Post, Category

choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)

class AddPostForm(forms.ModelForm):
    class Meta: 
        model = Post
        fields = ('title', 'subtitle', 'author', 'category', 'body')

        widgets = {
            
            'author': forms.TextInput(attrs={'id': 'elder', 'value': '', 'type': 'hidden',}),
            'category': forms.Select(choices=choice_list),

        }

class UpdatePostForm(forms.ModelForm):
    class Meta: 
        model = Post
        fields = ('title', 'subtitle', 'author', 'category','body')

        widgets = {

            'category': forms.Select(choices=choice_list),

        }
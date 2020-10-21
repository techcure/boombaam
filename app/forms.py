from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        #widget = {'title': forms.TextInput(attrs={'class':"title", 'reaonly':True})}
class PostViewForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = '__all__'
class DeleteViewForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = '__all__'
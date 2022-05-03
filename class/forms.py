from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Class_1_1,Class_1_2,Class_1_3,Class_1_4,Class_1_5,Class_1_6
from django import forms




class UserCreateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        
    class Meta:
        model = User 
        fields = ("username", "password1", "password2",)
        


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'


#授業詳細編集フォーム
class CommentForm_1(forms.ModelForm):
    
    class Meta:
        model = Class_1_1
        exclude = ('target',)
        
class CommentForm_2(forms.ModelForm):
    
    class Meta:
        model = Class_1_2
        exclude = ('target',)
        
class CommentForm_3(forms.ModelForm):
    
    class Meta:
        model = Class_1_3
        exclude = ('target',)
        
class CommentForm_4(forms.ModelForm):
    
    class Meta:
        model = Class_1_4
        exclude = ('target',)
        
class CommentForm_5(forms.ModelForm):
    
    class Meta:
        model = Class_1_5
        exclude = ('target',)
        
class CommentForm_6(forms.ModelForm):
    
    class Meta:
        model = Class_1_6
        exclude = ('target',)
        
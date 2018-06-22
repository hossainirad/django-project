from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


#########################################
#    RegistrationForm
#########################################
class Registration(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )

    def save(self, commit=True):
        user = super(Registration, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user

class EditUserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = (
            'city',
            'website',
            'phone',    
        )


    def __init__(self, user=None, *args, **kwargs):
        print(kwargs.pop('instance'))
        super(EditUserProfileForm, self).__init__(*args, **kwargs)
        
    # def save(self, commit=True):
    #     user = super(EditUserProfileForm, self).save(commit=False)
    #     user.city = self.cleaned_data['city']
    #     user.website = self.cleaned_data['website']
    #     user.phone = self.cleaned_data['phone']

    #     if commit:
    #         print(user.city)
    #         user.save()
    #         print(user.city)
    #     return user







#########################################
#    SubForm
#########################################
# class SubForm(forms.ModelForm):
#     class Meta:
#         model = models.UserProfile
#         fields = (
#             'city',
#             'website',
#             'phone',
#         )
#
#     def save(self, commit=True):
#         user = super(SubForm, self).save(commit=False)
#         user.city = self.cleaned_data['city']
#         user.website = self.cleaned_data['website']
#         user.phone = self.cleaned_data['phone']
#
#         if commit:
#             user.save()
#         return user


#########################################
#    Article form
#########################################
class CreateArticle(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'slug', 'body']


class NewArticleForm(forms.ModelForm):
    
    class Meta:
        model = Articles
        fields = (
            'title',
            'slug',
            'body',
            'author'
        )

#
# class UserCreationForm(forms.Form):
#     name = forms.CharField(max_length=30)
#     email = forms.EmailField(max_length=254)
#     message = forms.CharField(
#         max_length=2000,
#         widget=forms.Textarea(),
#         help_text='Write here your message!'
#     )
#     password = forms.PasswordInput()
#
#     def clean(self):
#         cleaned_data = super(UserCreationForm, self).clean()
#         name = cleaned_data.get('name')
#         email = cleaned_data.get('email')
#         message = cleaned_data.get('message')
#         message = cleaned_data.get('password')
#         if not name and not email and not message:
#             raise forms.ValidationError('You have to write something!')

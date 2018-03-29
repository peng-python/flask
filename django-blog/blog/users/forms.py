from django import forms


class RegisterForm(forms.Form):
    user_name=forms.CharField(required=True)
    pass_word1=forms.CharField(required=True,min_length=8)
    pass_word2=forms.CharField(required=True,min_length=8)
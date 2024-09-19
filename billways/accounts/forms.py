from django import forms
from .models import User, Blog

from .models import Blog

from .models import Account

from .models import Subscription

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email',
                'required': True
            })
        }
class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['user', 'balance', 'account_type', 'last_savings_date']


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'image', 'video']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'image']

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'surname', 'first_name', 'middle_name', 'gender', 'citizenship',
            'marital_status', 'id_number', 'phone_number', 'email', 
            'employment_type', 'company_name', 'salary', 'employer_contact', 
            'business_name', 'business_type', 'business_income', 
            'next_of_kin_name', 'next_of_kin_phone', 'next_of_kin_relation', 
            'id_upload', 'passport_photo', 'kra_document'
        ]
        widgets = {
            'employment_type': forms.Select(attrs={'onchange': 'toggleEmploymentFields()'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control'}),
            'employer_contact': forms.TextInput(attrs={'class': 'form-control'}),
            'business_name': forms.TextInput(attrs={'class': 'form-control'}),
            'business_type': forms.TextInput(attrs={'class': 'form-control'}),
            'business_income': forms.NumberInput(attrs={'class': 'form-control'}),
            'next_of_kin_name': forms.TextInput(attrs={'class': 'form-control'}),
            'next_of_kin_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'next_of_kin_relation': forms.TextInput(attrs={'class': 'form-control'}),
            'id_upload': forms.FileInput(attrs={'class': 'form-control-file'}),
            'passport_photo': forms.FileInput(attrs={'class': 'form-control-file'}),
            'kra_document': forms.FileInput(attrs={'class': 'form-control-file'}),
        }

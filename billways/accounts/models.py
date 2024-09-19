from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
import random
import string

from django.db import models

class Subscription(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Account(models.Model):
    ACCOUNT_TYPES = [
        ('FD', 'Fixed Deposit'),
        ('J', 'Junior'),
        ('SC', 'Shared Capital'),
        ('C', 'Chama'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    last_savings_date = models.DateTimeField(null=True, blank=True)
    account_type = models.CharField(max_length=2, choices=ACCOUNT_TYPES, default='FD')
    account_number = models.CharField(max_length=12, unique=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s account"

    def save(self, *args, **kwargs):
        if not self.account_number:
            self.account_number = self.generate_account_number()
        super().save(*args, **kwargs)

    def generate_account_number(self):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))

    def can_borrow(self):
        return self.last_savings_date and timezone.now() >= self.last_savings_date + timedelta(days=90)

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('Deposit', 'Deposit'),
        ('Withdrawal', 'Withdrawal'),
    ]
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.transaction_type} of {self.amount} on {self.date}"

class Loan(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    borrowed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Loan of {self.amount} on {self.borrowed_at}"

class User(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    MARITAL_STATUS_CHOICES = [
        ('single', 'Single'),
        ('married', 'Married'),
        ('divorced', 'Divorced'),
        ('widowed', 'Widowed'),
    ]

    EMPLOYMENT_TYPE_CHOICES = [
        ('employed', 'Employed'),
        ('self-employed', 'Self Employed'),
    ]

    surname = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    citizenship = models.CharField(max_length=30)
    marital_status = models.CharField(max_length=10, choices=MARITAL_STATUS_CHOICES)
    id_number = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    employment_type = models.CharField(max_length=20, choices=EMPLOYMENT_TYPE_CHOICES)
    company_name = models.CharField(max_length=50, blank=True, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    employer_contact = models.CharField(max_length=50, blank=True, null=True)
    business_name = models.CharField(max_length=50, blank=True, null=True)
    business_type = models.CharField(max_length=50, blank=True, null=True)
    business_income = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    next_of_kin_name = models.CharField(max_length=50)
    next_of_kin_phone = models.CharField(max_length=15)
    next_of_kin_relation = models.CharField(max_length=30)
    id_upload = models.FileField(upload_to='uploads/')
        
   
   
    passport_photo = models.ImageField(upload_to='uploads/passport_photos/', default='path/to/default/passport_photo.jpg')
    kra_document = models.FileField(upload_to='uploads/kra_documents/', default='path/to/default/kra_document.pdf')


    def __str__(self):
        return f"{self.first_name} {self.surname}"

        

class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='blogs/images/', null=True, blank=True)
    video = models.FileField(upload_to='blogs/videos/', null=True, blank=True)  # Ensure this line is present
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

from .forms import UserRegistrationForm
from .models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
import csv
from django.http import HttpResponse

from .models import Blog
from .forms import BlogForm
from django.contrib import messages
from .forms import SubscriptionForm
from .models import Subscription

def blog_view(request):
    # Assuming you're rendering a blog page.
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if not Subscription.objects.filter(email=email).exists():
                form.save()
                messages.success(request, "Thank you for subscribing!")
            else:
                messages.warning(request, "You are already subscribed.")
        else:
            messages.error(request, "Please enter a valid email.")
    
    form = SubscriptionForm()
    context = {
        'form': form,
        'blog': ...  # Your blog data here
    }
    return render(request, 'blog_template.html', context)
@login_required
def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogForm()
    return render(request, 'blog_create.html', {'form': form})

@login_required
def blog_update(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blog_update.html', {'form': form})

def blog_list(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'blog_list.html', {'blogs': blogs})

def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'blog_detail.html', {'blog': blog})
def view_detail(request):
    users = User.objects.all()
    return render(request, 'view_detail.html', {'users': users})

def home(request):
    
    blogs = Blog.objects.all()[:3]  # Adjust this if you need specific ordering
    return render(request, 'index.html', {'blogs': blogs})
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')


def savings(request):
    return render(request, 'savings.html')


def loan(request):
    return render(request, 'loan.html')


def contact(request):
    return render(request, 'contact.html')




def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def success(request):
    return render(request, 'success.html')










#exporting csv file
def export_users_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'

    writer = csv.writer(response)
    writer.writerow(['surname', 'first_name', 'middle_name', 'gender', 'citizenship', 
                     'marital_status', 'id_number', 'phone_number', 'email', 
                     'employment_type', 'company_name', 'salary', 'employer_contact', 
                     'business_name', 'business_type', 'business_income', 
                     'next_of_kin_name', 'next_of_kin_phone', 'next_of_kin_relation', 
                     'id_upload', 'passport_photo', 'kra_document'])

    for user in User.objects.all():
        writer.writerow([user.surname, user.first_name, user.middle_name, user.gender, user.citizenship, 
                         user.marital_status, user.id_number, user.phone_number, user.email, 
                         user.employment_type, user.company_name, user.salary, user.employer_contact, 
                         user.business_name, user.business_type, user.business_income, 
                         user.next_of_kin_name, user.next_of_kin_phone, user.next_of_kin_relation, 
                         user.id_upload.url if user.id_upload else '',
                         user.passport_photo.url if user.passport_photo else '',
                         user.kra_document.url if user.kra_document else ''])

    return response

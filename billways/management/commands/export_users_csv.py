from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from .models import User
import csv

@staff_member_required
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

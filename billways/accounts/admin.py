import csv
from django.http import HttpResponse
from django.contrib import admin
from .models import User, Blog

from .models import Account, Transaction, Loan
from .models import Subscription

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at')
    search_fields = ('email',)
    
class AccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'balance', 'created_at', 'last_savings_date', 'account_type', 'account_number')
    fields = ('user', 'balance', 'account_type', 'last_savings_date')
    readonly_fields = ('account_number',)
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.account_number = obj.generate_account_number()
        super().save_model(request, obj, form, change)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('account', 'amount', 'transaction_type', 'date')

class LoanAdmin(admin.ModelAdmin):
    list_display = ('account', 'amount', 'borrowed_at')

admin.site.register(Account, AccountAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Loan, LoanAdmin)
# Define the custom action for downloading users as CSV
@admin.action(description='Download users as CSV')
def download_users_csv(modeladmin, request, queryset):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'

    writer = csv.writer(response)
    # Write the header row in the CSV file
    writer.writerow(['ID Number', 'Email', 'First Name', 'Surname', 'Phone Number'])

    # Write the data rows
    for user in queryset:
        writer.writerow([user.id_number, user.email, user.first_name, user.surname, user.phone_number])

    return response

# Register the Blog model
admin.site.register(Blog)

# Register the User model with search fields and custom action
class UserAdmin(admin.ModelAdmin):
    actions = [download_users_csv]
    search_fields = ['email', 'first_name', 'surname', 'phone_number']  # Updated fields based on your model

admin.site.register(User, UserAdmin)

from django.contrib import admin
from payment.models import PaymentCategory, PaymentChart, PaymentDetail

# Register your models here.
class PaymentCategoryAdmin(admin.ModelAdmin):
    list_display=('name', 'description',)

class PaymentChartAdmin(admin.ModelAdmin):
    
    list_display=('name', 'payment_cat', 'amount_due', 'session', 'term')

class PaymentDetailAdmin(admin.ModelAdmin):
    
    list_display=('payee', 'payment_name', 'amount_paid', 'payment_date', 'confirmed')
    


admin.site.register(PaymentCategory, PaymentCategoryAdmin)
admin.site.register(PaymentChart, PaymentChartAdmin)
admin.site.register(PaymentDetail, PaymentDetailAdmin)

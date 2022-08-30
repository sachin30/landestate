from django.contrib import admin
from enquiry.models import Enquiry
from django.utils.html import format_html

# Register your models here.
class EnquiryAdmin(admin.ModelAdmin):
    list_display=("visitor_name","visitor_email","visitor_phone","property_enquired")
    list_filter=("property_enquired",)
    
    list_per_page=10

admin.site.register(Enquiry,EnquiryAdmin)
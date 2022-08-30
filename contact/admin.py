from django.contrib import admin
from contact.models import Contact
from django.utils.html import format_html

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display=('name',"email","subject","message","phone")

admin.site.register(Contact,ContactAdmin)
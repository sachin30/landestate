from django.contrib import admin
from broker.models import Broker
from django.utils.html import format_html

# Register your models here.
class BrokerAdmin(admin.ModelAdmin):
    def broker_photo(self,obj):
        return format_html(f"<img src='/media/{obj.photo}' style='height:100px ;width:100px' >")

    list_display=("first_name","last_name","address","phone","broker_photo")

admin.site.register(Broker,BrokerAdmin)
from django.contrib import admin
from property.models import Property
from django.utils.html import format_html

# Register your models here.

class PropertyAdmin(admin.ModelAdmin):
    
    prepopulated_fields = {
        'slug': ['title','city'],
    }
    # fields=("title","address","city","state","zipcode","photo_main","description","slug","bedrooms","bathrooms","sqft","plot_size","slug")
    readonly_fields=("photo_preview",)
    list_display= ("title","address","city","state","zipcode","photo_preview","less_description","bedrooms","bathrooms","sqft","plot_size","view","slug")
    list_filter=('city',("bedrooms",admin.ChoicesFieldListFilter))
    #list_display_links=("title","less_description")
    radio_fields={"bedrooms":admin.HORIZONTAL}  #if you hide/remove this radio field option then it will show default select box
    save_on_top= True
    ordering = ('-id',)
    search_fields=("title","address","city","state","zipcode","bedrooms","bathrooms","sqft","plot_size","slug")
    list_per_page=10

    def less_description(self,obj):
        return format_html(f"<span style='color:red'>{obj.description[:10]}</span>")

    def view(self,obj):
        return format_html(f"<a href='/admin/property/{obj.id}/change/' class='default'>View</a>")

    def photo_preview(self,obj):
        return format_html(f"<img src='/media/{obj.photo_main}' style='height:100px ;width:100px' >")

    # def readonly_slug(self,obj):
    #     return format_html(f"<span style='color:red'>{obj.slug}</span>")

admin.site.register(Property,PropertyAdmin)
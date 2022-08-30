import django_filters
from django import forms
from django_filters import CharFilter
from property.models import Property


class PropertyFilter(django_filters.FilterSet):
    city=CharFilter(field_name="city",lookup_expr="icontains")
    class Meta:
        model=Property
        fields=("bedrooms","bathrooms","city","zipcode")

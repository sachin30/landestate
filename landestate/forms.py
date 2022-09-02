from django import forms
from contact.models import Contact
from property.models import Property
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class':'form-control border border-secondary', 'type':'password', 'align':'center', 'placeholder':'Password'}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'class':'form-control border border-secondary', 'type':'password', 'align':'center', 'placeholder':'Password'}),
    )
    
    class Meta:
        model = User
        fields = ("first_name",'last_name','username',"email","password1","password2")
        widgets = {
            'first_name':forms.TextInput(attrs={"class":'form-control border border-secondary',"type":"text","placeholder":"First Name","id":"first_name_id"}),
            'last_name':forms.TextInput(attrs={"class":'form-control border border-secondary',"type":"text","placeholder":"Last Name","id":"last_name_id"}),
            'username':forms.TextInput(attrs={"class":'form-control border border-secondary',"type":"text","placeholder":" Userame","id":"username_id"}),
            'email':forms.EmailInput(attrs={"class":'form-control border border-secondary',"placeholder":"E-mail","id":"email_id"}),
        }

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = ("name","email","subject","message","phone")
        widgets = {
            'name':forms.TextInput(attrs={"class":'form-control',"placeholder":"Name"}),
            'email':forms.EmailInput(attrs={"class":'form-control',"placeholder":"Email"}),
            'subject':forms.TextInput(attrs={"class":'form-control',"placeholder":"Subject"}),
            'message':forms.Textarea(attrs={"class":'form-control',"placeholder":"Message","style":"height:120px"}),
            'phone':forms.TextInput(attrs={"class":'form-control',"placeholder":"Phone"}),
            
        }


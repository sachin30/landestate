from django.http import BadHeaderError, HttpResponse, HttpResponseRedirect,FileResponse, JsonResponse#fileresponse for pdf return
from django.shortcuts import redirect, render, HttpResponse
##from justestate.settings import BASE_DIR
from property.models import Property
from broker.models import Broker
from enquiry.models import Enquiry
from contact.models import Contact

from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import login,authenticate,logout
from django.core.mail import send_mail,EmailMessage
from landestate.forms import RegistrationForm,ContactForm
from django.core.files.storage import FileSystemStorage
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group



#filters
from pages.filters import PropertyFilter


import base64
#from bs4 import BeautifulSoup

#from pages.serializer import PropertySerializer
# decorators
from pages.decorators import allowed_users, unauthenticateduser,loginfirst
# for pagination #not in use pagination is done manually
from django.core.paginator import Paginator

import math
import time

#razorpay import

from django.views.decorators.csrf import csrf_exempt


# Create your views here.
#add user through modal form provided by BS5


#CRUD through python over dashboard ....no ajax


#views
#filter and index page
def index(request):
    user_visits=request.session.get('user_visits', 0)
    print(user_visits)
    request.session['user_visits'] = user_visits + 1
    #print(request.session['_auth_user_id'])
    #request.session.clear()
    #request.session.flush()
    #print(request.session.items())
    #print(dir(request.session))
    
    
    
    property_list=Property.objects.all().order_by('-id')[0:6:1]
    property_filter=PropertyFilter()
    context={"property_filter":property_filter,"property_list":property_list}
    if request.method=="POST":
        property_list=Property.objects.all()

        property_filter=PropertyFilter(request.POST,queryset=property_list)
        property_list=property_filter.qs

        paginator = Paginator(property_list, 4) 
        page_number = request.GET.get('page')
        property_list = paginator.get_page(page_number)
        context={
            "property_filter": property_filter,
            "property_list": property_list,
            
        }
        return render(request,"pages/properties.html",context)

    
    return render(request,"pages/index.html",context)


def about_us(request):
    return render(request,"pages/about_us.html")
#property detials dashboard



#CRUD Through AJAX overuser deta il----------ajax------

#ajax save direct through table   

@loginfirst
@allowed_users(allowed_roles=['admin'])
def user_details(request):

    ##Django pagination is good but doesnt work well with AJAX soo....applying manual pagination
    # paginator=Paginator(users_list,10)  #show 10 users per page
    # page_number=request.GET.get("page") #anchor tag href value from html page, get its value to get page number
    # users = paginator.get_page(page_number)
    page_number=1
    # when page is loaded page value is not given so we need to manually assign page number to avoid type error
    if request.GET.get("page") is None:
        page_number=1
        print("page is NONE")
    else:
        page_number=int(request.GET.get("page"))
        print("page is available")

    print("page_number", page_number)
    # this line so when page value exceeds it converts it to last page value
    last_page_number=int(math.ceil(len(User.objects.all())/10))
    if page_number > last_page_number:
        page_number=last_page_number

    #print("page_number===",page_number)
    #pagination math for slicing object set
    print(page_number)
    if page_number is None:
        users = User.objects.all()[0:10:1]
    else:
        for i in range(1,page_number+1):
            if(i==page_number):
                global start_list
                global end_list
                    
                start_list=(page_number * 10)-10
                end_list=page_number * 10
        
        print(start_list)
        print(end_list)

        users = User.objects.all()[start_list:end_list:1]
    
    # print(users)
    # print(type(users))
    
    form=RegistrationForm()
    
    context={"users":users,"form":form,"page_number":page_number,"last_page_number":last_page_number}
    return render(request,"pages/user_details.html",context)

#display the list of properties for user or any viewer
#goes to properties html
def property_list_display(request):
    property_list = Property.objects.all()
    paginator = Paginator(property_list, 2) 

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context={'page_obj':page_obj}
    return render(request,"pages/properties.html",context)


#displaying the all details of single property
def property_details(request,slug):
    property_details= Property.objects.get(slug=slug)
    print(property_details)
    context={"property_details":property_details}
    return render(request, "pages/property_details.html",context)

#User registration # add user through registration page
@unauthenticateduser
def registration(request): 
    form=RegistrationForm()
    print(vars(form))
    context={}
    if request.method=="POST":
    
        #create form object
        form=RegistrationForm(request.POST) 
        print(vars(form))
        for field in form:
            print("Field Error:", field.name,  field.errors)
        print(form.is_valid())
        if form.is_valid(): 
            print("form is valid")
            user=form.save()
            username=form.cleaned_data.get("username")
            #assign user to a group # you will see this commented code in signals 
            # group= Group.objects.get(name="usergroup")
            
            # user.groups.add(group)
            messages.success(request,"User registered successful: "+username)
            return HttpResponseRedirect('/user_login/')
        else:
            form_err=form.errors
            context={"form_err":form_err,"form":form}
            return render(request,"pages/registration.html",context)
    
    
    context['form']= form
    return render(request,"pages/registration.html",context)

#user login
@unauthenticateduser
def user_login(request):

    if request.method=="POST":
        name=request.POST["Name"]
        password=request.POST["Password"]

        user=authenticate(request,username=name,password=password)

        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            messages.info(request,"Wrong Credentials")
            return redirect("/user_login")
    return render(request,"pages/login.html")
@loginfirst
def user_logout(request):
    logout(request)
    return redirect("/user_login")

#for contacts and mail send

def contact(request):
    form=ContactForm()
    context={}
    if request.method=="POST":
       
        #create form object
        form=ContactForm(request.POST) 
        
        
        if form.is_valid():
            print("form is valid")
            form.save()
            
            
            #sending mail to manager
            name=form.cleaned_data["name"]
            email=form.cleaned_data["email"]
            subject=form.cleaned_data["subject"]
            message=form.cleaned_data["message"]
            phone=form.cleaned_data["phone"]
            message=name+" has shown interest in your property and left a note:\n\n"+message+"\nEmail : "+email+"\nPhone Number : "+phone
            

            #get file to save in filestoragesystem for it to send through email
            # filetostorage=request.FILES['files']
            # print(filetostorage)
            # fs=FileSystemStorage()
            # filename=fs.save(filetostorage.name,filetostorage)
            # #get urls
            # filenameurl=fs.url(filename)
            # print(filenameurl)
           
            #Use Gmail's app password by turning 2step verification ON.
            #Then generate new app password.use that pass as USER_HOST_PASSWORD        
            email_from=settings.EMAIL_HOST_USER
            email_to="sachin.esenceweb@gmail.com"
        
            #create email object
            email_message= EmailMessage(subject, message, email_from, [email_to])
            
            # email_message.attach(filename,filenameurl)
            # fs.delete(filename)
 
            try:
                #send email
                email_message.send(fail_silently=False)
                messages.success(request,"Thanks for your Interest, We will contact you soon")

            except BadHeaderError:
                return HttpResponse('Invalid header found.')

            return HttpResponseRedirect('/')
   
        
    context['form']= form
    return render(request,"pages/contact.html",context)
    


#property enquiry (new) 
def property_enquiry(request):
    if request.method=="POST":
        print("adding enquiry property to database")
        name=request.POST["prop_enq_username"]
        email=request.POST["prop_enq_useremail"]
        phone=request.POST["prop_enq_userphone"]
        enquired_property=request.POST["enquired_property"]

        enquiryinstance=Enquiry(visitor_name=name, visitor_email=email, visitor_phone=phone)
        enquiryinstance.property_enquired_id=enquired_property
        enquiryinstance.save()

        email_from=settings.EMAIL_HOST_USER
        email_to="sachin.esenceweb@gmail.com"
        message=name+" made an enquiry about "+enquiryinstance.property_enquired.title+"\nEmail : "+email +"\nPhone : "+ phone

        email_message= EmailMessage("About User enquiry for Property",message, email_from, [email_to,email])
        try:
            #send email
            email_message.send(fail_silently=False)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')

        messages.success(request,"Thanks for your Interest, We will contact you soon")
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/property_details')



from django.shortcuts import render,redirect
from construction.models.contactusc import ContactUsc
from construction.models.contactus import ContactUs
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import get_template

# Create your views here.
def index(request):
    return render(request, 'index.html')


def contactUsConstruction(request):
    return render(request, 'contactUsConstruction.html')


def contactUsEvents(request):
    return render(request, 'contactUsEvents.html')


def services(request):
    return render(request, 'services.html')


def blog(request):
    return render(request, 'blogs.html')


def aboutUs(request):
    return render(request, 'aboutUs.html')


def contactConstruction(request):
    if request.method == "POST":
        postData = request.POST
        first_name = postData.get('first_name')
        last_name = postData.get('last_name')
        phone_number = postData.get('phone_number')
        email = postData.get('email')
        description = postData.get('description')
        problem = ContactUsc(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            email=email,
            description=description
        )
        problem.register()

        ctx = {
            'first_name' : first_name,
            'last_name' : last_name,
        }
        message = get_template('mccus.html').render(ctx)
        email = EmailMessage(
            'Thank You for Contacting Us!!😀 ',
            message,
            settings.EMAIL_HOST_USER,
            [email],
        )
        email.content_subtype = "html"
        email.fail_silently = False
        email.send()

        ctx2 = {
            'first_name': first_name,
            'last_name': last_name,
            'phone_number' : phone_number,
            'email' : email,
            'description' : description
        }
        message = get_template('mcclient.html').render(ctx2)
        email = EmailMessage(
            'New Client Details - Mountain Construction ',
            message,
            settings.EMAIL_HOST_USER,
            ['venkateshvenky5408@gmail.com'],
        )
        email.content_subtype = "html"
        email.fail_silently = False
        email.send()

        return render(request, 'index.html', {'cc': 1})


def contactEvents(request):
    if request.method == "POST":
        postData = request.POST
        first_name = postData.get('first_name')
        last_name = postData.get('last_name')
        phone_number = postData.get('phone_number')
        name_of_event=postData.get('name_of_event')
        email = postData.get('email')
        description = postData.get('description')
        problem = ContactUs(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            email=email,
            name_of_event=name_of_event,
            description=description
        )
        problem.register()
        ctx = {
            'first_name' : first_name,
            'last_name' : last_name,
        }
        message = get_template('mecus.html').render(ctx)
        email = EmailMessage(
            'Thank You for Contacting Us!!😀 ',
            message,
            settings.EMAIL_HOST_USER,
            [email],
        )
        email.content_subtype = "html"
        email.fail_silently = False
        email.send()

        ctx2 = {
            'first_name': first_name,
            'last_name': last_name,
            'phone_number': phone_number,
            'mail': email,
            'name_of_event': name_of_event,
            'description': description
        }
        message = get_template('meclient.html').render(ctx2)
        email = EmailMessage(
            'New Client Details - Mountain Event Management ',
            message,
            settings.EMAIL_HOST_USER,
            ['venkateshvenky5408@gmail.com'],
        )
        email.content_subtype = "html"
        email.fail_silently = False
        email.send()

        return render(request, 'index.html', {'cc': 1})
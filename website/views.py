from django.core.mail import send_mail
from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})


def index(request):
    return render(request, 'index.html', {})

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message =request.POST['message']

        #send a mail

        send_mail(
            name,
            message,
            email,
            ['arcticm2015@gmail.com'],
        )





        return render(request, 'contact.html', {'name': name})
    else:
        return render(request, 'contact.html', {})

def about(request):
    return render(request, 'about.html', {})

def pricing(request):
    return render(request, 'pricing.html', {})

def service(request):
    return render(request, 'service.html', {})

def blog(request):
    return render(request, 'blog.html', {})
# Create your views here.

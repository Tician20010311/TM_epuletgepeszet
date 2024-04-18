from django.shortcuts import render 
from .models import Job
from .models import Price_oofer
from django.http import HttpResponse


def landing(request):
    if request.method == 'POST':
        contact = Price_oofer()
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact.name = name
        contact.email = email
        contact.phone = phone
        contact.subject = subject
        contact.message = message

        contact.save()
        return HttpResponse("<h1>Köszönjük , hogy felvette velünk a kapcsolatot , munkatársunk hamarosan jelentkezik.</h1>")

    return render(request, 'tm_epuletgepeszet_app/base.html')
               
def privacy(request):
    return render(request, 'tm_epuletgepeszet_app/privacy.html')

def jobs(request):
    jobs = Job.objects.all()
    return render(request, 'tm_epuletgepeszet_app/jobs.html',{'jobs': jobs}) 

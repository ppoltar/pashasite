from django.shortcuts import render,get_object_or_404
from .models import Job, Education
# Create your views here.
def home(request):
    jobs = Job.objects
    return render(request,"jobs/home.html",{'jobs':jobs})

def details(request,job_id):
    job_details=get_object_or_404(Job, pk=job_id)
    return render(request, "jobs/details.html", {'jobs': job_details})

def education(request):
    education = Education.objects
    return render(request,"jobs/education.html",{'education': education})
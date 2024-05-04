from django.shortcuts import render
from .forms import PatientForm
# Create your views here.
from .models import Patient
from django.contrib import messages

def add(request):
    if request.method=="POST":
        form = PatientForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            messages.success(request,('please enter valed id'))
            return render(request,'add.html',{})
        messages.success(request,('Add Successful'))
        return render(request,'add.html',{})
    else:
        return render(request,'add.html',{})
    

def home(request):
    if request.method == "POST":
        patient_id = request.POST.get('patient_id')
        try:
            patient = Patient.objects.get(id=patient_id)
            return render(request, 'home.html', {'patient': patient})
        except Patient.DoesNotExist:
            return render(request, 'home.html', {'patient': None})
    return render(request, 'home.html')

def password(request):
    if request.method == "POST":
        patient_id = request.POST.get('patient_id')
        try:
            patient = Patient.objects.get(id=patient_id)
            return render(request, 'password.html', {'patient': patient})
        except Patient.DoesNotExist:
            return render(request, 'password.html', {'patient': None})
    return render(request, 'password.html')

def index(request):
    if request.method == "POST":
        patient_id = request.POST.get('patient_id')
        try:
            patient = Patient.objects.get(id=patient_id)
            return render(request, 'index.html', {'patient': patient})
        except Patient.DoesNotExist:
            return render(request, 'index.html', {'patient': None})
    return render(request, 'index.html')
    







from django.shortcuts import render
from django.http import HttpResponse
from routine.models import Computer_Second, Labroom
from .forms import Computer1ModelForm,Computer2ModelForm,Computer3ModelForm,Computer4ModelForm,Electrical1ModelForm, Electrical2ModelForm, Electrical3ModelForm, Electrical4ModelForm,LabroomModelForm
from .packages.run import call
from .packages.teacher_code import LecturerCode
import sys

# Create your views here.
def homepage(request):
    return render(request, 'routine/dashboard.html')

def generate_routine(request):
    print(sys.argv)
    if 'runserver' in sys.argv:
        call()   
        print(sys.argv)        
        return HttpResponse("Routine is generated")

def generate_code(request):
    if 'runserver' in sys.argv:
        LecturerCode(274)
        return HttpResponse("Code is generated")

def addLabroom(request):
    if request.method == "POST":
        form = LabroomModelForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'routine/lab_room.html')

def computerBatch(request):
    return render(request, 'routine/year_computer.html')

def electricalBatch(request):
    return render(request, 'routine/year_electrical.html')

def computerData_first(request):
    if request.method == "POST":
        form = Computer1ModelForm(request.POST)
    # print('\n'*10, form)
        if form.is_valid():
            form.save()
    labroom = Labroom.objects.all()
    form = LabroomModelForm()
    context = {
        'labrooms':labroom,
        'form':form,
    }
# return redirect('/')
    return render(request, 'routine/computer_first.html', context)


def computerData_second(request):
    if request.method == "POST":
        form = Computer2ModelForm(request.POST)
    
    # print('\n'*10, form)
        if form.is_valid():
            form.save()
# return redirect('/')
    return render(request, 'routine/computer_second.html')

def computerData_third(request):
    if request.method == "POST":
        form = Computer3ModelForm(request.POST)
    # print('\n'*10, form)
        if form.is_valid():
            form.save()
# return redirect('/')
    return render(request, 'routine/computer_third.html')

def computerData_fourth(request):
    if request.method == "POST":
        form = Computer4ModelForm(request.POST)
    # print('\n'*10, form)
        if form.is_valid():
            form.save()
# return redirect('/')
    return render(request, 'routine/computer_fourth.html')

def electricalData_first(request):
    if request.method == "POST":
        form = Electrical1ModelForm(request.POST)
    # print('\n'*10, form)
        if form.is_valid():
            form.save()

    return render(request, 'routine/electrical_first.html')

def electricalData_second(request):
    if request.method == "POST":
        form = Electrical2ModelForm(request.POST)
    # print('\n'*10, form)
        if form.is_valid():
            form.save()

    return render(request, 'routine/electrical_second.html')

def electricalData_third(request):
    if request.method == "POST":
        form = Electrical3ModelForm(request.POST)
    # print('\n'*10, form)
        if form.is_valid():
            form.save()

    return render(request, 'routine/electrical_third.html')

def electricalData_fourth(request):
    if request.method == "POST":
        form = Electrical4ModelForm(request.POST)
    # print('\n'*10, form)
        if form.is_valid():
            form.save()

    return render(request, 'routine/electrical_fourth.html')
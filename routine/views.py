from email import message
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect 
from django.contrib import messages
from matplotlib.style import context
from routine.models import Computer_Second, Labroom
from routine.packages.pdf_code import pdf_code
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
        # data=r"D:\Minor Project on Automated Timetable Generator\multiple database\output.pdf"      
        # context = {
        #     'output' : data
        # }
        with open('D:\Minor Project on Automated Timetable Generator\multiple database\output.pdf', 'rb') as pdf:
            response = HttpResponse(pdf.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'filename = output.pdf'
            return response

        

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
        period = int(form['Lecturer_Period'].value())
        codeLst, lecCodeLst, lectId, lab_lst, lab_lecturer, lab_room, lab_room_lst, mylist1, mylist2, mylist3, lab_len = LecturerCode(377)  
        if lab_lst != []:          
            period = period + max(lab_lst)
        if period <= 42:
            if form.is_valid():
                form.save()
                messages.success(request, 'Your data has been entered into the database.')
        else:
            messages.error(request, 'You cant add more lecturer.')
# return redirect('/')
    return render(request, 'routine/computer_first.html')


def computerData_second(request):
    if request.method == "POST":
        form = Computer2ModelForm(request.POST)
        period = int(form['Lecturer_Period'].value())
        codeLst, lecCodeLst, lectId, lab_lst, lab_lecturer, lab_room, lab_room_lst, mylist1, mylist2, mylist3, lab_len = LecturerCode(376)
        if lab_lst != []:          
            period = period + max(lab_lst)
        if period <= 42:
            if form.is_valid():
                form.save()
                messages.success(request, 'Your data has been entered into the database.')
        else:
            messages.error(request, 'You cant add more lecturer.')
# return redirect('/')
    return render(request, 'routine/computer_second.html')

def computerData_third(request):
    if request.method == "POST":
        form = Computer3ModelForm(request.POST)
        period = int(form['Lecturer_Period'].value())
        codeLst, lecCodeLst, lectId, lab_lst, lab_lecturer, lab_room, lab_room_lst, mylist1, mylist2, mylist3, lab_len = LecturerCode(375)
        if lab_lst != []:          
            period = period + max(lab_lst)
        if period <= 42:
            if form.is_valid():
                form.save()
                messages.success(request, 'Your data has been entered into the database.')
        else:
            messages.error(request, 'You cant add more lecturer.')
    return render(request, 'routine/computer_third.html')

def computerData_fourth(request):
    if request.method == "POST":
        form = Computer4ModelForm(request.POST)
        period = int(form['Lecturer_Period'].value())
        codeLst, lecCodeLst, lectId, lab_lst, lab_lecturer, lab_room, lab_room_lst, mylist1, mylist2, mylist3, lab_len = LecturerCode(374)
        if lab_lst != []:          
            period = period + max(lab_lst)
        if period <= 42:
            if form.is_valid():
                form.save()
                messages.success(request, 'Your data has been entered into the database.')
        else:
            messages.error(request, 'You cant add more lecturer.')
    return render(request, 'routine/computer_fourth.html')

def electricalData_first(request):
    if request.method == "POST":
        form = Electrical1ModelForm(request.POST)
        period = int(form['Lecturer_Period'].value())
        codeLst, lecCodeLst, lectId, lab_lst, lab_lecturer, lab_room, lab_room_lst, mylist1, mylist2, mylist3, lab_len = LecturerCode(277)
        if lab_lst != []:          
            period = period + max(lab_lst)
        if period <= 42:
            if form.is_valid():
                form.save()
                messages.success(request, 'Your data has been entered into the database.')
        else:
            messages.error(request, 'You cant add more lecturer.')

    return render(request, 'routine/electrical_first.html')

def electricalData_second(request):
    if request.method == "POST":
        form = Electrical2ModelForm(request.POST)
        period = int(form['Lecturer_Period'].value())
        codeLst, lecCodeLst, lectId, lab_lst, lab_lecturer, lab_room, lab_room_lst, mylist1, mylist2, mylist3, lab_len = LecturerCode(276)
        if lab_lst != []:          
            period = period + max(lab_lst)
        if period <= 42:
            if form.is_valid():
                form.save()
                messages.success(request, 'Your data has been entered into the database.')
        else:
            messages.error(request, 'You cant add more lecturer.')

    return render(request, 'routine/electrical_second.html')

def electricalData_third(request):
    if request.method == "POST":
        form = Electrical3ModelForm(request.POST)
        period = int(form['Lecturer_Period'].value())
        codeLst, lecCodeLst, lectId, lab_lst, lab_lecturer, lab_room, lab_room_lst, mylist1, mylist2, mylist3, lab_len = LecturerCode(275)
        if lab_lst != []:          
            period = period + max(lab_lst)
        if period <= 42:
            if form.is_valid():
                form.save()
                messages.success(request, 'Your data has been entered into the database.')
        else:
            messages.error(request, 'You cant add more lecturer.')

    return render(request, 'routine/electrical_third.html')

def electricalData_fourth(request):
    if request.method == "POST":
        form = Electrical4ModelForm(request.POST)
        period = int(form['Lecturer_Period'].value())
        codeLst, lecCodeLst, lectId, lab_lst, lab_lecturer, lab_room, lab_room_lst, mylist1, mylist2, mylist3, lab_len = LecturerCode(274)
        if lab_lst != []:          
            period = period + max(lab_lst)
        if period <= 42:
            if form.is_valid():
                form.save()
                messages.success(request, 'Your data has been entered into the database.')
        else:
            messages.error(request, 'You cant add more lecturer.')

    return render(request, 'routine/electrical_fourth.html')
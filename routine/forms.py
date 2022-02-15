from django import forms
from .models import Computer_First,Computer_Second,Computer_Third,Computer_Fourth, Electrical_First, Electrical_Second, Electrical_Third, Electrical_Fourth

class Computer1ModelForm(forms.ModelForm):
    class Meta:
        model = Computer_First
        fields = ['batch','semester','Lecturer_Name','Lecturer_Code',
                   'Lecturer_Id', 'Lecturer_Subject', 'Lecturer_Period',
                   'Lab_Class', 'Lab_Period']

class Computer2ModelForm(forms.ModelForm):
    class Meta:
        model = Computer_Second
        fields = ['batch','semester','Lecturer_Name','Lecturer_Code',
                   'Lecturer_Id', 'Lecturer_Subject', 'Lecturer_Period',
                   'Lab_Class', 'Lab_Period']

class Computer3ModelForm(forms.ModelForm):
    class Meta:
        model = Computer_Third
        fields = ['batch','semester','Lecturer_Name','Lecturer_Code',
                   'Lecturer_Id', 'Lecturer_Subject', 'Lecturer_Period',
                   'Lab_Class', 'Lab_Period']

class Computer4ModelForm(forms.ModelForm):
    class Meta:
        model = Computer_Fourth
        fields = ['batch','semester','Lecturer_Name','Lecturer_Code',
                   'Lecturer_Id', 'Lecturer_Subject', 'Lecturer_Period',
                   'Lab_Class', 'Lab_Period']

class Electrical1ModelForm(forms.ModelForm):
    class Meta:
        model = Electrical_First
        fields = ['batch','semester','Lecturer_Name','Lecturer_Code',
                   'Lecturer_Id', 'Lecturer_Subject', 'Lecturer_Period',
                   'Lab_Class', 'Lab_Period']

class Electrical2ModelForm(forms.ModelForm):
    class Meta:
        model = Electrical_Second
        fields = ['batch','semester','Lecturer_Name','Lecturer_Code',
                   'Lecturer_Id', 'Lecturer_Subject', 'Lecturer_Period',
                   'Lab_Class', 'Lab_Period']

class Electrical3ModelForm(forms.ModelForm):
    class Meta:
        model = Electrical_Third
        fields = ['batch','semester','Lecturer_Name','Lecturer_Code',
                   'Lecturer_Id', 'Lecturer_Subject', 'Lecturer_Period',
                   'Lab_Class', 'Lab_Period']

class Electrical4ModelForm(forms.ModelForm):
    class Meta:
        model = Electrical_Fourth
        fields = ['batch','semester','Lecturer_Name','Lecturer_Code',
                   'Lecturer_Id', 'Lecturer_Subject', 'Lecturer_Period',
                   'Lab_Class', 'Lab_Period']      
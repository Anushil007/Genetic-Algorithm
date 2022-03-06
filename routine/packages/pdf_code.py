from routine.models import *

def pdf_code(batch):
    if batch == 375:
        c = Computer_Third.objects.all()
        Lecturer_Sub = []
        lab = []
        lab_leccode = []
        for code in c:
            Lecturer_Sub.append(code.Lecturer_Subject)
            if code.Lab_Class != '':
                lab.append(code.Lab_Class)
                lab_leccode.append(code.Lab_Lec_Period)


        return Lecturer_Sub, lab, lab_leccode

    if batch == 376:
        c = Computer_Second.objects.all()
        Lecturer_Sub = []
        lab = []
        lab_leccode = []
        for code in c:
            Lecturer_Sub.append(code.Lecturer_Subject)
            if code.Lab_Class != '':
                lab.append(code.Lab_Class)
                lab_leccode.append(code.Lab_Lec_Period)


        return Lecturer_Sub, lab, lab_leccode
    
    if batch == 377:
        c = Computer_First.objects.all()
        Lecturer_Sub = []
        lab = []
        lab_leccode = []
        for code in c:
            Lecturer_Sub.append(code.Lecturer_Subject)
            if code.Lab_Class != '':
                lab.append(code.Lab_Class)
                lab_leccode.append(code.Lab_Lec_Period)


        return Lecturer_Sub, lab, lab_leccode
    
    if batch == 374:
        c = Computer_Fourth.objects.all()
        Lecturer_Sub = []
        lab = []
        lab_leccode = []
        for code in c:
            Lecturer_Sub.append(code.Lecturer_Subject)
            if code.Lab_Class != '':
                lab.append(code.Lab_Class)
                lab_leccode.append(code.Lab_Lec_Period)


        return Lecturer_Sub, lab, lab_leccode
    
    if batch == 276:
        c = Electrical_Second.objects.all()
        Lecturer_Sub = []
        lab = []
        lab_leccode = []
        for code in c:
            Lecturer_Sub.append(code.Lecturer_Subject)
            if code.Lab_Class != '':
                lab.append(code.Lab_Class)
                lab_leccode.append(code.Lab_Lec_Period)


        return Lecturer_Sub, lab, lab_leccode

    if batch == 277:
        c = Electrical_First.objects.all()
        Lecturer_Sub = []
        lab = []
        lab_leccode = []
        for code in c:
            Lecturer_Sub.append(code.Lecturer_Subject)
            if code.Lab_Class != '':
                lab.append(code.Lab_Class)
                lab_leccode.append(code.Lab_Lec_Period)


        return Lecturer_Sub, lab, lab_leccode
    
    if batch == 275:
        c = Electrical_Third.objects.all()
        Lecturer_Sub = []
        lab = []
        lab_leccode = []
        for code in c:
            Lecturer_Sub.append(code.Lecturer_Subject)
            if code.Lab_Class != '':
                lab.append(code.Lab_Class)
                lab_leccode.append(code.Lab_Lec_Period)


        return Lecturer_Sub, lab, lab_leccode

    if batch == 274:
        c = Electrical_Fourth.objects.all()
        Lecturer_Sub = []
        lab = []
        lab_leccode = []
        for code in c:
            Lecturer_Sub.append(code.Lecturer_Subject)
            if code.Lab_Class != '':
                lab.append(code.Lab_Class)
                lab_leccode.append(code.Lab_Lec_Period)


        return Lecturer_Sub, lab, lab_leccode



from django.shortcuts import render, redirect

# Create your views here.

def signin(request):
    return render(request,'login.html', {'title': 'login'})


def adjustment_reprocess(request):
    return render(request,'adjustment_reprocess.html', {'title': 'adjustment_reprocess'})


def asrsusageReport(request):
    return render(request,'asrsusageReport.html', {'title': 'asrsusageReport'})


def changepassword(request):
    return render(request,'changepassword.html', {'title': 'changepassword'})


def company(request):
    return render(request,'company.html', {'title': 'company'})


def detailreport(request):
    return render(request,'detailreport.html', {'title': 'detailreport'})


def employee(request):
    return render(request,'employee.html', {'title': 'employee'})


def header(request):
    return render(request,'header.html', {'title': 'header'})


def material_inword(request):
    return render(request,'material_inword.html', {'title': 'material_inword'})
    

def material_outword(request):
    return render(request,'material_outword.html', {'title': 'material_outword'})


def material_reload(request):
    return render(request,'material_reload.html', {'title': 'material_reload'})


def pallet_q(request):
    return render(request,'pallet_q.html', {'title': 'pallet_q'})


def pallet(request):
    return render(request,'pallet.html', {'title': 'pallet'})


def q_status(request):
    return render(request,'q_status.html', {'title': 'q_status'})


def screen_storage(request):
    return render(request,'screen_storage.html', {'title': 'screen_storage'})


def shifts(request):
    return render(request,'shifts.html', {'title': 'shifts'})


def summaryreport(request):
    return render(request,'summaryreport.html', {'title': 'summaryreport'})


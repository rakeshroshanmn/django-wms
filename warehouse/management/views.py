from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def adjustment_reprocess(request):
    return render(request,'adjustment_reprocess.html', {'title': 'adjustment_reprocess'})

@login_required
def asrsusageReport(request):
    return render(request,'asrsusageReport.html', {'title': 'asrsusageReport'})

@login_required
def changepassword(request):
    return render(request,'changepassword.html', {'title': 'changepassword'})

@login_required
def company(request):
    return render(request,'company.html', {'title': 'company'})

@login_required
def detailreport(request):
    return render(request,'detailreport.html', {'title': 'detailreport'})

@login_required
def employee(request):
    return render(request,'employee.html', {'title': 'employee'})

@login_required
def header(request):
    return render(request,'header.html', {'title': 'header'})

@login_required
def material_inword(request):
    return render(request,'material_inword.html', {'title': 'material_inword'})
    
@login_required
def material_outword(request):
    return render(request,'material_outword.html', {'title': 'material_outword'})

@login_required
def material_reload(request):
    return render(request,'material_reload.html', {'title': 'material_reload'})

@login_required
def pallet_q(request):
    return render(request,'pallet_q.html', {'title': 'pallet_q'})

@login_required
def pallet(request):
    return render(request,'pallet.html', {'title': 'pallet'})

@login_required
def q_status(request):
    return render(request,'q_status.html', {'title': 'q_status'})

@login_required
def screen_storage(request):
    return render(request,'screen_storage.html', {'title': 'screen_storage'})

@login_required
def shifts(request):
    return render(request,'shifts.html', {'title': 'shifts'})

@login_required
def summaryreport(request):
    return render(request,'summaryreport.html', {'title': 'summaryreport'})


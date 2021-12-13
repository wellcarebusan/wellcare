from django.shortcuts import render, redirect, HttpResponse
from .models import employee
from .forms import employeeFoam

################ 회사소개 ##############
def index(request):
    context = {}
    return render(request, 'main/index.html', context)

def greeting(request):
    context = {}
    return render(request, 'main/greeting.html', context)

def status(request):
    context = {}
    return render(request, 'main/status.html', context)

def way(request):
    context = {}    
    return render(request, 'main/way.html', context)

################ 장기요양보험 ##############

def insurance(request):
    context = {}
    return render(request, 'main/insurance.html', context)

def procedure(request):
    context = {}
    return render(request, 'main/insurance_procedure.html', context)

def enroll(request):
    context = {}    
    return render(request, 'main/insurance_enroll.html', context)


################ 방문요양 ##############

def homecare(request):
    context = {}
    return render(request, 'main/homecare.html', context)

def wash(request):
    context = {}
    return render(request, 'main/homecare_wash.html', context)

################ 중산층케어 ##############

def classcare(request):
    context = {}
    return render(request, 'main/classcare.html', context)


################ 고용 ##############

def hirement(request):
    context = {}
    all_employee=employee.objects.all()
    context['all_employee']=all_employee

    if request.POST:
        form = employeeFoam(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hirement')
        else:
            context['employee_form']=form
    else: #GET Requset
        form = employeeFoam()
        context['employee_form']=form
    return render(request, 'main/hirement.html', context)


def employee_delete(request, delete_employee_id):
    context = {}
    delete_employee=employee.objects.get(id=delete_employee_id)
    delete_employee.delete()
    return redirect('hirement')

def employee_detail(request, detail_employee_id):
    context = {}
    detail_employee=employee.objects.get(id=detail_employee_id)
    context['detail_employee']=detail_employee

    return render(request, 'main/detail.html', context)


################ 24시간 돌봄 ##############

def allday(request):
    context = {}
    return render(request, 'main/allday.html', context)

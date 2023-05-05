from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from .forms import UserForm, UserProfileForm
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import UserProfile, EmployeeProfile, FinDistribution, Report
from django.db import IntegrityError
from .employee_functions.employee_functions import *

def main(request):
    return render(request, "mif/main.html")

def signupuser(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        user_profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and user_profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            user_profile = user_profile_form.save(commit=False)
            user_profile.user = user
            user_profile.share = 0
            user_profile.current_balance = 0
            user_profile.save()
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            login(request, user)
            return redirect('currentuser')
    else:
        user_form = UserForm()
        user_profile_form = UserProfileForm()
    return render(request, 'mif/signupuser.html', {'user_form': user_form, 'user_profile_form': user_profile_form})

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'mif/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'mif/loginuser.html', {'form': AuthenticationForm(), 'error': 'Username password did not match'})
        else:
            login(request, user)
            return redirect('currentuser')

@login_required
def currentuser(request):
    if request.method == 'POST':
        if request.POST['username'] != '':
            request.user.username = request.POST['username']
        elif request.POST['first_name'] != '':
            request.user.first_name = request.POST['first_name']
        elif request.POST['last_name'] != '':
            request.user.last_name = request.POST['last_name']
        elif request.POST['email'] != '':
            request.user.email = request.POST['email']
        elif request.POST['phone_number'] != '':
            request.user.userprofile.phone_number = request.POST['phone_number']
        elif request.POST['password'] != '':
            request.user.password = request.POST['password']
            request.user.set_password(request.user.password)
            login(request, request.user)
        else: 
            return redirect('currentuser')
        request.user.save()
        request.user.userprofile.save()
        return redirect('currentuser') 
    else:    
        user_profile = UserProfile.objects.get(user_id=request.user.id)
        calculate_current_client_income(request.user)
    return render(request, 'mif/currentuser.html', {'user_profile': user_profile})

@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('main')

def login_employee(request):
    if request.method == 'GET':
        return render(request, 'mif/login-employee.html', {'form': AuthenticationForm()})
    else:
        employee = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if employee is None:
            return render(request, 'mif/login-employee.html', {'form': AuthenticationForm()})
        else:
            login(request, employee)
            match employee.employeeprofile.position:
                case "бухгалтер":
                    return redirect('accountant')
                case "менеджер":
                    return redirect('manager')
                case "аналитик":
                    return redirect('analyst')
                case "директор":
                    return redirect('director')

@login_required
def accountant(request):
    if request.method == 'GET':
        current_value_share, change = calculate_share()
        current_income_expenses_shares, current_other_expenses, current_other_income, current_budget = get_list_income_expenses()
        employees, employee_expense = calculate_salary_employees()
        clients, client_expense = calculate_incomes_clients()
    else:
        report = Report(employee=request.POST['employee'], report=request.FILES['report'])
        report.save()
        return redirect('accountant')

    return render(request, 'mif/employees/accountant.html', {'current_value_share': current_value_share, 'change': change, 'current_income_expenses_shares': current_income_expenses_shares, 'current_other_expenses': current_other_expenses, 'current_other_income': current_other_income, 'current_budget': current_budget, 'employees': employees, 'employee_expense': employee_expense, 'clients': clients, 'client_expense': client_expense})

@login_required
def manager(request):
    if request.method == 'POST':
        if 'token' in request.POST and request.POST['token'] != '': 
            plan_obj = AnalyticalPlan.objects.get(token=request.POST['token'])
            plan_obj.is_completed = True
            plan_obj.save()
        elif ('employee' in request.POST) and ('report' in request.FILES) and request.POST['employee'] != '':
            report = Report(employee=request.POST['employee'], report=request.FILES['report'])
            report.save()
        return redirect('manager')
    else:
        plan_objects = get_analytical_plan()
    return render(request, 'mif/employees/manager.html', {'plan_objects': plan_objects})

@login_required
def analyst(request):
    if request.method == 'POST':
        plan_obj = AnalyticalPlan(name_obj=request.POST['name_obj'], status=request.POST['status'], quantity=request.POST['quantity'], datetime=request.POST['datetime'], token=generate_token())
        plan_obj.save()
        return redirect('analyst')
    else: 
        plan_objects = get_analytical_plan()
        date1, date2, articles_arr_1, articles_arr_2 = parse_news() 
    return render(request, 'mif/employees/analyst.html', {'plan_objects': plan_objects, 'date1': date1, 'date2': date2, 'articles_arr_1': articles_arr_1, 'articles_arr_2': articles_arr_2})

@login_required
def director(request):
    calculate_remaining_number_shares()
    fin_struct = FinDistribution.objects.get(id=1)
    reports = Report.objects.all()
    return render(request, 'mif/employees/director.html', {'fin_struct': fin_struct, 'reports': reports})


def view_pdf(request, report_id):
    report = Report.objects.get(id=report_id)
    return HttpResponse(content=report.report, content_type='application/pdf')
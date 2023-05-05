from ..models import *
from datetime import datetime
import random
import requests 
from bs4 import BeautifulSoup


def calculate_share():
    fin_struct = FinDistribution.objects.get(id=1)
    new_current_value_share = fin_struct.current_net_asset_value / fin_struct.all_shares
    date = datetime.now().date()
    valueshare_obj, created = ValueShare.objects.get_or_create(value_share=fin_struct.current_value_share, date=date)
    if created == False:
        valueshare_obj.value_share = new_current_value_share
        valueshare_obj.save()
    fin_struct.current_value_share = new_current_value_share
    fin_struct.save()
    change = ((new_current_value_share / fin_struct.current_value_share) - 1) * 100
    
    return [new_current_value_share, change]

def get_list_income_expenses():
    income_expenses_shares = DepositoryInstance.objects.all()
    other_expenses = OtherExpense.objects.all()
    other_income = OtherIncome.objects.all()
    fin_struct = FinDistribution.objects.get(id=1)

    for entry in income_expenses_shares:
        if entry.is_processed == False: 
            entry.amount = entry.share_price * entry.number_shares
            entry.is_processed = True
            entry.save()
            if entry.status == 'покупка': 
                fin_struct.budget -= (entry.amount)
            else:
                fin_struct.budget += (entry.amount)

    for entry in other_expenses:
        if entry.is_processed == False:
            fin_struct.budget -= entry.amount_spent
            entry.is_processed = True
            entry.save()

    for entry in other_income:
        if entry.is_processed == False:
            fin_struct.budget += entry.amount_received 
            entry.is_processed = True
            entry.save()

    current_budget = fin_struct.budget
    fin_struct.save()

    return [income_expenses_shares, other_expenses, other_income, current_budget]

def calculate_salary_employees():
    employees = EmployeeProfile.objects.all()
    employee_expense = 0

    for employee in employees:
        employee_expense += employee.salary

    return [employees, employee_expense]

def calculate_incomes_clients():
    clients = UserProfile.objects.exclude(share__exact=None)    
    fin_struct = FinDistribution.objects.get(id=1)
    client_expense = 0

    for client in clients:
        client.current_balance = client.share * fin_struct.current_net_asset_value
        client_expense += client.current_balance

    return [clients, client_expense]

def get_analytical_plan():
    plan_objects = AnalyticalPlan.objects.exclude(is_completed__exact=True)
    
    return plan_objects

def generate_token():
    token = ''
    symbols = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()0123456789')
    for i in range(0, 16):
        token += random.choice((symbols))

    return token

def parse_news():
    url = 'https://1prime.ru/finance/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    articles = soup.find_all("article", class_="rubric-list__article")

    class Date:
        def __init__(self, date):
            self.date = date

    dates = soup.find_all("div", class_="rubric-list__date-delimiter")
    date1_text = dates[0].text
    date2_text = dates[1].text
    date1 = Date(date1_text)
    date2 = Date(date2_text)
    dates_dict = {"Января": "01", "Февраля": "02", "Марта": "03", "Апреля": "04", "Мая": "05", "Июня": "06", "Июля": "07", "Августа": "08", "Сентября": "09", "Октября": "10", "Ноября": "11", "Декабря": "12"}
    articles_arr_1 = []
    articles_arr_2 = []

    class Article:
        def __init__(self, time, h2, href):
            self.time = time
            self.h2 = h2
            self.href = href

    for article in articles:
        time = article.find("time")
        date = time.get("datetime")[5:10]
        h2 = article.find("h2")
        href = article.find("a").get("href")
        new_article = Article(time.text, h2.text, href)
        if date[:2] == dates_dict[date1_text[3:]] and date[3:] == date1_text[:2]:
            articles_arr_1.append(new_article)
        elif date[:2] == dates_dict[date2_text[3:]] and date[3:] == date2_text[:2]:
            articles_arr_2.append(new_article)

    return [date1, date2, articles_arr_1, articles_arr_2]

def calculate_current_client_income(user):
    client = UserProfile.objects.get(user_id=user.id)
    fin_struct = FinDistribution.objects.get(id=1)
    client.current_balance = client.share * fin_struct.current_net_asset_value
    client.save()

def calculate_remaining_number_shares():
    fin_struct = FinDistribution.objects.get(id=1)
    clients = UserProfile.objects.exclude(share=0) & UserProfile.objects.exclude(is_processed=True)
    
    for client in clients:
        fin_struct.shares_left = fin_struct.shares_left - client.share * fin_struct.all_shares
        client.is_processed = True
        client.save()

    fin_struct.save()    
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    phone_number = models.CharField(max_length=20, null=True)
    share = models.FloatField(null=True, blank=True)
    current_balance = models.FloatField(null=True, blank=True)
    bank_card_number = models.CharField(max_length=50, null=True, blank=True)
    opened_personal_account = models.BooleanField(default=False)
    recent_purchase = models.IntegerField(null=True)
    is_processed = models.BooleanField(default=False)
    
class EmployeeProfile(models.Model):
    employee = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    phone_number = models.CharField(max_length=20)
    is_staff = models.BooleanField(default=True)
    position = models.CharField(max_length=150)
    salary = models.FloatField(null=True)
    bank_card_number = models.CharField(max_length=50, null=True)
    passport = models.FileField(upload_to='employee_documents/passports/')
    employment_record = models.FileField(upload_to='employee_documents/employment_records/')
    state_pension_insurance_policy = models.FileField(upload_to='employee_documents/spi_policies/')
    taxpayer_identification_code = models.FileField(upload_to='employee_documents/ti_codes/')

class FinDistribution(models.Model):
    current_net_asset_value = models.FloatField(null=True)
    current_value_share = models.FloatField(null=True)
    budget = models.FloatField(null=True)
    all_shares = models.IntegerField(null=True)
    shares_left = models.IntegerField(null=True)

class DepositoryInstance(models.Model):
    stock_company = models.CharField(max_length=500, null=True)
    share_price = models.FloatField(null=True)
    number_shares = models.IntegerField(null=True)
    status = models.CharField(max_length=20, null=True)
    amount = models.FloatField(null=True, blank=True)
    datetime = models.DateTimeField(null=True)
    is_processed = models.BooleanField(default=False)

class StockStorage(models.Model):
    stock_company = models.CharField(max_length=500, null=True)
    number_shares = models.IntegerField(null=True)
    share_in_portfolio = models.FloatField(null=True)

class OtherExpense(models.Model):
    name_expense = models.CharField(max_length=300, null=True)
    amount_spent = models.FloatField(null=True, default=0)
    date = models.DateField(null=True)
    is_processed = models.BooleanField(default=False)

class OtherIncome(models.Model):
    name_income = models.CharField(max_length=300, null=True)
    amount_received = models.FloatField(null=True)
    date = models.DateField(null=True)
    is_processed = models.BooleanField(default=False)

class Report(models.Model):
    employee = models.CharField(max_length=150, null=True)
    report = models.FileField(upload_to='records/')
    date = models.DateField(auto_now=True)

class AnalyticalPlan(models.Model):
    name_obj = models.CharField(max_length=300, null=True)
    status = models.CharField(max_length=20, null=True)
    quantity = models.IntegerField(null=True)
    datetime = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    token = models.CharField(max_length=100, null=True)

class ValueShare(models.Model):
    value_share = models.FloatField(null=True)
    date = models.DateField(null=True)

class NetAssetValue(models.Model):
    net_asset_value = models.FloatField(null=True)
    date = models.DateField(null=True)



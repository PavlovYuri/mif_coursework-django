from django.contrib import admin
from django.contrib.auth.models import User
from .models import *

admin.site.register(UserProfile)
admin.site.register(EmployeeProfile)
admin.site.register(FinDistribution)
admin.site.register(DepositoryInstance)
admin.site.register(OtherExpense)
admin.site.register(OtherIncome)
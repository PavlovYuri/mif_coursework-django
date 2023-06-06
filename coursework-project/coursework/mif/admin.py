from django.contrib import admin
from .models import *

admin.site.register(UserProfile)
admin.site.register(EmployeeProfile)
admin.site.register(FinDistribution)
admin.site.register(DepositoryInstance)
admin.site.register(OtherExpense)
admin.site.register(OtherIncome)
admin.site.register(StockStorage)
admin.site.register(Report)
admin.site.register(AnalyticalPlan)
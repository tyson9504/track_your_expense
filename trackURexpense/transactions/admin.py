from django.contrib import admin

from configuration.admin import admin_site
from transactions.models import Expenditure, Income


class ExpenditureAdmin(admin.ModelAdmin):
    list_display = ('id', 'user','amount', 'date')


class IncomeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user','amount', 'date')


admin_site.register(Expenditure, ExpenditureAdmin)
admin_site.register(Income, IncomeAdmin)

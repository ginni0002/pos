from django.contrib import admin
from trans.models import transactions
from import_export.admin import ImportExportModelAdmin
# Register your models here.
@admin.register(transactions)
class TransactionsAdmin(ImportExportModelAdmin):
    pass

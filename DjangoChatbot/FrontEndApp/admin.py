from django.contrib import admin
from .models import Client,ParticularClient,BankWorker,BusinessClient,User,Account,SavingAccount,CheckingAccount,CreditCard,Transaction,Beneficiary
# Register your models here.


admin.site.register(ParticularClient)
admin.site.register(BusinessClient)
admin.site.register(BankWorker)
admin.site.register(User)
admin.site.register(SavingAccount)
admin.site.register(CheckingAccount)
admin.site.register(CreditCard)
admin.site.register(Beneficiary)
admin.site.register(Transaction)

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
from django.db.models.signals import post_save


class Client(models.Model):
    phone = models.IntegerField(blank=True)
    location = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=50, blank=True)


class ParticularClient(Client):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    cin = models.IntegerField()
    sexe = models.CharField(max_length=10)


class BusinessClient(Client):
    name = models.CharField(max_length=30)
    crn = models.IntegerField()  # Company Registration Number


class BankWorker(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    location = models.CharField(max_length=50, blank=True)
    phone = models.IntegerField(blank=True)
    cin = models.IntegerField()
    available = models.BooleanField()


class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    Client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
    BankWorker = models.ForeignKey(BankWorker, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.username


User = get_user_model()


class Account(models.Model):
    account_number = models.IntegerField(primary_key=True)
    BIC = models.CharField(max_length=60)
    IBAN = models.CharField(max_length=60)
    balance = models.FloatField()
    creationDate = models.DateField()
    isSuspended = models.BooleanField()
    Client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)


class SavingAccount(Account):
    annualInterestRate = models.IntegerField()


class CheckingAccount(Account):
    insufficientFundsFee = models.FloatField()


class CreditCard(models.Model):
    type = models.CharField(max_length=20)
    cardNumber = models.IntegerField()
    dateDue = models.DateField()
    amountDue = models.FloatField()
    regularPayment = models.FloatField()
    CheckingAccount = models.ForeignKey(CheckingAccount, on_delete=models.SET_NULL, null=True, blank=True)

class Beneficiary(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.DO_NOTHING, null=False,related_name="client_id")
    beneficiary_client_id = models.ForeignKey(Client, on_delete=models.DO_NOTHING, null=False,related_name="beneficiary_client_id")



class Transaction(models.Model):
    sender = models.ForeignKey(Account, on_delete=models.DO_NOTHING, null=False, related_name="sender_id")
    beneficiary = models.ForeignKey(Account, on_delete=models.DO_NOTHING, null=False,
                                       related_name="beneficiary_id")
    amount = models.FloatField()
    date = models.DateField()

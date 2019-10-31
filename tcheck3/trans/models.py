from django.db import models

# Create your models here.
import datetime as dt

class transactions(models.Model):
	transaction_id=models.IntegerField(primary_key=True,default=1)
	title=models.CharField(max_length=20)
	datetime=models.DateTimeField(default=dt.datetime.now,blank=True)
	TNcash=models.BooleanField()
	TNcard=models.BooleanField()
	amount=models.IntegerField(blank=False,default=None)
class transet(models.Model):
	transaction=models.ForeignKey(transactions,on_delete=models.CASCADE)
	datetime=models.DateField(auto_now=True,blank=True)
	total_amount=models.IntegerField()

	def __str__(self):
			
			return self.title

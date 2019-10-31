from django.shortcuts import render,get_object_or_404
from trans.models import transactions
import datetime as dt
import csv
from django.http import Http404
from .forms import transform

# Create your views here.
def create_view(request):
	form=transform(request.POST or None)
	if form.is_valid():
		print('yes its valid')
		form.save()
	context={
		'form':form,
			}
	if request.method=='POST':
		print('from insert view yes method is post')
	dict2=request.POST
	with open(r'templates/abc1.csv','a') as csvfile2:
		wrt2=csv.writer(csvfile2)
		for key,value in dict2.items():
			wrt2.writerow([key,value])
	return render(request,'create.html',context)
def index_view(request):
	obj=transactions.objects.all()
	list1=['title','transaction_id','datetime','TNcash','TNcard','amount']
	context2={
	    'obj':obj,
        'list1':list1,  
        
	}
	return render(request,'index.html',context2)
def detail_view(request,my_id):
	list1=['title','transaction_id','datetime','TNcash','TNcard','amount']
	obj=get_object_or_404(transactions,transaction_id=my_id)
	context={
        'obj':obj ,
			
            }
	return render(request,'detail.html',context)

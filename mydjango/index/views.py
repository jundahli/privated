from django.shortcuts import render
from django.http import HttpResponse
import csv

# Create your views here.

def index(request):
    return HttpResponse('hello world')

def mydate(request,year,month,day):
    return HttpResponse(str(year)+'/'+str(month)+'/'+str(day))

def myyear(request,year):
    return render(request,'myyear.html')

def myyear_dict(request,year,month):
    return render(request,'myyear_dict.html',{'month':month})

def download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;filename="somefilename.csv"'
    writer = csv.writer(response)
    writer.writerow(['First row','A','B','C'])
    return response
from django.shortcuts import render
import datetime

def home(request):
	nowtime = datetime.datetime.now()
	return render(request,'portfolio/home.html',{'time':nowtime})

def works(request):
	return render(request,'portfolio/works.html',{})
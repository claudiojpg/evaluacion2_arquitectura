from django.shortcuts import render


def home (request):
    context={}
    return render(request,'ev2/home.html',context)
from django.shortcuts import render

# Create your views here.
def mainpage(request):
    return render(request,'pages/mainpage.html')

def company(request):
    return render(request, 'pages/company_info.html')

def history(request):
    return render(request, 'pages/history.html')

def target(request):
    return render(request, 'pages/target.html')

def business_area(request):
    return render(request, 'pages/business_area.html')

def information(request):
    return render(request, 'pages/information.html')
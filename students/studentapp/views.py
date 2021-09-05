from django.shortcuts import render
from .models import USER
# Create your views here.
def listone(request):
    try:
        unit = USER.objects.get(cName = "YB")
    except:
        errormessage = '(error message!)'
    return render(request,'listone.html',locals())

def listall(request):
    student = USER.objects.all().order_by('id')
    return render(request, 'listall.html', locals())

def listall2(request):
    student = USER.object.all().order_by('id')
    return render(request, 'listall2.html',locals())

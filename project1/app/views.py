from django.shortcuts import render


# Create your views here.
def jinja_tag(request):
    d={'name':'anil','age':22,'gender':'male'}
    return render(request,'jinja.html',d)
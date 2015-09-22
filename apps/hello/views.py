from django.shortcuts import render
from hello.models import Devinfo

""" Subscribe developer information view to return all fields of the models into the html page """


def devinfo_view(request):
    devinfo_data = Devinfo.objects.get(pk=1)
    return render(request, 'home.html', {"devinfo_data": devinfo_data})

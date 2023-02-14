from django.shortcuts import render
from CRUDFirst.models import EmpModel
from django.contrib import messages
from CRUDFirst.forms import EmpForms
from django.db.models import Q
from django.db.models import Value as V
from django.http import HttpResponse
import json
from django.core.serializers.json import DjangoJSONEncoder


def showemp(request):
    """Show Class
    """
    name = request.GET.get('name')
    sort = request.GET.get('sort')
    sort_type = request.GET.get('sort_type')
    showall = EmpModel.objects.all()
    if request.user.is_authenticated:
        if name:
            showall = EmpModel.objects.filter(
                empname__icontains=name
            ).values()
        if sort:
            showall = SortUpId(showall, sort, sort_type)
        # showall = some_function(showall, sort)
        # showall_json = json.dumps(list(showall), cls=DjangoJSONEncoder)
        # return render(request, 'Index.html', {"data": showall_json})
        return render(request, 'Index.html', {"data": showall})
    else:
        return render(request, 'Index.html', )

    # return HttpResponse({'foo': 'bar'})
# print(showall_json)


def insertemp(request):
    """ins class
    """
    if request.method == 'POST':
        if request.POST.get('empname') and request.POST.get('email') and request.POST.get('occuapation') and request.POST.get('salary') and request.POST.get('gender'):
            saverecord = EmpModel()
            saverecord.empname = request.POST.get('empname')
            saverecord.email = request.POST.get('email')
            saverecord.occuapation = request.POST.get('occuapation')
            saverecord.salary = request.POST.get('salary')
            saverecord.gender = request.POST.get('gender')
            saverecord.save()
            messages.success(request, 'employ11' +
                             saverecord.empname + ' is saved successfully')
    return render(request, 'Insert.html')


# value_sort = 0


# сделать переменную динамическую, которая будет
def SortUpId(showall, sort_param, sort_type):
    # постоянно изменяться на обратное значение,
    """Sort"""
    # global value_sort  # сделать инверсию по сортпарам(синтаксис)
    if sort_type == 'abc':
        return showall.order_by(sort_param)
    return showall.order_by('-' + sort_param)
    # if (value_sort % 2 == 0):
    #     sortupId = showall.order_by(sort_param)
    # elif (value_sort % 2 != 0):
    #     sortupId = showall.order_by("-" + sort_param)

    # value_sort = value_sort + 1

    # return sortupId


def find_Slaves(request):
    """Find"""
    query = request.GET.get('search_phrase')
    find_empname = EmpModel.objects.filter(
        empname__icontains=query
    ).values()
    return render(request, 'find.html', {"data": find_empname})


def Editemp(request, id):
    """Edit"""
    editempobj = EmpModel.objects.get(id=id)
    return render(request, 'Edit.html', {"EmpModel": editempobj})


def updateemp(request, id):
    Updateemp = EmpModel.objects.get(id=id)
    form = EmpForms(request.POST, instance=Updateemp)
    if form.is_valid():
        form.save()
        messages.success(request, "Record update successfully")
        return render(request, 'Edit.html', {"EmpModel": Updateemp})


def deleteemp(request, id):
    Delemp = EmpModel.objects.get(id=id)
    Delemp.delete()
    showdata = EmpModel.objects.all()
    return render(request, 'Index.html', {'data': showdata})

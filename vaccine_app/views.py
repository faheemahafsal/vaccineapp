
from django.shortcuts import render,redirect
from .models import Task
from .forms import Vaccinationforms

# Create your views here.
def task_view(request):
    obj1=Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('name')
        centre=request.POST.get('centre')
        dose=request.POST.get('dose')
        date=request.POST.get('date')
        obj=Task(name=name,centre=centre,dose=dose,date=date)
        obj.save()

    return render(request,'task_view.html',{'obj1':obj1})

def delete(request,registrationid):
    task=Task.objects.get(id=registrationid)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html',{'task':task} )


def update(request,id):
    task=Task.objects.get(id=id)
    form=Vaccinationforms(request.POST or None,instance = task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'task':task,'form':form})
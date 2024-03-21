from django.shortcuts import render,redirect
from .models import Contactinfo

from .contactform import Contactform

# Create your views here.
def index(request):
    contactinfo= Contactinfo.objects.all() 
    context={
        'contactinfo':contactinfo,
     }
    return render(request,"index.html",context)


def create(request):
    if(request.method=="POST"):
        name=request.POST['name']
        number=request.POST['number']
        form=Contactinfo(name=name,number=number)
        form.save()
        print(form)
        print(type(form))
        return redirect("/")
    return render(request,"index.html")

def update(request,id):
    d=Contactinfo.objects.get(id=id)
    if(request.method=='POST'):      
        d.name= request.POST['name']
        d.number=request.POST['number']
        print(d.name,d.number,"gh")
        d.save()
        print("update page edit page with after values ",d.name,d.number)
        
        return redirect('index')
    print(" u pdate page edit page with before values ",d.name,d.number)
    return render(request,"update.html",{'d':d})
    
    




def delete(request,id):
    print(id+"deleted")
    d= Contactinfo.objects.get(id=id)
    d.delete()
    return redirect("/")






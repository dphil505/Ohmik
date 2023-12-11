from django.shortcuts import render, HttpResponse
from django.contrib.messages import get_messages
from django.contrib import messages


# Create your views here.
def main(request):
    return render(request,"main_dev.html")

def home(request):
    testNames=['a', 'b', 'c']
    analysis_types=["DCIR", "Discharge Capability", "SOC-OCV", "Heat-generation", "dQdV", "Cycling"]
    return render(request,'home.html', {'test_name':testNames, 'analysis_type':analysis_types})

def cellTrack(request):
    return render(request,'cellTrackingMain.html')

#@csrf_exempt
def supplierRegit(request):
    messages.info(request, "You are not allowed")
    if request.method == 'POST':
        sname = request.POST.get('sname') 
        saddress=request.POST.get('saddress')

        print(sname)
        print(saddress)

    return render(request,'supplier.html')

def modelRegit(request):
    messages.info(request, "You are not allowed")
    btypes=['Pouch', 'Cylindrical', 'Module', 'Sub-Module', 'Pack']
    if request.method == 'POST':
        sname = request.form.get('supplier_name')
        btype=request.form.get('btype')
        mname = request.form.get('mname')
        ah=request.form.get('ah') 
        wh=request.form.get('whpo') 
        maxv=request.form.get('maxv') 
        minv=request.form.get('minv') 
        dimen=request.form.get('dimen') 
        weight=request.form.get('wei')
    
    context={'btype':btypes}


    return render(request,'model.html',context)

'''def modelRegit(request):
    messages.info(request, "You are not allowed")
    btypes=['Pouch', 'Cylindrical', 'Module', 'Sub-Module', 'Pack']
    if request.method == 'POST':
        sname = request.form.get('supplier_name')
        btype=request.form.get('btype')
        mname = request.form.get('mname')
        ah=request.form.get('ah') 
        wh=request.form.get('whpo') 
        maxv=request.form.get('maxv') 
        minv=request.form.get('minv') 
        dimen=request.form.get('dimen') 
        weight=request.form.get('wei')
    
    context={'btype':btypes}


    return render(request,'model.html',context)'''
from django.shortcuts import render
from testapp.models import product
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from testapp.forms import addPostFormProduct

def getData(request):
    allProducts=product.objects.all()
    list=[]
    for i in allProducts:
        i=[i.pName,str(i.pDescription),str(i.pPrice)]
        list+=[i]
    records={'rec':list}
    return JsonResponse(records)

@csrf_exempt
def insertData(request):
    mess = 'ok'
    try:
        jsonData = json.loads(request.body)
        name = jsonData['name']
        description = jsonData['description']
        price = jsonData['price']
        newProduct = product(pName=name,pDescription=description,pPrice=price)
        newProduct.save()
    except Exception as err:
        mess=str(err)
    return JsonResponse({'mess':mess})

def index(request):
    form=addPostFormProduct()
    return render(request, "testapp/index.htm",{'form':form})
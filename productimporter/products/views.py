from django.shortcuts import render, HttpResponse
from .forms import ProductsForm, DocumentForm
import requests
import pandas as pd
from . import models
import csv
# Create your views here.
def product_form_view(request):
    if request.method=="POST":
        form=ProductsForm(request.POST)
        #todo need to write logic
    else:
        form=ProductsForm()
    context={
        'form':form
    }
    return render(request,'firstpage.html',context)


def upload_files_view(request):
    try:
        if request.method=="POST":
            form=DocumentForm(request.POST,request.FILES)
            form.save()
            form.save_to_db()
            return render(request,'index.html')
        else:
            form=DocumentForm()
        context={
            'form':form
        }
        return render(request,'secondpage.html',context)
    except StopIteration:
        print("exception occurred")
    finally:
        print("done")
    
def show_files_view(request):
    if request.method=="GET":
        products=models.Products.objects.all()
        context={
            'products':products
        }
        return render(request,'thirdpage.html',context)
    else:
        return HttpResponse("<h1>No data found</h1>")

def drop_product_data_view(request):
    if request.method=="GET":
        models.Products.objects.all().delete()
        return HttpResponse("<p>Successfully deleted</p>")
def get_csv_view(request):
    if request.method=="GET":
        data=pd.read_csv('./media/data/products.csv',low_memory=False)
        context={
            'data':data
        }
    return render(request,'sixthpage.html',context)


def search_product(request):
    if request.method=="POST":
        context={
        'name':request.POST.get('name'),
        'sku':request.POST.get('sku'),
        'description':request.POST.get('description'),
        'flag':request.POST.get('flag')
        }
        url = 'http://127.0.0.1:8000/graphql/'
        json=None
        
        r = requests.post(url=url, json=json)
        print(r)
        return render(request,'fifthpage.html',context)
    else:
        form=ProductsForm()
    context={
        'form':form
    }
    return render(request,'fourthpage.html',context)

from django.shortcuts import render
from django.shortcuts import HttpResponse
from banks.models import pnb
from banks.models import hdfc
from django.db import connection
# Create your views here.

def Home(request):
    return render(request,'home.html')

def t_pnb(request):
    return render(request,'pnb.html')

def t_hdfc(request):
    return render(request,'hdfc.html')

def form_pnb(request):
    return render(request,'pnb_form.html')
    

def Submit_pnb(request):
    data=request.POST
    with connection.cursor() as cursor:
        cursor.execute("select balance from banks_pnb WHERE id=(SELECT max(id) FROM banks_pnb)")
        bal=cursor.fetchone()
        
    if(bal==None):
        money=float(data["Deposit"])
    elif(data["Withdrawal"]=="-"):
        money=float(bal[0])+float(data["Deposit"])
    elif(data["Deposit"]=="-"):
        money= float(bal[0])-float(data["Withdrawal"])
    
    db=pnb(Date=data["Date"],Description=data["Description"],Withdrawal=data["Withdrawal"],Deposit=data["Deposit"],Balance=money)
    db.save() 

    return render(request,'pnb.html')

def Submit_hdfc(request):
    data=request.POST
    with connection.cursor() as cursor:
        cursor.execute("select balance from banks_hdfc WHERE id=(SELECT max(id) FROM banks_hdfc)")
        bal=cursor.fetchone()
        #print("balence is :{}".format(bal))
        
    if(bal==None):
        money=float(data["Deposit"])
    elif(data["Withdrawal"]=="-"):
        money=float(bal[0])+float(data["Deposit"])
    elif(data["Deposit"]=="-"):
        money= float(bal[0])-float(data["Withdrawal"])
    
    db=hdfc(Date=data["Date"],Description=data["Description"],Withdrawal=data["Withdrawal"],Deposit=data["Deposit"],Balance=money)
    db.save() 

    return render(request,'hdfc.html')

def form_hdfc(request):
    return render(request,'hdfc_form.html')

def table_pnb(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT Date,Description,Withdrawal,Deposit,Balance from (SELECT * FROM banks_pnb ORDER BY id DESC LIMIT 10) as myalias")
        data=cursor.fetchall()
    heading=["Date","Description","Withdrawal","Deposit","Balance"]
    context={
            "form":data,
            "heading":heading
        }
    #print(context["heading"])
    return render(request,"pnb_table.html",context)

def table_hdfc(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT Date,Description,Withdrawal,Deposit,Balance from(SELECT * FROM banks_hdfc ORDER BY id DESC LIMIT 10) as myalias")
        data=cursor.fetchall()
    heading=["Date","Description","Withdrawal","Deposit","Balance"]
    context={
            "form":data,
            "heading":heading
        }
    print(context["heading"])
    return render(request,"hdfc_table.html",context)
    
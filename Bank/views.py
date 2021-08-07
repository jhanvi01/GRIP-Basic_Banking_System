from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer, Transaction

# Create your views here.

def index(request):
    #To view all customers at the start and also to select the receiver
    id1=request.GET.get('id1')
    customers= Customer.objects.all
    return render(request,'index.html',{'customers':customers,'id1':id1})

def viewcust(request):
    #To view selected customer's details
    id= request.GET.get('id')
    customer= Customer.objects.get(id=id)
    return render(request,'view.html',{'customer':customer})

def transact(request):
    #To take the amount and perform transaction
    if request.method=="POST":
        id1=request.GET.get('id1')
        id2=request.GET.get('id2')
        amount=int(request.POST['amount'])
        
        print("POST",id1,id2,amount)

        #Doing the transaction
        customer1= Customer.objects.get(id=id1)
        customer2= Customer.objects.get(id=id2)   
        
        c1_bal=customer1.current_balance -amount 
        c2_bal=customer2.current_balance +amount 
        Customer.objects.filter(id=id1).update(current_balance=c1_bal)
        Customer.objects.filter(id=id2).update(current_balance=c2_bal)

        #saving data in transactions table
        T = Transaction.objects.create(sender_id=customer1.id,sender_name=customer1.name,receiver_id=customer2.id,receiver_name=customer2.name,Amount=amount)
        T.save()

        #Showing Suucess page
        return render(request,'success.html')


    id1=request.GET.get('id1')
    id2=request.GET.get('id2')
    print(id1,id2)
    customer1= Customer.objects.get(id=id1)
    customer2= Customer.objects.get(id=id2)
    # return HttpResponse("Transaction Page")
    return render(request,'transact.html',{'cust1':customer1,'cust2':customer2})


def viewtransact(request):
    #To view all Transactions and display it
    transactions= Transaction.objects.all
    return render(request,'showTransact.html',{'transactions':transactions})
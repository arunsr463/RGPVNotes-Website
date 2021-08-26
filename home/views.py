from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact, Login
from cryptography.fernet import Fernet

def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def login(request):
    if request.method=="POST":
        emailid=request.POST.get('emailid')
        password=request.POST.get('password')
        message=password
        key = Fernet.generate_key()
        fernet = Fernet(key)
        password = fernet.encrypt(message.encode())
        # decMessage = fernet.decrypt(encMessage).decode()
        login = Login(emailid=emailid,password=password,date=datetime.today())
        login.save()

    return render(request,"login.html")

def registration(request):
    return render(request,"registration.html")

def computerScienceIndexPage(request):
    return render(request,"computerScienceIndexPage.html")

def service(request):
    return render(request,"service.html")


def contact(request):
    if request.method=="POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        mail=request.POST.get('mail')
        state=request.POST.get('state')
        city=request.POST.get('city')
        desc=request.POST.get('desc')
        contact = Contact(fname=fname,lname=lname,mail=mail,state=state,city=city,desc=desc,date=datetime.today())
        contact.save()

    return render(request,"contact.html")

def computerScience(request):
    return render(request,"computerScience.html")
def civil(request):
    return render(request,"civil.html")

def mechanical(request):
    return render(request,"mechanical.html")

def informationAndTechnology(request):
    return render(request,"informationAndTechnology.html")

def basicElectricalAndElectronics(request):
    return render(request,"basicElectricalAndElectronics.html")

def engineeringDrawing(request):
    return render(request,"engineeringDrawing.html")

def engineeringChemistry(request):
    return render(request,"engineeringChemistry.html")

def mathematics1(request):
    return render(request,"mathematics1.html")

def english(request):
    return render(request,"english.html")

def engineeringPhysics(request):
    return render(request,"engineeringPhysics.html")

def mathematics2(request):
    return render(request,"mathematics2.html")

def basicMechanicalEngineering(request):
    return render(request,"basicMechanicalEngineering.html")

def basicCivilAndMechanicsEngineering(request):
    return render(request,"basicCivilAndMechanicsEngineering.html")

def basicComputerEngineering(request):
    return render(request,"basicComputerEngineering.html")


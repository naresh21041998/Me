from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login,logout,authenticate
from .models import *
# Create your views here.






##### from models class ###

def Home(request):
    ###### About data ###

    xx=About.objects.values("dob","web","phone","age","degree","email","freelancing","notes","city","heading","intro")
    abt=[]
    for i in xx:
        abt.append(i)

    dob=abt[0]["dob"]
    web=abt[0]["web"]
    phone = abt[0]["phone"]
    age = abt[0]["age"]
    degree = abt[0]["degree"]
    email = abt[0]["email"]
    freelancing = abt[0]["freelancing"]
    notes = abt[0]["notes"]
    city=abt[0]["city"]
    heading=abt[0]["heading"]
    intro=abt[0]["intro"]


    ####### Skills Data ######
    all_skill=Skills.objects.values("skill","percent")
    list_skill=[]
    for i in all_skill:
        list_skill.append(i)
    skill=list_skill[0]["skill"]
    percent=list_skill[0]["percent"]

    abt_dict = {
        "dob": dob, "web": web, "phone": phone, "age": age, "degree": degree, "email": email,
        "freelancing": freelancing, "notes": notes,
        "city": city, "heading": heading, "intro": intro,
        "skill": skill, "percent": percent
    }
################ Interest ##########

    #list_interest=[interest1,interest2,interest3,interest4,interest5,interest6,interest7,interest8,interest9]

    return render(request, "index.html", abt_dict)


def PortFolio(request):
    return render(request, "portfolio-details.html")


def Test(request):
    return render(request,"test.html")



def AdminForm(request):
    error=False
    last_username=""
    if request.method=="POST":
        dict=request.POST
        un=dict["username"]
        pwd=dict["password"]
        usr=authenticate(username=un,password=pwd)
        if usr!=None:
            login(request,usr)
            return HttpResponse("welcome,start data uploading  : "+un)

        error=True
        last_username=un
        error_dict={"error":error,"last_username":last_username}
        return render(request,"admin_form.html",error_dict)

    return render(request,"admin_form.html")

def ContactForm(request):
    if request.method=="POST":
        if request.user.is_authenticated:
               dict=request.POST
               name=dict["name"]
               email=dict["email"]
               subject=dict["subject"]
               msg=dict["message"]
               print("dataaa",name,email,msg)
               thanks="Thank You !"
               thanks_dict={"thanks":thanks}
               return redirect(request,"admin_form.html",thanks_dict)



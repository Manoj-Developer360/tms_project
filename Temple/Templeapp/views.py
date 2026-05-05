import random
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import LoginUser

# Create your views here.

def home(request):
    return render(request,'home.html')

# LOGIN VIEW

def login(request):

    if request.method == "POST":

        mobile = request.POST.get("mobile")

        # CHECK ALREADY EXISTS

        if LoginUser.objects.filter(
            Mobile_number=mobile
        ).exists():

            messages.error(
                request,
                "This number already exists"
            )

            return redirect("login")

        # GENERATE RANDOM OTP

        otp = random.randint(100000, 999999)

        # STORE SESSION

        request.session['mobile'] = mobile

        request.session['otp'] = str(otp)

        # SHOW OTP IN TERMINAL

        print("OTP:", otp)

        messages.success(
            request,
            "OTP Sent Successfully"
        )

        return redirect("otp")

    return render(request, "login.html")


# OTP VERIFY VIEW

def otp(request):

    if request.method == "POST":

        entered_otp = request.POST.get("otp")

        session_otp = request.session.get("otp")

        # OTP VALIDATION

        if entered_otp == session_otp:

            mobile = request.session.get("mobile")

            # STORE MOBILE NUMBER IN DATABASE

            LoginUser.objects.create(

                Mobile_number=mobile

            )

            # LOGIN SESSION

            request.session['is_logged_in'] = True

            return redirect("home")

        else:

            messages.error(
                request,
                "Incorrect OTP"
            )

            return redirect("otp")

    return render(request, "otp.html")


# LOGOUT VIEW

def logout(request):

    mobile = request.session.get("mobile")

    # DELETE MOBILE NUMBER FROM DATABASE

    LoginUser.objects.filter(

        Mobile_number=mobile

    ).delete()

    # CLEAR SESSION

    request.session.flush()

    return redirect("login")

# views.py

def profile(request):

    # CHECK LOGIN

    if not request.session.get('is_logged_in'):

        return redirect("login")

    # GET MOBILE NUMBER

    mobile = request.session.get("mobile")

    context = {

        "mobile": mobile

    }

    return render(request,"profile.html",context)

def darshan (request):
    return render (request,'darshan.html')
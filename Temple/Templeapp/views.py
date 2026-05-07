import random
import uuid

from django.shortcuts import render, redirect 
from django.contrib import messages
from django.contrib.auth import logout

from .models import (

    LoginUser,

    DarshanBooking,

    SevaBooking,

    Donation

)

# HOME PAGE

def home(request):
    return render(request, 'home.html')

def festival(request):
    return render(request, 'festival.html')


# LOGIN PAGE

def login(request):

    if request.method == "POST":

        name = request.POST.get("name")

        email = request.POST.get("email")

        mobile = request.POST.get("mobile")

        aadhar = request.POST.get("aadhar")

        address = request.POST.get("address")

        # CHECK MOBILE EXISTS

        if LoginUser.objects.filter(
            mobile_number=mobile
        ).exists():

            messages.error(
                request,
                "Mobile Number Already Registered"
            )

            return redirect("login")

        # CHECK AADHAR EXISTS

        if LoginUser.objects.filter(
            aadhar_number=aadhar
        ).exists():

            messages.error(
                request,
                "Aadhar Number Already Registered"
            )

            return redirect("login")

        # GENERATE OTP

        otp = random.randint(100000, 999999)

        print("OTP :", otp)

        # STORE SESSION

        request.session['otp'] = str(otp)

        request.session['name'] = name

        request.session['email'] = email

        request.session['mobile'] = mobile

        request.session['aadhar'] = aadhar

        request.session['address'] = address

        messages.success(
            request,
            "OTP Sent Successfully"
        )

        return redirect("otp")

    return render(request, "login.html")


# OTP VERIFY

def otp(request):

    if request.method == "POST":

        entered_otp = request.POST.get("otp")

        session_otp = request.session.get("otp")

        # CHECK OTP

        if entered_otp == session_otp:

            user = LoginUser.objects.create(

                name=request.session.get("name"),

                email=request.session.get("email"),

                mobile_number=request.session.get("mobile"),

                aadhar_number=request.session.get("aadhar"),

                address=request.session.get("address")

            )

            # LOGIN SESSION

            request.session['user_id'] = user.id

            request.session['is_logged_in'] = True

            messages.success(
                request,
                "Login Successful"
            )

            # REDIRECT TO HOME PAGE

            return redirect("home")

        else:

            messages.error(
                request,
                "Incorrect OTP"
            )

            return redirect("otp")

    return render(request, "otp.html")


# PROFILE PAGE

def profile(request):

    if not request.session.get('is_logged_in'):

        return redirect("login")

    user_id = request.session.get("user_id")

    user = LoginUser.objects.get(id=user_id)

    # FETCH BOOKINGS

    darshan_bookings = DarshanBooking.objects.filter(
        user=user
    ).order_by('-id')

    seva_bookings = SevaBooking.objects.filter(
        user=user
    ).order_by('-id')

    donations = Donation.objects.filter(
        user=user
    ).order_by('-id')

    context = {

        "user": user,

        "darshan_bookings": darshan_bookings,

        "seva_bookings": seva_bookings,

        "donations": donations

    }

    return render(
        request,
        "profile.html",
        context
    )


# DARSHAN BOOKING

def darshan(request):

    if not request.session.get('is_logged_in'):

        return redirect("login")

    user_id = request.session.get("user_id")

    user = LoginUser.objects.get(id=user_id)

    if request.method == "POST":

        full_name = request.POST.get("full_name")

        mobile = request.POST.get("mobile")

        aadhar = request.POST.get("aadhar")

        darshan_date = request.POST.get("darshan_date")

        slot = request.POST.get("slot")

        booking_id = "DSN" + str(
            random.randint(10000,99999)
        )

        DarshanBooking.objects.create(

            user=user,

            full_name=full_name,

            mobile_number=mobile,

            aadhar_number=aadhar,

            darshan_date=darshan_date,

            slot=slot,

            booking_id=booking_id
        )

        messages.success(
            request,
            "Darshan Ticket Booked Successfully"
        )

        return redirect("profile")

    return render(request, 'darshan.html')


# SEVA BOOKING

def seva_booking(request):

    if not request.session.get('is_logged_in'):

        return redirect("login")

    user_id = request.session.get("user_id")

    user = LoginUser.objects.get(id=user_id)

    if request.method == "POST":

        full_name = request.POST.get("full_name")

        mobile = request.POST.get("mobile")

        seva_name = request.POST.get("seva_name")

        seva_time = request.POST.get("seva_time")

        seva_date = request.POST.get("seva_date")

        booking_id = "SEVA" + str(
            random.randint(10000,99999)
        )

        SevaBooking.objects.create(

            user=user,

            full_name=full_name,

            mobile_number=mobile,

            seva_name=seva_name,

            seva_time=seva_time,

            seva_date=seva_date,

            booking_id=booking_id
        )

        messages.success(
            request,
            "Seva Booked Successfully"
        )

        return redirect("profile")

    return render(request, 'seva.html')


# DONATION

def donation(request):

    if not request.session.get('is_logged_in'):

        return redirect("login")

    user_id = request.session.get("user_id")

    user = LoginUser.objects.get(id=user_id)

    if request.method == "POST":

        full_name = request.POST.get("full_name")

        mobile = request.POST.get("mobile")

        amount = request.POST.get("amount")

        payment_id = str(uuid.uuid4())

        Donation.objects.create(

            user=user,

            full_name=full_name,

            mobile_number=mobile,

            amount=amount,

            payment_id=payment_id
        )

        messages.success(
            request,
            "Donation Successful"
        )

        return redirect("profile")

    return render(request, 'donation.html')


# LOGOUT

def logout(request):

    request.session.flush()

    messages.success(
        request,
        "Logout Successful"
    )

    return redirect("home")



# DOWNLOAD DARSHAN TICKET

def download_darshan(request, id):

    if not request.session.get('is_logged_in'):

        return redirect('login')

    booking = DarshanBooking.objects.get(id=id)

    context = {

        'type': 'Darshan Ticket',

        'booking': booking
    }

    return render(
        request,
        'download.html',
        context
    )


# DOWNLOAD SEVA TICKET

def download_seva(request, id):

    if not request.session.get('is_logged_in'):

        return redirect('login')

    booking = SevaBooking.objects.get(id=id)

    context = {

        'type': 'Seva Ticket',

        'booking': booking
    }

    return render(
        request,
        'download.html',
        context
    )


# DOWNLOAD DONATION RECEIPT

def download_donation(request, id):

    if not request.session.get('is_logged_in'):

        return redirect('login')

    booking = Donation.objects.get(id=id)

    context = {

        'type': 'Donation Receipt',

        'booking': booking
    }

    return render(
        request,
        'download.html',
        context
    )

def user_logout(request):

    if request.user.is_authenticated:

        # Delete user related bookings
        DarshanBooking.objects.filter(user=request.user).delete()

        SevaBooking.objects.filter(user=request.user).delete()

        Donation.objects.filter(user=request.user).delete()

        # Delete user account
        request.user.delete()

    logout(request)

    return redirect('login')
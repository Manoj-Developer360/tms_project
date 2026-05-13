# models.py

from django.db import models


# LOGIN USER

class LoginUser(models.Model):

    name = models.CharField(
        max_length=200
    )

    email = models.EmailField()

    mobile_number = models.CharField(
        max_length=10,
        unique=True
    )

    aadhar_number = models.CharField(
        max_length=12,
        unique=True
    )

    address = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.name


# DARSHAN BOOKING

class DarshanBooking(models.Model):

    SLOT_CHOICES = (

        ("6AM - 8AM", "6AM - 8AM"),

        ("8AM - 10AM", "8AM - 10AM"),

        ("10AM - 12PM", "10AM - 12PM"),

        ("4PM - 6PM", "4PM - 6PM"),

    )

    user = models.ForeignKey(
        LoginUser,
        on_delete=models.CASCADE
    )

    full_name = models.CharField(
        max_length=200
    )

    mobile_number = models.CharField(
        max_length=10
    )

    aadhar_number = models.CharField(
        max_length=12
    )

    darshan_date = models.DateField()

    slot = models.CharField(
        max_length=50,
        choices=SLOT_CHOICES
    )

    booking_id = models.CharField(
        max_length=30
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.booking_id


# SEVA MODEL

class SevaBooking(models.Model):

    SEVA_CHOICES = (

        ("Suprabhata Seva - 3:00 AM",
         "Suprabhata Seva - 3:00 AM"),

        ("Thomala Seva - 4:00 AM",
         "Thomala Seva - 4:00 AM"),

        ("Archana - 4:30 AM",
         "Archana - 4:30 AM"),

        ("Kalyanotsavam - 10:00 AM",
         "Kalyanotsavam - 10:00 AM"),

        ("Unjal Seva - 7:00 PM",
         "Unjal Seva - 7:00 PM"),

        ("Sahasra Deepalankara Seva - 5:30 PM",
         "Sahasra Deepalankara Seva - 5:30 PM"),

    )

    user = models.ForeignKey(
        LoginUser,
        on_delete=models.CASCADE
    )

    full_name = models.CharField(
        max_length=200
    )

    mobile_number = models.CharField(
        max_length=10
    )

    seva_name = models.CharField(
        max_length=200,
        choices=SEVA_CHOICES
    )

    seva_date = models.DateField()

    booking_id = models.CharField(
        max_length=30
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.booking_id


# DONATION MODEL

class Donation(models.Model):

    user = models.ForeignKey(
        LoginUser,
        on_delete=models.CASCADE
    )

    full_name = models.CharField(
        max_length=200
    )

    email = models.EmailField()

    mobile_number = models.CharField(
        max_length=10
    )

    address = models.TextField()

    amount = models.IntegerField()

    payment_id = models.CharField(
        max_length=100
    )

    donated_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.payment_id
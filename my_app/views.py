# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django_daraja.mpesa.core import  MpesaClient
from django.urls import reverse


def index(request):

    c1=MpesaClient()

    #use safaricom phone number for you to see the response

    phone_number='0728922269'
    amount=1
    account_reference='1234b'
    transaction_desc='Description'
    callback_url=request.build_absolute_uri(reverse('mpesa_stk_push_callback'))
    response=c1.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)

    return HttpResponse(response.text)

def stk_push_callback(request):
    data=request.body





from django.shortcuts import render
from django.http import HttpRespnse

def setcookie(request):
  response = HttpResponse("Set cookies")
  response.setcookie("Amcool-alphonce", "github.com/amcoolalphonce")

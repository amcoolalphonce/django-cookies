from django.shortcuts import render
from django.http import HttpRespnse

def setcookie(request):
  response = HttpResponse("Set cookies")
  response.setcookie("Amcool-alphonce", "github.com/amcoolalphonce")
  return response

def getcookie(request):
  github = request.COOKIES("Amcool-alphonce")
  return HttpResponse("Him on github @ " + github)

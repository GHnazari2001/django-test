from django.shortcuts import render
from django.views import View



#def messageView(request):
   # return render(request, "home.html")
   
class MessageView(View):
   def get(self, request):
       return render(request,'home.html')
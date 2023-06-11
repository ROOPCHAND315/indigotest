from django.shortcuts import render
from core.models import Book_ticket

# Create your views here.
# def home(request):
#     ticket=Book_ticket.objects.all()
#     print("fffffffffffffff",ticket)

#     return render(request,'index.html',{'ticket':ticket})

def home(request):
    if request.method=="POST":
        post=Book_ticket()
        post.boofrom=request.POST['boofrom']
        post.bookTo=request.POST['bookTo']
        post.dep_date=request.POST['dep_date']
        post.save()
        return render(request, 'index.html')
    if request.method=="GET":
        ticket=Book_ticket.objects.all()
        return render(request,'index.html',{'ticket':ticket})
    else:
        return render(request, 'index.html')
    
     
# def getdata(request):
#     ticket=Book_ticket.objects.all()
#     # print("fffffffffffffff",ticket)

#     return render(request,'index.html',{'ticket':ticket})   
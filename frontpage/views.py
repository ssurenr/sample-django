from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required()
def index(request):
    if request.user.is_staff:
        return render(request, "index.html", context={})
    else:
        return HttpResponse('Permission Denied')

from django.shortcuts import render
from accounts.models import User
def about_us(request):
    members = User.objects.all()
    context = {'members': members}
    return render(request, "about_us.html", context)

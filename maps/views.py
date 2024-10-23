from django.shortcuts import render
#from django.contrib.auth.decorators import login_required

#@login_required(login_url='/auth/login')
def show_map(request):
    return render(request, "map/map.html")
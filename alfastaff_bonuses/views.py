from django.shortcuts import render

def profile(request):
    return render(request, template_name='alfastaff-bonuses/profile.html')
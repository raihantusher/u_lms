from django.shortcuts import  render
from django.http import HttpResponseRedirect
def Home(request):
    return render(request, 'home.html')


def advertisment(request):
    return HttpResponseRedirect("https://crowdfire.grsm.io/o0fqs0u2n22f")

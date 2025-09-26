from django.http import HttpResponse, JsonResponse

def home(request):
    return HttpResponse("hello")


def about(request):
    return HttpResponse("we are at the abut page")

def contact(request):
    return HttpResponse("we are at the contact page")





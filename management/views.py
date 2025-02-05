from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "management/index.html")


def organizers(request):
    return render(request, "management/organizers.html")


def participants(request):
    return render(request, "management/participants.html")


def analytics_home(request):
    return render(request, "management/analytics_home.html")


def analytics_event_detail(request):
    return render(request, "management/analytics_event_detail.html")
  

def create_event(request):
    return render(request, "management/create_event.html")

  
def request_create_event(request):
    return render(request, "management/request_create_event.html")
  
  
def event_publish_requests(request):
    return render(request, "management/organizer_event_submit_requests.html")


def event_publish_request_detail(request):
    return render(request, "management/organizer_event_submit_detail.html")


def event_submit_dashboard(request):
    return render(request, "management/event_submit_dashboard.html")


def event_submit_detail(request):
    return render(request, "management/event_submit_detail.html")

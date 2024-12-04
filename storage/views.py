from django.http import JsonResponse
from .models import Request, Response


def get_all_requests(request):
    requests = Request.objects.all().values()
    return JsonResponse(list(requests), safe=False)


def get_all_responses(request):
    responses = Response.objects.all().values()
    return JsonResponse(list(responses), safe=False)

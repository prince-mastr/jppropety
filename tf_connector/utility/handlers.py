from django.http import JsonResponse


def handle_404_as_JSON(request, exc):
    return JsonResponse({
        'status': 404,
        'msg': "The requested resource wasn't found!",
        'data': []
    })

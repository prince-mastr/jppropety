from rest_framework.exceptions import APIException
from rest_framework.views import exception_handler
from rest_framework import status


class Service500Exception(APIException):
    status_code = 500
    default_detail = 'Internal Server was Ocurred!.'
    default_code = None


def custom_service_ex_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None and response.status_code == \
            status.HTTP_500_INTERNAL_SERVER_ERROR:
        response.data["status"] = status.HTTP_500_INTERNAL_SERVER_ERROR
        response.data["msg"] = str(exc)
        response.data["data"] = None
        del response.data["detail"]
    return response

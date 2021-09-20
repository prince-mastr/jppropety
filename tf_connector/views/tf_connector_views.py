from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.http import HttpResponse
from django.template import loader
from django.db import transaction
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
import datetime
import logging
from tf_connector.service.connectors import ConnectorHandler
from tf_connector.serializers.connector_serializer import CreateConnectorSerializer, UpdateConnectorSerializer, RemoveConnectorSerializer, SearchConnectorSerializer

# Create your views here.

logger = logging.getLogger(__name__)

class CreateConnectorAPI(APIView):
    """Associates requested connections to groups"""
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        try:
            requested_data = request.data
            serializer = CreateConnectorSerializer(
                data=requested_data,
                context={"request": request}
            )
            if serializer.is_valid():
                try:
                    new_connector, new_connector_info = ConnectorHandler().create_connector_new(
                        request, serializer.data)
                    if new_connector:
                        return Response({
                            "status": 200,
                            "data": new_connector_info
                        }, status=status.HTTP_200_OK)
                except:
                    return Response({
                        "status": 500,
                        "data": "Invalid Parameters Provided!"
                    }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                return Response({
                    "status": 400,
                    "data": "Invalid remark  Provided!"
                }, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(
                {
                    "status": 500,
                    "data": "Error Creating Connector"
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UpdateConnectorAPI(APIView):
    """Associates requested connections to groups"""
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        try:
            requested_data = request.data
            serializer = UpdateConnectorSerializer(
                data=requested_data,
                context={"request": request}
            )

            if serializer.is_valid():
                try:
                    update_connector, update_connector_info = ConnectorHandler().update_connector(request, serializer.data)
                    if update_connector:
                        return Response({
                            "status": 200,
                            "data": update_connector_info
                        }, status=status.HTTP_200_OK)

                    elif update_connector_info == "No Query Found":
                        return Response({
                            "status": 200,
                            "data": update_connector_info
                        }, status=status.HTTP_200_OK)
                    else:
                        return Response({
                        "status": 400,
                        "data": ""
                        }, status=status.HTTP_400_BAD_REQUEST)


                except Exception as e:
                    return Response({
                        "status": 500,
                        "data": " Service Failed"
                    }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                return Response({
                    "status": 400,
                    "data": serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(
                {
                    "status": 500,
                    "data": "Error Updating Connector"
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GetConnectorAPI(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request, connectorid):
        try:
            if request.user.is_authenticated:
                try:
                    get_connection , get_connection_info = ConnectorHandler().get_connector(request, connectorid)
                    if get_connection:
                        return Response({
                            "status": 200,
                            "data": ""
                        }, status=status.HTTP_200_OK)

                    elif get_connection_info == "No Query Found":
                        return Response({
                        "status": 400,
                        "data": get_connection_info
                    }, status=status.HTTP_400_BAD_REQUEST)
                    else:
                        return Response({
                        "status": 400,
                        "data": ""
                        }, status=status.HTTP_400_BAD_REQUEST)

                except Exception as e:

                    return Response({
                        "status": 401,
                        "data": ""
                    }, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({
                    "status": 403,
                    "data": "Access Forbidden"
                }, status=status.HTTP_403_FORBIDDEN)

        except Exception as e:
            return Response(
                {
                    "status": 500,
                    "data": "Error finding  Connector"
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GetConnectorByNameAPI(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request, name):
        try:
            if request.user.is_authenticated:
                try:
                    get_connection , get_connection_info = ConnectorHandler().get_connector_by_name(request, name)
                    if get_connection:
                        return Response({
                            "status": 200,
                            "data": ""
                        }, status=status.HTTP_200_OK)

                    elif get_connection_info == "No Query Found":
                        return Response({
                        "status": 400,
                        "data": get_connection_info
                    }, status=status.HTTP_400_BAD_REQUEST)
                    else:
                        return Response({
                        "status": 400,
                        "data": ""
                        }, status=status.HTTP_400_BAD_REQUEST)

                except Exception as e:

                    return Response({
                        "status": 400,
                        "data": ""
                    }, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({
                    "status": 403,
                    "data": "Access Forbidden"
                }, status=status.HTTP_403_FORBIDDEN)

        except Exception as e:
            return Response(
                {
                    "status": 500,
                    "data": "Error finding  Connector"
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GetConnectorStatusAPI(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request, connectorid):
        try:
            if request.user.is_authenticated:
                try:
                    get_connection , get_connection_info = ConnectorHandler().get_connector_status(request, connectorid)
                    if get_connection:
                        return Response({
                            "status": 200,
                            "data": ""
                        }, status=status.HTTP_200_OK)

                    elif get_connection_info == "No Query Found":
                        return Response({
                        "status": 400,
                        "data": get_connection_info
                    }, status=status.HTTP_400_BAD_REQUEST)
                    else:
                        return Response({
                        "status": 400,
                        "data": get_connection_info
                    }, status=status.HTTP_400_BAD_REQUEST)

                except:
                    return Response({
                        "status": 500,
                        "data": "Error finding Connector"
                    },
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                   
            else:
                return Response({
                    "status": 403,
                    "data": "Access Forbidden"
                }, status=status.HTTP_403_FORBIDDEN)

        except:
            return Response(
                {
                    "status": 500,
                    "data": "Error finding Connector"
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GetConnectorStatusByNameAPI(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request, name):
        try:
            if request.user.is_authenticated:
                try:
                    get_connection , get_connection_info = ConnectorHandler().get_connector_status_by_name(request, name)
                    if get_connection:
                        return Response({
                            "status": 200,
                            "data": ""
                        }, status=status.HTTP_200_OK)

                    elif get_connection_info == "No Query Found":
                        return Response({
                        "status": 400,
                        "data": get_connection_info
                    }, status=status.HTTP_400_BAD_REQUEST)
                    else:
                        return Response({
                        "status": 400,
                        "data": get_connection_info
                    }, status=status.HTTP_400_BAD_REQUEST)

                except:
                    return Response({
                        "status": 500,
                        "data": "Error finding Connector"
                    },
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                   
            else:
                return Response({
                    "status": 403,
                    "data": "Access Forbidden"
                }, status=status.HTTP_403_FORBIDDEN)

        except:
            return Response(
                {
                    "status": 500,
                    "data": "Error finding Connector"
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class SearchAPI(APIView):
    # permission_classes = [IsAuthenticated,]
    def put(self, request):
        try:
            if request.user.is_authenticated:

                try:
                    requested_data = request.data
                    serializer = SearchConnectorSerializer(
                        data=requested_data,
                        context={"request": request}
                    )
                    if serializer.is_valid():
                        connector_search, connector_search_info = ConnectorHandler.search(request, serializer.data)
                        if connector_search:
                            return Response({
                                "status": 200,
                                "data": connector_search_info
                            }, status=status.HTTP_200_OK)

                        elif connector_search_info == "No connector Found":
                            return Response({
                                "status": 200,
                                "data": connector_search_info
                            }, status=status.HTTP_200_OK)
                        else:
                            return Response({
                            "status": 400,
                            "data": connector_search_info
                        }, status=status.HTTP_400_BAD_REQUEST)
                    else:
                        return Response({
                            "status": 400,
                            "data":serializer.errors
                        }, status=status.HTTP_403_FORBIDDEN)


                except Exception as e:
                    return Response({
                        "status": 500,
                        "data": "Invalid  Provided!"
                    }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                return Response({
                    "status": 403,
                    "data": "Access Forbidden"
                }, status=status.HTTP_403_FORBIDDEN)

        except:
            return Response(
                {
                    "status": 500,
                    "data": "Error finding Connector"
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class RemoveConnectorAPI(APIView):
    permission_classes = [IsAuthenticated, ]

    def put(self, request):
        try:
            if request.user.is_authenticated:
                try:
                    requested_data = request.data
                    serializer = RemoveConnectorSerializer(
                        data=requested_data,
                        context={"request": request}
                    )
                    if serializer.is_valid():
                        remove_connector, remove_connector_info = ConnectorHandler().remove_connector(request, serializer.data)
                        if remove_connector:
                            return Response({
                                "status": 200,
                                "data": remove_connector_info
                            }, status=status.HTTP_200_OK)

                        elif remove_connector_info == "No Query Found":
                            return Response({
                            "status": 400,
                            "data": remove_connector_info
                        }, status=status.HTTP_400_BAD_REQUEST)
                        else:
                            return Response({
                            "status": 400,
                            "data": remove_connector_info
                        }, status=status.HTTP_400_BAD_REQUEST)
                    else:
                        return Response({
                            "status": 400,
                            "data":serializer.errors
                        }, status=status.HTTP_400_BAD_REQUEST)
                    
                except:
                    return Response({
                        "status": 400,
                        "data": "Invalid  Provided!"
                    }, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({
                    "status": 403,
                    "data": "Access Forbidden"
                }, status=status.HTTP_403_FORBIDDEN)

        except:
            return Response(
                {
                    "status": 500,
                    "data": "Error removing Coneector"
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def custom404(request, exception=None):
    return Response({
        'status_code': 404,
        'error': 'The resource was not found'
    })

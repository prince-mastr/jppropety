from django.urls import path 
from tf_connector.views.tf_connector_views import CreateConnectorAPI , UpdateConnectorAPI , GetConnectorAPI, GetConnectorByNameAPI , SearchAPI , GetConnectorStatusAPI, GetConnectorStatusByNameAPI ,RemoveConnectorAPI ,custom404

urlpatterns = [
    
    path("create/", CreateConnectorAPI().as_view(), name="create_connector"),
    path("get/<int:connectorid>/",GetConnectorAPI.as_view(), name="get_connector"),
    path("get/<str:name>/",GetConnectorByNameAPI.as_view(), name="get_connector_by_name"),
    path("get/status/<int:connectorid>/", GetConnectorStatusAPI.as_view(), name="get_connector_status"),
    path("get/status/<str:name>/", GetConnectorStatusByNameAPI.as_view(), name="get_connector_status_by_name"),
    path("search/", SearchAPI.as_view(), name="search_connector"),
    path("update/", UpdateConnectorAPI.as_view(), name="update_connector"),
    path("remove/", RemoveConnectorAPI.as_view(), name="remove_connector"),

]

handler404 = custom404

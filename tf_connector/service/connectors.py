from django.db import models
from django.contrib.auth.models import User
import logging
from collections import deque
from django.db import transaction
import datetime
from django.shortcuts import HttpResponse
import datetime
import time
from datetime import date
from tf_connector.models.models import TFconnector
from django.core.paginator import Paginator
from django.db.models import Q


logger = logging.getLogger(__name__)

class ConnectorHandler:

    logger.info("Inside Connector Handler")
    
    def create_connector_new(self, request, data):
        try:
            NewTFconnector = TFconnector.objects.create(
                connector_name = data["Connectorname"],
                connector_desc = data["Connectordesc"],
                connector_value = data["Connectorvalue"],
                connector_remark = data["Connectorremark"],
                create_date = datetime.date.today(),
                update_date = datetime.date.today(),
                create_by_id = 0,
                is_visible = 1,
                is_active = 1,
                is_verified = 1,
                is_approved = 1,
                is_archived = 1,
                is_dormant = 1,
                is_so_delete = 1
                )
            NewTFconnector.save()

            return True , NewTFconnector.id

        except Exception as e:
            print(str(e))
            msg = "Create Connector Failed"
            logger.exception(msg + str(e))
            
            return False , msg

    def update_connector(self,request,data):
        try:
            
            connector = TFconnector.objects.get(id=1)
            
            if data["connectorname"] is not None:
                connector.connector_name = data["connectorname"],
            if data["connectordesc"] is not None:
                connector.connector_desc = data["connectorname"],
            if data["connectorvalue"] is not None:
                connector.connector_value = data["connectorvalue"]
            if data["connectorremark"] is not None:
                connector.connector_remark = data["connectorremark"]
            
            connector.update_by_id = request.User.id
            connector.update_date = datetime.date.today()

            connector.save()

            return True
            
        except TFconnector.DoesNotExist:
            msg = "No Query Found"
            logger.exception(msg)
            return False, msg
        except Exception as e:
            msg = "Update Connector Failed"
            logger.exception(msg + str(e))
            return False , msg

    def get_connector(self,request,connectorid):
        try:
            connector = TFconnector.objects.get(id=connectorid)
            context = {
                'connector_name' : connector.connector_name,
                'connector_desc' :connector.connector_desc
            }
            return True , context
        except TFconnector.DoesNotExist:
            msg = "No Query Found"
            logger.exception(msg)
            return False, msg

        except Exception as e:
            msg = "get Connector Failed"
            logger.exception(msg + str(e))
            return False, msg

    def get_connector_by_name(self,request,name):
        try:
            connector = TFconnector.objects.get(connector_name = name)
            context = {
                'connector_name' : connector.connector_name,
                'connector_desc' :connector.connector_desc
            }
            return True , context
        except TFconnector.DoesNotExist:
            msg = "No Query Found"
            logger.exception(msg)
            return False, msg

        except Exception as e:
            msg = "get Connector Failed"
            logger.exception(msg + str(e))
            return False, msg

    def get_connector_status(self,request,connectorid):
        try:
            connector = TFconnector.objects.get(id=connectorid)
            return True, connector.is_active

        except TFconnector.DoesNotExist:
            msg = "No Query Found"
            logger.exception(msg)
            return False, msg

        except Exception as e:
            msg = "get Connector Failed"
            logger.exception(msg + str(e))
            return False, msg

    def get_connector_status_by_name(self,request,name):
        try:
            connector = TFconnector.objects.get(connector_name = name)
            context = {
                'connector_name' : connector.connector_name,
                'connector_desc' :connector.connector_desc
            }
            return True , context
        except TFconnector.DoesNotExist:
            msg = "No Query Found"
            logger.exception(msg)
            return False, msg

        except Exception as e:
            msg = "get Connector Failed"
            logger.exception(msg + str(e))
            return False, msg

    def search(request, search_query):
        query = search_query
        query_list = query.split()
        search_list = []
        
        try:
            for q in query_list:
                search_list = search_list + list(TFconnector.objects.filter(
                    Q(connector_name__icontains=q)))
            for q in query_list:
                search_list = search_list + list(TFconnector.objects.filter(
                    Q(connector_desc__icontains=q)))
            if len(search_list) is 0:
                return False , "No connector Found"

            page = request.GET.get('page', 1)
            paginator = Paginator(search_list, 18)
            try:
                products = paginator.page(page)
            except PageNotAnInteger:
                products = paginator.page(1)
            except EmptyPage:
                products = paginator.page(paginator.num_pages)

            context = {
                'search_list' :products,
                "page_obj":paginator.page(1)
            }
            return True , context
        except:
            msg= "Configuration Search Failed"
            return False , msg

    def remove_connector(self, request, connectorid):
        try:
            connector = TFconnector.objects.get(id=connectorid)
            connector.is_so_delete = "True"
            msg = "Remove Successful"
            return True, msg
        
        except TFconnector.DoesNotExist:
            msg = "No Query Found"
            logger.exception(msg)
            return False, msg

        except Exception as e:
            msg = "Get Connectror Status Failed"
            logger.exception(msg + str(e))
            return False, msg    






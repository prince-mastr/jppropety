from rest_framework import fields
from rest_framework import serializers


class CreateConnectorSerializer(serializers.Serializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True,
                                              default=serializers
                                              .CurrentUserDefault())
    Connectorname = fields.CharField(
        required=True,
    )
    Connectorvalue = fields.CharField(
        required=False,
    )
    Connectordesc = fields.CharField(
        required=False
    )
    Connectorremark = fields.CharField(
        required=False
    )

    def validate_connector_name(self, value):
        if len(value) >= 2 and len(value) <= 20:
            return value
        raise serializers.ValidationError("The connector \
            name should not be greater then 20 and less than 2.")

    def validate_connector_value(self, value):
        if len(value) >= 2 and len(value) <= 1000:
            return value
        raise serializers.ValidationError("The connector \
            value should not be greater then 1000 and less than 2.")

    def validate_connector_desc(self, value):
        if len(value) >= 2 and len(value) <= 100:
            return value
        raise serializers.ValidationError("The connector \
            desc should not be greater then 100 and less than 2.")

    def validate_connector_remark(self, value):
        if len(value) >= 2 and len(value) <= 100:
            return value
        raise serializers.ValidationError("The connector \
            should not be greater then 100 and less than 2.")
    


class UpdateConnectorSerializer(serializers.Serializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True,
                                              default=serializers
                                              .CurrentUserDefault())
    connectorid = fields.IntegerField(
        required=True,
    )

    connectorname = fields.CharField(
        required=True,
    )
    connectorvalue = fields.CharField(
        required=False,
    )
    connectordesc = fields.CharField(
        required=False
    )
    connectorremark = fields.CharField(
        required=False
    )
    
    def validate_connector_name(self, value):
        if len(value) >= 2 and len(value) <= 20:
            return value
        raise serializers.ValidationError("The connector \
            name should not be greater then 20 and less than 2.")

    def validate_connector_value(self, value):
        if len(value) >= 2 and len(value) <= 1000:
            return value
        raise serializers.ValidationError("The connector \
            value should not be greater then 1000 and less than 2.")

    def validate_connector_desc(self, value):
        if len(value) >= 2 and len(value) <= 100:
            return value
        raise serializers.ValidationError("The connector \
            desc should not be greater then 100 and less than 2.")

    def validate_connector_remark(self, value):
        if len(value) >= 2 and len(value) <= 100:
            return value
        raise serializers.ValidationError("The connector \
            should not be greater then 100 and less than 2.")
    
class SearchConnectorSerializer(serializers.Serializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True,
                                              default=serializers
                                              .CurrentUserDefault())
    search_query = fields.CharField(
        required=True,
    )

    def validate_search_query(self, value):
        if len(value) >= 2 and len(value) <= 100:
            return value
        raise serializers.ValidationError("The search \
            should not be greater then 100 and less than 2.")


class RemoveConnectorSerializer(serializers.Serializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True,
                                              default=serializers
                                              .CurrentUserDefault())

    connector_id = fields.IntegerField(
        required=True,
    )

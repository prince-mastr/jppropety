from drf_yasg import openapi

openapi_400_Schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "status": openapi.Schema(
            description="Status code.",
            type=openapi.TYPE_INTEGER
        ),
        "msg": openapi.Schema(
            description="Message.",
            type=openapi.TYPE_STRING
        ),
        "data": openapi.Schema(
            description="Data containing cause for invalid \
                request.",
            type=openapi.TYPE_STRING
        )
    },
)

openapi_403_Schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "status": openapi.Schema(
            description="Status code.",
            type=openapi.TYPE_INTEGER
        ),
        "msg": openapi.Schema(
            description="Message.",
            type=openapi.TYPE_STRING
        ),
        "data": openapi.Schema(
            description="Data containing cause for forbidding\
            request.",
            type=openapi.TYPE_STRING
        )
    },
)

openapi_500_Schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "status": openapi.Schema(
            description="Status code.",
            type=openapi.TYPE_INTEGER
        ),
        "msg": openapi.Schema(
            description="Message.",
            type=openapi.TYPE_STRING
        ),
        "data": openapi.Schema(
            description="Data containing cause for failure",
            type=openapi.TYPE_STRING
        )
    },
)

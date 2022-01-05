from rest_framework.response import Response
from rest_framework.views import APIView
from apps.users.models import User
from apps.users.api.serializers import UserSerializer

from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes

class UserAPIView(APIView):
  
  # @extend_schema(
  #     request=UserSerializer,
  #     responses={201: UserSerializer},
  # )

  @extend_schema(
    # extra parameters added to the schema
    request=UserSerializer,
    responses={201: UserSerializer},
    parameters=[
      OpenApiParameter(name='artist', description='Filter by artist', required=False, type=str),
      OpenApiParameter(
          name='release',
          type=OpenApiTypes.DATE,
          location=OpenApiParameter.QUERY,
          description='Filter by release date',
          examples=[
              OpenApiExample(
                  'Example 1',
                  summary='short optional summary',
                  description='longer description',
                  value='1993-08-23'
              ),
              # ...
          ],
      ),
    ],
    #override default docstring extraction
    description='Texto de descripcion del endpoint',
    # provide Authentication class that deviates from the views default
    auth=None,
    # change the auto-generated operation name
    operation_id=None,
    # or even completely override what AutoSchema would generate. Provide raw Open API spec as Dict.
    operation=None,
    # attach request/response examples to the operation.
    examples=[
      OpenApiExample(
          'Example 1',
          description='longer description',
          # value=...
      ),
      # ...
    ],
  )
  def get(self, request):
    users = User.objects.all()
    ## many = True is a plural method
    users_serializer = UserSerializer(users, many = True)
    return  Response(users_serializer.data)
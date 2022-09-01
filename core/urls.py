from django.urls import path, include
from .views import MyTokenObtainPairView

# from rest_framework_simplejwt.views import (
#     TokenRefreshView,
# )


urlpatterns = [
    #path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # path('jwt/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('jwt/token/', include('djoser.urls')),
]
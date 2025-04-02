from django.contrib import admin
from django.urls import path, include
from api.views import CreateUserView, UserList, delete_user, UserDetail
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/user/register/", CreateUserView.as_view(), name="register"),
    path("api/token/", TokenObtainPairView.as_view(), name="get_token"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("api-auth/", include("rest_framework.urls")),
    path("api/", include("api.urls")),
    path("api/users/", UserList.as_view(), name="users" ),
    path("api/deleteuser/<int:pk>/", delete_user, name="user-detail"),
    path("api/user/<int:pk>/", UserDetail.as_view(), name="user-detail")
]
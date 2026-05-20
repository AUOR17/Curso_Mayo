from django.contrib import admin
from django.urls import path, include
from core.views import (
    CookieTokenObtainPairView, 
    CookieTokenRefreshView, 
    RegisterView,
    BovedaSecretaView,
    PerfilUsuarioView,
    LogoutView,
    CandidatosView, 
    LiquidarOroView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/quests/', include('quests.urls')), 
    path('api/', include('gremios.urls')),
    path('api/register/', RegisterView.as_view(), name='auth_register'),
    path('api/token/', CookieTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', CookieTokenRefreshView.as_view(), name='token_refresh'),
    path('api/logout/', LogoutView.as_view(), name='auth_logout'),
    path('api/me/', PerfilUsuarioView.as_view(), name='user_profile'), 
    path('api/boveda/', BovedaSecretaView.as_view(), name='boveda_secreta'),
    path('api/candidatos/', CandidatosView.as_view(), name='lista_candidatos'),
    path('api/usuarios/<int:user_id>/liquidar/', LiquidarOroView.as_view(), name='liquidar_oro'),
]
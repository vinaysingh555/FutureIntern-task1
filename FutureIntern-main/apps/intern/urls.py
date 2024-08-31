from django.urls import path

from apps.intern import views
from apps.intern.views import Login, Sign, logout_view, HomeView

urlpatterns = [
    path('', Login.as_view(),name='user_login'),
    path('sign/', Sign.as_view(),name='signup'),
    path('logout/user/', logout_view, name='logout_user'),
    path('dashboard/', HomeView.as_view(), name='home'),

]
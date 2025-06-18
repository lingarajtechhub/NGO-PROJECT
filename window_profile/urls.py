from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from profiles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.public_profile_create, name='public_profile_create'),
    path('admin-panel/signin/', views.admin_signin, name='admin_signin'),
    path('admin-panel/signup/', views.admin_signup, name='admin_signup'),
    path('admin-panel/signout/', views.signout, name='signout'),
    path('admin-panel/', views.profile_list, name='profile_list'),
    path('admin-panel/profile/add/', views.profile_create, name='profile_create'),
    path('admin-panel/profile/<int:pk>/', views.profile_detail, name='profile_detail'),
    path('admin-panel/profile/<int:pk>/edit/', views.profile_edit, name='profile_edit'),
    path('admin-panel/profile/<int:pk>/delete/', views.profile_delete, name='profile_delete'),
    path('admin-panel/profile/<int:pk>/print/', views.profile_print, name='profile_print'),
    path('admin-panel/print-empty-form/', views.print_empty_profile, name='print_empty_form'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.urls import path
from portal import views as portal_views 
from . import views


app_name = 'portal'

urlpatterns = [
    path('home/', portal_views.portal_home, name="portal-home"),
    path('register-class/', portal_views.register_new_standard, name="register-class"),
    path('register-class-section/', portal_views.register_new_classgroup, name="register-classgroup"),
    path('register-new-session/', portal_views.register_new_session, name="register-session"),
    path('register-exam/', portal_views.register_exam, name="register-exam"),
    path('<int:pk>/', views.StudentCardDetailView.as_view(), name='my_idcard'),


]

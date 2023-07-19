from django.urls import path
from documentary.views import documentary_list, documentary_details, register_documentary, documentary_registered
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('documentary/', documentary_list, name='documentary_list'),
    path('documentary/<int:documentary_id>/', documentary_details, name='documentary_details'),
    path('register_documentary/', register_documentary, name='register_documentary'),
    path('documentary_registered/', documentary_registered, name='documentary_registered'),
    # comment and replies URL patterns...
    path('documentary/<int:documentary_id>/submit_comment/', views.submit_comment, name='submit_comment'),
    path('documentary/<int:documentary_id>/submit_comment/<int:comment_id>/', views.submit_reply, name='submit_reply'),
]

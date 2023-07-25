from django.urls import path
from . import views

urlpatterns = [
    path('api/account/', views.account_list_create),
    path('api/account/<int:account_id>/', views.account_retrieve_update_delete),
    path('api/destination/', views.destination_list_create),
    path('api/destination/<int:destination_id>/', views.destination_retrieve_update_delete),
    path('api/account/<int:account_id>/destinations/', views.get_destinations_for_account, name='get-destinations-for-account'),
    path('server/incoming_data/', views.incoming_data, name='incoming-data'),
]


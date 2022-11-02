from django.urls import path
from .views import new_checkbalance, retrieve_checkbalance, delete_balance, new_balance, index


urlpatterns = [
      path('checkbalance/<int:id>', retrieve_checkbalance, name='retrieve'),
      path("delete-balance/<int:checkbalance_id>/<int:item_id>", delete_balance, name='delete-balance'),  
      path('new-balance', new_balance, name='new-balance'), 
      path('', index, name='home'),
      path('new', new_checkbalance, name='new')
]
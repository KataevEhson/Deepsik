from django.urls import path
from .views import *
urlpatterns = [
 path('get_name/<str:name>', get_name_of_user),
 path('priv' ,say_hello),
 path('show/<str:name>', show_photo),
 path('priv/<str:status>', otdat_chest_polzovatelu),
 path('dont/<str:name>', show_image_and_photo),
 path('', zefacebook)

]

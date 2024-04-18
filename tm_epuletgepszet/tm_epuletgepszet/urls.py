from django.contrib import admin
from django.urls import path , include 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tm_epuletgepszet_app.urls')),
    path('privacy/', include('tm_epuletgepszet_app.urls')),
    path('jobs/', include('tm_epuletgepszet_app.urls')),

]

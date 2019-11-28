from django.urls import path

from . import views

urlpatterns =[
        path('sightings/',views.sightings),
        path('<int:squirrel_id>/',views.squirrel_id),
        path('add/',views.add),
        path('stats/',views.stats),
        ]

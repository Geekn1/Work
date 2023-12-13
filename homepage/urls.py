from django.urls import path
from .views import HomePageView,AboutPageViews
urlpatterns=[
       path('about/',AboutPageViews.as_view(),name='about'),
       path('', HomePageView.as_view(), name='home')
]



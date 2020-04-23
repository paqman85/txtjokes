from django.urls import path

from .views import HomePageView, AboutPageView, ThanksView, sendjoke


urlpatterns = [
    path('about/', AboutPageView.as_view(),name='about'),
    path('', HomePageView.as_view(),name='home'),
    path('joke/', sendjoke,name='sendjoke'),
    path('thanks/', ThanksView.as_view(),name='thanks'),
    # path('sendjoke/', sendjoke,name='sendjoke')
]

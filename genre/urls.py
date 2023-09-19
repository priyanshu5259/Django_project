from django.urls import path
from.import views

urlpatterns = [
    path('',views.genre_view.as_view(),name='genre'),

    path('register/',views.UserFormView.as_view(),name='userform'),

    path('<pk>/',views.details.as_view(),name='details'),
    
    

]

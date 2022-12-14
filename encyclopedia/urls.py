from django.urls import path

from . import views

app_name = 'encyclopedia'
urlpatterns = [
    path("", views.index, name="index"),
    path('CSS', views.CSS, name='CSS'),
    path('Django', views.Django, name='Django'),
    path('Git', views.Git, name='Git'),
    path('Python', views.Python, name='Python'),
    path('HTML', views.HTML, name='HTML')
]

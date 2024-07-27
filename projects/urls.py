from rest_framework import routers
from .api import ProjectViewSet
from . import views
from django.urls import path



router= routers.DefaultRouter()
router.register('api/projects', ProjectViewSet,'projects')

urlpatterns = router.urls

urlpatterns = [
    #agregar y elminar cartas
    path('prueba/', views.prueba, name='prueba'),
]
from django.contrib import admin
from django.urls import path, include
from escola.views import CursoViewSet, AlunosViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('alunos', AlunosViewSet, basename='Alunos')
router.register('cursos', CursoViewSet, basename='Cursos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]

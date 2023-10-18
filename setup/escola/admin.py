from django.contrib import admin
from escola.models import Aluno, Curso

class Alunos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20

admin.site.register(Aluno, Alunos)

class Cursos(admin.ModelAdmin):
    list_display = ('codigo_curso', 'descricao', 'nivel')
    list_display_links = ('codigo_curso', 'descricao')
    search_fields = ('descricao',)


admin.site.register(Curso, Cursos)
    
# Register your models here.

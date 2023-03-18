from django.contrib import admin

# Para criar um usuario na area admin, executar o seguinte comando:
# ------- python manage.py createsuperuser --------------

from .models import Categoria, Contato


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone', 'email',
                    'data_criacao', 'categoria') # Mostra principais elementos
    
    list_display_links = ('id', 'nome') # Deixa clicar no id/ nome

    # list_filter = ('nome', 'sobrenome')

    list_per_page = 10 # Limita mostrar 10 elementos por pagina

    search_fields = ('nome', 'sobrenome', 'telefone') # Cria-se um campo de pesquisa


admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)




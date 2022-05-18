from django.contrib import admin
from .models import *


@admin.action(description='Ativar os selecionados')
def ativar_todos(modeladmin, request, queryset):
    queryset.update(ativa=True) #muito fácil
#isso não funciona sem uma lista actions no pessoa admin


@admin.action(description='Desativar os selecionados')
def desativar_todos(modeladmin, request, queryset):
    queryset.update(ativa=False)


class PessoaAdmin(admin.ModelAdmin):
    list_display=[
        'nome',
        'nasc', 
        'ativa'
    ]
    list_filter=[
        'ativa'
    ]
    search_fields=[
        'nome'
    ]
    actions=[
        ativar_todos,
        desativar_todos
    ]
    
admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(Contato)



#minha página favorita de fazer <3

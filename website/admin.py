from django.contrib import admin
from .models import Prato

@admin.register(Prato)
class PratoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'preco', 'ativo')
    list_filter = ('categoria', 'ativo')
    search_fields = ('nome', 'descricao')
    list_editable = ('preco', 'ativo')

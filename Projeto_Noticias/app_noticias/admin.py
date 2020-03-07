from django.contrib import admin
from .models import Noticia,Pessoa,Tag,Cometario

@admin.register(Pessoa)
@admin.register(Tag)
@admin.register(Noticia)
@admin.register(Cometario)
class NoticiaAdmin(admin.ModelAdmin):
    pass

# Register your models here.

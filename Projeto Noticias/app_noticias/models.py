from django.db import models
class Noticia(models.Model):
    conteudo = models.TextField()
    class Meta:
        verbose_name = 'Notícia'
        verbose_name_plural = 'Notícias'
    titulo = models.CharField('título', max_length=128, blank = True,
    null = True)
    autor = models.CharField('Autor', max_length=128, blank = True,
    null = True)
   
    def __str___(self):
        return self.conteudo
    

# Create your models here.

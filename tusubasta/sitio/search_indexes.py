from haystack import indexes
from sitio.models import Subastas, Comentarios
import datetime

class SubastasIndex(indexes.SearchIndex, indexes.Indexable):
    text 		= indexes.CharField(document=True, use_template=True)
    titulo 		= indexes.CharField(model_attr='titulo')
    fechaFin 	= indexes.DateTimeField(model_attr='fechaFin')
    ofertaMax	= indexes.DecimalField(model_attr='ofertaMax')
    detalle 	= indexes.CharField(model_attr='detalle')
    
    def get_model(self):
        return Subastas

    def index_queryset(self, using=None):
        """Queremos que se indexen todas las noticias que tengan archivada=False"""
        return self.get_model().objects.filter(fechaBaja=None, fechaFin__gt = datetime.datetime.now())


class ComentariosIndex(indexes.SearchIndex, indexes.Indexable):
    text        = indexes.CharField(document=True, use_template=True)
    comentario  = indexes.CharField(model_attr='comentario')
    
    def get_model(self):
        return Comentarios

    def index_queryset(self, using=None):
        """Queremos que se indexen todas las noticias que tengan archivada=False"""
        return self.get_model().objects.filter(fechaBaja=None)

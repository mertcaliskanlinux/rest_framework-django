# from rest_framework.generics import GenericAPIView
# from rest_framework.mixins import ListModelMixin,CreateModelMixin

from kitaplar.api.serializers import KitapSerializers
from kitaplar.models import Kitap
from rest_framework import generics




class KitapListCreatedAPIView(generics.ListCreateAPIView):
    queryset = Kitap.objects.all()
    serializer_class = KitapSerializers

class KitapDetailAPIView(generics.RetrieveDestroyAPIView):
    
    queryset = Kitap.objects.all()
    serializer_class = KitapSerializers






# class KitapListCreatedAPIView(ListModelMixin,CreateModelMixin,GenericAPIView):
    
#     queryset = Kitap.objects.all()
#     serializer_class = KitapSerializers

#     #Listelemek
#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args, **kwargs)
    
#     #Yaratabilmek
#     def post(self,request,*args, **kwargs):
#         return self.create(request, *args, **kwargs)
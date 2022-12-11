# from rest_framework.generics import GenericAPIView
# from rest_framework.mixins import ListModelMixin,CreateModelMixin

from kitaplar.api.serializers import KitapSerializers,YorumSerializers
from kitaplar.models import Kitap,Yorum
from rest_framework import generics
from rest_framework.generics import get_object_or_404





class KitapListCreatedAPIView(generics.ListCreateAPIView):
    queryset = Kitap.objects.all()
    serializer_class = KitapSerializers

class KitapDetailAPIView(generics.RetrieveDestroyAPIView):
    
    queryset = Kitap.objects.all()
    serializer_class = KitapSerializers


class YorumCreateAPIView(generics.CreateAPIView):
    queryset = Yorum.objects.all()
    serializer_class = YorumSerializers
    
    def perform_create(self, serializer):
        # path('kitaplar/<int:kitap_pk>/yorum_yap/', api_views.YorumCreateAPIView.as_view(), name='kitap-yorumla'),
        kitap_pk = self.kwargs.get('kitap_pk')
        kitap = get_object_or_404(Kitap,pk=kitap_pk)
        serializer.save(kitap=kitap)
        
        
class YorumDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Yorum.objects.all()
    serializer_class = YorumSerializers
    
    
    
    
    
    
    



# class KitapListCreatedAPIView(ListModelMixin,CreateModelMixin,GenericAPIView):
    
#     queryset = Kitap.objects.all()
#     serializer_class = KitapSerializers

#     #Listelemek
#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args, **kwargs)
    
#     #Yaratabilmek
#     def post(self,request,*args, **kwargs):
#         return self.create(request, *args, **kwargs)
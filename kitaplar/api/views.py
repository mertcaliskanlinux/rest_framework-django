# from rest_framework.generics import GenericAPIView
# from rest_framework.mixins import ListModelMixin,CreateModelMixin

from kitaplar.api.serializers import KitapSerializers,YorumSerializers
from kitaplar.models import Kitap,Yorum
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework import permissions
from rest_framework.exceptions import ValidationError
from kitaplar.api.permission import IsAdmınUserOrReadOnly,IsYorumSahibiorReadOnly
from kitaplar.api.pagination import SmallPagination,LargePagination


class KitapListCreatedAPIView(generics.ListCreateAPIView):
    queryset = Kitap.objects.all().order_by('id')
    serializer_class = KitapSerializers
    permission_classes = [IsAdmınUserOrReadOnly]
    # pagination_class = LargePagination #Büyük Data
    pagination_class = SmallPagination




class KitapDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Kitap.objects.all()
    serializer_class = KitapSerializers
    permission_classes = [IsAdmınUserOrReadOnly]
    


class YorumCreateAPIView(generics.CreateAPIView):
    queryset = Yorum.objects.all()
    serializer_class = YorumSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        # path('kitaplar/<int:kitap_pk>/yorum_yap/', api_views.YorumCreateAPIView.as_view(), name='kitap-yorumla'),
        kitap_pk = self.kwargs.get('kitap_pk')
        kitap = get_object_or_404(Kitap,pk=kitap_pk)
        kullanici = self.request.user
        yorumlar = Yorum.objects.filter(kitap=kitap,yorum_sahibi=kullanici)
        
        if yorumlar.exists():
            raise ValidationError('Bir Kitaba Sadece Bir Kere Yorum Yapabilirsiniz')
        
        serializer.save(kitap=kitap,yorum_sahibi=kullanici)
        
        
        
        
class YorumDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Yorum.objects.all()
    serializer_class = YorumSerializers
    permission_classes = [IsYorumSahibiorReadOnly]
    
    
    
    
    
    



# class KitapListCreatedAPIView(ListModelMixin,CreateModelMixin,GenericAPIView):
    
#     queryset = Kitap.objects.all()
#     serializer_class = KitapSerializers

#     #Listelemek
#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args, **kwargs)
    
#     #Yaratabilmek
#     def post(self,request,*args, **kwargs):
#         return self.create(request, *args, **kwargs)
from rest_framework import serializers
from haberler.models import Makale,Gazateci
from django.utils.timesince import timesince
from datetime import datetime
from datetime import date







class MakaleSerializers(serializers.ModelSerializer):
    
    time_since_pub = serializers.SerializerMethodField()
    # yazar = serializers.StringRelatedField()  
    # yazar = GazetecilerSerializer()
    
    class Meta:
        model = Makale
        fields = '__all__'
        # fields = ['yazar','baslik','metin']
        # exclude = ['yazar','baslik','metin']
        read_only_fields = ['id','yaratilma_tarihi','güncelleneme_tarihi']
    
    def get_time_since_pub(self,object):
        now = datetime.now()
        pb_date = object.yayimlanma_tarihi
        if object.aktif == True:
            
            time_delta = timesince(pb_date,now)
            
            return time_delta
        else:
            self.aktif_degil = "Aktif Değil"
            return self.aktif_degil

    def validate_yayimlanma_tarihi(self,tarihDegeri):
        today = date.today()
        if tarihDegeri > today:
            raise serializers.ValidationError('Yayımlanma tarihi ileri bir tarih olmaz!!')
        return tarihDegeri






class GazetecilerSerializer(serializers.ModelSerializer):
    # makaleler = MakaleSerializers(many=True,read_only=True)

    makaleler = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='makale-detay',
        
    )    
    
    
    class Meta:
        model = Gazateci
        fields = '__all__'






































#### STANDART SERİALİZER ###
class MakaleDefaultSerializers(serializers.Serializer):
    
    id = serializers.IntegerField(read_only=True)
    yazar = serializers. CharField()
    baslik = serializers. CharField()
    aciklama = serializers.CharField()
    metin = serializers. CharField()
    sehir = serializers.CharField()
    yayimlanma_tarihi = serializers.DateField()
    aktif = serializers.BooleanField()
    yaratilma_tarihi = serializers.DateTimeField(read_only=True)
    güncelleneme_tarihi = serializers.DateTimeField(read_only=True)


    def create(self, validated_data):
        return Makale.objects.create(**validated_data)
    
    
    def update(self, instance, validated_data):
        
        instance.yazar = validated_data.get('yazar', instance.yazar)
        instance.baslik = ('baslik', instance.baslik)
        instance.aciklama = validated_data.get( 'aciklama', instance.aciklama)
        instance.metin = validated_data.get('metin', instance.metin)
        instance.sehir = validated_data.get('sehir', instance.sehir)
        instance.yayimlanma_tarihi = validated_data.get('yayanlanna_tarihi', instance.yayimlanma_tarihi)
        instance.aktif - validated_data.get('aktif' ,instance.aktif)
        instance.save()
     
        return instance


    def validate(self, data):
        if data['baslik'] == data['aciklama']:
            raise serializers.ValidationError(
                'Baslik Ve Açıklama Alanları Aynı Olamaz Lütfen Farklı Bir Açıklama Giriniz.'
            )
        return data
    
    def validate_baslik(self, value):
        if len(value) < 20:
            raise serializers.ValidationError(
                'Başlık Alanı Minimum 20 karakter olmalıdır Siz {} karakter girdiniz'.format(len(value))
            )
        return value
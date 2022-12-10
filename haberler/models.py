from django.db import models

# Create your models here.



class Gazateci(models.Model):
    isim = models.CharField(max_length=120)
    soyisim = models.CharField(max_length=120)
    biyografi = models.TextField(blank=True, null=True)
    
    
    def __str__(self):
        self.baslik = f"{self.isim} {self.soyisim}" 
        return self.baslik

    
class Makale(models.Model):
    yazar = models.ForeignKey(Gazateci,on_delete=models.CASCADE,related_name="makaleler")
    baslik = models.CharField(max_length=120)
    aciklama = models.CharField(max_length=200)
    metin = models.TextField()
    sehir = models.CharField(max_length=120)
    yayimlanma_tarihi = models.DateField()
    aktif = models.BooleanField(default=True)
    yaratilma_tarihi = models.DateTimeField(auto_now_add=True)
    güncelleneme_tarihi = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.baslik
    
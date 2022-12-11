import os
import random

os.environ.setdefault('DJANGO_SETTING_MODULE','haberbulteni.settings')
import django
django.setup()

from django.contrib.auth.models import User

from faker import Faker
import requests

def set_user():
    fake = Faker(['tr_TR'])
    f_name = fake.first_name()
    l_name = fake.last_name()
    u_name = f"{f_name.lower()}_{l_name.lower()}"
    email = f"{u_name}@{fake.domain_name()}"
    print(f_name,l_name,email)
 
 
    user_check = User.objects.filter(username=u_name)
    
    while user_check.exists():
        u_name = u_name + str(random.randrange(1,99))
        user_check = User.objects.filter(username=u_name)

    user = User(
            username = u_name,
            first_name = f_name,
            last_name = l_name,
            email = email,
            is_staff = fake.boolean(chance_of_getting_true=50),
        )
    
    user.set_password('testing321..')
    user.save()
    print("Kullanıcı Kaydedildi !",u_name)
    
from kitaplar.api.serializers import KitapSerializers

def kitap_ekle(konu):
    
    fake = Faker(['tr-TR'])
    
    url = "https://openlibrary.org/search.json"
    payload = {
        'q':konu
    }
    response = requests.get(url,params=payload)

    if response.status_code != 200:
        print('Hatalı İstek Yapıldı',response.status_code)
        return 

    jsn = response.json()
    kitaplar = jsn.get('docs')
    for kitap in kitaplar:
        kitap_adi = kitap.get('title')
        data = dict(
            isim = kitap_adi,
            yazar = kitap.get('author_name')[0],
            aciklama = '-'.join(kitap.get('publisher_facet')),
            yayın_tarihi = fake.date_time_between(start_date='-10y',end_date='now',tzinfo=None)
        )
        serializer = KitapSerializers(data=data)
        print(data)
        if serializer.is_valid():
            serializer.save()
            print("kaydedildi")
            
        else:continue
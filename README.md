"https://x.com/bengilgin/status/1898083572805751027"
Twit de bahselin 7.sınıf matematik sorusunun python dilinde kodlanmış hali xD



# Sayı İşleme Algoritması

Bu program, kullanıcıdan bir sayı alarak belirli bir matematiksel algoritma uygulayan basit bir Python uygulamasıdır.

## Algoritma Adımları

Program aşağıdaki adımları takip eder:

1. Kullanıcıdan bir sayı alır (tam sayı, ondalıklı sayı veya kesir olabilir)
2. Sayının küpünü alır ve sayının kendisini ekler: `sayı³ + sayı`
3. Eğer sonuç pozitifse, sonucu gösterir ve program sonlanır
4. Eğer sonuç negatif veya sıfırsa, sonuca 1 ekler ve tekrar kontrol eder:
   - Eğer sonuç pozitif olursa, sonucu gösterir ve program sonlanır
   - Eğer sonuç hala negatif veya sıfırsa, bu yeni değeri alıp 2. adıma geri döner

## Kullanım

Programı çalıştırmak için:

```
python main.py
```

Program çalıştığında:
- Tam sayı girebilirsiniz: `5`
- Ondalıklı sayı girebilirsiniz: `2.5`
- Kesir girebilirsiniz: `-1/2`

## Özel Durumlar

- Program, negatif tam sayılar girildiğinde sonsuz döngüye girebileceğini tespit eder ve kullanıcıyı uyarır.
- Sonuç hem ondalıklı formatta hem de kesir formatta (payda=8) gösterilir.

## Örnek Çıktı

```
Adım 1: Sayıyı oku.
Adım 2: Sayının küpüne sayıyı ekle.
Adım 3: Eğer sonuç pozitifse 5. adıma geç, aksi halde 4. adıma geç.
Adım 4: Sonucu 1 artır, ardından 2. adımdan devam et.
Adım 5: Sonucu yazdır.

Bir sayı girin (kesir için örnek: -1/2): 2
Adım 1: Girilen sayı 2.000

Adım 2: Sayının küpü (2.000^3) = 8.000
Adım 2: Küp + sayı = 8.000 + 2.000 = 10.000
Adım 3: Sonuç pozitif, 5. adıma geç.
Adım 5: Sonuç (ondalık) = 10.000
Adım 5: Sonuç (payda = 8) = 80/8 
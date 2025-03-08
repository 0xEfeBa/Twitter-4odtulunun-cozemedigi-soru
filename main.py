def main():
    denominator = 8

    print("Adım 1: Sayıyı oku.")
    print("Adım 2: Sayının küpüne sayıyı ekle.")
    print("Adım 3: Eğer sonuç pozitifse 5. adıma geç, aksi halde 4. adıma geç.")
    print("Adım 4: Sonucu 1 artır, ardından 2. adımdan devam et.")
    print("Adım 5: Sonucu yazdır.\n")

    user_input = input("Bir sayı girin (kesir için örnek: -1/2): ")

    if '/' in user_input:
        try:
            num_str, denom_str = user_input.split('/')
            num = int(num_str.strip())
            denom = int(denom_str.strip())
            number = num / denom
            print(f"Adım 1: Girilen kesir {number:.3f} (ondalık form)\n")
        except Exception as e:
            print("Geçersiz kesir formatı.")
            return
    else:
        try:
            number = float(user_input)
            print(f"Adım 1: Girilen sayı {number:.3f}\n")
          
            if number < 0 and number == int(number):
                print("Soru hatalı: Negatif tam sayı girildiğinde bu döngü sonsuza kadar sürüyor xD")
                return
        except Exception as e:
            print("Geçersiz sayı formatı.")
            return

    while True:
        cube = number ** 3
        result = cube + number

        print(f"Adım 2: Sayının küpü ({number:.3f}^3) = {cube:.3f}")
        print(f"Adım 2: Küp + sayı = {cube:.3f} + {number:.3f} = {result:.3f}")

        if result > 0:
            print("Adım 3: Sonuç pozitif, 5. adıma geç.")
            numerator = int(result * denominator)
            print(f"Adım 5: Sonuç (ondalık) = {result:.3f}")
            print(f"Adım 5: Sonuç (payda = 8) = {numerator}/{denominator}")
            break
        else:
            print("Adım 3: Sonuç pozitif değil, 4. adıma geç.")
            previous_result = result 
            result += 1
            print(f"Adım 4: Sonuç + 1 = {previous_result:.3f} + 1 = {result:.3f}")

            if result > 0:
                numerator = int(result * denominator)
                print(f"Adım 5: Sonuç (ondalık) = {result:.3f}")
                print(f"Adım 5: Sonuç (payda = 8) = {numerator}/{denominator}")
                break
            else:
                print("Adım 3: Sonuç hâlâ negatif, 2. adıma geri dön.")
                number = result

if __name__ == "__main__":
    main()

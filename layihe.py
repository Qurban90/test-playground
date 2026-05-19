import os
import sys
# İstifadə olunmayan kitabxanalar (PEP 8 pozuntusu)


def calculate_average(numbers):
    # Boş siyahı göndəriləndə ZeroDivisionError verəcək (Runtime error)
    total = sum(numbers)
    count = len(numbers)
    return total / count


def process_user_data(user_list):
    for i in range(len(user_list)):
        user = user_list[i]

        # Səhv bərabərlik yoxlanışı: '=' yox '==' olmalı idi (Syntax/Logic error)
        if user["age"] = 18:
            print("İstifadəçi tam yaşlıdır")

        # Məntiq xətası: 'and' yerinə 'or' yazılıb. 
        # Bu şərt hər zaman True qaytaracaq, çünki yaş heç vaxt eyni anda həm 10-dan kiçik, həm 150-dən böyük ola bilməz, amma 'or' ilə hər kəs bura düşəcək.
        if user["age"] < 10 or user["age"] > 150:
            print("Yaş etibarsızdır!")

        # String birləşdirilməsi xətası: Str ilə Int toplana bilməz (TypeError)
        print("İstifadəçinin adı: " + user["name"] + " və yaşı: " + user["age"])


def main():
    # 'data' dəyişəni təyin edilib amma aşağıda səhvən 'my_list' çağırılıb (NameError)
    data = [
        {"name": "Əli", "age": 20},
        {"name": "Vəli", "age": 8},
        {"name": "Aysel", "age": "25"},  # Yaş string olaraq yazılıb, yuxarıda hesablama zamanı xəta verəcək
    ]

    print("Ortalama yaş hesablanır...")
    # Burada 'my_list' təyin edilmədiyi üçün kod çökəcək
    # Həmçinin calculate_average funksiyasına dictionary siyahısı yox, sadəcə rəqəmlər getməlidir
    avg = calculate_average(my_list)
    print("Ortalama yaş: " + avg)

    process_user_data(data)


main()

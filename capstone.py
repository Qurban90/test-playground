def hesabla_ortalama(reqemler):
    cem = 0
    for i in range(len(reqemler)):
        # SƏHV 1: Əgər element sətir (string) olarsa, proqram çökəcək (Tip yoxlanışı yoxdur)
        cem = cem + reqemler[i]
        
    # SƏHV 2: "len(reqemler)" sıfır ola bilər, bu da "ZeroDivisionError" yaradacaq
    ortalama = cem / len(reqemler)
    return ortalama

def neticeni_goster():
    X = [10, 20, "30", 40] # SƏHV 3: Siyahıda string var
    
    # SƏHV 4: Funksiya səhv adla çağırılıb (hesabla_ortalama yerinə hesabla_ortalamasi)
    cavab = hesabla_ortalamasi(X) 
    
    # SƏHV 5: 'cavab' dəyişəni formatlanarkən string və float birbaşa toplana bilməz (TypeError)
    print("Nəticə: " + cavab) 

neticeni_goster()

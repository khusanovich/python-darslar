#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 15:22:40 2021

@author: khusanovich
"""

# for sikli

# mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
# for mehmon in mehmonlar:
#     print(mehmon)
    
# sonlar = [1, 2, 3, 4, 5, 6, 7]
# for son in sonlar:
#     print(son)

# mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
# for mehmon in mehmonlar:
#     print(f"Hurmatli {mehmon}, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz")
# print("Hurmat bilan, Palonchiyevlar oilasi")

# mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
# for mehmon in mehmonlar:
#     print(mehmon)
    
#     print(mehmonlar) # bu qator tsikl tashqarisida bo'lishi kerak edi

# sonlar = list(range(1,11))
# for son in sonlar:
#     print(f"{son} ning kvadrati {son**2}ga teng")

# # for yordamida yangi ro'yxat ham shakllantirish mumkin
# sonlar = list(range(11)) # 1 dan 10 gacha sonlay ro'yxatini yaratamiz
# sonlar_kvadrati = [] # bo'sh ro'yxat yaratamiz
# for son in sonlar:
#     sonlar_kvadrati.append(son**2) # sonning kvadratini hisoblab sonlar_kvadratiga yuklayamiz
# print(f"ro'yxatimizda quyidagi sonlar mavjud: {sonlar}")
# print(f"bu sonlarning kvadratlari quyidagicha bo'ladi: {sonlar_kvadrati}")

# #for operatori va input() funktsiyasini jamlab, ro'yxatni foydalanuvchidan olingan qiymatlar bilan to'ldirish mumkin:
# dostlar = []
# print("Beshta do'stingizning ismini kiriting.")
# for n in range(5):
#     dostlar.append(input(f"{n+1}-do'stingizni kiritng: "))
# print(dostlar)

### Amaliyot
## Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing
# friends = ['Erkin', 'Jasur', 'Turob', 'Abror', 'Arslon']
# for friend in friends:
#     print(f"{friend}, tezda kel")
## Yuqoridagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan xabarni chiqaring (n o'rniga kod necha marta takrorlanganini yozing)  
# print(f"Kod {len(friends)} marta takrorlandi")

## 10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.
# toq_sonlar = list(range(11,100,2))
# for sonKubi in toq_sonlar:
#     print(f"{sonKubi} ning kubi {sonKubi**3} ga teng")
# print(toq_sonlar)

## Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.
# films = []
# print("5 ta sevimli filmingizni kiriting")
# for n in range(5):
#     films.append(input(f"{n+1} - filmni kiriting."))
# print(films)


#### quyidagi kodda xatolik bor !!!
## Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang, va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.
# n_odam = int(input("Bugun kimlar bilan gaplashdingiz?"))
# suhbatdoshlar = []
# for n in range(n_odam):
#     suhbatdoshlar.append(input(f"{n+1} - odamni kiriting: "))
# print(suhbatdoshlar)

# Foydalanuvchidan bugun nechta odam bilan 
# uchrashganini (suhbatlashganini) so'rang, 
# va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.
n_people = int(input("Bugun necha kishi bn suhbat qildingiz?>>>"))
ismlar = []
for n in range(n_people):
    ismlar.append(input(f"{n+1}-suhbat qilgan odamingiz kim edi: "))
print(ismlar)  


    













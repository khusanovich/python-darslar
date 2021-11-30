#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 21:06:34 2021

@author: khusanovich
"""
# Aksar holatlarda ro'yxat ichidagi elementlarni alifbo ketma-ketligida tartiblash talab qilinishi mumkin. Buning uchun list uchun maxsus .sort() metodidan foydalanamiz.
# cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# cars.sort()
# print(cars)

# # Ro'yxatni teskari tartibda saqlash uchun .sort() metodi ichida reverse=True argumentini ham kiritamiz.
# cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# cars.sort(reverse=True)
# print(cars)

# Ba'zida asl ro'yxat ichidagi elementlarning ketma-ketligini buzmagan holda ro'yxatni tartiblash talab qilinishi mumkin. Buning uchun sorted() funktsiyasidan foydalanamiz:
# cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# print(f"Men kelajakda {cars[3]} mashinasini olmoqchiman.")
    
# mehmonlar = ['Odil', 'Hamid', 'Temur', 'Avazbek', 'Farruh', 'Shamsiddin']
# print("sorted() qaytargan ro'yxat:", sorted(mehmonlar))
# print("Asl ro'yxat o'zgarmas qoldi:", mehmonlar)
# print(sorted(mehmonlar, reverse=True)) # bunda alfboga teskari tartibda tartibladi

# ages = [12, 98, 34, 65, 34, 76, 11]
# ages.sort()
# print(ages) # o'sish tartibida
# print(sorted(ages, reverse=True)) # kamayish tartibida sort qiladi

# oilamizdagilarning_yoshlari = {'men':26, 'opam':29, 'akam':31, 'onam':56, 'otam':58}
# oy = oilamizdagilarning_yoshlari
# oy.sort()
# print(sorted(oy))
# print(oy['otam'])

# Ba'zida ro'yxatni aylantirish (boshini oxiriga, oxirini boshiga) talab qilinishi mumkin. Buning uchun .reverse() metodidan foydalanamiz.
# fruits = ['pear','banana','apple','watermelon','lemon']
# fruits.reverse()
# print(fruits)

# Ro'yxatning uzunligi, ya'ni uning ichidagi elementlar sonini aniqlash uchun len() funktsiyasidan foydalanamiz:
# fruits = ['pear','banana','apple','watermelon','lemon']
# print("Elementlar soni:",len(fruits)) # len(fruits) ro'yxat uzunligini qaytaradi
# print(len(fruits))

# # **`range()`** FUNKTSIYASI: Bu funktsiya yordamida biz ma'lum oraliqdagi sonlar ketma-ketligini yaratishimiz mumkin. **`list()`** funktsiyasi yordamida esa bu oraliqni ro'yxat shaklida saqlab olamiz:
# sonlar = list(range(0,10)) # 10 soni kirmaydi, ro'yxatning oxirgi soni 9 bo'ladi
# print(sonlar)

# `range()` yordamida qadamni ham berishimiz mumkin:
# juft_sonlar = list(range(0,20,2)) # 0 dan 20 gacha 2 qadam bilan
# toq_sonlar = list(range(1,20,2))  # 1 dan 20 gacha 2 qadam bilan
# print("Juft sonlar: ", juft_sonlar)
# print("Toq sonlar: ", toq_sonlar)

# bazi_sonlar = list(range(0,100,10))
# print(bazi_sonlar)

# # > Agar sonlar ketma-ketligi 0 dan boshlansa, `range()` funktsiyasida yakuniy indeksni ko'rsatish kifoya. Misol uchun `range(0,10)` emas `range(10)` deb yozsak ham bo'laveradi.
# bazi_sonlar = list(range(10))
# print(bazi_sonlar)

# # SONLI RO'YXAT USTIDA SODDA AMALLAR
# Pythonda ro'yxatlar ustida ba'zi sodda amallarni ham bajarish mumkin. Misol uchun ro'yxatdagi eng kichik sonni topish uchun `min()` funktsiyasidan, eng katta sonni topish uchun esa `max()` funktsiyasidan, sonlarning yig'indisini topish uchun esa `sum()` funktsyasidan foydalansak bo'ladi:
# narhlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
# arzon = min(narhlar)
# qimmat = max(narhlar)
# jami = sum(narhlar)
# print("Eng arzon narh ", arzon, ". Eng qimmati ", qimmat, ". Jami: ", jami)

# preise = [32, 3.4, 24, 11, 189]
# billigste = min(preise)
# teuerste = max(preise)
# insgesamt = sum(preise)
# print(f"Men yaqinda olgan eng arzon mahsulot {billigste} yevro edi, eng qimmati esa {teuerste} yevro bo'ldi, jami xarajatlarim {insgesamt} yevro bo'lib chiqdi.")

# # # RO'YXATNI KESISH
# # Ba'zida ro'yxatning ma'lum bir bo'lagini ajratib olish talab qilinishi mumkin, deylik biz quyidagi cars degan ro'yxatdan birinchi 3 ta elementni ajratib olmoqchimiz, buning uchun biz boshlang'ich va oxirgi indekslarni beramiz:
# cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# my_cars = cars[0:3] # 0-indeskdan boshlab 3 ta element ajratib olamiz
# print(my_cars) 

# # RO'YXATDAN NUSXA OLISH
# Dastur davomida biror ro'yxatdan nusxa olish talab qilinishi mumkin. Buning uchun biz tenglik(`=`) belgisidan foydalansak bo'ladimi? Quyidagi misolga e'tibor bering:
# sonlar = [1, 2, 3, 4, 5] # donlar degan ro'yxat yaratamiz
# sonlar2 = sonlar # sonlar2 degan ro'yxatni sonlar ga tenglaymiz
# sonlar2.append(6) # sonlar2 ga 6 sonini qo'shamiz
# sonlar2.append(7) # sonlar2 ga 7 sonini qo'shamiz
# print("Bu sonlar ro'yxati:", sonlar)
# print("Bu sonlar2 ro'yxati:", sonlar2)
# Natija biz kutgandek chiqdimi? Yo'q. Biz 6 va 7 sonlarini sonlar2 degan ro'yxatga qo'shgan edik, lekin bu ikki son sonlar degan asl ro'yxatga ham qo'shilib qoldi.
# Demak yuqorida biz sonlar2=sonlar deb yozgan komandamiz yangi ro'yxat yaratish o'rniga, ikkala o'zgaruvchini ham bitta ro'yxatga bog'lab (yo'naltirib) qo'ydi. Biz sonlar yoki sonlar2 ustida bajargan amallarimiz aslida bitta ro'yxat ustida bajarilyapt

# # Unda, qanday qilib ro'yxatdan nusxa olamiz? Buning uchun yuoqirdagi ka'bi ro'yxatni kesish usulidan foydalanamiz. Faqatgina, kvadrat qavs ichida ikkala indeksni ham ko'rsatmasdan, bo'sh qoldiramiz:
# sonlar = [1, 2, 3, 4, 5] # donlar degan ro'yxat yaratamiz
# sonlar2 = sonlar[:] # [:] ro'yxatni to'liq ko'chirib oladi
# sonlar2.append(6) # sonlar2 ga 6 sonini qo'shamiz
# sonlar2.append(7) # sonlar2 ga 7 sonini qo'shamiz
# print("Bu sonlar ro'yxati:", sonlar)
# print("Bu sonlar2 ro'yxati:", sonlar2)

# olmoshlar = ['men', 'sen', 'u', 'biz']
# kishilik_olmoshlari = olmoshlar[:]
# olmoshlar.append('siz')
# olmoshlar.append('ular')
# kishilik_olmoshlari.append('sizlar')
# print(olmoshlar)
# print(kishilik_olmoshlari)

# Agar Tuple ga o'zgartirish talab qilinsa, yagona yo'li o'zgarmas ro'yxatni list() funktsiyasi yordamida List (oddiy ro'yxat) ko'rinishiga keltirib olish, o'zgarishlarni bajarsih va qaytarib tuple() funktsiyasi yordamida o'zgarmas ro'yxatga o'tkazish mumkin:

# toys = ('bus','car','bear','dino','snake','lizard') # o'zgarmas ro'yxat
# toys = list(toys) # o'zgarmas ro'yxatni oddiy ro'yxatga (List) aylantiramiz
# # Ro'yxatga o'zgartirishlar kiritamiz
# toys.append('dragon')
# toys.remove('bus')
# toys[1] = 'mcqueen'
# toys = tuple(toys) # Ro'yxatni qaytadan o'zgarmas ro'yxatga (Tuple) aylantiramiz
# print(toys)

# oilamiz = ('otam', 'men', 'onam', 'akam', 'opam')
# oilamiz = list(oilamiz)
# oilamiz.append('yangam')
# oilamiz.append('Muhammad Yusuf')
# oilamiz.remove('otam')
# oilamiz[0] = 'Asliddin'
# oilamiz = tuple(oilamiz)
# print(oilamiz)

# Amaliyot javoblari
# O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
# davlatlar = ['uzbekistan', 'germany', 'england', 'denmark']
# print(len(davlatlar)) #Ro'yxatning uzunligini konsolga chiqaring
# davlatlar.sort()
# print(sorted(davlatlar) # sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
# print(davlatlar)
# print(sorted(davlatlar, reverse=True)) #sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
# print(davlatlar) #Asl ro'yxatni qaytadan konsolga chiqaring
# davlatlar.sort(reverse=True)
# print(davlatlar)

# juftSonlar = list(range(120, 1200))
# print(juftSonlar)
# sonlar = list(range(120,1200))
# print(sonlar)
# print(sum(juftSonlar))
# print(max(juftSonlar)-min(juftSonlar))
# print(len(juftSonlar))
# print(juftSonlar[:20])
# print(sonlar[:20])
# print(sonlar[-20:])
# print(sonlar[530:550])

# taomlar = ['palov', 'manti', 'makaron', 'xonim', 'dimlama']
# nonushta = taomlar[:]
# nonushta.remove('palov')
# nonushta.remove('dimlama')
# nonushta.remove('makaron')
# nonushta.append('omlet')
# nonushta.append('quymoq')
# print(taomlar)
# nonushta = tuple(nonushta)
# nonushta[0] = 'qaymoq va non'
# print(nonushta)


















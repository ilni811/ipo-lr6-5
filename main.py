import random
# Генерация списка из 25 случайных чисел от -50 до 50
list = [random.randint(-50,50) for x in range(25)]
print(list)
polozh = 0
otric = 0
nul = 0
for i in list:
    if i > 0: 
        polozh+=1
    elif i < 0:
        otric+=1
    else:
        nul+=1
      # Вычисление процентов
polozh_prosent = (polozh/25) * 100
otric_prosent = (otric/25) * 100
nul_prosent = (nul/25) * 100
# Вывод результатов
print(f"kolvo polozhitelnih = {polozh}, ih porcent = {polozh_prosent}") 
print(f"kolvo otric = {otric}, ih porcent = {otric_prosent}") 
print(f"kolvo nulevih = {nul}, ih porcent = {nul_prosent}") 
print(f"minimalnoe = {min(list)}, maximalnoe = {max(list)}")

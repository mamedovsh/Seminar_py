#Задача 2: Найдите сумму цифр трехзначного числа.

a = int(input("Введите трехзначное число:"))
print(a//100 + a//10%10 +a%10)
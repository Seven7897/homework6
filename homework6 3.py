# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
number = input("Задайте число : ")
list = [int(number[i]) for i in range(len(number)) if number[i] != '.']
print(sum(list))

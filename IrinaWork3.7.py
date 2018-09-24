import math
print ("Лабораторна робота №3. Поняття змінної та типу даних у Python")
print ("Завдання №7")
print ("Автор: Арістова Ірина, КМ-82")

FullMinutes = int (input("Введіть кількість хвилин "))
FullHours, Minutes = divmod(FullMinutes, 60)
Hours = FullHours % 24
print ("З момента півночі пройшло {0} ч {1} хв.".format(Hours, Minutes))
input("Нажміть Enter")


 

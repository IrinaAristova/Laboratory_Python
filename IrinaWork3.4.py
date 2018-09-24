import math
print ("Лабораторна робота №3. Поняття змінної та типу даних у Python")
print ("Завдання №4")
print ("Автор: Арістова Ірина, КМ-82")

Students = int(input("Введіть кількість студентів "))
Apples = int(input("Введіть кількість яблук "))
InStudent, InBasket = divmod(Apples/Students)
print ("Кількість яблук у студента дорівнює %.3f, кількість у кошику" % (InStudent, InBasket))
input("Нажміть Enter")


 

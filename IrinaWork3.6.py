import math
print ("Лабораторна робота №3. Поняття змінної та типу даних у Python")
print ("Завдання №6")
print ("Автор: Арістова Ірина, КМ-82")

Students1 = int(input("Введіть кількість студентів у першій групі "))
Students2 = int(input("Введіть кількість студентів у другій групі "))
Students3 = int(input("Введіть кількість студентів у третій групі "))
MinTables1 = (Students1+1) // 2
MinTables2 = (Students2+1) // 2
MinTables3 = (Students3+1) // 2
print ("Кількість необхідних столів дорівнює %i" % (MinTables1+MinTables2+MinTables3))
input("Нажміть Enter")


 


class Animal:

    alive = True

    def eat(self):
        print("this animal is eating")
    def sleep(self):
        print("this animal is sleeping ZZZZ")

class Rabbit(Animal):
   def run(self):
       print("rabbit is running")
rabbit =Rabbit()
print(rabbit.alive)
rabbit.run()

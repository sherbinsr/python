
# MethodChaning - Calling multiple mehtod sequentially but we have to return self in  every method

class Cars:
    def run(self):
        print("this car is runnning now")
        return  self
    def brake(self):
        print("Brake is applied")
        return self
    def stop(self):
        print("car is stopped now")

car = Cars()

car.run().brake()

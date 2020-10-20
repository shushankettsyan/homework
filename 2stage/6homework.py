class HeathingSystem:

    def __init__(self,current_tempriture, goal_tempriture):
        self.current_tempriture = current_tempriture
        self.goal_tempriture = goal_tempriture
        self.difference = goal_tempriture - current_tempriture

    def get_tempriture(self):
        return "current tempriture is {}".format(self.current_tempriture)

    def set_tempriture(self):
        self.current_tempriture = self.goal_tempriture
        return "goal tempriture is {}".format(self.goal_tempriture)

    def __int__(self):
        return self.difference



house_1 = HeathingSystem(14, 22)
house_2 = HeathingSystem(15, 24)
house_3 = HeathingSystem(16, 26)
house_4 = HeathingSystem(17, 28)


print("house1",house_1.get_tempriture())
print("\nhouse1",house_1.set_tempriture())

print("\nhouse2",house_2.get_tempriture())
print("\nhouse2",house_2.set_tempriture())

print("\nhouse3",house_3.get_tempriture())
print("\nhouse3",house_3.set_tempriture())

print("\nhouse4",house_4.get_tempriture())
print("\nhouse4",house_4.set_tempriture())

print("For house1 the difference between goal tempriture and current tempriture is",int(house_1))
print("For house2 the difference between goal tempriture and current tempriture is",int(house_2))
print("For house3 the difference between goal tempriture and current tempriture is",int(house_3))
print("For house4 the difference between goal tempriture and current tempriture is",int(house_4))

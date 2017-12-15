#-*-coding:utf-8-*-
from car import Car

my_car=Car('4个圈','a6',2017)
print(my_car.get_descriptive_name())

my_car.increment_odometer(100)
my_car.read_odometer()
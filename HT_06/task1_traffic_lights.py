'''1. Програма-світлофор.
Створити програму-емулятор світлофора для авто і пішоходів.
Після запуска програми на екран виводиться в лівій половині - колір автомобільного, а в правій - пішохідного світлофора.
Кожну секунду виводиться поточні кольори. Через декілька ітерацій - відбувається зміна кольорів - логіка така сама як і в звичайних світлофорах.
Приблизний результат роботи наступний:
    Red        Green
    Red        Green
    Red        Green
    Red        Green
    Yellow     Green
    Yellow     Green
    Green      Red
    Green      Red
    Green      Red
    Green      Red
    Yellow     Red
    Yellow     Red
    Red        Green
    .......'''
import time


def traffic_lights(light_num):
    car_lights = ['Red', 'Yellow', 'Green']
    peoples_lights = ['Red', 'Green']
    while True:
        for light in range(4):
            print(car_lights[0], peoples_lights[1])
            time.sleep(1)
        for light in range(2):
            print(car_lights[1], peoples_lights[1])
            time.sleep(1)
        for light in range(4):
            print(car_lights[2], peoples_lights[0])
            time.sleep(1)


traffic_lights(10)

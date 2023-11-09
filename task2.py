#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from math import pi

def cylinder(r: float, h: float, request_full_area: bool = False) -> str:

    def circle(r: float) -> float:
        return pi*(r**2)
    
    lateral_area: float = 2*pi*r*h
    full_area: float = lateral_area + 2*(circle(r))
    
    if request_full_area:
        return f"Полная площадь цилиндра: {full_area}"
    return f"Площадь боковой поверхности цилиндра: {lateral_area}"


if __name__ == "__main__":
    r = float(input("Введите радиус цилиндра: "))
    h = float(input("Введите высоту цилиндра: "))
    request_full_area = input("Хотите получить боковую(1) или полную(2) площадь?: ")
    if request_full_area == '1':
        print(cylinder(r, h))
    elif request_full_area == '2':
        print(cylinder(r, h, True))

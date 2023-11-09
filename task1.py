#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def positive() -> str:
    return "Число положительное"


def negative() -> str:
    return "Число отрицательное"


def test(num: float) -> str:
    if num > 0:
        return positive()
    return negative()


if __name__ == "__main__":
    print(test(float(input("Введите любое число: "))))

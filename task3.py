#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

prod = 1


def main(x: int):
    global prod
    if x != 0:
        prod *= x
    else:
        print(f"Было введено число 0.\nИтоговый рельзутат: {prod}")
        sys.exit()


if __name__ == "__main__":
    while True:
        x = int(input("Введите число: "))
        main(x)

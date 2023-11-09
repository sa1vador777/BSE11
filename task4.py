#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_input() -> str:
    return input("Введите строку: ")


def test_input(inp: str) -> bool:
    try:
        int(inp)
        return True
    except ValueError:
        return False


def str_to_int(inp: str) -> int:
    return int(inp)


def print_int(num: int) -> None:
    print(num)


if __name__ == "__main__":
    inp = get_input()
    if test_input(inp):
        num = str_to_int(inp)
        print_int(num)

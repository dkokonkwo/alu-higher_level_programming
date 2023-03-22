#!/usr/bin/python3
"""creates a class Myint and defines its methods"""


class MyInt(int):
    "instantiates  and defines compartors"
    def __init__(self, x: int) -> None:
        self.x = x

    def __eq__(self, __x: object) -> bool:
        "negates equality"
        return self.x != __x

    def __ne__(self, __x: object) -> bool:
        "negates not equality"
        return self.x == __x

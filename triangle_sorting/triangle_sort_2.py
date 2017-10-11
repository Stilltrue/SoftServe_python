#!/usr/bin/env python3

import math


class Triangle:
    def __init__(self, name, side_a, side_b, side_c):
        if type(side_a) != float or type(side_b) != float \
                or type(side_c) != float:
            raise TypeError
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError
        self.name = name
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.area = self.calculate_area()

    def __cmp__(self, other):
        if self.area < other.area:
            return -1
        elif self.area > other.area:
            return 1
        else:
            return 0

    def __le__(self, other):
        return self.__lt__(other)

    def __gt__(self, other):
        if self.area > other.area:
            return True
        else:
            return False

    def __ge__(self, other):
        return self.__gt__(other)

    def __eq__(self, other):
        if self.area == other.area:
            return True
        else:
            return False

    def __ne__(self, other):
        return self.__eq__(other)

    def __lt__(self, other):
        if self.area < other.area:
            return True
        else:
            return False

    @staticmethod
    def create_triangle():
        input_data = input("\nPlease, enter triangle name and three "
                           "triangle sides, separated by commas\n")
        try:
            data_list = input_data.split(',')
            if len(data_list) >= 5 or len(data_list) < 4:
                raise IndexError()
            triangle_data = dict(name=data_list[0], side_a=data_list[1],
                                 side_b=data_list[2], side_c=data_list[3])
            if not Triangle.check_triangle(data_list[1], data_list[2],
                                           data_list[3]):
                raise ValueError()
            return Triangle(str(triangle_data['name']),
                            float(triangle_data['side_a']),
                            float(triangle_data['side_b']),
                            float(triangle_data['side_c']))
        except (IndexError, ValueError):
            print(Triangle.get_error_msg())
            return Triangle.create_triangle()

    @staticmethod
    def is_positive_numbers(triangle_sides):
        for side in triangle_sides:
            if side > 0:
                return True
        return False

    @staticmethod
    def check_triangle(a, b, c):
        sides = [float(a), float(b), float(c)]

        if (sides[0] > sides[1] + sides[2])\
            or (sides[1] > sides[0] + sides[2])\
                or (sides[2] > sides[0] + sides[1]):
            return False

        if not Triangle.is_positive_numbers(sides):
            return False
        print("\nTriangle was successfully created and added!")
        return True

    def calculate_area(self):
        semi_perimeter = (self.side_a + self.side_b + self.side_c) / 2
        return round(math.sqrt(semi_perimeter
                               * (semi_perimeter - self.side_a)
                               * (semi_perimeter - self.side_b)
                               * (semi_perimeter - self.side_c)), 2)

    @staticmethod
    def get_error_msg():
        error_msg = "\nSorry, triangle isn't able to be constructed\n" \
                    "Verify you type the correct name and positive numbers:" \
                    " triangle name and three sides separated by comma\n" \
                    "The two sides sum must be greater than the third side\n" \
                    "Example: Illuminati, 22, 15.5, 22"
        return error_msg

    @classmethod
    def print_triangles(cls, triangles):
        print('========== Triangles list: ===========')
        for triangle in triangles:
            print('[Triangle {}]: {} cm'.format(triangle.name, triangle.area))


def is_program_continue():
    user_response = input("\nDo you want to add new triangle? ")
    if user_response.lower() in ('y', 'yes'):
        return True
    return False


def main():
    is_continue = True
    triangles_list = list()

    while is_continue:
        triangle_obj = Triangle.create_triangle()
        triangles_list.append(triangle_obj)
        triangles_list.sort(reverse=True)
        is_continue = is_program_continue()

    Triangle.print_triangles(triangles_list)


if __name__ == '__main__':
    main()

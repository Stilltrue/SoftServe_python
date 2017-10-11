#!/usr/bin/env python3
import sys

import argparse


class ChessBoard:
    def __init__(self, rows, elem_in_row):
        self.rows = rows
        self.elem_in_row = elem_in_row

    def print_chess_board(self):
        elem_to_print = "* "
        for i in range(self.rows):
            if i % 2 == 0:
                print(elem_to_print * ChessBoard.check_size(self.elem_in_row))
            else:
                print(elem_to_print[::-1]
                      * ChessBoard.check_size(self.elem_in_row))

    @staticmethod
    def check_size(elem_count):
        max_size = 80
        if elem_count > max_size:
            return max_size
        return elem_count


def get_arguments_data():
    arguments = list()
    if len(sys.argv) != 3 or (not sys.argv[1].isdecimal()) \
            or (not sys.argv[2].isdecimal()):
        print("\n******* Chess board *******\n"
              "Instructions for using program:\n"
              "Please enter two correct arguments\n"
              "MAX board size is 80\n"
              "Arguments are represented as the width and height of "
              "sought-for chess board\n"
              "Note: arguments must be a positive integer numbers\n")
        sys.exit()
    else:
        arguments.append(int(sys.argv[1]))
        arguments.append(int(sys.argv[2]))
        return arguments


def main():
    try:
        rows = get_arguments_data()[0]
        elements_in_row = get_arguments_data()[1]

        if not rows or not elements_in_row:
            raise ValueError
        else:
            new_chessboard = ChessBoard(rows, elements_in_row)
            new_chessboard.print_chess_board()

    except ValueError:
        print("Incorrect data. Numbers must be positive")


if __name__ == '__main__':
    main()

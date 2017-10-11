#!/usr/bin/env python3
import sys


class NumSequence:
    def __init__(self, max_value):
        self.max_value = max_value

    def __repr__(self):
        return "Ordinary numbers sequence: {}" \
               .format(str(self.calc_number_squares()))

    def calc_number_squares(self):
        result_list = list()
        for current_number in range(1, self.max_value):
            if (current_number ** 2) < self.max_value:
                result_list.append(current_number)
        return result_list \
            if result_list else "\tThere is no numbers in this sequence"


def get_arguments_data():
        if len(sys.argv) != 2 or not sys.argv[1].isdecimal():
            print("\n******* Number Sequence *******\n"
                  "Instructions for using the program:\n"
                  "Please enter the correct argument\n"
                  "Argument is the end of sought-for sequence\n"
                  "Note: argument must be a positive number")
            sys.exit()
        else:
            return int(sys.argv[1])


def main():
    max_value = get_arguments_data()
    num_sequence = NumSequence(max_value)
    print(num_sequence)


if __name__ == '__main__':
    main()

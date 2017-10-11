#!/usr/bin/env python3
import sys


class FibonacciSequence:
    def __init__(self, sequence_start, sequence_end):
        if sequence_start > sequence_end:
            self.sequence_start = sequence_end
            self.sequence_end = sequence_start
        else:
            self.sequence_start = sequence_start
            self.sequence_end = sequence_end

    def __repr__(self):
        return "Fibonacci sequence: {}".format(str(self.create_sequence()))

    def create_sequence(self):
        required_number = 0
        next_number = 1
        sequence_list = list()
        while required_number <= self.sequence_end:
            if required_number >= self.sequence_start:
                sequence_list.append(required_number)
            required_number, next_number = \
                next_number, required_number + next_number
        return sequence_list if sequence_list else "\tThere is no numbers in " \
                                                   "this sequence"


def get_arguments_data():
    if len(sys.argv) != 3 or (not sys.argv[1].isdecimal()) \
                          or (not sys.argv[2].isdecimal()):
        print("\n******* Fibonacci Sequence *******\n"
              "Instructions for using program:\n"
              "Please enter two correct arguments\n"
              "Arguments are represented as the start and the end of "
              "sought-for sequence\n"
              "Note: arguments must be a positive numbers\n"
              "The second argument must be greater than first")
        sys.exit()
    else:
        return [int(sys.argv[1]), int(sys.argv[2])]


def main():
    sequence_start = get_arguments_data()[0]
    sequence_end = get_arguments_data()[1]
    fibonacci_sequence = FibonacciSequence(sequence_start, sequence_end)
    print(fibonacci_sequence)


if __name__ == '__main__':
    main()

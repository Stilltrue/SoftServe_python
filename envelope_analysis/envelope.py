#!/usr/bin/env python3
import sys


class Envelope:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def determine_nested_ability(self, second_env):
        if (self.width > second_env.width) \
                and (self.height > second_env.height):
            self.print_nested_ability(second_env, 'first', 'second')
        elif (second_env.width > self.width) \
                and (second_env.height > self.height):
            second_env.print_nested_ability(self, 'second', 'first')
        else:
            print("\nEnvelopes {} and {} can't be nested inside each "
                  "other".format(str([self.width, self.height]),
                                 str([second_env.width,
                                      second_env.height])))

    def print_nested_ability(self, second_env, env_one, env_two):
        print("\n{} envelope {} can be put to the {} {}"
              .format(env_two, str([second_env.width, second_env.height]),
                      env_one, str([self.width, self.height])))


def continue_program():
    user_response = input("\nDo you want to continue? ")
    if user_response.lower() in ('y', 'yes'):
        main()
    else:
        sys.exit()


def create_input(side, current_number):
    while True:
        try:
            text = "{} {} {} {} {} ".format("Enter the", side, "of",
                                            current_number, "envelope" ": " "=")
            side_value = float(input(text))
            if side_value <= 0:
                raise ValueError
            return side_value
        except ValueError:
            print("\n========= Envelope Analysis =========\n"
                  "\nPlease, enter the correct envelopes sides to determinate "
                  "whether one envelope is able to contain the other. "
                  "\nEach side must be a positive number\n")


def main():
    first_env_width = create_input('width', 'first')
    first_env_height = create_input('height', 'first')
    second_env_width = create_input('width', 'second')
    second_env_height = create_input('height', 'second')

    first_envelope = Envelope(first_env_width, first_env_height)
    second_envelope = Envelope(second_env_width, second_env_height)

    first_envelope.determine_nested_ability(second_envelope)
    continue_program()


if __name__ == '__main__':
    main()

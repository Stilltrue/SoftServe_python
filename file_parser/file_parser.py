#!/usr/bin/env python3
import sys


class Parser:
    @staticmethod
    def count_occurrence(file_path, str_to_find):
        try:
            with open(file_path, 'r') as file:
                count = 0
                for line in file:
                    if str_to_find in line:
                        count = count + 1
                if count:
                    print("String [{}] has been found {} times".format(
                                                            str_to_find, count))
                else:
                    print("There're no any strings matches in this file\n")
        except FileNotFoundError:
            print("File path has not been found\n"
                  "Please, check the file path and try again")

    @staticmethod
    def make_replacement(file_path, str_to_delete, replacement_str):
        try:
            with open(file_path, 'r') as file:
                current_file = file.read()
            current_file = current_file.replace(str_to_delete, replacement_str)

            with open(file_path, 'w') as file:
                file.write(current_file)
            print("File [{}] has been changed. [{}] has been inserted instead "
                  "of [{}]".format(file_path, replacement_str, str_to_delete))

        except FileNotFoundError:
            print("File path has not been found\n"
                  "Please, check the file path and try again")


def main():
    if len(sys.argv) == 3:
        Parser.count_occurrence(sys.argv[1], sys.argv[2])
    elif len(sys.argv) == 4:
        Parser.make_replacement(sys.argv[1], sys.argv[2], sys.argv[3])
    elif len(sys.argv) < 3 or len(sys.argv) > 4:
        print("\n======= File parser =======\n"
              "Instructions for using\n"
              "Program has two operation mode:\n"
              "First - counts string occurrence in file\n"
              "Required arguments for first: file path, string for counting\n"
              "Second - replaces a string to another in the specified file\n"
              "Required arguments for second: file path, string which must be "
              "replaced, replacement string which changes previous\n"
              "Please enter two correct arguments\n")


if __name__ == '__main__':
    main()

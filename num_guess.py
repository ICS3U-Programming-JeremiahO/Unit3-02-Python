#!/usr/bin/env python3
# Created By: Jeremiah omoike
# Date: October 7 2022
# This program takes a guess number from user and checks if it is correct
import constants


def main():
    # get user input
    guessed_number = float(input("Guess a number between 0 and 9:"))

    # check if the number is correct or incorrect
    if guessed_number > constants.CORRECT_NUMBER:
        print()
        print("you are incorrect!")

    if guessed_number < constants.CORRECT_NUMBER:
        print()
        print("you are incorrect!")

    if guessed_number == constants.CORRECT_NUMBER:
        print()
        print("you are correct!")


if __name__ == "__main__":

    main()

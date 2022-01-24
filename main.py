#!/usr/bin/env python3

# Created by: Daniel Pawelko
# Created on: Jan 2022
# Assignment 6


def pentagon(side: float):
    return side * 5


def main():
    # main function for calling function

    try:
        # input
        side = input("Length of one side(mm): ")
        side = float(side)

        print(f"Perimeter of your pentagon is: {pentagon(side)} mm")
    except ValueError:
        print("Please input a number")

    # done
    print("")
    print("Done.")


if __name__ == "__main__":
    main()

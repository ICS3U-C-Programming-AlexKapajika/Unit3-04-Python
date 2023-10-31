#!/usr/bin/env python3
# Created by: Alex Kapajika
# Created on: Oct 19, 2023
# This program make


def main():
    color_of_light = input("What is the color of the light: ")
    print("")

    if color_of_light == "red":
        print("Stop!")
    elif color_of_light == "yellow":
        print("Slow down.")
    elif color_of_light == "green":
        print("Go, if all clear.")

    else:
        print("No idea!")


if __name__ == "__main__":
    main()

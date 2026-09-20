#!/usr/bin/env python3
# Elijah Walker - AICC 120 Assignment A0B - Cleaning Data
import statistics as s

data = [
    [64, 0, 0, 52, 69, 46, 58, 67, 0, 55],
    [0, 37, 53, 71, 0, 60, 72, 75, 43, 0],
    [0, 61, 49, 58, 0, 73, 71, 75, 41, 66],
    [43, 0, 71, 29, 0, 74, 72, 47, 0, 62],
    [67, 64, 0, 0, 61, 42, 70, 0, 59, 30],
    [0, 72, 69, 67, 0, 41, 62, 0, 48, 59],
    [50, 74, 69, 0, 42, 0, 38, 0, 73, 61],
    [0, 0, 59, 64, 31, 48, 62, 0, 53, 46],
    [57, 0, 68, 73, 59, 75, 0, 27, 62, 0],
    [35, 54, 0, 0, 29, 62, 75, 71, 0, 48]
]

show_means = False


def calculate_average(row):
    # returns the average of the non-zero numbers in the row.
    # formatting like this means i dont even need a counter function for zeros!
    return round(s.mean(num for num in row if num != 0), 2)


def replace_zeros(row, avg):
    # replaces all zeroes in the row with the row's average.
    new_row = [avg if item == 0 else item for item in row]
    data[data.index(row)] = new_row


def process_data(data):
    # for each row in the data, calculate the average (disregading zeros),
    # replace the zeros with the average, and output the row
    for row in data:
        replace_zeros(row, calculate_average(row))
    global show_means
    show_means = True


def display_data():
    # outputs data in the format i usually use
    for lists in data:
        conc = "\t"
        for items in lists:
            conc += str(items) + ", "
        if show_means:
            print(f"{conc[:-2]}\t\t{calculate_average(lists)}")
        else:
            print(conc[:-2])


def main():
    print("\n------------------------------------------------------\n"
          "------------------- Cleaning Data! -------------------\n"
          "------------------------------------------------------\n")
    print("\nRaw data set (a list of lists, divided by row):\n")
    display_data()
    print("\n\n\nLet's calculate the mean of each list, disregarding zeroes.\n"
          "We'll then replace each zero within the list(s) with said mean.\n"
          "\n\tPROCESSED DATA SET:\t\t\t\t\tMEANS:\n")
    process_data(data)
    display_data()
    print("\n\n\nTa-da! Short and sweet.\n\n")
    print("------------------------------------------------------\n")


if __name__ == "__main__":
    main()

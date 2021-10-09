import random


# Entrance of the program.
def main():
    repeat_main = True
    while repeat_main:
        # Menu
        print("[1] Manuel Entrance")
        print("[2] Random Entrance")
        print("[3] Exit")
        menu_input = check_menu_input()

        if menu_input == 3:
            repeat_main = False

        elif menu_input == 1 or menu_input == 2:

            # Repeat until valid matrix dimensions are given.
            not_valid = True
            while not_valid:
                # Dimensions are entered.
                first_matrix_row, first_matrix_col, second_matrix_row, second_matrix_col = enter_dimensions()

                # Check if matrix multiplication is possible.
                if first_matrix_col == second_matrix_row:
                    not_valid = False
                    print("--------------------------------------")
                    print("The Matrix is Valid. Continue..")

                    # Manual matrix entrance.
                    if menu_input == 1:
                        first_matrix, second_matrix = enter_matrices(first_matrix_row, first_matrix_col,
                                                                     second_matrix_row, second_matrix_col)
                    # Random matrices.
                    else:
                        lower_bound, upper_bound = enter_bounds()
                        first_matrix, second_matrix = random_matrices(first_matrix_row, first_matrix_col,
                                                                      second_matrix_row, second_matrix_col,
                                                                      lower_bound, upper_bound)
                else:
                    print("Invalid calculation! "
                          "The column of column of first matrix have to be equal to row of the second matrix!")
                    print("--------------------------------------\n")


# Check keyboard inputs for main menu, dimensions and matrix data.
def check_menu_input():
    while True:
        keyboard_input = input()
        try:
            keyboard_input = int(keyboard_input)
            if not keyboard_input == 1 and keyboard_input == 2 and keyboard_input == 3:
                raise ValueError
            break
        except ValueError:
            print("Please enter a number between 1-3")

    return keyboard_input


def check_dimension_input():
    while True:
        keyboard_input = input()
        try:
            keyboard_input = int(keyboard_input)
            if 100 >= keyboard_input > 0:
                break
            print("Supported dimension values are between 1-100.")
        except ValueError:
            print("Please enter a valid dimension.")

    return keyboard_input


def check_float():
    while True:
        keyboard_input = input()
        try:
            keyboard_input = float(keyboard_input)
            break
        except ValueError:
            print("Please enter a number.")

    return keyboard_input


def enter_matrix_dimension(_message):
    print(_message)
    _row = check_dimension_input()
    _col = check_dimension_input()
    return _row, _col


# Enter both matrix dimensions.
def enter_dimensions():
    _first_row, _first__col = enter_matrix_dimension("Write the ROW and COLUMN of FIRST MATRIX respectively :")
    _second_row, _second_col = enter_matrix_dimension("Write the ROW and COLUMN of SECOND MATRIX respectively :")

    return _first_row, _first__col, _second_row, _second_col


def initialize_matrix(_rows, _cols):
    return [[0 for _ in range(_cols)] for _ in range(_rows)]


def enter_matrix_data(_message, _rows, _cols):
    print(_message)
    _matrix = initialize_matrix(_rows, _cols)

    for i in range(_rows):
        for j in range(_cols):
            _matrix[i][j] = check_float()

    return _matrix


def enter_matrices(_first_matrix_row, _first_matrix_col, _second_matrix_row, _second_matrix_col):
    _first_matrix = enter_matrix_data("FIRST MATRIX : ", _first_matrix_row, _first_matrix_col)
    print_matrix(_first_matrix)
    _second_matrix = enter_matrix_data("Second MATRIX : ", _second_matrix_row, _second_matrix_col)
    print_matrix(_second_matrix)
    return _first_matrix, _second_matrix


def enter_one_bound(_message):
    print(_message)
    _bound = check_float()
    return _bound


def enter_bounds():
    _lower_bound = enter_one_bound("Enter lower bound: ")
    _upper_bound = enter_one_bound("Enter upper bound")
    return _lower_bound, _upper_bound


def random_matrix_data(_rows, _cols, _lower_bond, _upper_bond):
    _matrix = initialize_matrix(_rows, _cols)

    for i in range(_rows):
        for j in range(_cols):
            _matrix[i][j] = random.uniform(_lower_bond, _upper_bond)

    return _matrix


def random_matrices(_first_matrix_row, _first_matrix_col, _second_matrix_row, _second_matrix_col,
                    _lower_bond, _upper_bond):
    _first_matrix = random_matrix_data(_first_matrix_row, _first_matrix_col, _lower_bond, _upper_bond)
    print_matrix(_first_matrix)
    _second_matrix = random_matrix_data(_second_matrix_row, _second_matrix_col, _lower_bond, _upper_bond)
    print_matrix(_second_matrix)
    return _first_matrix, _second_matrix


def print_matrix(_matrix):
    print("-----------")
    for i in range(len(_matrix)):
        for j in range(len(_matrix[i])):
            print(str(_matrix[i][j]) + " ", end=" ")
        print()
    print("-----------\n")


if __name__ == "__main__":
    main()

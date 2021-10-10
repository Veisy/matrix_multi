import random
import seaborn as sns
import matplotlib.pyplot as plt
sns.set()


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

                    result_matrix = matrix_multiplication(first_matrix, second_matrix)
                    print_and_draw_matrix("RESULT MATRIX: ", result_matrix)

                else:
                    print("Invalid calculation! "
                          "The column of column of first matrix have to be equal to row of the second matrix!")
                    print("--------------------------------------\n")


# # Functions are defined below.

# # Functions with '_' at the beginning of their names are functions that are not used directly,
# # but only used by other functions.

# Matrix multiplication function.
def matrix_multiplication(_first_matrix, _second_matrix):
    # Initialize result matrix with empty fields.
    result_matrix = _initialize_matrix(len(_first_matrix), len(_second_matrix[0]))

    # Loop over first matrix's row and second matrix's column.
    for i in range(len(_first_matrix)):
        for j in range(len(_second_matrix[0])):
            # Multiply the values in the row of the first matrix the values in the column of the second matrix,
            # and add them all.
            # Then save this value to the row and column index of the result matrix.
            multiplied_value = 0
            for k in range(len(_second_matrix)):
                multiplied_value += _first_matrix[i][k] * _second_matrix[k][j]

            result_matrix[i][j] = multiplied_value

    return result_matrix


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


def _check_dimension_input():
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


def _check_float():
    while True:
        keyboard_input = input()
        try:
            keyboard_input = float(keyboard_input)
            break
        except ValueError:
            print("Please enter a number.")

    return keyboard_input


def _enter_matrix_dimension(_message):
    print(_message)
    row = _check_dimension_input()
    col = _check_dimension_input()
    return row, col


# Enter both matrix dimensions.
def enter_dimensions():
    first_row, first__col = _enter_matrix_dimension("Write the ROW and COLUMN of FIRST MATRIX respectively :")
    second_row, second_col = _enter_matrix_dimension("Write the ROW and COLUMN of SECOND MATRIX respectively :")

    return first_row, first__col, second_row, second_col


def _initialize_matrix(_rows, _cols):
    return [[0 for _ in range(_cols)] for _ in range(_rows)]


def _enter_matrix_data(_message, _rows, _cols):
    print(_message)
    matrix = _initialize_matrix(_rows, _cols)

    for i in range(_rows):
        for j in range(_cols):
            matrix[i][j] = _check_float()

    _print_matrix(_message, matrix)

    return matrix


def enter_matrices(_first_matrix_row, _first_matrix_col, _second_matrix_row, _second_matrix_col):
    first_matrix = _enter_matrix_data("FIRST MATRIX : ", _first_matrix_row, _first_matrix_col)
    second_matrix = _enter_matrix_data("Second MATRIX : ", _second_matrix_row, _second_matrix_col)
    return first_matrix, second_matrix


def _enter_one_bound(_message):
    print(_message)
    bound = _check_float()
    return bound


def enter_bounds():
    # Check if lower bound is smaller then upper bound. If not, ask again.
    while True:
        lower_bound = _enter_one_bound("Enter lower bound: ")
        upper_bound = _enter_one_bound("Enter upper bound")
        if lower_bound < upper_bound:
            break
        print("Upper bound must be bigger than lower bound.")
    return lower_bound, upper_bound


def _random_matrix_data(_message, _rows, _cols, _lower_bond, _upper_bond):
    matrix = _initialize_matrix(_rows, _cols)

    for i in range(_rows):
        for j in range(_cols):
            matrix[i][j] = random.uniform(_lower_bond, _upper_bond)

    _print_matrix(_message, matrix)
    return matrix


def random_matrices(_first_matrix_row, _first_matrix_col, _second_matrix_row, _second_matrix_col,
                    _lower_bond, _upper_bond):
    first_matrix = _random_matrix_data("FIRST MATRIX : ", _first_matrix_row, _first_matrix_col,
                                       _lower_bond, _upper_bond)
    second_matrix = _random_matrix_data("SECOND MATRIX : ", _second_matrix_row, _second_matrix_col,
                                        _lower_bond, _upper_bond)
    return first_matrix, second_matrix


def _print_matrix(_message, _matrix):
    print(_message)
    print("-----------")
    for i in range(len(_matrix)):
        for j in range(len(_matrix[0])):
            print(str(_matrix[i][j]) + " ", end=" ")
        print()
    print("-----------\n")


def _draw_matrix(_message, _matrix):
    # Draw only if elements are smaller then 100, and row-column smaller then 20.
    if not int(max(map(max, _matrix))) < 10000 \
            and len(_matrix) < 20 \
            and len(_matrix[0]) < 20:
        return

    # Convert float array to int array.
    result_array_as_int = _initialize_matrix(len(_matrix), len(_matrix[0]))
    for i in range(len(_matrix)):
        for j in range(len(_matrix[0])):
            result_array_as_int[i][j] = int(_matrix[i][j])

    sns.heatmap(result_array_as_int, annot=True, fmt="d")
    plt.title(_message, fontsize=12)
    plt.show()


def print_and_draw_matrix(_message, _matrix):
    _print_matrix(_message, _matrix)
    _draw_matrix(_message, _matrix)


if __name__ == "__main__":
    main()

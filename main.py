from ctypes import *

# Loading my c_matrix_multi library functions.
c_matrix_multi = CDLL('./c_matrix_multi.so')

c_matrix_multi.main()

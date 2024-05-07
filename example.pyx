cdef extern from "my_function.cpp":
    void my_cpp_function()

def call_cpp_function():
    my_cpp_function()

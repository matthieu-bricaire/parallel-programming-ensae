This repository contains a basic example of how to call a C++ function in python, using Cython.

Here are the different steps to perform:

- Create a .cpp file, that contains the C++ code of the desired function (my_function.cpp)
- Create a .pyx file that defines the function in Cython (importing it from my_function.cpp), and specifies how to call it (example.pyx)
- Create the setup.py file, which contains the code required to build the python extension from the .pyx file. Inside it, you may need to specify a directory for the C++ libraries used in the .cpp code (include_dirs argument). To locate a specific library (eg iostream), you may run : "find /usr/include /usr/local/include -name iostream" in your terminal, and collect the returned directory. Also, you have to choose the name of the created extension (mylib here).
- Build the extension by running "python setup.py build_ext --inplace". This command creates:
    - An example.cpp file (referring to the example.pyx file)
    - A build/ folder, containing specific files related to the built extension
    - The mylib.cpython-312-x86_64-linux-gnu.so file, which corresponds to the extension that will be called in python
- Finally, create the main.py file, in which you can call the created "mylib" extension. You may treat it as a regular package, and call it with "import mylib". Then, you can use the function (originally written in C++) with mylib.my_cpp_function()
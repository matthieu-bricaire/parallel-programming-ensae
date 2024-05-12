#include <iostream>
#include <vector>
#include <cmath>
#include <omp.h>

// Definition of a type alias corresponding to a 2D float matrix
#define my_matrix std::vector<std::vector<float>>

// Function to compute the sigmul operation in parallel
my_matrix sigmul(const my_matrix& A) {

    int numRows = A.size();
    int numCols = (numRows > 0) ? A[0].size() : 0;

    my_matrix B(numRows, std::vector<float>(numCols));

    #pragma omp parallel for simd collapse(2)
    for (int i = 0; i < numRows; i++) {
        for (int j = 0; j < numCols; j++) {
            float a = A[i][j];
            B[i][j] = a / (1 + exp(-a));
        }
    }

    return B;
}

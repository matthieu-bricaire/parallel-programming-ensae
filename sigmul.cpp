#include <iostream>
#include <vector>
#include <cmath>
#include <omp.h>

#define my_matrix std::vector<std::vector<float>>

my_matrix sigmul(const my_matrix& A) {

    // Declare size of A
    int numRows = A.size();
    int numCols = (numRows > 0) ? A[0].size() : 0;

    // Define matrix B
    my_matrix B(numRows, std::vector<float>(numCols));

    // Perform the operation in parallel
    #pragma omp parallel for simd collapse(2)
    for (int i = 0; i < numRows; i++) {
        for (int j = 0; j < numCols; j++) {
            float a = A[i][j];
            B[i][j] = a / (1 + exp(-a));
        }
    }

    return B;
}
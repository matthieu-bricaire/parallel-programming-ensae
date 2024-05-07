#include <iostream>
#include <vector>
#include <cmath>
#include <omp.h>

#define my_matrix std::vector<std::vector<float>>

my_matrix sigmul(const my_matrix& A) {
    int n_threads = omp_get_max_threads();
    std::cout << "Number of threads: " << n_threads << std::endl;

    // Define matrix B
    my_matrix B(A.size(), std::vector<float>(A[0].size()));

    // Perform the operation in parallel
    #pragma omp parallel for
    for (int i = 0; i < A.size(); i++) {
        for (int j = 0; j < A[i].size(); j++) {
            float a = A[i][j];
            float result = a / (1 + exp(-a));
            B[i][j] = result;
        }
    }

    return B;
}
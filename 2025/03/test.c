#include <omp.h>
#include <stdio.h>

int main(int argc, char** argv) {

    size_t line_count = 1000;
    int nthreads, tid;
    #pragma omp parallel for schedule(dynamic, 1) private(tid) shared(line_count)

    for (size_t i=0; i<line_count; i++) {
        tid = omp_get_thread_num();
        printf("[%i]\t%lu\n", tid, i);
    }

}
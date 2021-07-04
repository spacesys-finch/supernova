#include <stdlib.h>
#include <stdio.h>

// Parser for butcher table
void butcher(double*** a, double** b, double** c, char filename[], int* num) {
    /*
    a (pointer to 2D array) = steps: lower triangular array of size n, should be sent UNALLOCATED
    b (pointer to 1D array) = sums: single array of size n, should be sent UNALLOCATED
    c (pointer to 1D array) = weights: single array of size n, should be sent UNALLOCATED
    
    filename: filename of butcher tableau, space delimited with all numbers written as rationals
    n: length of tableau
    */
    FILE *fp = fopen(filename, "r");

    // PREAMBLE
    int lines = 0;
    char ch;
    // scan number of lines
    while(!feof(fp)) if(fgetc(fp) == '\n') lines++;
    rewind(fp); // rewind

    // PARSE
    // parse steps
    int n = lines-1;
    *num = n; // assign length

    *a = calloc(n, sizeof(double*));
    *b = calloc(n, sizeof(double));
    *c = calloc(n, sizeof(double));

    // BUTCHER TABLE CONSTRUCTION
    // first row of butcher table
    (*c)[0] = 0;
    (*a)[0] = NULL; // not needed, so make it null

    // dump first line of buffer
    float f1, f2; // numerator and denominator
    // MUST BE FLOAT TO PARSE PROPERLY

    fscanf(fp, "%f/%f\n", &f1, &f2);

    // start from the second matrix row, since the first is just zero.
    for (int i = 1; i <= n; i++) {        
        
        fscanf(fp, "%f/%f", &f1, &f2);
        (*c)[i] = f1/f2; // parse c coefficient

        // prepare list for a coefficients in this row
        (*a)[i] = calloc(i, sizeof(double));

        for (int j = 0; j < i; j++) {
            fscanf(fp, " %f/%f", &f1, &f2);
            (*a)[i][j] = f1/f2;
        }
        
        fscanf(fp, "\n"); // Skip line break
    }

    // SUMS
    fscanf(fp, "%f/%f", &f1, &f2);
    (*b)[0] = f1/f2;
    for (int i = 1; i <= n; i++) {
        fscanf(fp, " %f/%f", &f1, &f2);
        (*b)[i] = f1/f2;
    }
}

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <math.h>
#include <regex.h>
#include <omp.h>


#define FALSE 0
#define TRUE 1

const int max_joltage = (int)(1e12 - 1);
const int min_joltage = (int)(1e11);


int read_file(const char* filepath, char*** lines_array, size_t* line_count) {
    FILE* fp = fopen(filepath, "r");
    if (!fp) {
        return -1;
    }

    // read first line to get length
    long start_pos = ftell(fp);
    size_t line_len = 0;
    int curr_char;
    while ((curr_char=fgetc(fp)) != EOF && curr_char != '\n') {
        line_len++;
    }

    // close file if empty
    if (curr_char == EOF && line_len == 0) {
        fclose(fp);
        return -2;
    }
    
    // count number of lines
    fseek(fp, start_pos, SEEK_SET);
    size_t count = 0;
    while ((curr_char=fgetc(fp)) != EOF) {
        if (curr_char == '\n') {
            count++;
        }
    }
    
    // allocate array of string pointers to store complete file
    char** lines = malloc(count * sizeof(char*));
    if (!lines) {
        fclose(fp);
        return -3;
    }
    
    // allocate and read each line
    fseek(fp, start_pos, SEEK_SET);
    for (size_t i=0; i<count; i++) {
        lines[i] = malloc(line_len+1);

        // free all previously allocated lines and close file
        //  if malloc for curent line fails
        //  or read line does not match expected length
        if (!lines[i] || fread(lines[i], 1, line_len, fp) != line_len) {
            for (size_t j=0; j<i; j++) {
                free(lines[j]);
            }
            free(lines);
            fclose(fp);
            return -4;
        }

        lines[i][line_len] = 0;

        // skip new line char
        fgetc(fp);
    }

    // close file and return lines array and line count
    fclose(fp);
    *lines_array = lines;
    *line_count = count;
    return 0;
}


// return TRUE if every joltage digit matches with any bank digit in order
int bank_contains_joltage(char** bank, unsigned long long* joltage_num) {
    // convert joltage into a string
    size_t buffer_size = 32;
    char *joltage = malloc(buffer_size);
    if (!joltage) {
        return -1;
    }
    snprintf(joltage, buffer_size, "%llu", *joltage_num);
    
    // bank and joltage length
    size_t bank_len = strlen(*bank);
    size_t joltage_len = strlen(joltage);
    
    // iterate over bank digits and compare joltage digits to find a match
    char bank_digit;
    char joltage_digit;
    for (size_t bi=0, ji=0; bi<bank_len; bi++) {

        bank_digit = (*bank)[bi];
        joltage_digit = joltage[ji];
        if (bank_digit == joltage_digit) {
            ji++;

            // match found if end of joltage reached before end of bank
            if (ji == joltage_len) {
                free(joltage);
                return TRUE;
            }
        }

    }

    free(joltage);
    return FALSE;
}


// returns TRUE if the number contains the digit 0
int contains_digit_zero(unsigned long long num) {
    while (num > 0) {
        if (num % 10 == 0) {
            return TRUE;
        }
        num /= 10;
    }
    return FALSE;
}


// iterate backwards over all possible joltages until first match with bank
int find_max_joltage(char** bank, size_t digits, unsigned long long* found_max_joltage) {
    unsigned long long lower_joltage = (unsigned long long)powf(10.0f, (float)(digits-1));      // 1e(12-1) = 1e11 = 100_000_000_000
    unsigned long long upper_joltage = (unsigned long long)powf(10.0f, (float)digits) - 1;      // 1e12 - 1 =        999_999_999_999

    for (unsigned long long current_joltage = upper_joltage; current_joltage >= lower_joltage; current_joltage--) {
        if (contains_digit_zero(current_joltage) == TRUE) {
            continue;
        }
        // printf("%llu ", current_joltage);
        if (bank_contains_joltage(bank, &current_joltage) == TRUE) {
            *found_max_joltage = current_joltage;
            return 0;
        }
    }

    return -1;
}


int main(int argc, char** argv) {
    // get input file
    char filepath[250] = "example.txt";
    if (argc > 1) {
        strncpy(filepath, argv[1], 250);
    }

    // read file
    char** lines_array;
    size_t line_count = 0;
    int ret = read_file((const char*)filepath, &lines_array, &line_count);

    // // print file line by line
    // printf("line_count=%lu\n", line_count);
    // for (size_t i=0; i<line_count; i++) {
    //     printf("%lu: %s\n", i+1, lines_array[i]);
    // }

    // // testing
    // char* test_bank = lines_array[0];
    // unsigned long long test_joltage = 9887654321;
    // printf("expect %i, it is: %i\n", FALSE, bank_contains_joltage(&test_bank, &test_joltage));

    // get amount of digits to match
    size_t digits = 12;
    if (argc > 2) {
        digits = (size_t)strtoul(argv[2], NULL, 10);
    }

    // solve the file
    char** bank;
    unsigned long long total_max_joltage = 0ULL;
    unsigned long long found_max_joltage = 0ULL;
    for (size_t i=0; i<line_count; i++) {
        bank = &(lines_array[i]);
        printf("%lu: %s\n", i+1, *bank);

        find_max_joltage(bank, digits, &found_max_joltage);
        printf("found max joltage: %llu\n", found_max_joltage);
        total_max_joltage += found_max_joltage;
    }

    // memory cleanup
    if (lines_array) {
        for (size_t i=0; i<line_count; i++) {
            free(lines_array[i]);
        }
        free(lines_array);
    }

    return 0;
}

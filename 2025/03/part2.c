
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <math.h>
#include <omp.h>


#define max(a,b) (a>b ? a : b)

#define FALSE 0
#define TRUE 1
#define SUCCESS 0

#define MAX_DIGITS (size_t)32

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
    return SUCCESS;
}


// in-place array reverse
void reverse_string(char* string, size_t string_len) {
    size_t left = 0;
    size_t right = string_len - 1;
    char tmp;
    while (left < right)
    {
        tmp = string[left];
        string[left] = string[right];
        string[right] = tmp;
        left++;
        right--;
    }
}


// return TRUE if string contains char
int str_contains_char(const char *string, char c, size_t str_len) {
    for (size_t i=0; i<str_len; i++) {
        if (string[i] == c) {
            return TRUE;
        }
    }
    return FALSE;
}


// split integer into an array of digits and returns FALSE if it contains an disallowed digit
int split_to_digits(unsigned long long num, char* digits, size_t digits_len, size_t* digit_count, const char* allowed_digits, size_t allowed_digits_len) {
    char contains_disallowed_chars = FALSE;
    char digit;
    size_t buff_ind = 0;

    while (num > 0) {
        if (buff_ind == digits_len) {
            printf("out of bound\n");
            break;
        }
        
        // get ascii value for current digit
        digit = (char)('0' + (num % 10ULL));
        digits[buff_ind++] = digit;
        num /= 10ULL;

        if (str_contains_char(allowed_digits, digit, allowed_digits_len) == FALSE) {
            contains_disallowed_chars = TRUE;
        }
    }

    reverse_string(digits, buff_ind);
    *digit_count = buff_ind;
    return !contains_disallowed_chars;
}


// return TRUE if every joltage digit matches with any bank digit in order
int bank_contains_joltage(char* bank, char* joltage, size_t bank_len, size_t joltage_len) {
    // iterate over bank digits and compare joltage digits to find a match
    char bank_digit;
    char joltage_digit;
    for (size_t bi=0, ji=0; bi<bank_len; bi++) {

        bank_digit = bank[bi];
        joltage_digit = joltage[ji];
        if (bank_digit == joltage_digit) {
            ji++;

            // match found if end of joltage reached before end of bank
            if (ji == joltage_len) {
                return TRUE;
            }
        }

    }

    return FALSE;
}


// iterate over all possible joltages until first match with bank, returns SUCCESS if a max was found
int find_max_joltage(char* bank, size_t bank_len, size_t joltage_len, unsigned long long* found_max_joltage) {
    unsigned long long lower_joltage = (unsigned long long)powf(10.0f, (float)(joltage_len-1));      // 1e(12-1) = 1e11 = 100_000_000_000
    unsigned long long upper_joltage = (unsigned long long)powf(10.0f, (float)joltage_len) - 1;      // 1e12 - 1 =        999_999_999_999

    unsigned long long global_max_joltage = 0ULL;
    *found_max_joltage = global_max_joltage;
    size_t true_joltage_len;

    // get all digits used by the bank
    size_t true_used_digits_len = 0;
    char used_digits[11] = {bank[0]};

    for (size_t bi=1; bi<bank_len; bi++) {
        char current_digit = bank[bi];
        if (str_contains_char(used_digits, current_digit, true_used_digits_len) == FALSE) {
            if (true_used_digits_len < 10) {
                used_digits[true_used_digits_len] = current_digit;
                used_digits[++true_used_digits_len] = '\0';
            } else {
                return -1;
            }
        }
    }
    printf("used digits: %s\n", used_digits);

    // #pragma omp parallel for \
    //     schedule(dynamic, 1) \
    //     reduction(max:global_max_joltage) \
    //     shared(bank, bank_len, joltage_len, lower_joltage, upper_joltage) \
    //     private(true_joltage_len)
    
    for (unsigned long long joltage_num = upper_joltage; joltage_num >= lower_joltage; joltage_num--) {
        char joltage[MAX_DIGITS];
        // convert joltage to string and check for used digits
        if (split_to_digits(joltage_num, joltage, joltage_len, &true_joltage_len, used_digits, true_used_digits_len) == FALSE) {
            continue;
        }
        // printf("%llu ", joltage_num);

        if (bank_contains_joltage(bank, joltage, bank_len, true_joltage_len) == TRUE) {
            // global_max_joltage = joltage_num;
            // joltage_num = lower_joltage;        // effectivly a break
            
            global_max_joltage = max(joltage_num, global_max_joltage);
            break;
        }
    }

    *found_max_joltage = global_max_joltage;
    return (global_max_joltage == 0ULL) ? -2 : SUCCESS;
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

    // get amount of digits to match
    size_t joltage_digits = 12;
    if (argc > 2) {
        joltage_digits = (size_t)strtoul(argv[2], NULL, 10);
        if (joltage_digits > MAX_DIGITS) {
            printf("limit joltage digits from %lu to %lu\n", joltage_digits, MAX_DIGITS);
            joltage_digits = MAX_DIGITS;
        }
    }

    // solve the file parallalized
    char* bank;
    unsigned long long total_max_joltage = 0ULL;
    unsigned long long found_max_joltage;
    
    int nthreads, tid;
    #pragma omp parallel for \
        schedule(dynamic, 1) \
        reduction(+:total_max_joltage) \
        private(bank, found_max_joltage, tid) \
        shared(line_count, lines_array, joltage_digits)
    
    for (size_t i=0; i<line_count; i++) {
        tid = omp_get_thread_num();
        bank = lines_array[i];
        printf("[%i] %lu: %s\n", tid, i+1, bank);

        find_max_joltage(bank, strlen(bank), joltage_digits, &found_max_joltage);
        printf("[%i] %lu: found max joltage: %llu\n", tid, i+1, found_max_joltage);

        total_max_joltage += found_max_joltage;
    }

    printf("Solution: %llu\n", total_max_joltage);

    // memory cleanup
    if (lines_array) {
        for (size_t i=0; i<line_count; i++) {
            free(lines_array[i]);
        }
        free(lines_array);
    }

    return SUCCESS;
}

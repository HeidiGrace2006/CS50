#include <cs50.h>
#include <stdio.h>

//Problem: Integer Overflow. For C.. Ram cant process over 21 bil. pos or neg. So 'long' (long int)
//Problem: Truncation. Floats are truncated (lost) by using int or long. Solution: Type casting. aka (float) x
//Problem: Floating point impercision. Aka, not enough decimals. Solution: %.20f, and double in place of float. (double bits to 64)

int main(void)
{
    // Prompt user for x
    long x = get_long("x: ");

    // Prompt user for y
    long y = get_long("y: ");

    // Perform addition
    double z = (double) x / (double) y
    printf("%.20f\n", z);
}
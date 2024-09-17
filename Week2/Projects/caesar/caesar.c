#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// main
int main(int argc, string argv[])
{
    // error check command line input. (One value, positive int)
    if (argc != 2)
    {
        printf("Usage: ./caesar key \n");
        return 1;
    }
    // loop through to make sure all are digits.. or return false
    int all_num = 1;
    for (int i = 0; i < strlen(argv[1]); i++)
    {
        if (!isdigit(argv[1][i]))
        {
            all_num = 0;
        }
    }

    // convert argv string to int
    int k = atoi(argv[1]);

    // check all conditions
    if (k < 0 || all_num == 0)
    {
        // print usage, return error code
        printf("Usage: ./caesar key \n");
        return 1;
    }

    // prompt for plain text
    string plain = get_string("plaintext:  ");

    // output cipher text
    printf("ciphertext:  ");

    // convert
    for (int j = 0; j < strlen(plain); j++)
    {
        if (isalpha(plain[j]))
        {
            if (isupper(plain[j]))
            {
                // for each cipher letter.. minus 65 to be == 0, + key to change value, % 26 to loop thru alphabet, + 65 to go back to correct letter. (A == 65)
                printf("%c", (plain[j] - 65 + k) % 26 + 65);
            }
            if (islower(plain[j]))
            {
                // same thing but 97 bc (a == 97)
                printf("%c", (plain[j] - 97 + k) % 26 + 97);
            }
        }
        else
        {
            printf("%c", plain[j]);
        }
    }
    printf("\n");
    // if all works.. return 0
    return 0;
}


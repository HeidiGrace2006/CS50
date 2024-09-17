#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

// "teaser" for functions
int calculate(string text);
int print_grade(int grade);

// Control center
int main(void)
{
    // Get passage of text from user
    string text = get_string("Text: ");

    int grade = calculate(text);
    print_grade(grade);
}

// Count each letter, word, and sentence
int calculate(string text)
{
    int letters = 0;
    int words = 1;
    int sentences = 0;
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (isalpha(text[i]))
        {
            letters++;
        }
        else if (text[i] == ' ')
        {
            words++;
        }
        else if (text[i] == '.' || text[i] == '?' || text[i] == '!')
        {
            sentences++;
        }
    }

    // Calculate grade level
    float L = ((float) letters / (float) words) * 100;
    float S = ((float) sentences / (float) words) * 100;
    int grade = round(0.0588 * L - 0.296 * S - 15.8);
    return grade;
}

// Print out grade level
int print_grade(int grade)
{
    if (grade > 16)
    {
        printf("Grade 16+\n");
    }
    else if (grade < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %d\n", grade);
    }
    return 0;
}

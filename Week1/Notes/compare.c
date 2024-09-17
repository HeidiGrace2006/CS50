#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int x = get_int("What's x? ");
    int y = get_int("What's y? ");

    if (x < y)
    {
        printf("x is less than y\n");
    }
    else if (x > y)
    {
        printf("x is greater than y\n");
    }
    else
    {
        printf("x is equal to y\n");
    }



    //loops
    int i = 3;
    while (i > 0)
    {
        printf("meow\n");
        i--;
    }

    for (int i = 0; i < 3; i++)
    {
        printf("meow\n");
}


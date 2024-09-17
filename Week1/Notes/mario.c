#include <studio.h>
#include <stdio.h>

int main(void)
{
    //For ?'s
    for (int i = 0; i < 4; i++)
    {
        printf("?");
    }
    printf("\n");

    //For #'s
    for (int i = 0; i < 3; i++)
    {
        printf("#\n");
    }

    //For grid
    //const makes it a constant variable
    const int n = 3;

    //However, if input..
    int n;
    do
    {
        n = get_int("Size: ");
    }
    while (n < 1);

    for (int i = 0; n < 3; i++)
    {
        for (int j = 0; n < 3; j++)
        {
            printf("#");
        }
        printf("\n");
    }

////Final design with functions:
//this is how you "initialize" functions as a "teaser" that they'll exist
int get_size(void);
void print_grid(int n);

int main(void)
{
    int n = get_size();
    print_grid(n);
}

int get_size(void)
{
    int n;
    do
    {
        n = get_int("Size: ");
    }
    while (n < 1);
    return n;
}

void print_grid(int n)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            printf("#");
        }
        printf("\n");
    }

}}

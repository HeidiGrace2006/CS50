#include <cs50.h>
#include <stdio.h>

//"initializing" functions
int get_size(void);
void print_pyramid(int height);

//"control center"
int main(void)
{
    int height = get_size();
    print_pyramid(height);
}

//Function to get
int get_size(void)
{
    int height;
    do
    {
        height = get_int("Size: ");
    }
    while (height < 1 || height > 8);
    return height;
}

//Function to print
void print_pyramid(int height)
{
    //Counter set to 0.. as long as counter is less than requested height, keep counting (aka doing whats in the loop)
    for (int row = 0; row < height; row++)
    {
        //another counter for spaces before hashes
        for (int spaces = 0; spaces < height - row - 1; spaces++)
        {
            printf(" ");
        }
        //Left Columns
        for (int LColumn = 0; LColumn <= row; LColumn++)
        {
            printf("#");
        }
        //print gap
        printf("  ");
        //Right columns
        for (int RColumn = 0; RColumn <= row; RColumn++)
        {
            printf("#");
        }
        printf("\n");
    }
}

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size
    long start;
    do
    {
        start = get_long("Starting population: ");
    }
    while (start < 9);
    // TODO: Prompt for end size
    long end;
    do
    {
        end = get_long("Ending population: ");
    }
    while (end < start);
    // TODO: Calculate number of years until we reach threshold
    int years = 0;
    int pop = start;
    while (pop < end)
    {
        pop = pop + (pop / 3) - (pop / 4);
        years++;
    }
    // TODO: Print number of years
    printf("Years: %i\n", years);
}

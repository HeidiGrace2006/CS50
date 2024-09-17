// Implements a dictionary's functionality
#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"


// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table.. (Upper letter * charc in word * 26)
const unsigned int N = 80000;

int word_count = 0;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    int index = hash(word);
    node *cursor = table[index];
    while (cursor != NULL)
    {
        if (strcasecmp(cursor->word, word) == 0)
        {
            return true;
        }
        else
        {
            cursor = cursor->next;
        }
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    int sum = 0;
    for (int i = 0; word[i] != '\0'; i++)
    {
        sum = sum + toupper(word[i]);
    }
    unsigned int index = (toupper(word[0]) - 'A') + sum;
    return index;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // Open dictionary
    FILE *source = fopen(dictionary, "r");
    if (source == NULL)
    {
        printf("Error: Could not open card.\n");
        return false;
    }

    char word[LENGTH + 1];
    // Read through one word at a time
    while (fscanf(source, "%s", word) != EOF)
    {
        // Create a node
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            printf("Error: Could not allocate memory for node.\n");
            fclose(source);
            return false;
        }
        // Write to the node
        strcpy(n->word, word);
        n->next = NULL;
        // Hash (or, "sort") the node
        int index = hash(word);

        // Insert node into table
        n->next = table[index];
        table[index] = n;
        word_count++;
    }
    // Close dictionary
    fclose(source);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return word_count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (int i = 0; i < N; i++)
    {
        node *cursor = table[i];
        while (cursor != NULL)
        {
            node *temp = cursor;
            cursor = cursor->next;
            free(temp);
        }
    }
    return true;
}

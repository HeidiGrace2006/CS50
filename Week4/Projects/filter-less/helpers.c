#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    // Loop through pixels.. average values.. update.
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int average = round((image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3.0);
            image[i][j].rgbtRed = average;
            image[i][j].rgbtGreen = average;
            image[i][j].rgbtBlue = average;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    // loop
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // calculate
            int new_red = round(.393 * image[i][j].rgbtRed + .769 * image[i][j].rgbtGreen + .189 * image[i][j].rgbtBlue);
            if (new_red > 255)
            {
                new_red = 255;
            }
            int new_green = round(.349 * image[i][j].rgbtRed + .686 * image[i][j].rgbtGreen + .168 * image[i][j].rgbtBlue);
            if (new_green > 255)
            {
                new_green = 255;
            }
            int new_blue = round(.272 * image[i][j].rgbtRed + .534 * image[i][j].rgbtGreen + .131 * image[i][j].rgbtBlue);
            if (new_blue > 255)
            {
                new_blue = 255;
            }

            // update
            image[i][j].rgbtRed = new_red;
            image[i][j].rgbtGreen = new_green;
            image[i][j].rgbtBlue = new_blue;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    // Loop over all pixels
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
        // Swap pixels
            // temp is set equal to the left_pixel
            RGBTRIPLE temp = image[i][j];
            // the left_pixel is set equal to the right_pixel
            image[i][j] = image[i][width - (j + 1)];
            // the right pixel is set equal to temp
            image[i][width - (j + 1)] = temp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // Create a copy of image
    RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }

    // focus on one pixel
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // initialize totals
            int totR = 0, totG = 0, totB = 0;
            // count how many pixels to divide by
            int pixel_count = 0;

            // loop to find pixels to average
            for (int x = -1; x < 2; x++)
            {
                for (int y = -1; y < 2; y++)
                {
                    // set current x and y
                    int currX = i + x;
                    int currY = j + y;

                    // check for corner cases
                    if (currX < 0 || currX > (height - 1) || currY < 0 || currY > (width - 1))
                    {
                        // aka.. if the current cordinate is an outside pixel, stop collecting values and move on to calculating
                        continue;
                    }

                    // count values for each color
                    totR += copy[currX][currY].rgbtRed;
                    totG += copy[currX][currY].rgbtGreen;
                    totB += copy[currX][currY].rgbtBlue;

                    pixel_count++;
                }
            }
            // Averages
            image[i][j].rgbtRed = round((float) totR / pixel_count);
            image[i][j].rgbtGreen = round((float) totG / pixel_count);
            image[i][j].rgbtBlue = round((float) totB / pixel_count);
        }
    }

    return;
}

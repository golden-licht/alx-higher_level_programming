#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * is_palindrome - Checks if a singly listed list is a palindrome
 * @head: Pointer to pointer of a list node
 * Return: 1, if the list is palindrome, 0 otherwise
*/

int is_palindrome(listint_t **head)
{
	listint_t *temp = *head, *temp2 = *head;
	int len = 0, i = 0;
	int *arr;

	if (*head == NULL)
		return (1);

	while (temp)
	{
		temp = temp->next;
		len++;
	}

	arr = malloc(sizeof(int) * len);
	if (arr == NULL)
	{
		printf("Allocation failed");
		return (0);
	}

	while (temp2)
	{
		arr[i] = temp2->n;
		temp2 = temp2->next;
		i++;
	}

	for (i = 0; i < len / 2; i++)
	{
		if (arr[i] != arr[len - 1 - i])
		{
			free(arr);
			return (0);
		}
	}

	free(arr);
	return (1);
}

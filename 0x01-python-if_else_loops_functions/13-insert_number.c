#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - Insterts a node into a sorted list
 * @head: Pointer to pointer of head of a sorted list
 * @number: The number to be inserted into the list
 *
 * Return: The address of the new node, or NULL on failure
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;
	listint_t *past = NULL;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	else
	{
		while (current != NULL && current->n <= number)
		{
			past = current;
			current = current->next;
		}
		if (past != NULL)
			past->next = new;

		new->next = current;
		/* if new is the first element now, make it head */
		if (current == *head)
			*head = new;
	}

	return (new);
}

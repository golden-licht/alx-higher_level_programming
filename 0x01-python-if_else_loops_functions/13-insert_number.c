#include "lists.h"
#include <stdlib.h>

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;
	listint_t *temp = NULL;

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
			current = current->next;
		if (current->next != NULL)
			temp = current->next;
		
		current->next = new;
		new->next = temp;
	}

	return (new);
}

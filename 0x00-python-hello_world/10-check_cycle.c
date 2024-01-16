#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *current;

	current = list;

	while (current != NULL)
	{
		current = current->next;
		if (current == list)
			return (1);
	}
	return 0;
}

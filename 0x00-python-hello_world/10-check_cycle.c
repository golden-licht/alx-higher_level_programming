#include "lists.h"

/*
 * check_cycle - Checks if a linked list has a cycle in it
 * listint_t: The list to check the cycle for
 *
 * Return: 0, if there is no cycle, 1 otherwise.
 */

int check_cycle(listint_t *list)
{
	listint_t *tortoise = list, *hare = list;

	if (list == NULL)
		return (0);

	while (hare->next != NULL && (hare->next)->next != NULL)
	{
		tortoise = tortoise->next;
		hare = (hare->next)->next;

		if (tortoise == hare)
			return (1);
	}
	return (0);
}

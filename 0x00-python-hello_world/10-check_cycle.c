#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the head of the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *tmp, *end;

	if (list == NULL)
		return (0);

	for (tmp = list ,end = list->next; end;)
	{
		if (end == tmp)
			return (1);
		end = end->next;
		if (!end)
			return (0);
		end = end->next;
		if (!end)
			return (0);
		tmp = tmp->next;
	}
	return (0);
}

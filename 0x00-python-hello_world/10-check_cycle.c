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

	for (end = list->next; end != NULL; end = end->next)
	{
		if (end == end->next)
			return (1);
		for (tmp = list; tmp != end; tmp = tmp->next)
			if (tmp == end->next)
				return (1);
	}
	return (0);
}

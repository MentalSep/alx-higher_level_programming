#include "lists.h"

/**
 * Findmiddle - finds the middle node of a listint_t linked list
 * @head: pointer to head of list
 * Return: pointer to middle node
 */
listint_t *Findmiddle(listint_t *head)
{
	listint_t *slow = head, *fast = head;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	return (slow);
}

/**
 * reverse_listint - revreses a listint_t linke list
 *
 * @head: pointer to head of list
 *
 * Return: pointer to the first node of the reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *tmp, *next;

	if (!head || !(*head))
		return (NULL);

	tmp = NULL;
	while (*head)
	{
		next = (*head)->next;
		(*head)->next = tmp;
		tmp = *head;
		*head = next;
	}
	*head = tmp;

	return (*head);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to head of list
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *middle = Findmiddle(*head);
	listint_t *tmp = *head;

	if (!head || !*head || !(*head)->next)
		return (1);
	reverse_listint(&middle);
	while (middle)
	{
		if (tmp->n != middle->n)
			return (0);
		tmp = tmp->next;
		middle = middle->next;
	}
	return (1);
}

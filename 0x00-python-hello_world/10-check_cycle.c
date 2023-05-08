#include "lists.h"

/**
 * check_cycle - checks whether a singly linkedlist has a cycle
 * @list: pointer to linkedlist head
 * Return: 1 if true, 0 if false
 */
int check_cycle(listint_t *list)
{
	listint_t *slow;
	listint_t *fast;

	if (list == NULL || list->next == NULL)
		return (0);

	slow = list->next;
	fast = list->next->next;
	while (fast != NULL && fast->next != NULL)
	{
		if (slow == fast)
			return (1);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}

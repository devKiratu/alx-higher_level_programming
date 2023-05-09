#include "lists.h"

/**
 * insert_node - inserts a new @number in a sorted linkedlist @head
 * @head: pointer to linkedlist head
 * @number: number to insert
 * Return: address of new node or NULL if operation fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prev;
	listint_t *curr;
	listint_t *new;

	if (head == NULL)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (*head == NULL)
	{
		*head = new;
		return (*head);
	}
	if (number < (*head)->n)
	{
		new->next = *head;
		*head = new;
		return (*head);
	}
	prev = *head;
	curr = (*head)->next;
	while (curr != NULL)
	{
		if (number < curr->n)
		{
			new->next = curr;
			prev->next = new;
			return (new);
		}
		prev = curr;
		curr = curr->next;
	}
	free(new);
	return (NULL);
}

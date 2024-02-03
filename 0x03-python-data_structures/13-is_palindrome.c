#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * add_nodeint - add node to list
 * @head: list to add node in
 * @n: value to add
 *
 * return: returns the list
 */
listint_t *add_nodeint(listint_t **head, int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = n;
	new->next = *head;
	*head = new;

	return (*head);
}

/**
 * is_palindrome - checks if a linked list is a palindrom
 * @head: the list to check
 *
 * Return: returns 1 if it's a palindrome and 0 if not
 */

int is_palindrome(listint_t **head)
{
	listint_t *current, *new, *current_new;

	if (*head == NULL)
		return (1);

	current = *head;
	new = NULL;

	while (current != NULL)
	{
		add_nodeint(&new, current->n);
		current = current->next;
	}

	current = *head;
	current_new = new;
	while (current != NULL)
	{
		if (current->n != current_new->n)
		{
			free_listint(new);
			return (0);
		}
		current = current->next;
		current_new = current_new->next;
	}

	free_listint(new);
	return (1);
}

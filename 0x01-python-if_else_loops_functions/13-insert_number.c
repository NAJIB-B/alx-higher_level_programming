#include "lists.h"
#include <stdio.h>
#include <stdlib.h>




/**
 * insert_node - insert's a node in a sorted linked list
 * @head: the linked list
 * @number: the number to insert in the node
 *
 * Return: returns the address of the new_list node or NULL if any error occur
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prev, *current, *new_list, *temp;

	prev = NULL;
	current = *head;	

	new_list = malloc(sizeof(listint_t));
	if (new_list == NULL)
		return NULL;
	new_list->n = number;
	new_list->next = NULL;
	if (*head == NULL)
		*head = new_list;

	while (current != NULL)
	{
		if (new_list->n <= current->n)
		{
			if (prev == NULL)
			{
				temp = *head;
				new_list->next = temp;
				*head = new_list;
			}
			else
			{
				prev->next = new_list;
				new_list->next = current;
			}

			return (new_list);
		}
		prev = current;
		current = current->next;
	}
	prev->next = new_list;
	return (new_list);	
}

#include "lists.h"
#include <stdio.h>
#include <stdlib.h>


/**
 * add_node_front - adds node in front of another node
 * @real_head: head of the whole list
 * @prev: previous head
 * @current: current head 
 * @new_list: node to add
 *
 * Return: returns the address of the new_list node
 */
listint_t *add_node_front(listint_t *real_head, listint_t *prev, listint_t *current, listint_t *new_list)
{
	listint_t *temp;

	if (prev == NULL)
	{
		printf("yap it came here");
		temp = real_head;
		real_head = new_list;
		new_list->next = temp;	
	}
	else
	{
		prev->next = new_list;
		new_list->next = current;
	}
	return (new_list);
}


/**
 * insert_node - insert's a node in a sorted linked list
 * @head: the linked list
 * @number: the number to insert in the node
 *
 * Return: returns the address of the new_list node or NULL if any error occur
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prev, *current, *new_list, *real_head, *result;

	prev = NULL;
	real_head = *head;
	current = *head;	

	new_list = malloc(sizeof(listint_t));
	if (new_list == NULL)
		return NULL;
	new_list->n = number;
	new_list->next = NULL;

	while (current != NULL)
	{
		if (new_list->n <= current->n)
		{
			result = add_node_front(real_head, prev, current, new_list);
			return (result);
		}
		prev = current;
		current = current->next;
	}
	prev->next = new_list;
	return (new_list);	
}

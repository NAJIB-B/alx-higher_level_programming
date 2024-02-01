#include "lists.h"
#include <stdlib.h>
#include <stdio.h>


/**
 * check_cycle - checks for cycle in a linked list
 * @list: list to check
 *
 * Return: 0 if there is no cycle and 1 if there is
 */

int check_cycle(listint_t *list)
{
	listint_t *current_head, *temp, *count;	
	count = list;
	
	current_head = list;

	while(count != NULL)
	{
		if (current_head == NULL)
			break;
		temp = current_head->next;
		while(temp != NULL)
		{
			if (temp->next == current_head)
			{
				return (1);
			}
			temp = temp->next;

		}
		current_head = current_head->next;
		count = count->next;
	}

	return (0);
}

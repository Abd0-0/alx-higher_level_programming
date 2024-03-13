#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 *
 * @head: pointer to pointer of first node of listint_t list.
 * @number: integer to be included in new node
 *
 * Return: the address of the new node, or NULL if it failed.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr, *new;

	new = malloc(sizeof(listint_t));
	if (new)
	{
		new->n = number;
		new->next = NULL;
	}
	else
		return (NULL);

	if (!head || !*head)
	{
		new->n = number;
		return (new);
	}

	ptr = *head;

	while (ptr && ptr->next)
	{
		if (ptr->n < number && ptr->next->n > number)
		{
			new->next = ptr->next;
			ptr->next = new;
			break;
		}
		ptr = ptr->next;
	}

	if (ptr && !ptr->next)
		ptr->next = new;
	return (new);
}	

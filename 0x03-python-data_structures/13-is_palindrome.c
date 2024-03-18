#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to head of list
 * Return: 0 if  it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	int i, n;
	listint_t *ptr;
	int arr[256];

	if (!head || !*head)
		return (1);
	ptr = *head;
	n = 0;

	while (ptr)
	{
		arr[n] = ptr->n;
		ptr = ptr->next;
		n++;
	}

	if (n == 1)
		return (1);

	i = 0;

	while (i < (n / 2))
	{
		if (arr[i] != arr[n - (i + 1)])
			return (0);
		i++;
	}

	return (1);
}

#include "lists.h"
#include <stdint.h>


/**
 * int check_cycle(listint_t *list) - finds a loop in listint_t linked list.
 *
 * @list: a pointer to the head.
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	int i, count = 0;
	listint_t *ptr, *check;

	if (list == NULL)
		return (0);

	ptr = list;

	while (ptr)
	{
		i = 0;
		check = list;

		while (i < count)
		{
			if (check == ptr)
			{
				return (1);
			}
			check = check->next;
			i++;
		}
		ptr = ptr->next;
		count++;
	}

	return (0);
}

#include "lists.h"

/**
 * print_dlistint - prints all the elements of a dlistint_t list
 * @h: pointer to the head node of the list
 *
 * Return: number of nodes in the list
 */

size_t print_dlistint(const dlistint_t *h)
{
	size_t counts = 0;

	while (h)
	{
		counts++;
		printf("%d\n", h->n);
		h = h->next;
	}

	return (counts);
}

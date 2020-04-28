#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts node
 * @head: double pointer to head
 * @number: value of new node
 * Return: pointer to new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current, *aux;

	if (head == NULL)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	(*new).n = number;
	(*new).next = NULL;
	aux = NULL;
	current = *head;

	while (current && (*current).n < number)
	{
		aux = current;
		current = (*current).next;
	}
	(*new).next = current;
	if (aux)
		(*aux).next = new;
	else
		*head = new;
	return (new);
}

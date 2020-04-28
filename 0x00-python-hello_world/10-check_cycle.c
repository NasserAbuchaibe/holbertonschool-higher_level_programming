#include "lists.h"
/**
*check_cycle - print circle
*@list: argument listint_t
*Return: int
*/
int check_cycle(listint_t *list)
{
	listint_t *tmp, *aux;

	tmp = list, aux = list;
	while (aux != NULL && tmp != NULL && tmp ->next != NULL)
	{
		tmp = tmp->next->next;
		aux = aux->next;
		if (tmp == aux)
		{
			return (1);
		}
	}
	return (0);
}

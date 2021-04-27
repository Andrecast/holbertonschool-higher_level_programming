#include "lists.h"
/**
 * check_cycle - Function hat checks if a singly linked list has a cycle in it
 * @list: linked list head
 * Return: 0 for no cycle, 1 for cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *one = NULL, *two = NULL;

	one = list;
	two = list;
	while (one && two && two->next)
	{
		one = one->next; /*avanza un nodo a la vez*/
		two = two->next->next; /*avanza dos nodos a la vez*/
		if(one == two)/*si los dos punteros apuntan al mismo nodo,*/
		{/* es porque es un ciclo*/
			return (1);
		}
	}
	return (0);
}

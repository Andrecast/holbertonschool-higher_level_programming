#include "lists.h"
/**
 * insert_node - Function that inserts a number in a list
 * @head: head of the linked list
 * @number: number to be insert
 * Return: new node address or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *temporal = NULL, *nuevo = NULL;
    temporal = *head;
    nuevo = malloc(sizeof(listint_t));
    if (nuevo == NULL)
        return (NULL);
    nuevo->n = number;
    if (number < 0)
    {
        nuevo->next = *head;
        *head = nuevo;
        return (nuevo);
    }
    if (!*head)
    {
        *head = nuevo;
        nuevo->next = NULL;
        return (nuevo);
    }
    while (temporal)
    {
        if (temporal->next == NULL)
        {
            nuevo->next = NULL;
            temporal->next = nuevo;
            return (nuevo);
        }
        if (temporal->n < number && number <= temporal->next->n)
        {
            nuevo->next = temporal->next;
            temporal->next = nuevo;
            return (nuevo);
        }
        temporal = temporal->next;
    }
    return (NULL);
}

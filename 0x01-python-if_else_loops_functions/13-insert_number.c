#include "lists.h"
/**
 * insert_node - Inserts a new node
 * @head: Head of the reference list
 * @number: Node value
 * Return: Pointer to the new head
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *now = NULL, *t = NULL;
	listint_t *newNode = malloc(sizeof(listint_t));

	if (!newNode)
	{
		return (NULL);
	}
	newNode->n = number;
	if (*head)
	{
		now = *head;
		if (number <= now->next->n)
		{
			newNode->next = now;
			*head = newNode;
		}
		else
		{
			while (now->next)
			{
				if (number <= now->next->n)
				{
					t = now->next;
					now->next = newNode;
					newNode->next = t;
					return (*head);
				}
				now = now->next;
			}
			t = now->next;
			now->next = newNode;
			newNode->next = t;
		}
		return (*head);
	}
	newNode->next = NULL;
	*head = newNode;
	return (*head);
}

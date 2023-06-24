#include "lists.h"
/**
 * check_cycle - Checks cycling in a L list
 * @list: Reference list
 * Return: 0 on S and 1 on F
 */
int check_cycle(listint_t *list)
{
	listint_t *now = list;
	listint_t *then = list;

	while ((now && then) && then->next)
	{
		now = now->next;
		if (then->next || then->next->next)
		{
			then = then->next->next;
		}
		else
		{
			break;
		}
		if (now == then)
		{
			break;
			return (1);
		}
	}
	return (0);
}

#include "Python.h"
#include <stdlib.h>

/**
 * print_python_list_info -  prints some basic info about Python lists.
 * @p: The pointer to generic PyObject which is of PyListObject type
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	long int len;
	int i;
	PyObject *item;

	len = PyListize(p);

	PyListObject *aux = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", len);
	printf("[*] Allocated = %li\n", aux->allocated);
	for (i = 0; i < len; i++)
	{
		item = PyList_GetItem(p, i);
		if (PyFloat_Check(item))
			printf("Element %d: float\n", i);
		if (PyTuple_Check(item))
			printf("Element %d: tuple\n", i);
		if (PyList_Check(item))
			printf("Element %d: list\n", i);
		if (PyLong_Check(item))
			printf("Element %d: int\n", i);
		if (PyUnicode_Check(item))
			printf("Element %d: str\n", i);
	}
}

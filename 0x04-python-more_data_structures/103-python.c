#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - prints some basic info about Python lists
 * @p: PyObject
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
	int i, size;
	char *str;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = PyBytes_Size(p);
	str = PyBytes_AsString(p);
	printf("  size: %d\n", size);
	printf("  trying string: %s\n", str);
	if (size < 10)
		printf("  first %d bytes:", size + 1);
	else
		printf("  first 10 bytes:");
	for (i = 0; i <= size && i < 10; i++)
		printf(" %02hhx", str[i]);
	printf("\n");
}

/**
 * print_python_list - prints some basic info about Python lists
 * @p: PyObject
 * Return: void
 */
void print_python_list(PyObject *p)
{
	int i, size, alloc;
	const char *type;

	size = PyList_Size(p);
	alloc = ((PyListObject *)p)->allocated;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);
	for (i = 0; i < size; i++)
	{
		type = ((PyListObject *)p)->ob_item[i]->ob_type->tp_name;
		printf("Element %d: %s\n", i, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(((PyListObject *)p)->ob_item[i]);
	}
}

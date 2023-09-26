#include <Python.h>
#include <stdio.h>


/**
 * print_python_float - prints some basic info about Python float objects
 * @p: pointer to PyObject
 */
void print_python_float(PyObject *p)
{
	char *buffer;
	PyFloatObject *float_obj = (PyFloatObject *)p;

	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	buffer = PyOS_double_to_string(float_obj->ob_fval, 'r',
			0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", buffer);
}

/**
 * print_python_bytes - prints some basic info about Python bytes objects
 * @p: pointer to PyObject
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes_obj = (PyBytesObject *) p;
	int len, i;
	char *tmp;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes"))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	len = PyBytes_Size(p);
	tmp = bytes_obj->ob_sval;
	printf("  size: %d\n", len);
	printf("  trying string: %s\n", bytes_obj->ob_sval);
	len++;
	if (len > 10)
		len = 10;
	printf("  first %d bytes:", len);
	for (i = 0; i < len; i++)
		printf(" %02hhx", tmp[i]);
	printf("\n");
}

/**
 * print_python_list - prints information about a python list
 * and extra info on bytes objects
 *
 * @p: list to print information about
 *
 * Return: void
 */
void print_python_list(PyObject *p)
{
	int i, size;
	const char *type;
	PyListObject *lst = (PyListObject *) p;

	size = ((PyVarObject *) lst)->ob_size;

	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list"))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %ld\n", lst->allocated);
	for (i = 0; i < size; i++)
	{
		type = lst->ob_item[i]->ob_type->tp_name;
		printf("Element %d: %s\n", i, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(lst->ob_item[i]);
		if (strcmp(type, "float") == 0)
			print_python_float(lst->ob_item[i]);
	}
}

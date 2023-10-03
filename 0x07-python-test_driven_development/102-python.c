#include <Python.h>
#include <stdio.h>

/**
 * print_python_string - prints info about python strings
 * @p: PyObject
 * Return: void
 */
void print_python_string(PyObject *p)
{
	Py_ssize_t len;
	Py_UNICODE *buffer = NULL;

	printf("[.] string object info\n");
	if (p != NULL && (strcmp((p->ob_type)->tp_name, "str") == 0)
		&& (p->ob_type != NULL) && ((p->ob_type)->tp_name != NULL))
	{
		printf("  type: %s%s\n",
			   ((PyASCIIObject *)p)->state.compact ? "compact " : "",
			   ((PyASCIIObject *)p)->state.ascii ? "ascii" : "unicode object");
		buffer = PyUnicode_AsWideCharString(p, &len);
		printf("  length: %d\n", (int)len);
		printf("  value: %ls\n", buffer);
		PyMem_Free(buffer);
	}
	else
		printf("  [ERROR] Invalid String Object\n");
}

#include <Python.h>
#include <textify.h>

static PyObject * toText(PyObject *self, PyObject *args) {
    const char *input;

    if(!PyArg_ParseTuple(args, "s", &input))
        return NULL;

    return Py_BuildValue("s", textify(input));
}


static PyMethodDef TextifyMethods[] = {
    {"toText",  toText, METH_VARARGS,
     "Runs OCR on input image"},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

PyMODINIT_FUNC
inittextify(void)
{
    (void) Py_InitModule("textify", TextifyMethods);
}


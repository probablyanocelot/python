#include <stdio.h>

struct SomeStructure {int i; char c; char *s;};

double SomeFunction(struct SomeStructure *s)
{
    print("int is %d, char is %c, string is %s/n", s->i, s->c, s->s);
    s->s = "goodbye";
    return 42;
}

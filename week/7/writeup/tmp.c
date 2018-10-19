#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv) {
    char buf[1024];
    FILE *f;
    f = fopen("/tmp/.stego", "rb");

    if (f == NULL) {
        printf("Noah broke stuff\n");
        return 1;
    }

    while (fgets(buf, 1024, f) != NULL) {
        for (int i = 0; i < 1024; i++) {
            printf("%x ", buf[i]);
        }
    }

    fclose(f);
}

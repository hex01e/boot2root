#include <stdio.h>

char getme1()  { return 'I'; }
char getme2()  { return 'h'; }
char getme3()  { return 'e'; }
char getme4()  { return 'a'; }
char getme5()  { return 'r'; }
char getme6()  { return 't'; }
char getme7()  { return 'p'; }
char getme8()  { return 'w'; }
char getme9()  { return 'n'; }
char getme10() { return 'a'; }
char getme11() { return 'g'; }
char getme12() { return 'e'; }

int main() {
	printf("MY PASSWORD IS: ");
	printf("%c", getme1());
	printf("%c", getme2());
	printf("%c", getme3());
	printf("%c", getme4());
	printf("%c", getme5());
	printf("%c", getme6());
	printf("%c", getme7());
	printf("%c", getme8());
	printf("%c", getme9());
	printf("%c", getme10());
	printf("%c", getme11());
	printf("%c", getme12());
	printf("\n");
	printf("Now SHA-256 it and submit\n");
}
#include<graphics.h>

int main() {
int gd = DETECT, gm;
initgraph(&gd, &gm, NULL);

line(50, 40, 250, 40); //CD
line(70, 40, 100, 20); // EA
line(100, 20, 200, 20); // AB
line(200, 20, 230, 40); // BF
line(50, 60, 250, 60); // GH
line(50, 40, 50, 60); //CG
line(250, 40, 250, 60); // DH
circle(75, 60, 5);
circle(75, 60, 7);
circle(225, 60, 5);
circle(225, 60, 7);

delay(50000);
closegraph();
}

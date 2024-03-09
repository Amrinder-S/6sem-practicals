#include<graphics.h>

int main() {
	int gd = DETECT, gm;
	initgraph(&gd, &gm, NULL);
	circle(50,50,30);
  bar3d(200,200, 300, 300, 50, 1);
  delay(50000);
	closegraph();
	return 0;
}

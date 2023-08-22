void setup() {
  size(400, 400);
}

void draw() {
  background(128);
  float a = 0.0;
  float inc = TWO_PI/25.0;

  for (int i = 0; i < 400; i=i+16) {
    line(i, 200, i, 200+sin(a+(float)frameCount/60)*160.0);
    a = a + inc;
  }
}

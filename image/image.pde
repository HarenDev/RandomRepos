PImage image;

void Setup(){
  size(400, 400, P3D);
  image = loadImage("funny.jpg");
}

void Draw(){
  image(image, 0, 0);
 
}

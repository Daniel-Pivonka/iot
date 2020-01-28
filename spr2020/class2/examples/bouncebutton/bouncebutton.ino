#define BUTTON 4
bool buttonstate;
bool clickedflag = false;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(BUTTON, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  buttonstate = digitalRead(BUTTON);

  if (buttonstate and not clickedflag){
      clickedflag = true;
  }
  if (not buttonstate and clickedflag){
    clickedflag = false;
    Serial.println("clicked");
  }
  
}

#define BUTTON 4
bool buttonstate;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(BUTTON, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:

  buttonstate = digitalRead(BUTTON);
  Serial.println(buttonstate);
}

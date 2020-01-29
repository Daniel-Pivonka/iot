// vars
#define BUTTON 4
bool buttonstate;

void setup() {
  // put your setup code here, to run once:

  // setup serial connunication speed
  Serial.begin(115200);

  // setup pin as input
  pinMode(BUTTON, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:

  buttonstate = digitalRead(BUTTON);
  Serial.println(buttonstate);
}

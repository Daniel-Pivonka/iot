// vars
#define LED 5

void setup() {
  // put your setup code here, to run once:

  // setup pin as output
  pinMode(LED, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:

  // wait a second
  delay(1000);

  // turn the pin on 
  digitalWrite(LED, HIGH);
}

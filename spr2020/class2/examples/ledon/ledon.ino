#define LED 5

void setup() {
  // put your setup code here, to run once:
  pinMode(LED, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  delay(1000);
  digitalWrite(LED, HIGH);
}

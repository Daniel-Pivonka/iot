// vars
int lightstate;

void setup() {
  // put your setup code here, to run once:

  // setup serial connunication speed
  Serial.begin(115200);

}

void loop() {
  // put your main code here, to run repeatedly:

  //read analog sensor
  lightstate = analogRead(A0);

  //print value
  Serial.println(lightstate);
}

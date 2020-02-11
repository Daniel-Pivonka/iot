// vars
int lightstate;

void setup() {
  // put your setup code here, to run once:

  // setup serial connunication speed
  Serial.begin(115200);

}

void loop() {
  // put your main code here, to run repeatedly:

  //vars to keep track of time
  static const unsigned long REFRESH_INTERVAL = 1000; // ms
  static unsigned long lastRefreshTime = 0;


  //if time between now and last update is more than time interval
  if(millis() - lastRefreshTime >= REFRESH_INTERVAL)
  {
    lastRefreshTime += REFRESH_INTERVAL;
    lightstate = analogRead(A0);
    Serial.println(lightstate);
  }

  Serial.println("tick");
}

#define SIGNAL_PIN A0

int value = 0;

void setup() {
  Serial.begin(9600);
  pinMode(SIGNAL_PIN, INPUT); 
}

void loop() {
  value = analogRead(SIGNAL_PIN); 
  Serial.println(value);
  delay(1000);
}
#define SIGNAL_PIN A0

int value = 0;
bool flagDefinedPort = false;
bool definePort();

void setup() {
  Serial.begin(9600);
  pinMode(SIGNAL_PIN, INPUT); 
}

void loop() {
  if (flagDefinedPort == false){
    flagDefinedPort = definePort();
  }
  
  else if (flagDefinedPort == true){
    value = analogRead(SIGNAL_PIN); 
    Serial.println(value);
    delay(1000);
  } 

  if (Serial.available() <= 0){
    flagDefinedPort = false;
  }
}

bool definePort(){
  String dataStr = Serial.readStringUntil('\n');
  int code = dataStr.toInt();
  if (code == 100){
    Serial.println(1);
    return true;
  }
  return false;
}
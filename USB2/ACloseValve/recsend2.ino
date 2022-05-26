int recievedCode;
int resultStatus;

void setup() {
 Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0){
    String dataStr = Serial.readStringUntil('\n');
    int data = dataStr.toInt();
    if (data == 1){
      data = data + 2;
      Serial.println(data);
      digitalWrite(A0, HIGH);   // включает светодиод
      delay(15000);
    }
    if (data == 2){
      data = data + 3;
      Serial.println(data);
      digitalWrite(A0, LOW);   // включает светодиод
      delay(15000);
    }
  }
}

int recievedCode;
int resultStatus;

void setup() {
 Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0){
    String dataStr = Serial.readStringUntil('\n');
    int data = dataStr.toInt();
    if (data == 1){ // закрытие крана
      data = data + 2;
      Serial.println(data);
      digitalWrite(A0, HIGH);
      delay(15000);
    }
    if (data == 2){ // открытие крана
      data = data + 3;
      Serial.println(data);
      digitalWrite(A0, LOW);
      delay(15000);
    }
  }
}

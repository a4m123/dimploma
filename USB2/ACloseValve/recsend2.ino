int recievedCode;
int resultStatus;
int data;
int flagPortDefined;

void setup() {
 Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0){
    if (flagPortDefined == 0){
      String dataStr = Serial.readStringUntil('\n');
      int code = dataStr.toInt();
      if (code == 300){
        Serial.println(1);
        flagPortDefined = 1;
      }
    }
    else if (flagPortDefined == 1){
      String dataStr = Serial.readStringUntil('\n');
      ::data = dataStr.toInt();
      if (data == 1){ // закрытие крана
        data = data + 2;
        Serial.println(data);
        digitalWrite(A0, HIGH);
      }
      if (data == 2){ // открытие крана
        data = data + 3;
        Serial.println(data);
        digitalWrite(A0, LOW);
      }
    }
  }

  else if (Serial.available() == 0){
    flagPortDefined = 0;
      if (data == 1){ // закрытие крана
      digitalWrite(A0, HIGH);
      delay(15000);
    }
    if (data == 2){ // открытие крана
      digitalWrite(A0, LOW);
      delay(15000);
    }
  }
}

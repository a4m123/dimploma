int recievedCode;
int resultStatus;
int data;
bool flagPortDefined = false;
bool definePort();

void setup() {
 Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0){
    if (flagPortDefined == false){
      String dataStr = Serial.readStringUntil('\n');
      int code = dataStr.toInt();
      if (code == 300){
        Serial.println(1);
        flagPortDefined = true;
      }
    }
    else if (flagPortDefined == true){
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

  else if (Serial.available() <= 0){
    flagPortDefined = false;
      if (data == 1){ // закрытие крана
      digitalWrite(A0, HIGH);
    }
    if (data == 2){ // открытие крана
      digitalWrite(A0, LOW);
    }
  }
}

bool definePort(){
  String dataStr = Serial.readStringUntil('\n');
  int code = dataStr.toInt();
  if (code == 300){
    Serial.println(1);
    return true;
  }
  return false;
}

#include "nRF24L01.h" 
#include "RF24.h"
#include "SPI.h"


int recievedCode = 0;
int resultStatus = 0;
int data = 0;
bool flagPortDefined = true; // ИСПРАВИТЬ НА FALSE
bool definePort();
const uint64_t pipe = 0xF0F1F2F3F4LL;
RF24 radioTransmit(9,53);

void setup() {
  Serial.begin(9600);
  radioTransmit.begin();      
  radioTransmit.setChannel(84); 
  radioTransmit.setDataRate(RF24_1MBPS);
  radioTransmit.setPALevel(RF24_PA_HIGH);
  radioTransmit.openWritingPipe(pipe);      
  radioTransmit.stopListening();
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
        radioTransmit.write(&data, sizeof(data));
        data = data + 2;
        Serial.println(data);
        digitalWrite(A0, HIGH);
      }
      if (data == 2){ // открытие крана
        radioTransmit.write(&data, sizeof(data)); // отправляем данные и указываем байты
        data = data + 3;
        Serial.println(data);
        digitalWrite(A0, LOW);
      }
    }
  }

  else if (Serial.available() <= 0){
    flagPortDefined = true; // ИСПРАВИТЬ НА FALSE
      if (data == 1){ // закрытие крана
      radioTransmit.write(&data, sizeof(data)); // отправляем данные и указываем байты
      digitalWrite(A0, HIGH);
    }
    if (data == 2){ // открытие крана
      radioTransmit.write(&data, sizeof(data)); // отправляем данные и указываем байты
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
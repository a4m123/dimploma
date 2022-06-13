#include "nRF24L01.h" 
#include "SPI.h"      
#include "RF24.h"     

const uint64_t pipe = 0xF0F1F2F3F4LL;
RF24 radioRecieve(9,53); 
int data = 0;

void setup() {
  Serial.begin(9600);
  radioRecieve.begin();
  radioRecieve.setChannel(0); 
  radioRecieve.setDataRate(RF24_1MBPS);
  radioRecieve.setPALevel(RF24_PA_HIGH);
  radioRecieve.openReadingPipe(1, pipe);    
  radioRecieve.startListening();           
}

void loop() {
  if (radioRecieve.available()){
    radioRecieve.read(&data, sizeof(data));    
  }
  if (data == 1){
    Serial.println("recieved from radioRecieve to close Valve");
    digitalWrite(A0, HIGH);
    }
  if (data == 2){
    Serial.println("recieved from radioRecieve to open Valve");
    digitalWrite(A0, LOW);
    }
}
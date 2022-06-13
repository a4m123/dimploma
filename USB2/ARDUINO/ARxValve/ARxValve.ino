#include "nRF24L01.h" 
#include "SPI.h"      
#include "RF24.h"     

const uint64_t pipe = 0xF0F1F2F3F4LL;
RF24 radio(9,53); 
int data = 0;

void setup() {
  Serial.begin(9600);
  radio.begin();
  radio.setChannel(0); 
  radio.setDataRate(RF24_1MBPS);
  radio.setPALevel(RF24_PA_HIGH);
  radio.openReadingPipe(1, pipe);    
  radio.startListening();           
}

void loop() {
  if (radio.available()){
    radio.read(&data, sizeof(data));    
  }
  if (data == 1){
    Serial.println("recieved from radio to close Valve");
    digitalWrite(A0, HIGH);
    }
  if (data == 2){
    Serial.println("recieved from radio to open Valve");
    digitalWrite(A0, LOW);
    }
}
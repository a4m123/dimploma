#include <SPI.h> 
#include <RF24.h> 
#define PIN_CE  10 
#define PIN_CSN 9 

RF24 radio(PIN_CE, PIN_CSN);

void setup(void){
  radio.begin();
  radio.setPALevel(RF24_PA_MAX);
  radio.setChannel(0x76);
  radio.openWritingPipe(0xF0F0F0F0E1LL);
  radio.enableDynamicPayloads();
  radio.powerUp();

  }

void loop(void){
  const char text[] = "Hello world!";
  radio.write(&text, sizeof(text));
  delay(1000);
  
  }

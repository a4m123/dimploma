#define triggerPin1 11
#define echoPin1 12
#define triggerPin2 9
#define echoPin2 8

bool flagPortDefined = false;
bool definePort();

int peopleNow = 0;
int peopleTotal = 0;
byte w = 0;

long duration1, cm1, duration2, cm2;
int i = 0;
int control_distance = 10;

void setup() {
  Serial.begin (9600);
  pinMode(triggerPin1, OUTPUT);
  pinMode(echoPin1, INPUT);
  pinMode(triggerPin2, OUTPUT);
  pinMode(echoPin2, INPUT);

}

void loop() {
  if (flagPortDefined == false){
      flagPortDefined = definePort();
    }
  
    delay(100);
    digitalWrite(triggerPin1, LOW);
    delayMicroseconds(5);
    digitalWrite(triggerPin1, HIGH);
    delayMicroseconds(10);
    digitalWrite(triggerPin1, LOW);
    duration1 = pulseIn(echoPin1, HIGH);
    cm1 = (duration1 / 2) / 29.1;

    digitalWrite(triggerPin2, LOW);
    delayMicroseconds(5);
    digitalWrite(triggerPin2, HIGH);
    delayMicroseconds(10);
    digitalWrite(triggerPin2, LOW);
    duration2 = pulseIn(echoPin2, HIGH);
    cm2 = (duration2 / 2) / 29.1;

    if (cm1 < control_distance) {
      w = 1;
    }
    if (cm2 < control_distance) {
      w = 2;
    }

    if (cm1 > control_distance) {}
    if (cm2 > control_distance) {}

    int i = 0;
    while (w == 1) {
      digitalWrite(triggerPin2, LOW);
      delayMicroseconds(5);
      digitalWrite(triggerPin2, HIGH);
      delayMicroseconds(10);
      digitalWrite(triggerPin2, LOW);
      duration2 = pulseIn(echoPin2, HIGH);
      cm2 = (duration2 / 2) / 29.1;
      
      if (cm2 < control_distance) {
        peopleNow = peopleNow + 1;
        peopleTotal = peopleTotal + 1;
        delay(2000); w = 0;
      }
      i++;
      if (i == 100){
        i = 0;
        w=0;
        break;
        }
      if (cm2 > 10) {}
    }

    while (w == 2) {
      digitalWrite(triggerPin1, LOW);
      delayMicroseconds(5);
      digitalWrite(triggerPin1, HIGH);
      delayMicroseconds(10);
      digitalWrite(triggerPin1, LOW);
      duration1 = pulseIn(echoPin1, HIGH);
      cm1 = (duration1 / 2) / 29.1;
      

      if (cm1 < control_distance) {
        peopleNow = peopleNow - 1;
        if (peopleNow < 0) {
          peopleNow = 0;
        }
        delay(2000); w = 0;
      }
      i++;
      if (i == 100){
        i = 0;
        w=0;
        break;
        }
      if (cm1 > control_distance) {}
    }

    delay(250);
    switch (peopleNow) {
      case 0:
        Serial.println(peopleNow);
        break;
      default:
        Serial.println(peopleNow);
        break;
    }
  
  if (Serial.available() <= 0){
    flagPortDefined = false;
  }
}

bool definePort(){
  String dataStr = Serial.readStringUntil('\n');
  int code = dataStr.toInt();
  if (code == 200){
    Serial.println(1);
    return true;
  }
  return false;
}
#define PIN_TRIG_1 11
#define PIN_ECHO_1 12
#define PIN_TRIG_2 9
#define PIN_ECHO_2 8


int peopleNow = 0;
int peopleTotal = 0;
byte w = 0;

long duration1, cm1, duration2, cm2;
int i = 0;
int control_distance = 10;

void setup() {
  Serial.begin (9600);
  pinMode(PIN_TRIG_1, OUTPUT);
  pinMode(PIN_ECHO_1, INPUT);
  pinMode(PIN_TRIG_2, OUTPUT);
  pinMode(PIN_ECHO_2, INPUT);

}

void loop() {
  delay(100);


  digitalWrite(PIN_TRIG_1, LOW);
  delayMicroseconds(5);
  digitalWrite(PIN_TRIG_1, HIGH);
  delayMicroseconds(10);
  digitalWrite(PIN_TRIG_1, LOW);
  duration1 = pulseIn(PIN_ECHO_1, HIGH);
  cm1 = (duration1 / 2) / 29.1;

  digitalWrite(PIN_TRIG_2, LOW);
  delayMicroseconds(5);
  digitalWrite(PIN_TRIG_2, HIGH);
  delayMicroseconds(10);
  digitalWrite(PIN_TRIG_2, LOW);
  duration2 = pulseIn(PIN_ECHO_2, HIGH);
  cm2 = (duration2 / 2) / 29.1;

  if (cm1 < control_distance) {
    w = 1;
  }
  if (cm2 < control_distance) {
    w = 2;
  }

  if (cm1 > control_distance) {}
  if (cm2 > control_distance) {}

  // цикл запускается при срабатывании первого датчика
  // ждем, пока не сработает прерывание на втором датчике
  // когда лазер прерывается, прибавляем людей и выходим из цикла
  int i = 0;
  while (w == 1) {
    digitalWrite(PIN_TRIG_2, LOW);
    delayMicroseconds(5);
    digitalWrite(PIN_TRIG_2, HIGH);
    delayMicroseconds(10);
    digitalWrite(PIN_TRIG_2, LOW);
    duration2 = pulseIn(PIN_ECHO_2, HIGH);
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
    digitalWrite(PIN_TRIG_1, LOW);
    delayMicroseconds(5);
    digitalWrite(PIN_TRIG_1, HIGH);
    delayMicroseconds(10);
    digitalWrite(PIN_TRIG_1, LOW);
    duration1 = pulseIn(PIN_ECHO_1, HIGH);
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
  // Задержка между измерениями для корректной работы скеча
  delay(250);
  switch (peopleNow) {
    case 0:
      Serial.println(peopleNow);
      break;
    default:
      Serial.println(peopleNow);
      break;
  }
}

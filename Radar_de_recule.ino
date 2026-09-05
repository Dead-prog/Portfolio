#include <NewPing.h>

#define green 12
#define yellow 11
#define red 10

#define echo 7
#define trig 8

#define buzz 5

NewPing ultrasons(8, 7, 200);

void setup() {
  // put your setup code here, to run once:
  pinMode(green, OUTPUT);
  pinMode(yellow, OUTPUT);
  pinMode(red, OUTPUT);

  pinMode(buzz, OUTPUT);

  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int distance = ultra();
  Serial.println(distance);

  if (distance <= 30 && distance >= 20) {
    green_warn();
  }

  if (distance <= 20 && distance >= 10) {
    yellow_warn();
  }

  if (distance <= 10 && distance >= 2) {
    red_warn();
  }

  delay(50);
}

int ultra() {
  return ultrasons.ping_cm();
}

void green_warn() {
  digitalWrite(green, HIGH);
  digitalWrite(buzz, HIGH);
  delay(150);
  digitalWrite(green, LOW);
  digitalWrite(buzz, LOW);
  delay(150);
}

void yellow_warn() {
  digitalWrite(yellow, HIGH);
  digitalWrite(buzz, HIGH);
  delay(100);
  digitalWrite(yellow, LOW);
  digitalWrite(buzz, LOW);
  delay(100);
}

void red_warn() {
  digitalWrite(red, HIGH);
  digitalWrite(buzz, HIGH);
  delay(50);
  digitalWrite(red, LOW);
  digitalWrite(buzz, LOW);
  delay(50);
}
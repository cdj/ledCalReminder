// This code is for the Arduino RSS feed project, by Fritter
// Read the comment lines to figure out how it works

const int ledPin = 9;

void setup() {
  Serial.begin(9600);  // opens serial port, sets data rate to 9600 bps
  pinMode(ledPin, OUTPUT);
}

void loop() {
  char incomingByte = 0;  // for incoming serial data

  if (Serial.available() > 0) {  // Check for incoming Serial Data
    incomingByte = Serial.read();
    if (incomingByte == '1') {
      digitalWrite(ledPin, HIGH);  // Some event was found
    } else {
      digitalWrite(ledPin, LOW);  // No events found or unknown/error
    }
    delay(5000);  // reset the character count to 0
  }
  
  delay(10);  // 10ms delay for stability
} 


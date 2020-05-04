int analogPin = A0;
int val = 0;

void setup(){ //lcd.begin(16, 2);
  Serial.begin(9600); // open serial port, set the baud rate to 9600 bps
}
void loop(){int val;
      val = analogRead(analogPin);
      Serial.println(val);        
     
delay(400);}

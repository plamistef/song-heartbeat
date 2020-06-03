int analogPin = A0;

int waterPin = A3;

void setup(){ //lcd.begin(16, 2);
  Serial.begin(9600); // open serial port, set the baud rate to 9600 bps
}
void loop(){
      int val;
      int value;
      
      val = analogRead(analogPin);
      Serial.print("s: ");
      Serial.println(val);        

     value = analogRead(waterPin);
     Serial.print("w: ");
     Serial.println(value);
     
delay(400);}

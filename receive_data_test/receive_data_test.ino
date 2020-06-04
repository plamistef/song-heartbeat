char serial;
int waterPin = A3;
int soundPin = A0;

void setup(){ //lcd.begin(16, 2);
  Serial.begin(9600); // open serial port, set the baud rate to 9600 bps
}
void loop(){
     int waterValue;
     int soundValue;

     while(Serial.available() > 0) {
        
         if(Serial.read() == 's') {
                  
       soundValue = analogRead(soundPin);
       Serial.print("s: ");
       Serial.println(soundValue);
       delay(400);
          
     }
     else if(Serial.read() == 'w') {
       waterValue = analogRead(waterPin);
       Serial.print("w: ");
       Serial.println(waterValue);
       delay(400);
         } 
     }
}

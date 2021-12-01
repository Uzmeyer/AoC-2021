#include <Arduino.h>

#define INBUFF_SIZE 10

char incomingByte = 0;
char inBuffer[INBUFF_SIZE];
int writepointer = 0;
int recvals = 0;
int largerthanprev = 0;
int prev = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  Serial.println("Waiting for input...");
  while(!Serial.available()){
  }
  
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()){
    incomingByte = Serial.read();
    //Serial.print(incomingByte);
    switch(incomingByte)
    {
      case 0x0A: //Linefeed
        inBuffer[writepointer] = '\0';
        //Serial.println(inBuffer);
        writepointer = 0;
        int curval;
        curval = atoi(inBuffer);
        //Serial.println(curval, DEC);
        if(recvals)
        {
          if(curval > prev)
          {
            largerthanprev++;
            //Serial.print("Values larger than prev: ");
            Serial.println(largerthanprev, DEC);
          }
        }
        recvals++;
        prev = curval;
        break;
      case 0x0D: //Carriage return
        break;
      default:
        if(incomingByte >= 0x30 && incomingByte <= 0x39)
        {
          inBuffer[writepointer] = incomingByte;
          writepointer++;
        }
        break;      
    }
  }
}

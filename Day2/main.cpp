#include <Arduino.h>
#include <Vector.h>
#include <Streaming.h>

const int INPU_COUNT_MAX = 20000;
const int DATA_COUNT_MAX = 2000;
char inbyte;
char inbufferStorage[INPU_COUNT_MAX];
Vector<char> inbuffer;
int transfertimer = 0;
bool xfercomplete = false;
char conversionbuffer[10];
int buffpointer = 0;
int dataStorage[DATA_COUNT_MAX];
Vector<int> data;
int largerthanprev = -1;
int prev = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  inbuffer.setStorage(inbufferStorage);
  data.setStorage(dataStorage);
  Serial << "Waiting for Data..." << endl;
  while(!Serial.available()){

  }
  Serial << "begin receiving data" << endl;

}

void loop() {
  // put your main code here, to run repeatedly:
  if(transfertimer < 100 )
  {
    if(Serial.available())
    {
      inbyte = Serial.read();
      //Serial << inbyte << endl;
      inbuffer.push_back(inbyte);
      transfertimer = 0;
    } 
  }
  else if(!xfercomplete)
  {
    xfercomplete = true;
    Serial << "Data receive complete" << endl;
    //Serial << "received data:" << endl;
    //Serial << inbuffer << endl;
    Serial << "Bytes received: " << inbuffer.size() << endl;
    for(char element : inbuffer)
    {
      switch(element)
      {
        case 0x0A: //Linefeed
        conversionbuffer[buffpointer] = '\0';
        //Serial.println(inBuffer);
        buffpointer = 0;
        int curval;
        curval = atoi(conversionbuffer);
        data.push_back(curval);
        //Serial.println(curval, DEC);
        
        break;
        case 0x0D: //Carriage return
        break;
        default:
        if(element >= 0x30 && element <= 0x39)
        {
          conversionbuffer[buffpointer] = element;
          buffpointer++;
        }
        break;      
      }
    }
    Serial << "Data: " << endl;
    Serial << data;
    for(int i; i < (data.size() - 2); i++)
    {
      int val = data.at(i) + data.at(i+1) + data.at(i+2);
      Serial << "Val = " <<  val << endl;
      if(val > prev)
      {
        largerthanprev++;
      }
      prev = val;
    }
    Serial << "Values larger than prev: " << largerthanprev << endl;
  }

  if(!xfercomplete)
  {
    transfertimer++;
    //Serial << transfertimer << endl;
  }
  
}

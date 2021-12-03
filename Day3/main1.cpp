#include <Arduino.h>
//#include <Vector.h>
#include <Streaming.h>
#include <string.h>
#include <vector>
#include <String>

std::vector<char> inbuffer;
std::vector<uint32_t> data;
char inbyte;
int transfertimer = 0;
bool xfercomplete = false;
char conversionbuffer[20];
int buffpointer = 0;
int bitcount[12] = {0,0,0,0,0,0,0,0,0,0,0,0};
uint32_t epsilonrate = 0;
uint32_t gammarate = 0;

uint32_t bitFromChar(char input)
{
  switch(input)
  {
    case '0':
    return 0;
    break;
    case '1':
    return 1;
    break;
  }
  return 0;
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
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
    Serial << "Size of inbuffer: " << inbuffer.size() << endl;
    for(char element : inbuffer)
    {
      uint32_t curval = 0;
      int length;
      switch(element)
      {
        case 0x0A: //Linefeed
        conversionbuffer[buffpointer] = '\0';
        //Serial.println(inBuffer);
        buffpointer = 0;
        
        length = strlen(conversionbuffer);
        for(int i = 0; i < length; i++)
        {
          uint32_t bit = bitFromChar(conversionbuffer[i]) << (length - i - 1);
          curval |= bit;
        }
        //Serial.print("Binary: ");
        //Serial.println(curval, BIN);
        data.push_back(curval);
        //Serial << "Data size: " << data.size() << endl;
        
        break;
        case 0x0D: //Carriage return
        break;
        default:
        if((element >= 0x30 && element <= 0x39) || (element >= 0x61 && element <= 0x7a) || element == 0x20)
        {
          conversionbuffer[buffpointer] = element;
          buffpointer++;
        }
        break;
      }
    }
    for(uint32_t element : data)
    {
      for(int i = 0; i<12; i++)
      {
        if(element & (1 << i))
        {
          bitcount[i]++;
        }
      }
    }
    for(int i = 0; i<12; i++)
    {
      Serial.printf("Bit %d count: %d", i, bitcount[i]);
      Serial << endl;
      if(bitcount[i] > data.size()/2)
      {
        gammarate |= (1 << i);
      }
      else
      {
        epsilonrate |= (1 << i);
      }
    }
    int solution = gammarate * epsilonrate;
    Serial.print("Gamma rate: ");
    Serial.println(gammarate, BIN);
    Serial.print("Epsilon rate: ");
    Serial.println(epsilonrate, BIN);
    Serial.print("Solution: ");
    Serial.println(solution, DEC);
  }
  if(!xfercomplete)
  {
    transfertimer++;
    //Serial << transfertimer << endl;
  }
}

#include <Arduino.h>
#include <Vector.h>
#include <Streaming.h>
#include <string.h>

const int INPU_COUNT_MAX = 20000;
const int DATA_COUNT_MAX = 2000;
char inbyte;
char inbufferStorage[INPU_COUNT_MAX];
Vector<char> inbuffer;
int transfertimer = 0;
bool xfercomplete = false;
char conversionbuffer[20];
int buffpointer = 0;
typedef enum direction
{
  FOWARD = 0,
  DOWN = 1,
  UP = 2
}direction_t;

typedef struct movement
{
  int distance;
  direction_t direction;
}movement_t;

movement_t dataStorage[DATA_COUNT_MAX];
Vector<movement_t> data;
int depth = 0;
int horizontal = 0;
int aim = 0;

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
        movement_t curval;
        char *pch;
        pch = strtok(conversionbuffer, " ");
        if(pch != NULL)
        {
          switch(pch[0])
          {
            case 'f':
            curval.direction = direction_t::FOWARD;
            break;
            case 'u':
            curval.direction = direction_t::UP;
            break;
            case 'd':
            curval.direction = direction_t::DOWN;
            break;
          }
          pch = strtok(NULL, " ");
        }
        if(pch != NULL)
        {
          curval.distance = atoi(pch);
        }
        Serial << "Direction: " << curval.direction << endl;
        Serial << "Distance: " << curval.distance << endl;
        data.push_back(curval);
        //Serial.println(curval, DEC);
        
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
    for(movement_t movement : data )
    {
      switch(movement.direction)
      {
        case direction_t::FOWARD:
        horizontal += movement.distance;
        depth += movement.distance * aim;
        break;
        case direction_t::DOWN:
        aim += movement.distance;
        break;
        case direction_t::UP:
        aim -= movement.distance;
        break;
      }
    }
    Serial << "Final depth: " << depth << " Final horizontal: " << horizontal << endl;
    Serial << "Multiplied: " << depth*horizontal << endl;
    
  }

  if(!xfercomplete)
  {
    transfertimer++;
    //Serial << transfertimer << endl;
  }
  
}

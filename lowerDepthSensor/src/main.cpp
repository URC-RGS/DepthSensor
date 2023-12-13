#include <Wire.h>
#include "MS5837.h"
#include "Config.h"

MS5837 sensor;

uint32_t turnTimer;
int ledState = LOW;

void setup() {
  Serial1.setRX(UART_RX);
  Serial1.setTX(UART_TX);

  pinMode(UART_COM, OUTPUT);
  digitalWrite(UART_COM, HIGH);

  Serial1.begin(57600);

  Serial.begin(57600);
  Serial.println("Starting");
  
  Wire.setSDA(8);
	Wire.setSCL(9);
  Wire.begin();

  // Initialize pressure sensor
  // Returns true if initialization was successful
  // We can't continue with the rest of the program unless we can initialize the sensor
  while (!sensor.init()) {
    Serial.println("Init failed!");
    Serial.println("Are SDA/SCL connected correctly?");
    Serial.println("Blue Robotics Bar30: White=SDA, Green=SCL");
    Serial.println("\n\n\n");
    delay(5000);
  }
  
  sensor.setModel(MS5837::MS5837_30BA);
  sensor.setFluidDensity(997); // плотность воды 

  pinMode(LED_BUILTIN, OUTPUT);

}

void loop() {
  
  // Update pressure and temperature readings
  sensor.read();
  // отправка в юсб 
  Serial.print(sensor.pressure());
  Serial.print(' ');
  Serial.print(sensor.temperature());
  Serial.print(' ');
  Serial.println(sensor.depth()); 

  // отправка в rs485
  Serial1.print(sensor.pressure());
  Serial1.print(' ');
  Serial1.print(sensor.temperature());
  Serial1.print(' ');
  Serial1.println(sensor.depth()); 

  if (ledState == LOW) ledState = HIGH;
  else ledState = LOW;

  digitalWrite(LED_BUILTIN, ledState);

  delay(250);
}
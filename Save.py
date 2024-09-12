"""import serial
import time
arduino = serial.Serial("COM6", 9600)
time.sleep(2)
rawString = arduino.readline()
print(rawString)
arduino.write("Hola Arduino".encode())
rawString = arduino.readline()
print(rawString)
arduino.close()

#include <Servo.h>
Servo servo1;

String entradaSerial = "";         // String para almacenar entrada
bool entradaCompleta = false;  // Indicar si el String está completo

void setup()
{
  Serial.begin(9600);
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
}

void loop()
{
  if (entradaCompleta) {
    if (entradaSerial == "Circle\n") {
      digitalWrite(2, HIGH);
    }
    else if (entradaSerial == "Triangle\n"){
      digitalWrite(3, HIGH);
    }
    else if (entradaSerial == "Square\n"){
      digitalWrite(4, HIGH);
    }
    else { // Cualquier otro dato recibido
      Serial.println("El dato recibido es inválido!!");
    }
    entradaSerial = "";
    entradaCompleta = false;
  }
}

// Función que se activa al recibir algo por
// el puerto serie, Interrupción del Puerto Serie.
void serialEvent() {
  while (Serial.available()) {
    // Obtener bytes de entrada:
    char inChar = (char)Serial.read();
    // Agregar al String de entrada:
    entradaSerial += inChar;
    // Para saber si el string está completo, se detendrá al recibir
    // el caracter de retorno de línea ENTER \n
    if (inChar == '\n') {
      entradaCompleta = true;
    }
  }
}"""
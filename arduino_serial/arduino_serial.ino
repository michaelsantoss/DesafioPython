
//#include <SoftwareSerial.h>
//SoftwareSerial Serialmesa(10,11); // RX, TX

String inputString = "";         // a string to hold incoming data
boolean stringComplete = false;  // whether the string is complete
int led=13;
int esteira=A0;
void workRoda();
void workMotor();
void echo(String mensagem);
void para_esteira();


void setup() {
  pinMode(led,OUTPUT);
  pinMode(A0,INPUT);
  // initialize serial:
  Serial.begin(9600);
  // reserve 200 bytes for the inputString:
  inputString.reserve(200);
  //Serialmesa.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  
  if (stringComplete) {
    //Serial.println(inputString);
    if(inputString == "DO1M\n"){
      digitalWrite(led,HIGH);
      Serial.println("OK1");
      inputString = "";
      stringComplete = false;
      workMotor();
    }
    
    if(inputString == "DO1R\n"){
      digitalWrite(led,LOW);
      Serial.println("OK1");
      inputString = "";
      stringComplete = false;
      workRoda();
    }
      inputString = "";
      stringComplete = false;
  }
}


void serialEvent() {
  while (Serial.available()) {
    char inChar = (char)Serial.read();
    inputString += inChar;
    if (inChar == '\n') {
      stringComplete = true;
    }
  }
}

void echo(String mensagem){
  Serial.print("ECHO"+mensagem+"\n");
}
void para_esteira(){
  Serial.println("ECHOEsteira parou");
}

//Fazer o Código Nestas Funções!
void workMotor(){
//while(digitalRead(esteira)==0){  
//}
para_esteira();
//exemplo
echo("PROCESSO DO MOTOR INICIADO");
delay(1000);
echo("Executando, em transporte");
delay(1000);
Serial.println("DONE1OK");
}

void workRoda(){
para_esteira();
//exemplo
echo("PROCESSO DA RODA INICIADO");
delay(1000);
echo("Executando, em transporte");
delay(1000);
Serial.println("DONE1OK");
}



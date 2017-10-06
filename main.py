import serial;

while(1):
    ser = serial.Serial('/dev/cu.usbserial-A600edm0',9600);
    

    #INICIAR ESCOLHENDO MOTOR OU RODA
    valor = raw_input("Digite o valor: ");
    ser.write(valor+"\n");

    #TESTA O QUE DEU, E ATRIBUI A OBJETO O QUE ï¿½
    if(valor == "DO1M"):
        objeto = "Motor";
    else:
        objeto = "Roda";
        
    #PEGA A RESPOSTA DA PRIMEIRA ESTAï¿½ï¿½O   
    resposta = str(ser.read(3));
    print resposta
    if(resposta=="OK1"):
        ser.write("START\n");
                
        resposta = str(ser.read(3));
        print(resposta)    
        arquivo = open('entrada.txt', 'w')
        arquivo.close()
        arquivo = open('entrada.txt', 'a');#ABRE O ARQUIVO TXT
        objeto_mensagem = "ECHOESTAÇÃO 1";#SALVA NA VARIAVEL O QUE QUER ARMAZENAR NO TXT
        arquivo.write('%s\n' % objeto_mensagem);#ESCREVE NO ARQUIVO
        arquivo.close()#FECHA O ARQUIVO
        if(objeto == "Motor"):
            arquivo = open('entrada.txt', 'a');
            objeto_mensagem = "ECHOiniciar a produção do MOTOR";
            print ("iniciar a produção do MOTOR");
            arquivo.write('%s\n' % objeto_mensagem);
            arquivo.write('\n')
            arquivo.close()
            
        else:
            arquivo = open('entrada.txt', 'w')
            arquivo.close()
            arquivo = open('entrada.txt', 'a');
            arquivo.write('ECHOESTAÇÃO 1\n')
            objeto_mensagem = "ECHOiniciar a produção da Roda";
            print ("iniciar a produção da Roda");
            arquivo.write('%s\n' % objeto_mensagem);
            arquivo.write('\n')
            arquivo.close()
        
        while(resposta != "DONE1OK"): #ENQUANTO A ESTAï¿½ï¿½O Nï¿½O ENCERRAR
            arquivo = open('entrada.txt', 'a')
            resposta = str(ser.read(90)); #COLETA AS ECHOS
            
            while(resposta.count("STOP", 0, 90)<0):
                resposta = str(ser.read(4));
            
            ser.write("STOP\n");
            ser.write("ECHOOK1\n");
            arquivo.write('%s\n' % resposta);
            arquivo.write('\n')
            arquivo.close()
                
            if(resposta == "DONE1"):#SE A REPOSTA FOR DONE1
                ser.write("DONE1OK\n");
                            
       
                        
            #TESTA QUAL ï¿½ O OBJETO E ENVIA O COMANDO PARA PROXIMA ESTAï¿½ï¿½O
            if(objeto == "Motor"):
                ser.write("DO2M\n")
            else:
               ser.write("DO2R\n")
               
            #PEGA A RESPOSTA DA SEGUNDA ESTAï¿½ï¿½O  
            resposta = str(ser.read(3));
            if(resposta=="OK2"):#TESTA A RESPOSTA
                ser.write("START\n");
                arquivo = open('entrada.txt', 'a')
                arquivo.write('%s\n' % objeto_mensagem);
                arquivo.close()
                if(objeto == "Motor"):
                    arquivo = open('entrada.txt', 'w')
                    arquivo.close()
                    arquivo = open('entrada.txt', 'a');
                    arquivo.write('ECHOESTAÇÃO 2\n');
                    objeto_mensagem = "ECHOInicia a uzinagem do MOTOR";#SALVA NA VARIAVEL O QUE QUER ARMAZENAR NO TXT
                    print ("Inicia a uzinagem do MOTOR");#MOSTRA NO CONSOLE O QUE TA FAZENDO
                    arquivo.write('%s\n' % objeto_mensagem);#ESCREVE NO ARQUIVO A STRING
                    arquivo.write('\n')#ESCREVE UM \N PARA GARANTIR
                    arquivo.close()#FECHA O ARQUIVO
                else:
                    arquivo = open('entrada.txt', 'w')
                    arquivo.close()
                    arquivo = open('entrada.txt', 'a');
                    arquivo.write('ECHOESTAÇÃO 2\n');
                    objeto_mensagem = "ECHOInicia a uzinagem da RODA";
                    print ("Inicia a uzinagem da RODA");
                    arquivo.write('%s\n' % objeto_mensagem);
                    arquivo.write('\n')
                    arquivo.close()
                    
                while(resposta != "DONE2"):#ENQUANTO A ESTAï¿½ï¿½O Nï¿½O ENCERRAR
                     arquivo = open('entrada.txt', 'a')
                     resposta = str(ser.read(90)); #COLETA AS ECHOS
                     print resposta;
                     while(resposta.count("STOP", 0, 90)<0):
                        resposta = str(ser.read(4));
                     ser.write("STOP\n");
                     ser.write("ECHOOK2\n");
                     arquivo.write('%s\n' % resposta);
                     arquivo.write('\n')
                     arquivo.close()
                    
                if(respota == "DONE2"):
                    ser.write("DONE2OK")#ENVIA UM DONE2OK
                    #TESTA QUAL ï¿½ O OBJETO E ENVIA O COMANDO PARA PROXIMA ESTAï¿½ï¿½O
                    if(objeto == "Motor"):
                        ser.write("DO3M\n")
                    else:
                        ser.write("DO3R\n")
                    #PEGA A RESPOSTA DA TERCEIRA ESTAï¿½ï¿½O      
                    resposta = str(ser.read(3));
                    if(resposta=="OK3"):
                        ser.write("START\n");
                        arquivo = open('entrada.txt', 'a')
                        arquivo.write('%s\n' % objeto_mensagem);
                        arquivo.close();
                        if(objeto == "Motor"):
                            arquivo = open('entrada.txt', 'w')
                            arquivo.close()
                            arquivo = open('entrada.txt', 'a');
                            arquivo.write('ECHOESTAÇÃO 3\n');
                            objeto_mensagem = "ECHOPosiciona o bloco do MOTOR";
                            print ("Posiciona o bloco do MOTOR");
                            arquivo.write('%s\n' % objeto_mensagem);
                            arquivo.close()
                        else:
                            arquivo = open('entrada.txt', 'w')
                            arquivo.close()
                            arquivo = open('entrada.txt', 'a');
                            arquivo.write('ECHOESTAÇÃO 3\n');
                            objeto_mensagem = "ECHOPosiciona o pneu da RODA";
                            print ("Posiciona o pneu da RODA");
                            arquivo.write('%s\n' % objeto_mensagem);
                            arquivo.close()

                        while(resposta != "DONE3"):#ENQUANTO A ESTAï¿½ï¿½O Nï¿½O ENCERRAR
                             arquivo = open('entrada.txt', 'a')
                             resposta = str(ser.read(90)); #COLETA AS ECHOS
                             print resposta;
                             while(resposta.count("STOP", 0, 90)<0):
                                resposta = str(ser.read(4));
                             ser.write("STOP\n");
                             ser.write("ECHOOK3\n");
                             arquivo.write('%s\n' % resposta);
                             arquivo.write('\n')
                             arquivo.close()

                        if(respota == "DONE3"):#SE A REPOSTA FOR DONE3
                            ser.write("DONE3OK")#ENVIA UM DONE3OK
                            #TESTA QUAL ï¿½ O OBJETO E ENVIA O COMANDO PARA PROXIMA ESTAï¿½ï¿½O
                            if(objeto == "Motor"):
                                ser.write("DO4M\n")
                            else:
                                ser.write("DO4R\n")
                            #PEGA A RESPOSTA DA QUARTA ESTAï¿½ï¿½O             
                            resposta = str(ser.read(3));

                            if(resposta=="OK4"):
                                arquivo = open('entrada.txt', 'a')
                                arquivo.write('%s\n' % objeto_mensagem);
                                arquivo.close()
                                if(objeto == "Motor"):
                                    arquivo = open('entrada.txt', 'w')
                                    arquivo.close()
                                    arquivo = open('entrada.txt', 'a');
                                    arquivo.write('ECHOESTAÇÃO 4\n');
                                    objeto_mensagem = "ECHOInicia a montagem do MOTOR";
                                    print ("Inicia a montagem do MOTOR");
                                    arquivo.write('%s\n' % objeto_mensagem);
                                    arquivo.close()
                                else:
                                    arquivo = open('entrada.txt', 'w')
                                    arquivo.close()
                                    arquivo = open('entrada.txt', 'a');
                                    arquivo.write('ECHOESTAÇÃO 4\n');
                                    objeto_mensagem = "ECHOInicia a montagem da RODA";
                                    print ("Inicia a montagem da RODA");
                                    arquivo.write('%s\n' % objeto_mensagem);
                                    arquivo.close()

                                while(resposta != "DONE4"):#ENQUANTO A ESTAï¿½ï¿½O Nï¿½O ENCERRAR
                                    arquivo = open('entrada.txt', 'a')
                                    resposta = str(ser.read(90)); #COLETA AS ECHOS
                                    print resposta;
                                    while(resposta.count("STOP", 0, 90)<0):
                                        resposta = str(ser.read(4));
                                    ser.write("STOP\n");
                                    ser.write("ECHOOK4\n");
                                    arquivo.write('%s\n' % resposta);
                                    arquivo.write('\n')
                                    arquivo.close()

                                if(respota == "DONE4"):#SE A REPOSTA FOR DONE4
                                    ser.write("DONE4OK")#ENVIA UM DONE4OK
                                    #TESTA QUAL ï¿½ O OBJETO E ENVIA O COMANDO PARA PROXIMA ESTAï¿½ï¿½O
                                    if(objeto == "Motor"):
                                        ser.write("DO5M\n")
                                    else:
                                        ser.write("DO5R\n")
                                    #PEGA A RESPOSTA DA QUINTA ESTAï¿½ï¿½O             
                                    resposta = str(ser.read(3));
                                    if(resposta=="OK5"):
                                        ser.write("START\n");
                                        arquivo = open('entrada.txt', 'a')
                                        arquivo.write('%s\n' % objeto_mensagem);
                                        arquivo.close()
                                        ser2 = serial.Serial('COM5',9600);
                                        if(objeto == "Motor"):
                                            arquivo = open('entrada.txt', 'w')
                                            arquivo.close()
                                            arquivo = open('entrada.txt', 'a');
                                            arquivo.write('ECHOESTAÇÃO 5\n');
                                            objeto_mensagem = "ECHOInicia a montagem do MOTOR";
                                            print ("Inicia a montagem do MOTOR");
                                            arquivo.write('%s\n' % objeto_mensagem);
                                            arquivo.close()
                                        else:
                                            arquivo = open('entrada.txt', 'w')
                                            arquivo.close()
                                            arquivo = open('entrada.txt', 'a');
                                            arquivo.write('ECHOESTAÇÃO 5\n');
                                            objeto_mensagem = "ECHOInicia a montagem da RODA";
                                            print ("Inicia a montagem da RODA");
                                            arquivo.write('%s\n' % objeto_mensagem);
                                            arquivo.close()

                                        while(resposta != "DONE5"):#ENQUANTO A ESTAï¿½ï¿½O Nï¿½O ENCERRAR
                                            arquivo = open('entrada.txt', 'a')
                                            resposta = str(ser2.read(90)); #COLETA AS ECHOS
                                            print resposta;
                                            while(resposta.count("STOP", 0, 90)<0):
                                                resposta = str(ser.read(4));
                                            ser.write("STOP\n");
                                            ser2.write("ECHOOK5\n");
                                            arquivo.write('%s\n' % resposta);
                                            arquivo.write('\n')
                                            arquivo.close()

                                        if(respota == "DONE5"):#SE A REPOSTA FOR DONE4
                                            ser2.write("DONE5OK")#ENVIA UM DONE4OK
                                            arquivo = open('entrada.txt', 'a')
                                            objeto_mensagem = "ECHOPROCESSO FINALIZADO";
                                            arquivo.write('%s\n' % objeto_mensagem);
                                            arquivo.close()
                                            
                                    
                                                                                                    

    
    ser.close()

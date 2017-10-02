import serial;

while(1):
    ser = serial.Serial('COM2',9600);
    

    #INICIAR ESCOLHENDO MOTOR OU RODA
    valor = raw_input("Digite o valor: ");
    ser.write(valor+"\n");

    #TESTA O QUE DEU, E ATRIBUI A OBJETO O QUE É
    if(valor == "DO1M"):
        objeto = "Motor";
    else:
        objeto = "Roda";
        
    #PEGA A RESPOSTA DA PRIMEIRA ESTAÇÃO   
    resposta = str(ser.read(3));
    print resposta
    if(resposta=="OK1"):
        if(objeto == "Motor"):
            arquivo = open('entrada.txt', 'a')
            objeto_mensagem = "ECHOiniciar a produção do MOTOR";
            print ("iniciar a produção do MOTOR");
            arquivo.write('%s\n' % objeto_mensagem);
            arquivo.write('\n')
            arquivo.close()
            
        else:
            arquivo = open('entrada.txt', 'a')
            objeto_mensagem = "ECHOiniciar a produção da Roda";
            print ("iniciar a produção da Roda");
            arquivo.write('%s\n' % objeto_mensagem);
            arquivo.write('\n')
            arquivo.close()
            
        while(resposta != "DONE1"): #ENQUANTO A ESTAÇÃO NÃO ENCERRAR
            arquivo = open('entrada.txt', 'a')
            resposta = str(ser.read(90)); #COLETA AS ECHOS
            print resposta
            ser.write("ECHOOK1\n")
            arquivo.write('%s\n' % resposta);
            arquivo.write('\n')
            arquivo.close()
                
        if(resposta == "DONE1"):#SE A REPOSTA FOR DONE1
            ser.write("DONE1OK\n");
                
            #TESTA QUAL É O OBJETO E ENVIA O COMANDO PARA PROXIMA ESTAÇÃO
            if(objeto == "Motor"):
                ser.write("DO2M\n")
            else:
               ser.write("DO2R\n")
            #PEGA A RESPOSTA DA SEGUNDA ESTAÇÃO  
            resposta = str(ser.read(3));
            if(resposta=="OK2"):
                if(objeto == "Motor"):
                    print ("Inicia a uzinagem do MOTOR");
                else:
                    print ("Inicia a uzinagem da Roda");
                    
                while(resposta != "DONE2"):#ENQUANTO A ESTAÇÃO NÃO ENCERRAR
                    resposta = str(ser.read(166));#COLETA AS ECHOS
                    
                if(respota == "DONE2"):
                    ser.write("DONE2OK")#ENVIA UM DONE2OK
                    #TESTA QUAL É O OBJETO E ENVIA O COMANDO PARA PROXIMA ESTAÇÃO
                    if(objeto == "Motor"):
                        ser.write("DO3M\n")
                    else:
                        ser.write("DO3R\n")
                    #PEGA A RESPOSTA DA TERCEIRA ESTAÇÃO      
                    resposta = str(ser.read(3));
                    if(resposta=="OK3"):
                        if(objeto == "Motor"):
                            print ("Posiciona o bloco do MOTOR");
                        else:
                            print ("Posiciona o pneu da RODA");

                        while(resposta != "DONE3"):#ENQUANTO A ESTAÇÃO NÃO ENCERRAR
                            resposta = str(ser.read(166));#COLETA AS ECHOS

                        if(respota == "DONE3"):#SE A REPOSTA FOR DONE3
                            ser.write("DONE3OK")#ENVIA UM DONE3OK
                            #TESTA QUAL É O OBJETO E ENVIA O COMANDO PARA PROXIMA ESTAÇÃO
                            if(objeto == "Motor"):
                                ser.write("DO4M\n")
                            else:
                                ser.write("DO4R\n")
                            #PEGA A RESPOSTA DA QUARTA ESTAÇÃO             
                            resposta = str(ser.read(3));

                            if(resposta=="OK4"):
                                if(objeto == "Motor"):
                                    print ("Inicia a montagem do MOTOR");
                                else:
                                    print ("Inicia a montagem da RODA");

                                while(resposta != "DONE4"):#ENQUANTO A ESTAÇÃO NÃO ENCERRAR
                                    resposta = str(ser.read(166));#COLETA AS ECHOS

                                if(respota == "DONE4"):#SE A REPOSTA FOR DONE4
                                    ser.write("DONE4OK")#ENVIA UM DONE4OK
                                    #TESTA QUAL É O OBJETO E ENVIA O COMANDO PARA PROXIMA ESTAÇÃO
                                    if(objeto == "Motor"):
                                        ser.write("DO5M\n")
                                    else:
                                        ser.write("DO5R\n")
                                    #PEGA A RESPOSTA DA QUINTA ESTAÇÃO             
                                    resposta = str(ser.read(3));
                                    if(resposta=="OK5"):
                                        if(objeto == "Motor"):
                                            print ("Inicia a montagem do MOTOR");
                                        else:
                                            print ("Inicia a montagem da RODA");

                                        while(resposta != "DONE5"):#ENQUANTO A ESTAÇÃO NÃO ENCERRAR
                                            resposta = str(ser.read(166));#COLETA AS ECHOS

                                        if(respota == "DONE5"):#SE A REPOSTA FOR DONE4
                                            ser.write("DONE5OK")#ENVIA UM DONE4OK
                                    
                                                                                                    

    
    ser.close()

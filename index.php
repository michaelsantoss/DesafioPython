<!DOCTYPE html>
<html lang="pt-br">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="description" content="">
        <meta name="keywords" content="">
        <meta name="author" content="">
        <title>Desafio Mercopar - PMFTEC</title>
        <meta http-equiv="refresh" content="5";>

        <!-- Bootstrap CSS -->
        <link href="css/bootstrap.min.css" rel="stylesheet">
        <!-- Bootstrap CSS -->
        <link href="css/font-awesome.min.css" rel="stylesheet">
        <!-- Animate CSS -->
        <link href="css/animate.css" rel="stylesheet">
        <!-- Theme CSS -->
        <link href="style.css" rel="stylesheet">
            <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
        <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
        <!--[if lt IE 9]>
            <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
            <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
        <![endif]-->

    </head>
    <body class="index">
        <!-- Header section start -->
        <header> 
            <div class="awesome-carousel"> 

                <div id="awesome-carousel" class="carousel slide" data-ride="carousel">
                  
                    <!-- Wrapper for slides -->
                    <div class="carousel-inner" role="listbox">

                        <!-- slider item -->
                        <div class="item active">
                            
                            <img src="images/slider/ve.jpg" alt="slider one">
                            

                            <div class="carousel-caption">
                                
                                <?php
                                    //o primeiro paramentro da função fopen é o caminho do seu txt e o segundo recebe o r
                                    //informando que será  apenas para a leitura
                                    $arquivo = fopen("entrada.txt","r");
                                    // a função feof verifica se o seu arquivo chegou ao fim , abaixo
                                    //ele vai ler o arquivo txt quando o arquivo for diferente do fim 
                                    while( !feof($arquivo)){
                                    
                                    //pega linha por linha e armazenda dentro da variavel $linha
                                    $linha = fgets($arquivo);
                                    
                                    ?>
                                    <h2><?php
                                    //exibe na tela as linhas do arquivo na tela 

                                    $echo = substr(utf8_encode($linha), 0, 4);

                                    ?>
                                    <?php
                                    if($echo == "ECHO"){

                                        echo substr($linha, 4, strlen($linha));
                                    }else{
                                        echo $linha;
                                    }

                                    }

                                    //fechamos o arquivo
                                    fclose($arquivo);

                                    ?></h2>
                                </div>
                        </div><!-- End slider item -->
                        <!-- slider item -->
                        <!-- End slider item -->
                    </div>

                  <!-- Controls -->
                    
                </div>
            </div>
        </header>
       
        <!-- Include jQuery -->
        <script src="js/jquery-1.12.4.min.js"></script>
        <!-- Bootstrap Core jQuery -->
        <script src="js/bootstrap.min.js"></script>
        <!-- Theme jquery -->
        <script src="js/main.js"></script>
    </body>
</html>

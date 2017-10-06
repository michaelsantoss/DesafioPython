<meta charset="utf-8">
<?php
//o primeiro paramentro da função fopen é o caminho do seu txt e o segundo recebe o r
//informando que será  apenas para a leitura
$arquivo = fopen("entrada.txt","r");

// a função feof verifica se o seu arquivo chegou ao fim , abaixo
//ele vai ler o arquivo txt quando o arquivo for diferente do fim 
while( !feof($arquivo)){

//pega linha por linha e armazenda dentro da variavel $linha
$linha = fgets($arquivo);

//exibe na tela as linhas do arquivo na tela 

$echo = substr($linha, 0, 4);

if($echo == "ECHO"){
	echo substr($linha, 4)."<br>";
}


}

//fechamos o arquivo
fclose($arquivo);

?>
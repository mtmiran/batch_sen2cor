# Correção Atmosférica Sen2cor em Lote

## Sobre

Esse script em python não se trata da correção atmosférica em si. Tratá-se apenas de uma automação que fiz pensando em facilitar o uso do sen2cor para correção em multiplas imagens Sentinel-2.

Nesse repositório encontra-se o script '"batch_sentinel2.py"' e o executável do mesmo ".exe". Fiz esse executável para quem não possui o python instalado e/ou não tem familiridade no terminal.

Recomendo assistir o vídeo que postei no YouTube para caso tenha alguma dúvida: [ainda não postei xp]()

## Uso

Basta clicar duas vezes no executável para o programa iniciar.

Lembrando que as imagens precisam estar **na mesma pasta** do programa já extraídas.

## Possíveis Erros

- fique atento no caminho da imagem sentinel-2, precisa ser a pasta com terminação *.SAFE* para o sen2cor entender a ordem dos diretórios.
- seu computador precisa ter pelo menos 8gigas de RAM. Em alguns testes que fiz em máquinas mais fracas o sen2cor não exporta as imagens corrigidas.

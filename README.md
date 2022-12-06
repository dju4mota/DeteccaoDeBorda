# DeteccaoDeBorda

## Introdução do tópico 
Extremamente necessário na visão computacional. Com a detecção de borda, é possível reconhecer objetos 

## Algoritmo e Técnica
Existem diversas técnicas para resolver esse problema, o estudado aqui é atrávez da comparação de um pixel com seus vizinhos.

Para analisar a imagem, separamos um grupo de pixels, a vizinhança, e dentro dela teremos um pixel "principal". O pixel principal 
é então comparado com os seus vizinhos, obtendo a média da diferença entre ele e os vizinhos. Se a média for maior que o limiar 
escolhido, é considerado que existe uma borda. Esse processo é repetido para toda a imagem, marcando todos os pixels considerados
como borda

## Conclusões 

### Pontos Fortes
Esse algortimo consegue solucionar os casos mais simples, levando em consideração tamanho e cores, com uma implementação 
simples e fácil 


### Pontos Fracos
Com a implementação mais simples da técnica, ficamos bem suscetível a ruídos. Porém, existem outras técnias, usando a derivada por exemplo, que podemos utilizar dependendo da situação, assim como também podemos adicionar mais camadas de tratamento para corrigir esses problemas

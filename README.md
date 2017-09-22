---
title: Camada Física -  APS 5 - DTMF - Encoder e recepção
author: Elisa Malzoni e Bruna Kimura - elisamm@al.insper.edu.br e brunamk@al.insper.edu.br
date: Setembro - 2017
---

# Proj-2-DTMF
Projeto 2 Camada Física - 2017.2

## Geração dos tons

Cada tom foi gerado a partir da soma de duas ondas com frequências diferentes. Para tanto, usamos a fórmula *sen(wt)* para gerar a onda, sendo *w = 2πf* (f é uma das frequncias que compõe cada tom) e com o seno variando em função do tempo. A geração deste sinal está no arquivo [encoderDTMF.py](https://github.com/elisamalzoni/Proj-2-DTMF/blob/master/encoderDTMF.py) e o som tem um segundo de duração. A chamda da função de gerar os tons estão no arquivo [keypad.py](https://github.com/elisamalzoni/Proj-2-DTMF/blob/master/keypad.py), que é a interface do projeto.

## Frequências que compõem cada tom
|             |1209 Hz  |1336 Hz  |1477 Hz  |1633 Hz  |
|:-----------:|:-------:|:-------:|:-------:|:-------:|
|**697 Hz**   |1        |2        |3        |A        |
|**770 Hz**   |4        |5        |6        |B        |
|**852 Hz**   |7        |8        |9        |C        |
|**941 Hz**   |*        |0        |#        |D        |


## Tons Gerados e Captados

Os gráficos abaixo corresponde o sinal de cada um dos tons em função do tempo. A coluna da esquerda representa a soma dos senos das duas frequências utilizadas. Já nos gráficos da direita, primeiramente, ouviu-se o som de outro computador, e a partir disso, foi gerado o gráfico correspondente. Como é possível notar, apesar de semelhantes, ainda é possível ver várias interferências (ruídos) que modificam a onda gerada. A captação de som e a geração deste gráfico está no arquivo [decoderDTMF.py](https://github.com/elisamalzoni/Proj-2-DTMF/blob/master/decoderDTMF.py)

| Tecla | Gerado                  |Captado               |
|:-----:|-------------------------|----------------------|
|1      | ![1](img/1e.png)        |![1](img/1.png)       |
|2      | ![2](img/2e.png)        |![2](img/2.png)       |
|3      | ![3](img/3e.png)        |![3](img/3.png)       |
|4      | ![4](img/4e.png)        |![4](img/4.png)       |
|5      | ![5](img/5e.png)        |![5](img/5.png)       |
|6      | ![6](img/6e.png)        |![6](img/6.png)       |
|7      | ![7](img/7e.png)        |![7](img/7.png)       |
|8      | ![8](img/8e.png)        |![8](img/8.png)       |
|9      | ![9](img/9e.png)        |![9](img/9.png)       | 
|0      | ![0](img/0e.png)        |![0](img/0.png)       |
|A      | ![A](img/ae.png)        |![A](img/a.png)       |
|B      | ![B](img/be.png)        |![B](img/b.png)       |
|C      | ![C](img/ce.png)        |![C](img/c.png)       |
|D      | ![D](img/de.png)        |![D](img/d.png)       |
|*      | ![*](img/estrelae.png)  |![*](img/hash.png)    |
|#      | ![#](img/hashe.png)     |![#](img/estrela.png) |

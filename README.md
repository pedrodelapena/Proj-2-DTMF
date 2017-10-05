---
title: Camada Física -  APS 5 - DTMF - Encoder e recepção
author: Elisa Malzoni e Bruna Kimura - elisamm@al.insper.edu.br e brunamk@al.insper.edu.br
date: Setembro - 2017
---


# Proj-2-DTMF
Projeto 2 Camada Física - 2017.2
# Parte 2 - Decoder

| Tom   | Sinal Transmitido       |Sinal Captado         |
|:-----:|-------------------------|----------------------|
|1      | ![1](img/1d.png)        |![1](img/1f.png)      |
|2      | ![2](img/2d.png)        |![2](img/2f.png)      |
|3      | ![3](img/3d.png)        |![3](img/3f.png)      |
|4      | ![4](img/4d.png)        |![4](img/4f.png)      |
|5      | ![5](img/5d.png)        |![5](img/5f.png)      |
|6      | ![6](img/6d.png)        |![6](img/6f.png)      |
|7      | ![7](img/7d.png)        |![7](img/7f.png)      |
|8      | ![8](img/8d.png)        |![8](img/8f.png)      |
|9      | ![9](img/9d.png)        |![9](img/9f.png)      | 
|0      | ![0](img/0d.png)        |![0](img/0f.png)      |
|A      | ![A](img/azaod.png)       |![A](img/af.png)      |
|B      | ![B](img/bd.png)        |![B](img/bf.png)      |
|C      | ![C](img/cd.png)        |![C](img/cf.png)      |
|D      | ![D](img/dd.png)        |![D](img/df.png)      |
|*      | ![*](img/estrelad.png)  |![*](img/hashf.png)   |
|#      | ![#](img/hashd.png)     |![#](img/estrelaf.png)|


## Frequências enviadas e recebidas
| Tom   | Frequência Enviada (Hz) |Frequência Recebida (Hz)|
|:-----:|:-----------------------:|:----------------------:|
|1      |697, 1209                |697, 1209               |
|2      |697, 1336                |697, 1336               |
|3      |697, 1477                |697, 1477               |
|4      |770, 1209                |770, 1209               |
|5      |770, 1336                |770, 1336               |
|6      |770, 1477                |770, 1477               |
|7      |852, 1209                |852, 1209               |
|8      |852, 1336                |852, 1336               |
|9      |852, 1477                |852, 1477               | 
|0      |941, 1336                |941, 1336               |
|A      |697, 1633                |697, 1633               |
|B      |770, 1633                |770, 1633               |
|C      |852, 1633                |852, 1633               |
|D      |941, 1633                |941, 1633               |
|*      |941, 1209                |941, 1209               |
|#      |941, 1477                |941, 1477               |

## Justificativa dos tempos utilizados
A cada 1 segundo atualizamos gráfico e informações na interface (tom e frequências recebidos) conforme aúdio recebido, já para o sinal gerado são 2 segundos, assim o [decoderDTMF.py](https://github.com/elisamalzoni/Proj-2-DTMF/blob/master/decoderDTMF.py) conseguirá identificar. 

# Parte 1 - Encoder
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

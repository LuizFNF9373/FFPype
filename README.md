# FFPype v0.1.0

Automação de transcodificação de vídeos usando Python e FFmpeg

---

## Sobre

FFPY é uma ferramenta de linha de comando para automatizar a análise
e conversão de vídeos.

O projeto utiliza o FFprobe para extrair metadados dos vídeos,
processa essas informações em Python e executa o FFmpeg usando parâmetros
dinâmicos baseados nas características obtidas a partir do FFprobe.

O objetivo é evitar configurações manuais repetitivas e lidar com diferentes
combinações de FPS, resolução e bitrate.

---

## Origem

O FFPY nasceu durante testes de encode de vídeos em um ambiente
Android utilizando o FFmpeg no Termux.

O objetivo inicial era automatizar um processo que envolvia diversas
etapas manuais: identificar características do vídeo, escolher parâmetros
adequados e realizar a conversão mantendo compatibilidade entre diferentes
arquivos de mídia.

Durante os testes foram encontrados desafios relacionados a codecs,
containers, timestamps, encoders de hardware e diferenças entre implementações
do FFmpeg em smartphones sem root.

O projeto saiu de um conjunto de comandos experimentais para uma ferramenta
em Python capaz de analisar metadados via FFprobe e gerar comandos
dinâmicos para o FFmpeg.

O motivo do decode do codec de entrada ser realizado via software
está relacionado à ausência de zero-copy (mecanismo que evita cópias
desnecessárias entre componentes). No ambiente de testes, o caminho
utilizando decode e encode via hardware apresentou desempenho inferior
ao decode via software combinado com encode via hardware.

---

## Nome

FFPype é uma junção de FFmpeg, Python e Pipeline,
representando o fluxo automatizado de análise e transcodificação
de vídeos realizado pelo projeto.

---

## Estado atual

O projeto encontra-se em desenvolvimento.

A versão atual já suporta:
- Extração automática de metadados;
- Detecção de várias características do vídeo;
- Conversão automatizada;
- Processamento de múltiplos arquivos.

---

## Exemplo de uso

Coloque os vídeos de entrada no diretório "./videos/" e execute:

```bash
python ffpy.py
```

O FFPY irá:

- Verificar se existem vídeos;
- Executar o FFprobe;
- Gerar e analisar os metadados;
- Montar os parâmetros do FFmpeg;
- Realizar a conversão.

Os vídeos convertidos serão salvos em "./final-v/"

---

## Problemas conhecidos

Alguns dispositivos podem apresentar limitações relacionadas a:

- Encoders de hardware
- Integração com MediaCodec
- Geração de timestamps
- Compatibilidade de containers e codecs

**Em casos de erros e inconsistências pode ser necessário reconstruir
timestamps ou utilizar uma etapa intermediária de muxing.**

---

## Recursos

- Extração de metadados via FFprobe
- Leitura de informações em JSON
- Normalização de FPS
- Conversão automatizada via FFmpeg
- Processamento em lote de múltiplos vídeos

---

## Como funciona

Fluxo básico:

         Vídeo
           |
           v
        FFprobe
           |
           v
    JSON com metadados
           |
           v
 Python interpreta informações
           |
           v
  FFmpeg recebe parâmetros
          |
          v
    Vídeo convertido


---

## Requisitos

- Python 3.10+
- FFmpeg
- FFprobe

---

## Compatibilidade testada

Projeto testado com:

- Vídeos H.264
- Resoluções Full HD
- Diferentes taxas de FPS
- Arquivos provenientes de câmeras digitais

---

## Fontes das amostras

Foram utilizados vídeos provenientes de:

- Câmeras Sony
- Câmeras Panasonic
- Smartphones Android

## Próximos passos e melhorias

- Arquivo de configuração para preferências do usuário;
- Detecção automática de codec e container;
- Melhor estimativa de bitrate;
- Maior compatibilidade com diferentes formatos de vídeo;
- Melhorias gerais.
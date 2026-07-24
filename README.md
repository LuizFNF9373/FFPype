# FFPype v0.1.0

Automação de transcodificação de vídeos usando Python e FFmpeg

---

## Sobre

FFPype é uma ferramenta de linha de comando para automatizar a análise
e conversão de vídeos.

O projeto utiliza o FFprobe para extrair metadados dos vídeos,
processa essas informações em Python e executa o FFmpeg usando parâmetros
dinâmicos baseados nas características obtidas a partir do FFprobe.

O objetivo é evitar configurações manuais repetitivas e lidar com diferentes
combinações de FPS, resolução e bitrate.

---

## Licença

Este projeto é distribuído sob a licença MIT.

---

## Origem

O FFPype nasceu durante testes de encode de vídeos em um ambiente
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

O motivo pelo qual o decode do codec de entrada é realizado via software
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

## Requisitos

- Python 3.10+
- FFmpeg disponível no PATH do sistema
- FFprobe disponível no PATH do sistema

---

## Instalação

Clone o repositório:

```bash
git clone https://github.com/LuizFNF9373/FFPype.git
cd FFPype
```

Certifique-se de que o FFmpeg e o FFprobe estejam disponíveis no sistema:

```bash
ffmpeg -version
ffprobe -version
```

---

## Estrutura de diretórios

Os diretórios abaixo são criados automaticamente pelo FFPype na primeira execução, caso ainda não existam.

```text
FFPype/
├── videos/             # Vídeos de entrada
├── final-v/            # Vídeos convertidos
├── es/                 # Arquivos intermediários
│   ├── ffprobe-json/   # Diretório dos metadados em JSON
│   └── raw-stream/     # Diretório dos Streams brutos
├── ffpype.py           # Programa principal
└── README.md           # Readme
```

---

## Como funciona

Fluxo básico:

```text
Vídeo
  │
  ▼
FFprobe
  │
  ▼
Metadados (JSON)
  │
  ▼
Python
  │
  ▼
FFmpeg
  │
  ▼
Vídeo convertido
```

---

## Exemplo de uso

```bash
python ffpype.py
```

Na primeira execução, o FFPype cria automaticamente os diretórios necessários,
caso ainda não existam. Em seguida, coloque os vídeos de entrada em
"./videos/" e execute o programa novamente para iniciar a conversão.

O FFPype irá:

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

## Compatibilidade testada

Projeto testado com:

- Vídeos H.264
- Resoluções Full HD
- Diferentes taxas de FPS
- Arquivos de câmeras digitais

---

## Fontes das amostras do teste

Foram utilizados vídeos provenientes de:

- Câmeras Sony
- Câmeras Panasonic
- Smartphones Android

---

## Próximos passos e melhorias

- Arquivo de configuração para preferências do usuário;
- Detecção automática de codec e container;
- Melhor estimativa de bitrate;
- Maior compatibilidade com diferentes formatos de vídeo;
- Melhorias gerais.
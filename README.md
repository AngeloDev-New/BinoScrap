# Projeto de Day Trading com IA

Este projeto tem como objetivo desenvolver um sistema de day trading utilizando IA e probabilidade. O projeto faz uso do Selenium para automatizar o login no Binomo, capturar o canvas da página de gráficos e analisar as velas para identificar padrões e tendências. A longo prazo, o objetivo é construir uma IA que possa tomar decisões de trading baseadas em análises preditivas.

## Funcionalidades

- **Login Automatizado:** Utiliza o Selenium para realizar o login automático na plataforma Binomo.
- **Captura de Canvas:** Captura o canvas da página para análise dos gráficos de velas.
- **Análise de Velas:** Processa os dados capturados usando OpenCV para identificar padrões e gerar insights sobre o comportamento do mercado.
- **IA de Day Trading:** Desenvolve e treina uma IA para tomar decisões de trading baseadas em análises de dados.

## Requisitos

- Python 3.x
- Selenium
- OpenCV
- WebDriver para o navegador (ex: ChromeDriver para Google Chrome)

## Instalação

1. Clone este repositório:

    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd seu-repositorio
    ```

3. Instale as dependências necessárias:

    ```bash
    pip install -r requirements.txt
    ```

4. Baixe e coloque o WebDriver no mesmo diretório do seu script ou adicione-o ao PATH do sistema.

## Requisitos Adicionais

O projeto utiliza o OpenCV para processamento de imagem. Você pode instalar o OpenCV com o seguinte comando:

```bash
pip install opencv-python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from io import BytesIO
import mplfinance as mpf
from PIL import Image
import cv2
import json

# Função para gerar o gráfico com 10 velas e redimensionar a imagem
def plot_and_resize_candles(data):
    df = pd.DataFrame(data)
    df['created_at'] = pd.to_datetime(df['created_at'])
    df.set_index('created_at', inplace=True)

    market_colors = mpf.make_marketcolors(up='lightgray', down='black')
    style = mpf.make_mpf_style(base_mpf_style='charles', marketcolors=market_colors)

    fig, ax = plt.subplots(figsize=(8, 6))
    mpf.plot(df, type='candle', style=style, volume=False, ax=ax)

    ax.grid(False)
    ax.legend().set_visible(False)
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_ylabel('')
    ax.set_xticks([])
    ax.set_yticks([])

    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    buf = BytesIO()
    plt.savefig(buf, format='png', dpi=100, bbox_inches='tight', pad_inches=0)
    plt.close(fig)

    buf.seek(0)
    image = Image.open(buf)
    image_gray = image.convert('L')
    image_array = np.array(image_gray)

    image_resized = cv2.resize(image_array, (300, 300), interpolation=cv2.INTER_LINEAR)
    return image_resized

# Função para calcular a tendência com base nas 40 velas
def get_trend_and_image(data):
    # Gerar a imagem com base nas 10 primeiras velas
    image_resized = plot_and_resize_candles(data[:10])

    # Usar as 40 velas para calcular a linha de tendência
    df = pd.DataFrame(data)
    df['created_at'] = pd.to_datetime(df['created_at'])
    df.set_index('created_at', inplace=True)

    # Usar o preço de fechamento das velas para análise
    prices = df['close'].values.reshape(-1, 1)  # Usando as 40 velas

    # Usar a indexação como variável independente (x)
    x = np.arange(len(prices)).reshape(-1, 1)

    # Criar o modelo de regressão linear
    model = LinearRegression()
    model.fit(x, prices)

    # A inclinação da linha (coeficiente angular) nos dará o ângulo
    slope = model.coef_[0][0]

    # Determinar a tendência com base na inclinação da linha
    if slope > 0.1:
        trend = 2  # COMPRA
    elif slope < -0.1:
        trend = 1  # VENDA
    else:
        trend = 3  # INSTABILIDADE

    return image_resized, trend

# Exemplo de uso
if __name__ == "__main__":
    # Dicionário de entrada com 40 velas
    with open('./convs/itens.json','r') as itens:
        data = json.load(itens)
    data = data[40:80]
    # Chama a função para gerar a imagem e calcular a tendência
    image_resized, trend = get_trend_and_image(data)
    image_resized = plot_and_resize_candles(data)
    # Mostrar a imagem redimensionada
    plt.imshow(image_resized, cmap='gray')
    plt.axis('off')
    plt.show()

    # Imprimir a tendência
    trend_map = {1: "VENDA", 2: "COMPRA", 3: "INSTABILIDADE"}
    print(f"Tendência: {trend_map[trend]}")

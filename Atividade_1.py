import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox

# Dados
tempo = np.array([4, 8, 12, 16, 20, 24])
densidade_optica = np.array([0.011, 0.046, 0.162, 0.459, 0.961, 1.366])

# Função polinomial
def polinomial(x, a, b, c):
    return a * x**2 + b * x + c

# Ajuste da curva aos dados
params, covariance = curve_fit(polinomial, tempo[:9], densidade_optica[:9])

# Extrair os coeficientes do ajuste
a, b, c = params

# Configurar o gráfico
fig, ax = plt.subplots()

# Função para atualizar o gráfico com a hora desejada
def atualizar(text):
    hora_desejada = float(text)
    densidade_estimada = polinomial(hora_desejada, a, b, c)

    ax.clear()  # Limpar o gráfico
    ax.plot(tempo, densidade_optica, marker='o', linestyle='-', label="Dados")
    for i, txt in enumerate(densidade_optica):
        ax.annotate(f'{txt:.4f}', (tempo[i], densidade_optica[i]), textcoords="offset points", xytext=(0, 10), ha='center')
    ax.plot(tempo, polinomial(tempo, a, b, c), label="Curva Ajustada", color='red')
    ax.plot(hora_desejada, densidade_estimada, 'bo', label=f'Estimativa em {hora_desejada}h: {densidade_estimada:.4f}', markersize=8)
    ax.set_xlabel("Tempo (h)")
    ax.set_ylabel("Densidade Óptica")
    ax.set_title("Ajuste de Curva Polinomial")
    ax.grid(True)
    ax.legend()
    plt.draw()

# Caixa de texto para inserir a hora desejada
ax_hora = plt.axes([0.125, 0.9, 0.10, 0.05])
texto_hora = TextBox(ax_hora, 'Hora:', initial="4")
texto_hora.on_submit(atualizar)

atualizar("4")  # Para exibir o gráfico inicial com a hora 4

plt.show()

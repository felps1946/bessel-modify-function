import numpy as np
import matplotlib.pyplot as plt

# Definindo a função modificada de Bessel do 1º tipo
def I_v(v, x):
    sum_term = 0
    k = 0
    term = (x / 2)**v / np.math.factorial(v)  # Primeiro termo da série
    while term > 1e-10:  # Continue até que o termo seja pequeno o suficiente
        sum_term += term
        k += 1
        term = (x / 2)**(v + 2*k) / (np.math.factorial(k) * np.math.factorial(v + k))
    return sum_term


# Definindo o intervalo de x de 0 a 10
x = np.linspace(0, 10, 400)

# Definindo os índices n
v_values = [0, 1, 2]  # Você pode adicionar mais índices conforme necessário

# Criando os gráficos
plt.figure(figsize=(12, 6))

# Gráfico da função modificada de Bessel do 1º tipo
plt.subplot(1, 2, 1)
for v in v_values:
    plt.plot(x, [I_v(v, xi) for xi in x], label=f'I_{v}(x)')
plt.title('Funções Modificadas de Bessel do 1º Tipo')
plt.xlabel('x')
plt.xlim(0, 6)  # Definindo os limites do eixo x
plt.ylabel('I_n(x)')
plt.ylim(0, 10)  # Definindo os limites do eixo y
plt.legend()
plt.grid()


# Exibindo os gráficos
plt.tight_layout()
plt.show()

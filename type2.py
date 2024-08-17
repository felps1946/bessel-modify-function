import numpy as np
import matplotlib.pyplot as plt

def K_v(v, x, n_terms=100):
    if x == 0:
        return np.inf  # K_v(0) é infinito para v >= 0
    sum_kv = 0
    for n in range(n_terms):
        term = ((-1)**n) * (x/2)**(2*n + v) / (np.prod(np.arange(1, n + 1)) * np.prod(np.arange(1, n + v + 1)))
        sum_kv += term
    return (np.pi / (2 * np.sin(np.pi * v))) * sum_kv

x = np.linspace(0.01, 10, 400)

v_values = [0, 1, 2] 

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)  
for v in v_values:
    plt.plot(x, [K_v(v, xi) for xi in x], label=f'K_{v}(x)')
plt.title('Funções Modificadas de Bessel do 2º Tipo')
plt.xlabel('x')
plt.xlim(0, 6)
plt.ylabel('K_n(x)')
plt.ylim(0, 10)  
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()

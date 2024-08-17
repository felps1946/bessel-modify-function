import numpy as np
import matplotlib.pyplot as plt
from scipy.special import kv

x = np.linspace(0.01, 10, 100)  
v_values = [0, 1, 2]

plt.figure(figsize=(10, 6))
for v in v_values:
    plt.plot(x, kv(v, x), label=f'K_{v}(x)')

plt.title('Funções Modificadas de Bessel do 2º Tipo')
plt.xlabel('x')
plt.xlim(0, 4)  
plt.ylabel('K_v(x)')
plt.ylim(0, 3.5)
plt.legend()
plt.grid()
plt.show()

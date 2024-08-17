import numpy as np
import matplotlib.pyplot as plt

def I_v(v, x):
    sum_term = 0
    k = 0
    term = (x / 2)**v / np.math.factorial(v)  
    while term > 1e-10: 
        sum_term += term
        k += 1
        term = (x / 2)**(v + 2*k) / (np.math.factorial(k) * np.math.factorial(v + k))
    return sum_term
    
x = np.linspace(0, 10, 400)

v_values = [0, 1, 2]

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)

for v in v_values:
    plt.plot(x, [I_v(v, xi) for xi in x], label=f'I_{v}(x)')
plt.title('Funções Modificadas de Bessel do 1º Tipo')
plt.xlabel('x')
plt.xlim(0, 6)  
plt.ylabel('I_n(x)')
plt.ylim(0, 10)
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()

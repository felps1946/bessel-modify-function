import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma

def K_v(v, x):
    if np.sin(v * np.pi) == 0:
        raise ValueError("K_v is undefined for integer values of v due to division by zero.")
    
    sum_term1 = 0
    sum_term2 = 0
    k = 0
    
    term1 = (x / 2)**(2 * k - v) / (gamma(k + 1) * gamma(k - v + 1))
    while k < 100:  
        if k >= v: 
            sum_term1 += term1
        k += 1
        term1 = (x / 2)**(2 * k - v) / (gamma(k + 1) * gamma(k - v + 1))
    
    k = 0  

    term2 = (x / 2)**(2 * k + v) / (gamma(k + 1) * gamma(k + v + 1))
    while k < 100: 
        sum_term2 += term2
        k += 1
        term2 = (x / 2)**(2 * k + v) / (gamma(k + 1) * gamma(k + v + 1))
    
    return (np.pi / (2 * np.sin(v * np.pi))) * (sum_term1 - sum_term2)


x = np.linspace(0.1, 10, 400)  

v_values = [0.5, 1.5, 2.5]


plt.figure(figsize=(12, 6))


plt.subplot(1, 2, 1)
for v in v_values:
    plt.plot(x, [K_v(v, xi) for xi in x], label=f'K_{v}(x)')
plt.title('Funções Modificadas de Bessel do Segundo Tipo')
plt.xlabel('x')
plt.xlim(0, 10) 
plt.ylabel('K_v(x)')
plt.ylim(0, 10)  
plt.legend()
plt.grid()


plt.tight_layout()
plt.show()

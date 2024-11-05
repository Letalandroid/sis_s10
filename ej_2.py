import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x = sp.symbols('x')
f_derivada = sp.sin(sp.sqrt(sp.E**2 + sp.pi)/2)
derivada_result = sp.diff(f_derivada, x) # 0 por ser constante

f_integral = (sp.pi * sp.sin(sp.sqrt(x)) * sp.exp(sp.sqrt(x))) / sp.sqrt(x)
integral_result = sp.integrate(f_integral, x)

derivada_value = float(derivada_result)
f_integral_lambdified = sp.lambdify(x, integral_result, 'numpy')

x_vals = np.linspace(0.01, 10, 400)
y_integral_vals = f_integral_lambdified(x_vals)

plt.figure(figsize=(12, 8))
plt.axhline(y=derivada_value, color='red', linestyle='--', label='Derivada: 0')
plt.plot(x_vals, y_integral_vals, label=r'$\int \frac{\pi \sin(\sqrt{x}) e^{\sqrt{x}}}{\sqrt{x}} \, dx$', color='blue')

plt.title("Derivada e Integral")
plt.xlabel("x")
plt.ylabel("y")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.grid(True)

plt.show()
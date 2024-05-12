import matplotlib.pyplot as plt
import Statistik as s
import numpy
df = s.csv
ma = max(df['Satzlänge'])
mi = min(df['Satzlänge'])
print(numpy.std(df['Satzlänge']))
print(numpy.mean(df['Satzlänge']))
#Erstellung Plot für Nachweis Normalverteilung
plt.hist(s.csv['Satzlänge'], density=True, bins=25)
mean = numpy.mean(df['Satzlänge'])
std = numpy.std(df['Satzlänge'])
x = numpy.linspace(mean - 3*std, mean + 3*std, 100)
plt.plot(x, numpy.exp(-x**2 / 2) / numpy.sqrt(2*numpy.pi), linewidth=2, color='r')
plt.text(0, 0.4, 'p-value = %.8f' % s.p)

plt.xlabel('Data')
plt.ylabel('Density')
plt.title('Normality Test')
plt.show()
'''Gauss-Funktion für Standardnormalverteilung:
f(x) = (1 / (σ * √(2*π))) * e^(-1/2 * ((x - μ) / σ)^2)
Wenn μ=0 und σ=1:
f(x) = (1 / (√(2*π))) * e^(-1/2 * x^2)
Diese Funktion erreicht ihr Maximum bei x=0.'''

import numpy
from scipy.stats import chi2_contingency
import pandas

'''to-do:
- signifikanzniveau? 0.05?
- t-test? lin. regression? welche stat tests kann ich machen?

'''

#H0: Fragesätze kommen in suspense sätzen weniger häufig vor als in nicht-suspense sätzen
#H0: Die Länge der Sätze variiert zwischen suspense und nicht-suspense Sätzen nicht.

#Daten einbinden
csv = pandas.read_csv('annotated csv/python_edit.csv')

#Kontingenztabelle

con = pandas.crosstab(csv['Suspense'], csv['Fragesatz'])

#chi2test
#p=0.05; k=3,84 -> kritischer Wert aus der Chi Quadrat Verteilungstabelle bei df=1 und signifikanzniveau=0.95

chi2, p, _, _= chi2_contingency(con)

print('chi2: ', chi2)
print('p: ', p)

#Fortführung: Kontingenzkoeffizient

#Berechnung n
n= numpy.sum(con.values)
rows, cols = con.shape

#Berechnung Kontingenzkoeffizient
k = numpy.sqrt(chi2/(n*(min(rows, cols)-1)))
print('k: ',k)
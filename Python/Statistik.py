import numpy
from scipy.stats import chi2_contingency
from scipy.stats.contingency import association
import pandas

'''to-do:
- signifikanzniveau? 0.05?
- t-test? lin. regression? welche stat tests kann ich machen?

'''

#H0: Fragesätze kommen in suspense sätzen weniger häufig vor als in nicht-suspense sätzen
#H0: Die Länge der Sätze variiert zwischen suspense und nicht-suspense Sätzen nicht.

#Daten einbinden
df = pandas.read_csv('annotated csv/python_edit.csv')
csv = df.drop(df[df.Suspense == '-'].index)

#Kontingenztabelle
def chi2extended(Spalte1, Spalte2):
    #Kontingenztabelle
    con = pandas.crosstab(csv[Spalte1], csv[Spalte2])
    #chi2test
    chi2, p, _, _ = chi2_contingency(con)
    # Fortführung: Kontingenzkoeffizient/Cramers V
    pearson = association(con, method="pearson")
    cramers = association(con, method="cramer")
    return pandas.Series([chi2, p, pearson, cramers], index=['chi2', 'pvalue', 'pearson', 'cramers'])


'''    
con = pandas.crosstab(csv['Suspense'], csv['Fragesatz'])
print(con)

#chi2test
#p=0.05; k=3,84 -> kritischer Wert aus der Chi Quadrat Verteilungstabelle bei df=1 und signifikanzniveau=0.95

chi2, p, _, _= chi2_contingency(con)

print('chi2: ', chi2)
print('p: ', p)

#Fortführung: Kontingenzkoeffizient/Cramers V
print(association(con, method="pearson"))
print(association(con, method="cramer"))
'''
#Für alle Erzählungen
print(chi2extended('Suspense', 'Fragesatz'))

#Ein Schritt weiter gedacht: auf einzelne Erzählungen angewendet

stories = csv.groupby('Titel')
def chi2extendedgroup(group):
    #Kontingenztabelle
    con = pandas.crosstab(group['Suspense'].values, group['Fragesatz'].values)
    #chi2Test
    chi2, p, _, _ = chi2_contingency(con)
    # Fortführung: Kontingenzkoeffizient/Cramers V
    pearson = association(con, method="pearson")
    cramers = association(con, method="cramer")
    return pandas.Series([chi2, p, pearson, cramers], index=['chi2', 'pvalue', 'pearson', 'cramers'])

print(stories.apply(chi2extendedgroup))



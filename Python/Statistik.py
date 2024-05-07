import numpy
from scipy.stats import chi2_contingency
from scipy.stats.contingency import association
from scipy.stats import ttest_ind
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
def chi2extended(Spalte1, Spalte2, df):
    #Kontingenztabelle
    con = pandas.crosstab(df[Spalte1], df[Spalte2])
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
print(chi2extended('Suspense', 'Fragesatz', csv))

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
#Für jede Erzählung einzeln
print(stories.apply(chi2extendedgroup))

#t-test für die Länge der Sätze

def ttest(df):
    s = df[df['Suspense']== '1']['Satzlänge']
    nos=df[df['Suspense']=='0']['Satzlänge']
    # Berechnung Mittelwerte
    ms = s.mean()
    mnos = nos.mean()
    #Standardabweichung
    sds=s.std()
    sdnos=nos.std()
    #unabhängiger ttest/zweistichproben ttest
    #t, p= ttest_ind(s, nos)
    t = ttest_ind(nos, s)

    #return pandas.Series([p, t, df], index=['pvalue', 't-test', 'freiheitsgrade'])
    return t, ms, mnos, sds, sdnos

print(ttest(csv))
#mit einem wert von -2 -> in der gruppe S=1 um ca 2 standardabweichungen geringer als bei S=0
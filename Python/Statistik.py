import math
from scipy.stats import chi2_contingency
from scipy.stats.contingency import association
from scipy.stats import mannwhitneyu
from scipy.stats import normaltest
from scipy.stats import pearsonr
import pandas

#Daten einbinden
df = pandas.read_csv('annotated csv/python_edit.csv')
df_cg = pandas.read_csv('annotated csv/python_edit_cg.csv')
#Es werden Daten ausgelassen, die für die Analyse nicht von Bedeutung sind, z. B. die Sprechernamen im "Der Fremde", da hierdurch das Ergbnis verfälscht wird.
csv = df.drop(df[df.Suspense == '-'].index)
csv_cg = df_cg.drop(df_cg[df_cg.Suspense == '-'].index)
bigmomma = pandas.concat([csv, csv_cg], axis=0)

##Test ob Daten normalverteilt
#https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.normaltest.html -> H0 des Tests immer, dass Normalverteilung vorherrscht
#d.h. wenn p<0.05, dass keine gauss verteilung vorhanden
def normal(df, column):
    stat, p = normaltest(df[column])
    return pandas.Series([p], index=['p-Wert'])

print('\n\nErgebnis Test Normalverteilung (für die Länge der Sätze) Gruppe A:\n')
print(normal(csv, 'Satzlänge'))
print('\n\nErgebnis Test Normalverteilung (für die Länge der Sätze) Gruppe B:\n')
print(normal(csv_cg, 'Satzlänge'))

#########################################################################################

#H01: Fragesätze kommen in suspense sätzen genauso häufig vor wie in nicht-suspense sätzen
def chi2extended(df):
    #Kontingenztabelle
    con = pandas.crosstab(df['Suspense'], df['Fragesatz'])
    #chi2test
    chi2, p, _, _ = chi2_contingency(con)
    # Fortführung: Kontingenzkoeffizient
    pearson = association(con, method="pearson")
    #cramers = association(con, method="cramer")
    return pandas.Series([chi2, p, pearson], index=['chi2', 'pvalue', 'Kontingenzkoeffizient'])


#Für alle Erzählungen
print('\n\nErgebnis H01 für Gruppe A (auf alle Erzählungen angewendet):\n')
print(chi2extended(csv))
#Für alle Erzählungen Vergleichsgruppe
print('\n\nErgebnis H01 für Gruppe B (auf alle Erzählungen angewendet):\n')
print(chi2extended(csv_cg))

#Ein Schritt weiter gedacht: auf einzelne Erzählungen angewendet
stories = csv.groupby('Titel')
stories_cg = csv_cg.groupby('Titel')

#Für jede Erzählung einzeln
print('\n\nErgebnis H01 für Gruppe A (auf einzelne Erzählungen angewendet):\n')
print(stories.apply(chi2extended))
print('\n\nErgebnis H01 für Gruppe B (auf einzelne Erzählungen angewendet):\n')
print(stories_cg.apply(chi2extended))


######################################################


#H02: Die Länge der Sätze variiert zwischen suspense und nicht-suspense Sätzen nicht.

def whitney(df):
    s = df[df['Suspense']== '1']['Satzlänge']
    nos = df[df['Suspense']=='0']['Satzlänge']
    #U-Test
    U, p = mannwhitneyu(nos, s, alternative='two-sided')
    #von https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mannwhitneyu.html
    #Berechnung der Effektstärke
    nx, ny = len(s), len(nos)
    N = nx + ny
    z = (U - nx * ny / 2 + 0.5) / math.sqrt(nx * ny * (N + 1) / 12)
    r=abs(z/math.sqrt(nx+ny))

    return pandas.Series([p, r, z], index=['p-Wert',"r","z"])


print('\n\nErgebnis H02 für Gruppe A (auf alle Erzählungen angewendet):\n')
print(whitney(csv))
print('\n\nErgebnis H02 für Gruppe B (auf alle Erzählungen angewendet):\n')
print(whitney(csv_cg))

print('\n\nErgebnis H02 für Gruppe A (auf einzelne Erzählungen angewendet):\n')
print(stories.apply(whitney))
print('\n\nErgebnis H02 für Gruppe B (auf einzelne Erzählungen angewendet):\n')
print(stories_cg.apply(whitney))

print('\n\nErgebnis für GruppeA+GruppeB')
print(whitney(bigmomma))
print(chi2extended(bigmomma))
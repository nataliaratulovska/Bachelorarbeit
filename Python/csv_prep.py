import pandas

#Einlesen der catma csv (hier wurden bereits unbrauchbare spalten entfernt)
#Probleme: die catma datei hatte keine Titelzeile, alles war durcheinander, musste ich händisch hinzufügen und die unbrauchbaren splaten auch entfernt)
df=pandas.read_csv('annotated csv/catma_editedutf8.csv', sep=';')

#sortieren nach Titel und Position des Satzes
df=df.sort_values(by=['Titel', 'Position1'])

#Entfernen der überschüssigen Spalten
rem = ['Position1', 'Position2']
df = df.drop(rem, axis=1)

#Bearbeiten der "Suspense" Spalte, hier hat Catma ein random Slah eingebaut und ich finds doof
def noslashes(text):
    return text.replace("/","")
df['Suspense']=df['Suspense'].apply(noslashes)

#Hinzufügen von ID
df.insert(0, 'id', range(len(df)))

#Hinzufügen leerer Spalten für die späteren Untersuchungen, hier Fragesatz, Ellipse, kurzer/simpler Satz (Basisstruktur) und Satzlänge
#ich glaube am einfachsten ist es wenn ich mich nur auf die Länge der Sätze festlege (Wörter pro Satz), und vergleiche ob diese in suspense Sätzen abnimmt
df['Fragesatz']=''
df['Satzlänge']=''

#Befüllen der Fragesatz Spalte
def isquestion(text):
    if '?' in text:
        return 1
    else:
        return 0
df['Fragesatz']=df['Satz'].apply(isquestion)

#Befüllen der Länge Spalte
def length(text):
    return len(text.split())
df['Satzlänge']=df['Satz'].apply(length)



#Speichern der bearbeiteten Datei
df.to_csv('annotated csv/python_edit.csv', sep=',', index=False)


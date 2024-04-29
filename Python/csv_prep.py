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

#Speichern der bearbeiteten Datei
df.to_csv('annotated csv/python_edit.csv', sep=',', index=False)


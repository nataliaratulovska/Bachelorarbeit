import pandas
#Einlesen der catma csv (hier wurden bereits unbrauchbare spalten entfernt)
#Probleme: die catma datei hatte keine Titelzeile, alles war durcheinander, musste ich händisch hinzufügen und die unbrauchbaren splaten auch entfernt)
df=pandas.read_csv('annotated csv/catma_editedutf8.csv', sep=';')

#sortieren nach Titel und Position des Satzes
df=df.sort_values(by=['Titel', 'Position1'])

rem = ['Position1', 'Position2']

df = df.drop(rem, axis=1)

df.to_csv('annotated csv/python_edit.csv', sep=';', index=False)


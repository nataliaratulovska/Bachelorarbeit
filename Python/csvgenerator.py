#Hier werden die csv dateien erstellt, welche im zweiten Schritt annotiert werden

import csv
import nltk
if __name__ == "__main__":
    fieldnames = ['Titel ID', 'Titel', 'Satz', 'Suspense']

    #Anmerkung: die Annotationen werden später händisch hinzugefügt, warum nicht mit externer software?
    #zu anstrengend... datentypen sind nicht die die ich haben will und so kann ich die csv individuell anpassen, geht flotter so

    #auslesen der txt dateien
    path_list = ['txt/locarno.txt', 'txt/usher.txt', 'txt/fremde.txt']
    def sentence_tokenize(filepath):
        title = open(filepath, 'r', encoding='utf-8').read()
        rep = title.replace('\n', ' ')
        tokenize = nltk.sent_tokenize(rep, language='german')
        return tokenize

    sent_token_list = []

    for path in path_list:
        sent_token_list.append(sentence_tokenize(path))

    '''new_stl = []
    for remove in sent_token_list:
        new = remove.replace('\n', ' ')
        new_stl.append(new)'''

    with open('Satzliste.csv', 'w', newline='', encoding='utf-8') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(fieldnames)

        for index, titel in enumerate(sent_token_list, start=1):
            for sentence in titel:
                titelid = str(index)
                if index==1:
                    csv_writer.writerow([titelid, 'Das Bettelweib von Locarno', sentence])
                elif index==2:
                    csv_writer.writerow([titelid, 'Der Untergang des Hauses Usher', sentence])
                else:
                    csv_writer.writerow([titelid, 'Der Fremde', sentence])


#Wichtige Fragen: wie genau will ich Sätze aufteilen?? Probleme: Semikolon, doppelpunkte, \n, wörtliche Rede (die nicht mit Apostrophen gekennzeichnet ist)
#will ich bei der fremde die namen ausklammern? -> kann ergebnis verfälschen
#jeder satz seine eigene ID? Für Referenzierung innerhalb der Arbeit evtl wichtig?
#bei fremde.txt ist dauernd dieser blöde bindestich, der kommt weg! >:-/
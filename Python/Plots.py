import matplotlib.pyplot as plt
import pandas
import numpy as np
from scipy.interpolate import make_interp_spline
from scipy.signal import find_peaks

#Daten einbinden
df = pandas.read_csv('annotated csv/python_edit.csv')
df_cg = pandas.read_csv('annotated csv/python_edit_cg.csv')
#Es werden Daten ausgelassen, die für die Analyse nicht von Bedeutung sind, z. B. die Sprechernamen im "Der Fremde", da hierdurch das Ergbnis verfälscht wird.
#csv = df.drop(df[df.Suspense == '-'].index)
#csv_cg = df_cg.drop(df_cg[df_cg.Suspense == '-'].index)
def dropminus(df):
    return df.drop(df[df.Suspense == '-'].index)

#Das Bettelweib von Locarno
#g1 = df[:33]
g1 = dropminus(df[:33])
#Der Fremde
g2 = dropminus(df[34:217])
#Der Untergang des Hauses Usher
g3 = dropminus(df[219:])
#Hauptgruppe
gall = dropminus(df)

########################################################################################
'''
#Verlauf der suspense, wichtig zur Veranschaulichung der Suspense Kurven
def suspensecurve(df,bin):

    x = np.array(df['id'],dtype=float)
    y = np.array(df['Suspense'], dtype=float)

    #nutzung von bins -> sätze werden zusammengenommen und durchschintt suspense wird berechnet
    # so wird der Verlauf der Suspense besser sichtbar, da aus kategorischer variable ('Suspense') eine numerische gemacht wird

    new_x = []
    new_y = []
    for i in range(0, len(x), bin):

        x_bin = x[i:i + bin]
        y_bin = y[i:i + bin]

        #neue Werte, berechnung mittelwert der bins
        new_x.append(x_bin.mean())
        new_y.append(y_bin.mean())


    new_x = np.array(new_x)
    new_y = np.array(new_y)

    #Ausglätten der Kurve durch spline interpolation
    x_smooth = np.linspace(new_x.min(), new_x.max(), 300)
    spline = make_interp_spline(new_x, new_y, k=3)
    y_smooth = spline(x_smooth)

    #Peaks finden
    peaks, _ = find_peaks(y_smooth, height=0)
    plt.plot(x_smooth[peaks], y_smooth[peaks], "x", label='Peaks')
    for i, peak in enumerate(peaks, start=1):
        plt.annotate(f'Peak {i}',
                     (x_smooth[peak], y_smooth[peak]),
                     textcoords="offset points",
                     xytext=(0, 10),
                     ha='center')

    #Plotting
    plt.plot(x_smooth, y_smooth, linestyle='-')
    plt.xlabel('Satz ID')
    plt.ylabel('Durchschnittswert der Suspense ')
    plt.ylim(0, 1.2)
    plt.title('Suspenseverlauf in der Erzählung '+df['Titel'].tolist()[1], pad=20)
    plt.show()

#da erzählungen alle verschieden lang sind und ich ca gleiche verzerrung haben will, ist die bin zahl rational zu anzahl instanzen
print(suspensecurve(g1, 3))
print(suspensecurve(g2, 17))
print(suspensecurve(g3, 26))
'''
########################################################
'''
#Plots für Fragesätze
#Zählen der Fragesätze in suspense und nicht suspense sätzen
def ycounter(df):
    s0_f1 = len(df[(df['Suspense'] == '0') & (df['Fragesatz'] == 1)])
    s1_f1 = len(df[(df['Suspense'] == '1') & (df['Fragesatz'] == 1)])
    return [s0_f1, s1_f1]

s0_f1 = [ycounter(g1)[0],ycounter(g2)[0],ycounter(g3)[0],ycounter(gall)[0]]

s1_f1 = [ycounter(g1)[1],ycounter(g2)[1],ycounter(g3)[1],ycounter(gall)[1]]

#beschriftung und xachse
labels = ['Das Bettelweib\nvon Locarno', 'Der Fremde', 'Der Untergang\ndes Hauses Usher', 'Gesamtgruppe']
x = np.arange(len(labels))
width = 0.35

#diagramm
fig, ax = plt.subplots()
balken1 = ax.bar(x - width/2, s0_f1, width, label='kein Suspensesatz', color='mediumseagreen')
balken2 = ax.bar(x + width/2, s1_f1, width, label='Suspensesatz', color='crimson')
ax.set_ylabel('Anzahl der Fragesätze')
ax.set_title('Verteilung der Fragesätze in Suspense und nicht-Suspense Sätzen', pad=20)
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

#beschriftung Balken
def add_labels(balken):
    for b in balken:
        height = b.get_height()
        ax.annotate('{}'.format(height),
                    xy=(b.get_x() + b.get_width() / 2, height),
                    xytext=(0, 1),
                    textcoords="offset points",
                    ha='center', va='bottom')
add_labels(balken1)
add_labels(balken2)

plt.tight_layout()
plt.show()
'''
#######################################################

#Plots für Satzlänge
#berechnen der Satzdurchschnittslänge
def ymean(df):
    s0=df[(df['Suspense'] == '0')]
    s1=df[(df['Suspense'] == '1')]
    mean_s0 = s0['Satzlänge'].mean()
    mean_s1 = s1['Satzlänge'].mean()
    return [round(mean_s0,2), round(mean_s1,2)]

mean_s0 = [ymean(g1)[0],ymean(g2)[0],ymean(g3)[0],ymean(gall)[0]]

mean_s1 = [ymean(g1)[1],ymean(g2)[1],ymean(g3)[1],ymean(gall)[1]]


#beschriftung und xachse
labels = ['Das Bettelweib\nvon Locarno', 'Der Fremde', 'Der Untergang\ndes Hauses Usher', 'Gesamtgruppe']
x = np.arange(len(labels))
width = 0.35

#diagramm
fig, ax = plt.subplots()
balken1 = ax.bar(x - width/2, mean_s0, width, label='kein Suspensesatz', color='mediumseagreen')
balken2 = ax.bar(x + width/2, mean_s1, width, label='Suspensesatz', color='crimson')
ax.set_ylabel('Satzlänge in gemessen nach Wortanzahl')
ax.set_title('Durchschnittliche Satzlänge in Suspense und nicht-Suspense Sätzen', pad=20)
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

#beschriftung Balken
def add_labels(balken):
    for b in balken:
        height = b.get_height()
        ax.annotate('{}'.format(height),
                    xy=(b.get_x() + b.get_width() / 2, height),
                    xytext=(0, 1),
                    textcoords="offset points",
                    ha='center', va='bottom')
add_labels(balken1)
add_labels(balken2)

plt.tight_layout()
plt.show()
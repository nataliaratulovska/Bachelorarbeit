import matplotlib.pyplot as plt
import pandas
import numpy as np
from scipy.interpolate import make_interp_spline

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

########################################################################################

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

    #Plotting
    plt.plot(x_smooth, y_smooth, linestyle='-')
    plt.xlabel('Satz ID')
    plt.ylabel('Dichte Suspense')
    plt.ylim(-0.2, 1.2)
    plt.title('Suspenseverlauf in der Erzählung '+df['Titel'].tolist()[1], pad=20)
    plt.show()

#da erzählungen alle verschieden lang sind und ich ca gleiche verzerrung haben will, ist die bin zahl rational zu anzahl instanzen
print(suspensecurve(g1, 5))
print(suspensecurve(g2, 28))
print(suspensecurve(g3, 42))
import sqlite3
import numpy as np
import matplotlib.pyplot as plt


    
def fetch():
    conn = sqlite3.connect('heart.db')
    c = conn.cursor()
    pulso = c.execute("SELECT pulso FROM sensor").fetchall()
    conn.commit()
    conn.close()
    return pulso

def estadistica(data):
    result = np.asanyarray([data])
    print(result.mean())
    print(result.min())
    print(result.max())
    print(result.std())
    
    
def show(data):
    fig = plt.figure()
    fig.suptitle('Evolucion Ritmo Cardiaco')
    ax = fig.add_subplot()
    ax.set_xlabel('Indice')
    ax.set_ylabel('Pulso')
    ax.plot(data)


def regiones(data):
    result = np.asanyarray([data])
    medio = result.mean()
    estandar = result.std()
    
    #Definiendo listas pulso,indice
    x1,y1,x2,y2,x3,y3 = [],[],[],[],[],[]
    
    for i in range(len(data)):
        if data[i] <= (medio-estandar):
            x1.append(i)
            y1.append(data[i])
    
    
    for i in range(len(data)):
        if data[i] >= (medio+estandar):
            x2.append(i)
            y2.append(data[i])
    
    
    for i in range(len(data)):
        if data[i] >(medio-estandar)and data[i] <(medio+estandar):
            y3.append(data[i])
            x3.append(i)
    
    #Grafico
    fig = plt.figure(figsize=(10,8))
    fig.suptitle('Datos durante el Partido',fontsize=17)
    
    ax1 = fig.add_subplot(1,3,1)
    ax2 = fig.add_subplot(1,3,2)
    ax3 = fig.add_subplot(1,3,3)
    
    ax1.scatter(y1,x1,c='darkred',marker='.',label='Aburrida')
    ax2.scatter(y2,x2,c='#90EE90',marker='.',label='Enganchada')
    ax3.scatter(y3,x3,c='blue',marker='.',label='Entusiasmada')
    
    ax1.legend(fontsize=9,shadow=True,title='Region',loc='upper center',title_fontsize=11)
    ax2.legend(fontsize=9,shadow=True,title='Region',loc='upper center',title_fontsize=11)
    ax3.legend(fontsize=9,shadow=True,title='Region',loc='upper center',title_fontsize=11)
    
    #Eje x
    ax1.set_xlabel('Pulso')
    ax2.set_xlabel('Pulso')
    ax3.set_xlabel('Pulso')
    
    #Eje y
    ax1.set_ylabel('Indice')
  
    #Color fondo
    ax1.set_facecolor('bisque')
    ax2.set_facecolor('bisque')
    ax3.set_facecolor('bisque')
    
    plt.show()
  
    
if __name__ == '__main__':
    data = fetch()
    estadistica(data)
    show(data)
    regiones(data)
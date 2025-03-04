import pandas as pd
import os

def get_reporte(resultados, dominio):
    save_dir = resultados[0].save_dir
    ruta_img = save_dir + "\\" + dominio + ".jpg"
    directorio_script = os.path.dirname(__file__)
    
    ruta_etiquetas = directorio_script + "\\etiquetas.txt"
    df_etiquetas = pd.read_csv(ruta_etiquetas, header=None)
    
    #Ruta etiquetas detectadas
    ruta_labels = directorio_script + "\\" + save_dir + "\\labels\\" + dominio + ".txt"
    
    # Componentes detectados
    df_detectados = pd.read_csv(ruta_labels, sep='\s+', header=None, index_col=0)
    
    # Detectados
    detectados = []
    for indice, fila in df_detectados.iterrows():
        detectados.append(df_etiquetas.loc[indice, 0])

    # No detectados
    no_detectados = []
    for indice, fila in df_etiquetas.iterrows():
        if indice not in df_detectados.index:
            no_detectados.append(fila[0])
    
    return detectados, no_detectados, ruta_img

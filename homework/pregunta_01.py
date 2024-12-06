# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""
import pandas as pd
import os


def pregunta_01():
    #La idea es crear un dataframe y unir los archivos
    #segun su sentimiento

    #crear el dataframe
    data_tren = pd.DataFrame(columns=['phrase', 'target'])
    sentimientos=['positive', 'negative', 'neutral']
    for sentimiento in sentimientos:
        #leer los archivos
        directorio="input/train/"+sentimiento
        # Listar archivos y carpetas
        for nombre in os.listdir(directorio):
            ruta_completa = os.path.join(directorio, nombre)
            with open(ruta_completa) as f:
                text = f.read()
                data_tren = pd.concat([data_tren, pd.DataFrame({'phrase': [text], 'target': [sentimiento]})], ignore_index=True)
            
    #guardar el dataframe
    data_tren.to_csv('files/output/train_dataset.csv', index=False)

    #crear el dataframe
    data_test = pd.DataFrame(columns=['phrase', 'target'])
    sentimientos=['positive', 'negative', 'neutral']
    for sentimiento in sentimientos:
        #leer los archivos
        directorio="input/test/"+sentimiento
        # Listar archivos y carpetas
        for nombre in os.listdir(directorio):
            ruta_completa = os.path.join(directorio, nombre)
            with open(ruta_completa) as f:
                text = f.read()
                data_test = pd.concat([data_test, pd.DataFrame({'phrase': [text], 'target': [sentimiento]})], ignore_index=True)
            
    #guardar el dataframe
    data_test.to_csv('files/output/test_dataset.csv', index=False)

    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """
pregunta_01()
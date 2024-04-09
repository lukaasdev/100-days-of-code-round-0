import numpy as np

def calculate(list):
    ERROR_MSG = "List must contain nine numbers."
    calculations = {}
    
    # Gestion des erreurs
    if len(list) != 9:
        raise ValueError(ERROR_MSG)

    # Trransformer la liste en matrice 3x3
    matrix = np.reshape(list, (3, 3))

    # Calcul de la moyenne
    mean_flattened = np.mean(list) # mean aplatie
    mean_axis_0 = (np.mean(matrix, axis=0)).tolist() # mean par colonne
    mean_axis_1 = (np.mean(matrix, axis=1)).tolist() # mean par ligne
    calculations['mean'] = [mean_axis_0, mean_axis_1, mean_flattened]

    # Calcul de la variance
    var_flattened = np.var(list) # var aplatie
    var_axis_0 = (np.var(matrix, axis=0)).tolist() # var par colonne
    var_axis_1 = (np.var(matrix, axis=1)).tolist() # var par ligne
    calculations['variance'] = [var_axis_0, var_axis_1, var_flattened]

    # Calcul de l'écart-type
    std_flattened = np.std(list) # std aplatie
    std_axis_0 = (np.std(matrix, axis=0)).tolist() # std par colonne
    std_axis_1 = (np.std(matrix, axis=1)).tolist() # std par ligne
    calculations['standard deviation'] = [std_axis_0, std_axis_1, std_flattened]

    # Calcul des max
    max_flattened = np.max(list) # max aplatie
    max_axis_0 = (np.max(matrix, axis=0)).tolist() # maximum par colonne
    max_axis_1 = (np.max(matrix, axis=1)).tolist() # maximum par ligne
    calculations['max'] = [max_axis_0, max_axis_1, max_flattened]

    # Calcul des min
    min_flattened = np.min(list) # min aplatie
    min_axis_0 = (np.min(matrix, axis=0)).tolist() # minimum par colonne
    min_axis_1 = (np.min(matrix, axis=1)).tolist() # minimum par ligne
    calculations['min'] = [min_axis_0, min_axis_1, min_flattened]

    # Calcul des sommes
    sum_flattened = np.sum(list) # somme aplatie
    sum_axis_0 = (np.sum(matrix, axis=0)).tolist() # somme par colonne
    sum_axis_1 = (np.sum(matrix, axis=1)).tolist() # somme par ligne
    calculations['sum'] = [sum_axis_0, sum_axis_1, sum_flattened]

    return calculations
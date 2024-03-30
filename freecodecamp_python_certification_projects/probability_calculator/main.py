# SCIENTIFIC COMPUTING WITH PYTHON
# FREECODECAMP CERTIFICATION
# PROBABILITY CALCULATOR

import copy
import random

class Hat:
    def __init__(self, **args):
        self.args = args
        self.contents = []
        for item in args:
            for i in range(args[item]):
                self.contents.append(item)
                
    def draw(self, n):
        contents_copy = copy.deepcopy(self.contents)
        if n > len(contents_copy):
            return contents_copy
        else:
            draw_result = []
            for i in range(n):
                random_index = random.randrange(len(contents_copy))
                draw_result.append(contents_copy.pop(random_index))
            return draw_result

# Vérifie si tous les éléments de la liste_source sont présents dans la liste_cible.
def is_subset_of(liste_source, liste_cible):
    copie_liste_source = copy.deepcopy(liste_source)
    copie_liste_cible = copy.deepcopy(liste_cible)
    temp = []
    for item in copie_liste_source:
        if item in copie_liste_cible:
            temp.append(copie_liste_cible.pop(copie_liste_cible.index(item)))
        else:
            return False
    if set(copie_liste_source) == set(temp):
        return True
    return False
        
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    # Préparation des variables de travail
    n = num_balls_drawn
    M = 0
    N = num_experiments
    expected_balls_contents = []
    for item in expected_balls:
        for i in range(expected_balls[item]):
            expected_balls_contents.append(item)
    
    # Exécution des N tirages        
    for i in range(N):
        draw_result = hat.draw(n)
        all_expected_drawn = is_subset_of(expected_balls_contents, draw_result)
        if all_expected_drawn:
            M += 1
    
    #Calcul de la probabilité  
    probability = M/N
    
    return probability
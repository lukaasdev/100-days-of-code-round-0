# SCIENTIFIC COMPUTING WITH PYTHON
# FREECODECAMP CERTIFICATION
# ARITHMETIC FORMATTER

# NOTE: Le code est certes fonctionnel 
# mais pourrait clairement être amélioré.
# Il y a notamment pas mal 
# de répétitions de code qu'on pourrait refactoriser.
def problem_length(operand_1, operand_2):
    return max(len(operand_1), len(operand_2)) + 2

def arithmetic_arranger(problems, show_answers=False):
    problems_count = len(problems)
    
    # Gestion de l'erreur 'Trop de problèmes'.
    if problems_count > 5:
        return 'Error: Too many problems.'
    
    line_1 = ''
    line_2 = ''
    dashes_line = ''
    answers_line = ''
    for i, problem in enumerate(problems):
        # Préparation des variables de travail
        elements = problem.split()
        operand_1 = elements[0]
        operator = elements[1]
        operand_2 = elements[2]
        
        # *** GESTION DES ERREURS ***
        # Gestion de l'erreur 'Mauvais opérateur'.
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        
        # Gestion de l'erreur 'Mauvais opérande(s)'.
        try:
            op_1 = int(operand_1)
            op_2 = int(operand_2)
        except ValueError:
            return 'Error: Numbers must only contain digits.'
        
        # Gestion de l'erreur 'Opérande(s) trop longs'.
        if len(operand_1) > 4 or len(operand_2) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        # *** FIN GESTION DES ERREURS ***
        
        # Si aucune erreur n'est détectée, on peut commencer à travailler.
        pl = problem_length(operand_1, operand_2)
        
        temp_1 = ' ' * (pl - len(operand_1)) + operand_1
        temp_2 = operator + ' ' + ' ' * (pl - len(operand_2) - 2) + operand_2
        temp_dashes_line = '-' * pl
        
        line_1 += temp_1 if i == 0 else (' ' * 4) + temp_1
        line_2 += temp_2 if i == 0 else (' ' * 4) + temp_2
        dashes_line += temp_dashes_line if i == 0 else (' ' * 4) + temp_dashes_line
        
        # On gère séparement le calcul des réponses
        temp_answers_line = ''
        if show_answers:
            if operator == '+':
                answer = int(operand_1) + int(operand_2)
            elif operator == '-':
                answer = int(operand_1) - int(operand_2)
                
            temp_answers_line = ' ' * (pl - len(str(answer))) + str(answer)
            answers_line += temp_answers_line if i == 0 else (' ' * 4) + temp_answers_line
      
    if not show_answers:
        result = line_1 + '\n' + line_2 + '\n' + dashes_line
    else:
        result = line_1 + '\n' + line_2 + '\n' + dashes_line + '\n' + answers_line
    
    return result

# Exemples fournis par freeCodeCamp
# Exemple 1
print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
# Exemple 2
print(f'\n{arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)}')
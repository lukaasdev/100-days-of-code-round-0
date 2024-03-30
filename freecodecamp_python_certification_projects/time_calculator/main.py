# SCIENTIFIC COMPUTING WITH PYTHON
# FREECODECAMP CERTIFICATION
# TIME CALCULATOR

WEEK_DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def add_time(start_time, duration, week_day = None):
    elements = start_time.split()
    start_time_hours, start_time_minutes = elements[0].split(':')
    start_time_xm = elements[1]
    duration_hours, duration_minutes = duration.split(':')
    
    # Calcul des minutes
    temp_minutes = int(start_time_minutes) + int(duration_minutes)
    end_time_minutes = temp_minutes if temp_minutes < 60 else temp_minutes - 60
    extra_hours = 0 if temp_minutes < 60 else 1
    end_time_minutes_display = str(end_time_minutes) if end_time_minutes >= 10 else '0' + str(end_time_minutes)
    
    # Calcul des heures
    i = 0
    temp_hours = int(start_time_hours) + int(duration_hours) + extra_hours
    while temp_hours >= 12:
        temp_hours -= 12
        i += 1
    end_time_hours_display = str(temp_hours) if temp_hours != 0 else str(12)
    
    # Déterminer 'AM' ou 'PM', extra_days
    # et les différents affichages (week_day_display et extra_days_display)
    # NOTE: Attention, code bourrin mais fonctionnel dans les lignes ci-dessous. 
    # Pourrait clairement être amélioré =D 
    end_time_xm = ''
    if i % 2 == 0:
        end_time_xm = start_time_xm
    else:
        if start_time_xm == 'AM':
            end_time_xm = 'PM'
        elif start_time_xm == 'PM':
            end_time_xm = 'AM'
            
    extra_days = 0
    extra_days_display = ''
    if i == 1 and start_time_xm == 'PM':
        extra_days = 1
    elif i == 2:
        extra_days = 1
    elif i > 1 and i != 2:
        extra_days = i // 2 + 1

    if extra_days == 1:
        extra_days_display = '(next day)'
    elif extra_days > 1:
        extra_days_display = f'({str(extra_days)} days later)'
    
    week_day_display = ''
    if week_day != None:
        index = WEEK_DAYS.index(week_day.lower())
        new_index = (index + extra_days) % 7
        week_day_display = f', {WEEK_DAYS[new_index].capitalize()}'
    
    # NOTE: Ici, également, on peut clairement faire mieux pour le résultat à retourner.
    result = ''
    if week_day_display == '' and extra_days_display == '':
        result = f'{end_time_hours_display}:{end_time_minutes_display} {end_time_xm}'
    elif week_day_display != '' and extra_days_display == '':
        result = f'{end_time_hours_display}:{end_time_minutes_display} {end_time_xm}{week_day_display}'
    elif week_day_display == '' and extra_days_display != '':
        result = f'{end_time_hours_display}:{end_time_minutes_display} {end_time_xm} {extra_days_display}'
    elif week_day_display != '' and extra_days_display != '':
        result = f'{end_time_hours_display}:{end_time_minutes_display} {end_time_xm}{week_day_display} {extra_days_display}'
        
    return result
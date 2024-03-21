# SCIENTIFIC COMPUTING WITH PYTHON
# FREECODECAMP CERTIFICATION
# TIME CALCULATOR

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
    while temp_hours > 12:
        temp_hours -= 12
        i += 1
    end_time_hours_display = str(temp_hours) if temp_hours != 0 else str(12)
    
    # TODO: Reste à déterminer 
    # end_time_xm : 'AM' ou 'PM'
    # et extra_days_display : (next day) ou ({extra_days} days later)
    # le code ci-dessous n'est pas encore fonctionnel.
    end_time_xm = ''
    if i % 2 == 0 :
        end_time_xm = start_time_xm
    else:
        if start_time_xm == 'AM':
            end_time_xm = 'PM' if temp_hours != 0 else 'AM'
        elif start_time_xm == 'PM':
            end_time_xm = 'AM' if temp_hours != 0 else 'PM'
            
    extra_days = 0
    extra_days_display = ''
    # END TODO:
    
    if extra_days == 1:
        extra_days_display = '(next day)'
    elif extra_days > 1:
        extra_days_display = f'({str(extra_days)} days later)'
    
    print(f'{end_time_hours_display}:{end_time_minutes_display} {end_time_xm} {extra_days_display}')
    
    # print(f'{end_time_hours_display}:{end_time_minutes_display} {end_time_xm}')
    
    # DELETE: 2 lignes ci-dessous
    # print(start_time, start_time_hours, start_time_minutes, start_time_xm)
    # print(duration, duration_hours, duration_minutes, '\n')

# Exemples fournis par freeCodeCamp
add_time('3:00 PM', '3:10')
# Returns: 6:10 PM

add_time('11:30 AM', '2:32', 'Monday')
# Returns: 2:02 PM, Monday

add_time('11:43 AM', '00:20')
# Returns: 12:03 PM

add_time('10:10 PM', '3:30')
# Returns: 1:40 AM (next day)

add_time('11:43 PM', '24:20', 'tueSday')
# Returns: 12:03 AM, Thursday (2 days later)

add_time('6:30 PM', '205:12')
# Returns: 7:42 AM (9 days later)
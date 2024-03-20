# SCIENTIFIC COMPUTING WITH PYTHON
# FREECODECAMP CERTIFICATION
# TIME CALCULATOR

def add_time(start_time, duration, week_day = None):
    elements = start_time.split()
    start_time_hours, start_time_minutes = elements[0].split(':')
    start_time_xm = elements[1]
    duration_hours, duration_minutes = duration.split(':')
    
    # Au 20/03/2024, le calcul des minutes semble être fonctionnel.
    # TODO : A retester demain pour être 100% sûr.
    # Calcul des minutes
    temp = int(start_time_minutes) + int(duration_minutes)
    end_time_minutes = temp if temp < 60 else temp - 60
    extra_hours = temp % 60
    end_time_minutes_display = str(end_time_minutes) if end_time_minutes >= 10 else '0' + str(end_time_minutes)
    
    # Calcul des heures
    temp = 0
    end_time_hours = 0
    end_time_xm = 'XM'
    extra_days = 'none'
    
    print(f'{end_time_hours}:{end_time_minutes_display} {end_time_xm}')
    
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
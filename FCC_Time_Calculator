#this is a function another program calls, passing either 2 or three arguments.  time duration and day.  e.g. 12:34, 4:36, monday -- and this program figures out how much time elapsed and kicks out the new time and day if day is passed.  definitely not as easy as it sounds.  no importing modules were allowed for the assignment.  I did study about 50 other solutions before doing this one.  
#TBH I'm using a few things like modulus and // for the first time here and I still don't know what I did but when it passed the tests I turned it in. 
#i just kept debugging and implementing solutions, now I want to save this to study for later...

def add_time(start, duration, current_day=None):
    start_time, period = start.split()
    start_hour, start_minute = [int(time_part) for time_part in start_time.split(':')]
    duration_hour, duration_minute = [int(time_part) for time_part in duration.split(':')]

    # Convert to 24-hour format
    if period == 'PM':
        start_hour += 12

    # total minutes
    total_minutes = start_hour * 60 + start_minute + duration_hour * 60 + duration_minute

    # new time and how many days later
    new_hour = (total_minutes // 60) % 24
    new_minute = total_minutes % 60
    days_later = total_minutes // (24 * 60)

    # Determine AM/PM
    if new_hour < 12:
        new_period = 'AM'
        if new_hour == 0: #12/0 issue
            new_hour = 12
    else:
        new_period = 'PM'
        if new_hour > 12:
            new_hour -= 12
        elif new_hour == 0: #12/0 issue
            new_hour = 12

    # Pinpoint day of the week, format data
    if current_day is not None:
        current_day = current_day.lower()
        current_day = current_day.capitalize()
        week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        current_day_index = week_days.index(current_day)
        new_day_index = (current_day_index + days_later) % 7
        new_day = week_days[new_day_index]
        new_time = f'{new_hour}:{new_minute:02} {new_period}, {new_day}'
    else:
        new_time = f'{new_hour}:{new_minute:02} {new_period}'

    # Add days later to the output
    if days_later == 1:
        new_time += ' (next day)'
    elif days_later > 1:
        new_time += f' ({days_later} days later)'

    return new_time

def add_time(start, duration, day=None):
  start_time, meridian = start.split(" ") 
  start_hour, start_min = start_time.split(':')
  start_hour = int(start_hour)
  start_min = int(start_min)

  extra_hour, extra_min = duration.split(":")
  extra_hour = int(extra_hour)
  extra_min = int(extra_min)

  # Adding the duration minutes
  new_min = start_min + extra_min
  if new_min >= 60:
    extra_hour += 1
    new_min -= 60
    
  if new_min < 10:
    new_min = f"0{new_min}"

  # Converting to 24 hour clock
  if start_hour == 12 and meridian == "AM":
    start_hour = 0
  elif start_hour == 12 and meridian == "PM":
    start_hour = 12
  elif start_hour != 12 and meridian == "PM":
    start_hour += 12
  else:
    start_hour = start_hour

  # Calculating how many days have past and what the new hour is.
  n_days = 0

  while extra_hour >= 24:
    extra_hour -= 24
    n_days += 1

  hours_left_in_day = 24 - start_hour 

  if extra_hour > hours_left_in_day:
    extra_hour -= hours_left_in_day
    n_days += 1
    new_hour = extra_hour
  elif extra_hour == hours_left_in_day:
    n_days += 1
    new_hour = 0
  else:
    new_hour = start_hour + extra_hour

  # Converting back to AM and PM
  if new_hour < 12:
    new_meridian = "AM"
    if new_hour == 0:
      new_hour = 12
  elif new_hour == 12:
    new_meridian = "PM"
  else:
    new_meridian = "PM"
    new_hour -= 12

  # Creating text for next day and how many days later
  if n_days == 1:
    text = f"(next day)"
  elif n_days > 1:
    text = f"({n_days} days later)"
  

  daysofweek = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

  if day != None:
    day = day.lower().capitalize()
    i_day = daysofweek.index(day)
    new_i_day = i_day + n_days
    if new_i_day > 6:
      new_i_day = ((new_i_day + 1) % 7) - 1
      new_day = daysofweek[new_i_day]
    else:
      new_day = daysofweek[new_i_day]

  if n_days == 0:
    if day != None:
      new_time = f"{new_hour}:{new_min} {new_meridian}, {new_day}"
    else:
      new_time = f"{new_hour}:{new_min} {new_meridian}"
  elif n_days == 1:
    if day != None:
      new_time = f"{new_hour}:{new_min} {new_meridian}, {new_day} (next day)"
    else:
      new_time = f"{new_hour}:{new_min} {new_meridian} (next day)"
  else:
    if day != None:
      new_time = f"{new_hour}:{new_min} {new_meridian}, {new_day} ({n_days} days later)"
    else:
      new_time = f"{new_hour}:{new_min} {new_meridian} ({n_days} days later)"

  return new_time
import pytz
from datetime import datetime


def get_days_later(days):
  """ Format the days later into string"""
  if days == 1:
    return "(next day)"
  elif days > 1:
    return f"({days} days later)"
  return ""


def get_current_time():
  #time in Buenos Aires
  buenos_aires_tz = pytz.timezone('America/Argentina/Buenos_Aires')
  current_time = datetime.now(tz=buenos_aires_tz)
  return current_time.strftime("%I:%M %p")


def add_time(start_time, end_time, day=False):


  results = ""  



  current_time = get_current_time()
  print("Current time in Buenos Aires:", current_time)



  return results.strip()



start_time = "10:00 AM"
end_time = "2:30 PM"
print(add_time(start_time, end_time, day=False))


def get_days_later(days):
  """ Format the days later into string"""
  if days == 1:
    return "(next day)"
  elif days > 1:
    return f"({days} days later)"
  return ""


def add_time(start_time, end_time, day=False):


  HOURS_IN_ONE_DAY = 24
  HOURS_IN_HALF_DAY = 12
  WEEK_DAYS = [
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
    "sunday",
  ]

  days_later = 0
  hours, mins = start_time.split(":")
  mins, period = mins.split(" ")
  end_time_hrs, end_time_mins = end_time.split(":")


  hours = int(hours) 
  mins = int(mins)  
  end_time_hrs = int(end_time_hrs)  
  end_time_mins = int(end_time_mins)  
  period = period.strip().lower()  # AM or PM


  total_mins = mins + end_time_mins
  total_hours = hours + end_time_hrs


  if total_mins >= 60:
    total_hours += int(total_mins / 60)
    total_mins = int(total_mins % 60)

  if end_time_hrs or end_time_mins:

    if period == "pm" and total_hours > HOURS_IN_HALF_DAY:

      if total_hours % HOURS_IN_ONE_DAY >= 1.0:
        days_later += 1

    if total_hours >= HOURS_IN_HALF_DAY:
      hours_left = total_hours / HOURS_IN_ONE_DAY
      days_later += int(hours_left)



    temp_hours = total_hours
    while True:

      if temp_hours < HOURS_IN_HALF_DAY:
        break
      if period == "am":
        period = "pm"
      else:
        period = "am"
      temp_hours -= HOURS_IN_HALF_DAY

  remaining_hours = int(total_hours % HOURS_IN_HALF_DAY) or hours + 1
  remaining_mins = int(total_mins % 60)


  results = f"{remaining_hours}:{remaining_mins:02} {period.upper()}"
  if day: 
    day = day.strip().lower()
    selected_day = int((WEEK_DAYS.index(day) + days_later) % 7)
    current_day = WEEK_DAYS[selected_day]
    results += f", {current_day.title()} {get_days_later(days_later)}"

  else: 
    results = " ".join((results, get_days_later(days_later)))

  return results.strip()

    results = " ".join((results, get_days_later(days_later)))

  return results.strip()

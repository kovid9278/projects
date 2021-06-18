def add_time(start, duration, day = None):
  
  # Weekly Index
  weeklyIndex = {
        "Saturday": 0,
        "Sunday": 1,
        "Monday": 2,
        "Tuesday": 3,
        "Wednesday": 4,
        "Thursday": 5,
        "Friday": 6
    }

  startTime = start.split()[0]
  check = start.split()[1].strip()
  
  # Capturing useful data from the input

  startHour = int(startTime.split(":")[0]) 
  startMinute = int(startTime.split(":")[1])
  # Splitting into hours and minutes and conveting them into integers
  extraHour = int(duration.split(":")[0])
  extraMin = int(duration.split(":")[1])

  if (check =='PM'):
    startHour += 12
  # Convert into a 24 hour format

  totalMin = startMinute + extraMin
  totalHour = 0
  tempHour = 0
  # Claculating extra hour
  while(totalMin > 59 ):
    totalMin = totalMin - 60
    tempHour += 1 

  totalHour = tempHour + extraHour + startHour

  days = 0
  # Calculating Days
  while(totalHour>23):
    totalHour = totalHour - 24
    days = days + 1
  
  midDay = ''
  
  # Checking for AM or PM   
  if (totalHour % 24) <= 11:
        midDay = "AM"
  else:
        midDay = "PM"

  #Converting it back to 12 hour format  
  if totalHour > 11:
     totalHour = totalHour -12

  if totalHour == 0:
      totalHour = 12

  # Converting single digit minutes to double digit
  totalMin = '{:02}'.format(totalMin)
  finalValue = str(totalHour) + ":" + str(totalMin) + " " + midDay
  # returning answers in prescribed format
  if day == None:
        if days == 0:
            return finalValue
        if days == 1:
            return finalValue + ' (next day)'
        return finalValue + ' (' + str(days) + ' days later)'
  else:
        answerDay = (weeklyIndex[day.lower().capitalize()] + days) % 7
        for i, j in weeklyIndex.items():
            if j == answerDay:
                answerDay = i
                break
        if days == 0:
            return finalValue + ', ' + answerDay
        if days == 1:
            return finalValue + ', ' + answerDay + ' (next day)'
        return finalValue + ', ' + answerDay + ' (' + str(
            days) + ' days later)'








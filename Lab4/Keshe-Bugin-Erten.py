import datetime

current_time = datetime.datetime.now()
tomorrow = current_time + datetime.timedelta(days=1)
yesterday = current_time - datetime.timedelta(days=1)

print("Yesterday's date:", yesterday)
print("Today's date: ", current_time)
print("Tomorrow's date: ", tomorrow)
#www.youtube.com/watch?v=UTHi8w3P0cY
import pywhatkit as kit
import csv

with open('numbers_and_messages.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        phone_number = row[0]
        message = row[1]
        hour = int(row[2])
        minute = int(row[3])
        print(phone_number)
        print(message)
        kit.sendwhatmsg(phone_number,message, hour, minute, 20,True,5)

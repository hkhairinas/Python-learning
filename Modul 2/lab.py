hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

jam = hour + (mins + dura) // 60
jamm = jam % 24
menit = (mins + dura) % 60

print (jamm,":",menit)
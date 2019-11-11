day = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
now = input("What day is today: ")
nextday = int(input("how many day before or after? "))
futureday = day.index(now)
whatday = nextday % len(day)
thenextday = day[(futureday+whatday)%7]
print(f'That day exactly {thenextday}')

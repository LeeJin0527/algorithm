day =['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
count = {1 : 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9:30, 10: 31, 11: 30, 12: 31}
x, y = map(int, input().split())
tmp = 0
for i in range(1, x):
	tmp += count[i]

tmp = tmp + y

print(day[tmp % 7])
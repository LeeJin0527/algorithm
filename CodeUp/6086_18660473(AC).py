
answer = int(input())
suma =0
for i in range(1, answer +1):
    suma += i
    if suma >= answer:
        break
print(suma)

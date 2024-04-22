a = 80000
taxa_a = 0.03

b = 200000
taxa_b = 0.015

anos = 0

while(a <= b):
    a += (a * taxa_a)
    b += (b * taxa_b)
    anos += 1
print(f"Será necessário {anos} anos para o país A ultrapassar o país B em número de habitantes")
num = []
for i in range(3):
    while True:
        texto = input(f"Digite o número {i + 1} (apenas números): ")
        if texto.isnumeric():
            break
    num.append(int(texto))
num = sorted(num)
num = num[::-1]
print(f"A ordem decrecente dos número que você esconheu, são: {num}")
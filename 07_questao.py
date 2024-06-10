nomeAluno = input("Digite o nome do aluno: ")
disciplina = input("Digite o nome da disciplina: ")
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = (n1+n2)/2 
print(f'A média do aluno é {media}.')
if media >=6:
    status = 'aprovado'
else :
    status = 'reprovado'
print(f'O(a) aluno(a) {nomeAluno} está {status} na disciplina de {disciplina}')
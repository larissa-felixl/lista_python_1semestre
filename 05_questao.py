hora = int(input('Me diga um número de 0 a 23: '))
if hora >= 0 and hora <12:
    periodo = "manhã"
elif hora >= 12 and hora <18:
    periodo = "tarde"
else:
    periodo = "noite"
print(f'Se esse número fosse a hora, agora seria de {periodo}! ')
import matplotlib.pyplot as plt 

horas_estudo = [2, 3, 5, 7, 8, 10, 12, 14]
notas_prova = [50, 60, 75, 80, 85, 90, 95, 100]

plt.scatter(horas_estudo, notas_prova, label='Notas dos Alunos')

plt.title('Relação entre horas de Estudo e Notas da Prova')
plt.xlabel('Horas de Estudo')
plt.ylabel('Notas da Prova')

plt.legend()
plt.show()


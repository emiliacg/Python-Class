agenda= []
for i in range(3):
    a= {}
    a["nombre"]= input("nombre: ")
    a["numero"]= input("numero: ")
    agenda.append(a)
print(agenda)
print(agenda[0]["nombre"], agenda[0]["numero"])
print(agenda[2]["nombre"], agenda[1]["numero"])
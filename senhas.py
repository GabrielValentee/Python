codigos_brutos = [
    "abc123",
    "def456",
    12345,          
    "gh789",
    "abc123",        
    None,          
    "jk1012",
    "GH789",      
    "",              
    "mno345"
]

codigos_validos = set()
codigos_invalidos = []

for codigo in codigos_brutos:
    try:
        codigo_str = str(codigo)
        codigo_processado = codigo_str.upper()
        codigos_validos.add(codigo_processado)
    except (TypeError, AttributeError) as e:
        print(f"Erro ao processar '{codigo}': {e}")
        codigos_invalidos.append(codigo)

print("Códigos válidos e únicos (em maiúsculas):")
for codigo in codigos_validos:
    print(codigo)

print("Códigos que falharam no processamento:")
for codigo in codigos_invalidos:
    print(codigo)




    
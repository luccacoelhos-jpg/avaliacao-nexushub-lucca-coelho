# -- 1° Etapa: Cadastro e projetos. --
startup = {
    "Nome": "CyberPulse Tech",
    "Segmento": "Segurança da informação",
    "Ano_adesao": "2026"
}

solucoes_ativas = ("Firewall IA","Scan de Vunerabiidades")
print("STARTUP:",startup["Nome"],"Segmento:",["Segmento"])
print("Projetos em andamento",solucoes_ativas[0])

# -- 2° Etapa: Mapeamento
# 1 = Ocupado - 0 = Livre
bancadas = [
       [1,0],
       [0,1]
]
print("Bancada N1",[1][0])
print("Bancada N2",[0][0])
print("Bancada S1",[0][0])
print("Bancada S2",[1][0])

print("1 = Ocupado - 0 = Livre.")

# -- 3° Etapa: Leitura Sequencial do CSV --
with open("custos_cloud.csv", "r", encoding="utf-8") as arquivo:
    cabecalho = arquivo.readline()
    linha1 = arquivo.readline()
    linha2 = arquivo.readline()
    linha3 = arquivo.readline()
    linha4 = arquivo.readline()

print("Cabeçalho:", cabecalho)
print("Linha 1:", linha1)
print("Linha 2:", linha2)
print("Linha 3:", linha3)
print("Linha 4:", linha4)

# -- 4° Etapa: Consolidação de Dados e Cálculo Final --
# Identificação da Empresa e Local
nome_empresa = startup["Nome"]
bancada_alocada = "Bancada N1"

# Tratamento de Dados e Extração de Custos
custo1 = float(linha1.split(',')[1].strip())
custo2 = float(linha2.split(',')[1].strip())
custo3 = float(linha3.split(',')[1].strip())
custo4 = float(linha4.split(',')[1].strip())

# Cálculo Total
total_infraestrutura = custo1 + custo2 + custo3 + custo4

# Exibição do Painel Final
print("\n" + "="*50)
print("PAINEL CONSOLIDADO DE INFRAESTRUTURA")
print("="*50)
print(f"Empresa: {nome_empresa}")
print(f"Bancada Alocada: {bancada_alocada}")
print(f"Custo Total de Infraestrutura Cloud: R$ {total_infraestrutura:.2f}")
print("="*50)
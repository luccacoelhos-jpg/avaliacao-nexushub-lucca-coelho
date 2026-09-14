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
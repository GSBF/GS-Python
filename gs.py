# Função de boas-vindas
def exibir_boas_vindas():
    print(100 * "-")
    print("Bem-vindo ao programa de simulação do nível do mar!")
    print("Este programa irá ajudá-lo a entender o impacto do aumento do nível do mar em áreas costeiras.")
    print("Você poderá simular o aumento do nível do mar, visualizar um gráfico e comparar com dados históricos.")
    print("Vamos começar!\n")
    print(100 * "-")

# Programa que vai fazer uma simulação do nível do mar 
def simular_nivel_do_mar(ano_inicial, ano_final, taxa_aumento):
    # Inicialização
    nivel_do_mar = 0.0
    niveis_ano_a_ano = []

    # Simulação ano a ano
    for ano in range(ano_inicial, ano_final + 1):
        nivel_do_mar += taxa_aumento
        niveis_ano_a_ano.append(nivel_do_mar)
        print(f"Ano {ano}: Aumento do nível do mar: {nivel_do_mar:.2f} cm")

    # Resumo da simulação
    print("\nResumo:")
    print(f"Período: {ano_inicial} a {ano_final}")
    print(f"Taxa de aumento: {taxa_aumento:.2f} cm/ano")
    print(f"Aumento total: {nivel_do_mar:.2f} cm")
    
    return niveis_ano_a_ano, nivel_do_mar

def avaliar_impacto_areas_costeiras(nivel_do_mar):
    print("\nAvaliação do impacto em áreas costeiras:")
    areas_costeiras = [
        {"nome": "Área A", "altitude": 50},
        {"nome": "Área B", "altitude": 150},
        {"nome": "Área C", "altitude": 100},
    ]

    for area in areas_costeiras:
        impacto = "Inundada" if nivel_do_mar >= area["altitude"] else "Não inundada"
        print(f"{area['nome']}: {impacto}")

def plotar_grafico(ano_inicial, niveis):
    print("\nVisualizando o gráfico do aumento do nível do mar (cm):")
    for i, nivel in enumerate(niveis):
        ano = ano_inicial + i
        print(f"Ano {ano}: {'*' * int(nivel)}")

def comparar_com_dados_historicos(ano_inicial, ano_final, niveis_simulados):
    niveis_historicos = []
    print("\nInsira os dados históricos do nível do mar (em cm) para o período:")
    for ano in range(ano_inicial, ano_final + 1):
        nivel_historico = float(input(f"Ano {ano}: "))
        niveis_historicos.append(nivel_historico)

    print("\nComparação entre os dados históricos e simulados:")
    for i in range(len(niveis_simulados)):
        ano = ano_inicial + i
        diferenca = niveis_historicos[i] - niveis_simulados[i]
        print(f"Ano {ano}: Simulado: {niveis_simulados[i]:.2f} cm, Histórico: {niveis_historicos[i]:.2f} cm, Diferença: {diferenca:.2f} cm")

def menu():
    print("\nMenu de Opções:")
    print("1. Simular o nível do mar")
    print("2. Avaliar impacto em áreas costeiras")
    print("3. Visualizar gráfico do aumento do nível do mar")
    print("4. Comparar com dados históricos")
    print("5. Fechar o programa")

# Função principal
def main():
    # Exibir mensagem de boas-vindas
    exibir_boas_vindas()

    niveis_ano_a_ano = []
    nivel_do_mar = 0.0

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                print("\nVocê escolheu a primeira opção.")
                print("Vamos simular o nível do mar!!!\n")
                ano_inicial = int(input("Digite o ano inicial: "))
                ano_final = int(input("Digite o ano final: "))
                taxa_aumento = float(input("Digite a taxa de aumento do nível do mar (cm/ano): "))
                niveis_ano_a_ano, nivel_do_mar = simular_nivel_do_mar(ano_inicial, ano_final, taxa_aumento)
            case "2":
                if niveis_ano_a_ano:
                    print("\nVocê escolheu a segunda opção.")
                    print("Vamos avaliar o impacto em áreas costeiras!!!\n")
                    avaliar_impacto_areas_costeiras(nivel_do_mar)
                else:
                    print("\nPor favor, execute a simulação do nível do mar primeiro (opção 1).")
            case "3":
                if niveis_ano_a_ano:
                    print("\nVocê escolheu a terceira opção.")
                    print("Vamos vizualizar o gráfico do aumento do nível do mar!!!\n")
                    plotar_grafico(ano_inicial, niveis_ano_a_ano)
                else:
                    print("\nPor favor, execute a simulação do nível do mar primeiro (opção 1).")
            case "4":
                if niveis_ano_a_ano:
                    print("\nVocê escolheu a quarta opção.")
                    print("Vamos comparar com dados históricos!!!\n")
                    comparar_com_dados_historicos(ano_inicial, ano_final, niveis_ano_a_ano)
                else:
                    print("\nPor favor, execute a simulação do nível do mar primeiro (opção 1).")
            case "5":
                print("\nFechando o programa. Até mais!")
                break
            case _:
                print("\nOpção inválida. Por favor, escolha uma opção válida.")

# Chamada da função principal
if __name__ == "__main__":
    main()
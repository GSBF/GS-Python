# Simulação do Nível do Mar

## Alunos
- Jean Matheus RM555519
- Thiago de Barros RM555485

## Descrição do Projeto
Este projeto consiste em um programa simples em Python que simula o aumento do nível do mar ao longo dos anos e avalia o impacto em áreas costeiras específicas. O programa permite ao usuário inserir o ano inicial, ano final e a taxa de aumento do nível do mar (em cm/ano). Após a simulação, o programa oferece a opção de verificar se determinadas áreas costeiras serão inundadas com base na altitude dessas áreas.

## Instruções de Uso
1. Certifique-se de ter Python instalado no seu sistema.
2. Baixe o arquivo e abra-o em um editor de texto ou IDE de sua preferência.
3. Execute o programa. Você será solicitado a inserir:
   - Ano inicial da simulação.
   - Ano final da simulação.
   - Taxa de aumento do nível do mar (em cm/ano).
4. Após a entrada dos dados, o programa realizará a simulação e exibirá o aumento do nível do mar ano a ano.
5. Opcionalmente, você pode avaliar o impacto em áreas costeiras específicas, informando se deseja essa avaliação.

## Requisitos
- Python 3.x

## Dependências
Não há dependências externas para este projeto. Apenas o Python padrão é necessário.

## Informações Relevantes
- O programa utiliza uma lista pré-definida de áreas costeiras com suas respectivas altitudes para avaliar o impacto do aumento do nível do mar.
- As áreas costeiras consideradas na avaliação são:
  - Área A: Altitude de 50 cm
  - Área B: Altitude de 150 cm
  - Área C: Altitude de 100 cm
- O usuário pode modificar ou adicionar novas áreas costeiras editando a lista `areas_costeiras` no código.

## Código do Projeto
```python
def simular_nivel_do_mar(ano_inicial, ano_final, taxa_aumento):
    # Simula o aumento do nível do mar em um intervalo de anos e informa o impacto em áreas costeiras.

    # Inicialização
    nivel_do_mar = 0.0

    # Simulação ano a ano
    for ano in range(ano_inicial, ano_final + 1):
        nivel_do_mar += taxa_aumento
        print(f"Ano {ano}: Aumento do nível do mar: {nivel_do_mar:.2f} cm")

    # Resumo da simulação
    print("\nResumo:")
    print(f"Período: {ano_inicial} a {ano_final}")
    print(f"Taxa de aumento: {taxa_aumento:.2f} cm/ano")
    print(f"Aumento total: {nivel_do_mar:.2f} cm")

    # Impacto em áreas costeiras (opcional)
    if input("\nDeseja avaliar o impacto em áreas costeiras? (S/N): ").upper() == "S":
        areas_costeiras = [
            {"nome": "Área A", "altitude": 50},
            {"nome": "Área B", "altitude": 150},
            {"nome": "Área C", "altitude": 100},
        ]

        for area in areas_costeiras:
            impacto = "Inundada" if nivel_do_mar >= area["altitude"] else "Não inundada"
            print(f"{area['nome']}: {impacto}")

# Solicitação de dados ao usuário
ano_inicial = int(input("Digite o ano inicial: "))
ano_final = int(input("Digite o ano final: "))
taxa_aumento = float(input("Digite a taxa de aumento do nível do mar (cm/ano): "))

# Execução da simulação
simular_nivel_do_mar(ano_inicial, ano_final, taxa_aumento)

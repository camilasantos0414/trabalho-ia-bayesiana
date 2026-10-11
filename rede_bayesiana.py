"""
Implementação da Rede Bayesiana para o Sistema de Diagnóstico do Farol de Bicicleta
Disciplina de Inteligência Artificial - UFAM
"""

from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

def main():
    # 1. Definir a estrutura do grafo da Rede Bayesiana
    modelo = BayesianNetwork([
        ('Str', 'R'),
        ('Flw', 'R'),
        ('R', 'V'),
        ('V', 'Li'),
        ('B', 'Li'),
        ('K', 'Li')
    ])

    # 2. Definir as CPTs (Tabelas de Probabilidade Condicional)
    
    # P(Str): dry (0.7), wet (0.2), snow_covered (0.1)
    cpd_str = TabularCPD(variable='Str', variable_card=3, values=[[0.7], [0.2], [0.1]])

    # P(Flw): t (0.1), f (0.9)
    cpd_flw = TabularCPD(variable='Flw', variable_card=2, values=[[0.1], [0.9]])

    # P(B): t (0.95), f (0.05)
    cpd_b = TabularCPD(variable='B', variable_card=2, values=[[0.95], [0.05]])

    # P(K): t (0.98), f (0.02)
    cpd_k = TabularCPD(variable='K', variable_card=2, values=[[0.98], [0.02]])

    # P(R | Str, Flw) - 6 combinações (3 estados de Str * 2 estados de Flw)
    cpd_r = TabularCPD(
        variable='R', variable_card=2,
        values=[
            [0.05, 0.4, 0.8, 0.01, 0.1, 0.4], # R = t (desliza)
            [0.95, 0.6, 0.2, 0.99, 0.9, 0.6]  # R = f (não desliza)
        ],
        evidence=['Str', 'Flw'],
        evidence_card=[3, 2]
    )

    # P(V | R)
    cpd_v = TabularCPD(
        variable='V', variable_card=2,
        values=[
            [0.1, 0.95], # V = t
            [0.9, 0.05]  # V = f
        ],
        evidence=['R'],
        evidence_card=[2]
    )

    # P(Li | V, B, K) - 8 combinações
    cpd_li = TabularCPD(
        variable='Li', variable_card=2,
        values=[
            [0.99, 0.01, 0.01, 0.001, 0.3, 0.005, 0.005, 0.0], # Li = t
            [0.01, 0.99, 0.99, 0.999, 0.7, 0.995, 0.995, 1.0]  # Li = f
        ],
        evidence=['V', 'B', 'K'],
        evidence_card=[2, 2, 2]
    )

    # Adicionar as CPTs ao modelo
    modelo.add_cpds(cpd_str, cpd_flw, cpd_b, cpd_k, cpd_r, cpd_v, cpd_li)

    # Verificar se o modelo é válido
    assert modelo.check_model(), "O modelo da rede bayesiana é inválido!"
    print("Rede Bayesiana criada e validada com sucesso!\n")

    # 3. Realizar a inferência para a alínea (e): P(V | Str = snow_covered)
    infer = VariableElimination(modelo)
    
    # No pgmpy, 'snow_covered' corresponde ao índice 2 da variável Str (dry=0, wet=1, snow_covered=2)
    resultado = infer.query(variables=['V'], evidence={'Str': 2})
    
    print("Cálculo da alínea (e): P(V | Str = snow_covered)")
    print(resultado)

if __name__ == '__main__':
    main()

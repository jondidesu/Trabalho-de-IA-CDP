# calculo_predicados.py

class Predicado:
    def __init__(self, nome, aridade):
        self.nome = nome
        self.aridade = aridade

    def __repr__(self):
        return f"{self.nome}/{self.aridade}"

class Fato:
    def __init__(self, predicado, *argumentos):
        if not isinstance(predicado, Predicado):
            raise ValueError("O primeiro argumento deve ser uma instância de Predicado.")
        if len(argumentos) != predicado.aridade:
            raise ValueError(f"Número incorreto de argumentos para o predicado {predicado.nome}. Esperado {predicado.aridade}, recebido {len(argumentos)}.")
        self.predicado = predicado
        self.argumentos = argumentos

    def __repr__(self):
        args_str = ', '.join(map(str, self.argumentos))
        return f"{self.predicado.nome}({args_str})"

    def __eq__(self, other):
        if not isinstance(other, Fato):
            return False
        return self.predicado == other.predicado and self.argumentos == other.argumentos

    def __hash__(self):
        return hash((self.predicado, self.argumentos))

class Regra:
    def __init__(self, cabeca, corpo):
        # cabeca e corpo são listas de Fatos (ou algo similar a Fatos para o corpo)
        self.cabeca = cabeca # Consequência da regra
        self.corpo = corpo   # Condições para a regra ser verdadeira

    def __repr__(self):
        corpo_str = ' AND '.join(map(str, self.corpo))
        cabeca_str = ' AND '.join(map(str, self.cabeca))
        return f"{cabeca_str} :- {corpo_str}"

class BaseDeConhecimento:
    def __init__(self):
        self.fatos = set()
        self.regras = []

    def adicionar_fato(self, fato):
        self.fatos.add(fato)

    def adicionar_regra(self, regra):
        self.regras.append(regra)

    def consultar(self, consulta):
        # Simplificação: Apenas verifica se a consulta é um fato existente
        # ou pode ser inferida diretamente por uma regra simples (sem variáveis)
        if consulta in self.fatos:
            return True

        for regra in self.regras:
            # Para simplificar, vamos considerar apenas regras com um único item no corpo
            # e sem variáveis por enquanto para a demonstração inicial.
            # Uma implementação completa exigiria unificação e backtracking.
            if len(regra.corpo) == 1 and len(regra.cabeca) == 1:
                condicao = regra.corpo[0]
                consequencia = regra.cabeca[0]

                # Se a condição da regra é um fato conhecido e a consequência
                # da regra corresponde à consulta, então a consulta é verdadeira.
                # Isso é uma simplificação extrema e não lida com variáveis.
                if condicao in self.fatos and consequencia == consulta:
                    return True

        return False

# --- Exemplo de Uso ---

# 1. Definir Predicados
homem = Predicado("homem", 1)
mortal = Predicado("mortal", 1)

# 2. Criar Base de Conhecimento
bc = BaseDeConhecimento()

# 3. Adicionar Fatos
bc.adicionar_fato(Fato(homem, "socrates"))
bc.adicionar_fato(Fato(homem, "platao"))
bc.adicionar_fato(Fato(mortal, "joao"))

# 4. Adicionar Regras
# Regra: Se X é homem, então X é mortal
# Esta representação de regra é simbólica e não executável diretamente ainda.
# A lógica de inferência precisaria interpretar isso.
# Para a nossa BaseDeConhecimento simplificada, vamos adicionar uma regra que
# o mecanismo de consulta possa entender (ainda que de forma limitada).

# Para demonstrar a regra 'mortal(X) :- homem(X)', precisamos de um mecanismo
# de inferência mais robusto. Por enquanto, a consulta simplificada não a usará
# de forma genérica. Vamos simular a inferência para o exemplo clássico.

# Regra simplificada para demonstração (apenas para o exemplo 'Sócrates é mortal')
# Isso não é uma regra genérica de LPO, mas uma forma de mostrar a inferência.
# Uma implementação real de LPO usaria unificação para 'X'.

# Vamos refatorar a consulta para lidar com a regra de forma mais inteligente.

class BaseDeConhecimentoMelhorada(BaseDeConhecimento):
    def consultar(self, consulta):
        # 1. Verificar se a consulta é um fato conhecido
        if consulta in self.fatos:
            return True

        # 2. Tentar inferir a consulta usando as regras
        for regra in self.regras:
            # Para cada regra, tentar unificar o corpo da regra com os fatos existentes
            # e, se bem-sucedido, verificar se a cabeça da regra unifica com a consulta.
            # Esta é uma simplificação do algoritmo de encadeamento para frente ou para trás.

            # Exemplo de regra: mortal(X) :- homem(X)
            # cabeca = [Fato(mortal, Variavel('X'))]
            # corpo = [Fato(homem, Variavel('X'))]

            # Para esta demonstração, vamos simular a unificação para o caso simples
            # de 'mortal(X) :- homem(X)' e uma consulta como 'mortal(socrates)'.

            # Se a regra tem uma única cabeça e um único corpo
            if len(regra.cabeca) == 1 and len(regra.corpo) == 1:
                cabeca_regra = regra.cabeca[0]
                corpo_regra = regra.corpo[0]

                # Se a consulta tem o mesmo predicado da cabeça da regra
                if consulta.predicado == cabeca_regra.predicado:
                    # Tentar unificar os argumentos da consulta com os da cabeça da regra
                    # Para simplificar, assumimos que a cabeça da regra tem uma variável
                    # e a consulta tem um valor concreto.
                    if len(cabeca_regra.argumentos) == 1 and isinstance(cabeca_regra.argumentos[0], Variavel):
                        variavel_na_regra = cabeca_regra.argumentos[0]
                        valor_da_consulta = consulta.argumentos[0]

                        # Substituir a variável no corpo da regra pelo valor da consulta
                        # e verificar se o fato resultante existe na base de conhecimento.
                        if len(corpo_regra.argumentos) == 1 and isinstance(corpo_regra.argumentos[0], Variavel) and corpo_regra.argumentos[0] == variavel_na_regra:
                            fato_necessario = Fato(corpo_regra.predicado, valor_da_consulta)
                            if fato_necessario in self.fatos:
                                return True

        return False

class Variavel:
    def __init__(self, nome):
        self.nome = nome

    def __repr__(self):
        return self.nome

    def __eq__(self, other):
        if not isinstance(other, Variavel):
            return False
        return self.nome == other.nome

    def __hash__(self):
        return hash(self.nome)

# --- Exemplo de Uso com a BaseDeConhecimentoMelhorada ---

# 1. Definir Predicados
homem = Predicado("homem", 1)
mortal = Predicado("mortal", 1)

# 2. Criar Base de Conhecimento
bc = BaseDeConhecimentoMelhorada()

# 3. Adicionar Fatos
bc.adicionar_fato(Fato(homem, "socrates"))
bc.adicionar_fato(Fato(homem, "platao"))
bc.adicionar_fato(Fato(mortal, "joao")) # Fato direto

# 4. Adicionar Regras
# Regra: Para todo X, se X é homem, então X é mortal
# Representamos a regra com uma variável simbólica 'X'
X = Variavel('X')
regra_homem_mortal = Regra(cabeca=[Fato(mortal, X)], corpo=[Fato(homem, X)])
bc.adicionar_regra(regra_homem_mortal)

# 5. Realizar Consultas
print("--- Consultas ---")

consulta1 = Fato(mortal, "socrates")
print(f"Consulta: {consulta1} -> {bc.consultar(consulta1)}") # Deve ser True

consulta2 = Fato(mortal, "platao")
print(f"Consulta: {consulta2} -> {bc.consultar(consulta2)}") # Deve ser True

consulta3 = Fato(mortal, "joao")
print(f"Consulta: {consulta3} -> {bc.consultar(consulta3)}") # Deve ser True (fato direto)

consulta4 = Fato(mortal, "maria")
print(f"Consulta: {consulta4} -> {bc.consultar(consulta4)}") # Deve ser False

consulta5 = Fato(homem, "socrates")
print(f"Consulta: {consulta5} -> {bc.consultar(consulta5)}") # Deve ser True (fato direto)

consulta6 = Fato(homem, "zeus")
print(f"Consulta: {consulta6} -> {bc.consultar(consulta6)}") # Deve ser False



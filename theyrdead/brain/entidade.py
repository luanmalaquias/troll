from random import choice
import random

generos = ['Male', 'Female']

tiposMonstrosWeak = ['Clicker', 'Toad', 'Boomer', 'Butcher']
tiposMonstrosStrong = ['Shambler', 'Jockey', 'Butcher', 'Charger']
tiposMonstrosOverPower = ['Volatile', 'Witch', 'Tank']

nomesF = ['Agatha','Camila','Esther','Isis','Maitê'
    ,'Natália','Alícia','Carolina','Fernanda','Joana'
    ,'Malu','Nicole','Amanda','Catarina','Gabriela'
    ,'Laís','Maria','Olívia','Ana','Cecília'
    ,'Gabrielle','Lara','Mariah','Pietra','Antonela'
    ,'Clara','Giovanna','Larissa','Mariana','Rafaela'
    ,'Aurora','Clarice','Giulia','Lavínia','Marina'
    ,'Rebeca','Bárbara','Eduarda','Heloísa','Letícia'
    ,'Maya','Sara','Beatriz','Elisa','Isabel','Liz'
    ,'Melissa','Sophie','Emanuelly','Isabelly','Lorena'
    ,'Milena','Stella','Bruna','Emilly','Isadora'
    ,'Luana','Mirella','Vitória','Yasmin']

nomesM = ['Alexandre','Eduardo','Henrique','Murilo','Theo'
    ,'André','Enrico','Henry','Nathan','Thiago'
    ,'Antônio','Enzo','Ian','Otávio','Thomas'
    ,'Augusto','Erick','Isaac','Pietro','Vicente'
    ,'Breno','Felipe','João','Rafael','Vinícius'
    ,'Bruno','Fernando','Kaique','Raul','Vitor'
    ,'Caio','Francisco','Leonardo','Rian','Yago'
    ,'Cauã','Frederico','Luan','Ricardo','Ygor'
    ,'Daniel','Guilherme','Lucas','Rodrigo','Yuri'
    ,'Danilo','Gustavo','Mathias','Samuel','Matuê']

def randomizarEntidade(tipo, sorte):
    entidade = ['','','','','','','','','','','','']
    pontuacaoTotal = 0
    pontuacao = []
    idade = random.randint(5, 60)
    genero = random.choices(population=generos, weights=[80,20], k=1)[0]
    nome = random.choice(nomesM) if genero == "Male" else random.choice(nomesF)        

    if tipo == "human":

        classe = "Human"

        for x in range(0,6):
            ponto = random.randint(0,25)
            if genero == 'Female':
                ponto //= 1.2
            if idade < 15 or idade > 45:
                ponto //= 2
            
            pontuacao.append(ponto)
            pontuacaoTotal += ponto

    else:

        # pontuacao maxima
        if tipo == 'weak':
            max = 15
        elif tipo == 'strong':
            max = 30
        elif tipo == 'overpower':
            max = 60
        
        # atribuicao da classe do monstro
        if sorte >= 15:
            classe = retornarTipo(0, tipo)
        elif sorte >= 10:
            classe = retornarTipo(1, tipo)
        elif sorte >= 5:
            classe = retornarTipo(2, tipo)
        elif sorte >= 0:
            classe = retornarTipo(3, tipo)

        # atribuicao do ponto do monstro
        for x in range(0, 6):
            ponto = Switch(classe, max)
            pontuacao.append(ponto)
            pontuacaoTotal += ponto

    level = pontuacaoTotal // 10

    # atribuicao do retorno da entidade
    entidade = [
        nome, genero, classe, idade, pontuacaoTotal, level, 
        pontuacao[0], pontuacao[1], pontuacao[2], pontuacao[3], pontuacao[4], pontuacao[5]
    ]    

    return entidade

def retornarTipo(index, tipo):
    if tipo == 'weak':
        return tiposMonstrosWeak[index]
    elif tipo == 'strong':
        return tiposMonstrosStrong[index]
    elif tipo == 'overpower':
        return tiposMonstrosOverPower[index]

def Switch(monstro, max):
    # weaks
    if monstro == "Clicker":
        ponto = random.randint(0,max-9)
    elif monstro == "Toad":
        ponto = random.randint(0,max-6)
    elif monstro == "Boomer":
        ponto = random.randint(0,max-3)
    elif monstro == "Butcher":
        ponto = random.randint(0,max)
    # strong
    elif monstro == 'Shambler':
        ponto = random.randint(0,max)
    elif monstro == 'Jockey':
        ponto = random.randint(0,max+2)
    elif monstro == 'Butcher':
        ponto = random.randint(0,max+4)
    elif monstro == 'Charger':
        ponto = random.randint(0,max+6)
    # overpower
    elif monstro == 'Volatile':
        ponto = random.randint(0,max+8)
    elif monstro == 'Witch':
        ponto = random.randint(0,max+10)
    elif monstro == 'Tank':
        ponto = random.randint(0,max+12)
    else:
        ponto = random.randint(0,max)
        
    return ponto

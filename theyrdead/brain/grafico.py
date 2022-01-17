import matplotlib.pyplot as plt 
import base64
from io import BytesIO

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format = 'png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph


def getGrafico(entity):
    # organizacao dos dados
    dados = [
        entity.strength,
        entity.constitution,
        entity.dexterity,
        entity.intelligence,
        entity.wisdom,
        entity.charisma
    ]
    nomeDados = ['strength', 'constitution', 'dexterity', 'intelligence', 'wisdom', 'charisma']
    # configuração do grafico
    plt.switch_backend('AGG')
    plt.figure(figsize=(5,2.47))
    plt.rcParams.update({'font.size': 7})
    plt.subplots_adjust(left=0.0, right=0.999, top=1, bottom=0.1)
    plt.axes().set_facecolor('black')
    plt.plot(nomeDados, dados, "red")
    
    # retorno
    graph = get_graph()
    return graph
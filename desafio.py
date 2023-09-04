import random

class heroi:
  def __init__(self, classe, ataque):
    self.classe = classe
    self.ataque = ataque

  def atacarOutroHeroi(self, outroHeroi):
    dano = random.randint(0, 12)
    print(f'Opção selecionada: Atacar\nO {self.classe} atacou o {outroHeroi.classe} usando: {self.ataque}.\n{outroHeroi.classe} recebeu {dano} de dano.')

  def usoPocao(self, classe):
    cura = random.randint(0, 12)
    print(f'Opção selecionada: Poção\nO {self.classe} usou poção e curou {cura} de HP')

  def recuar(self, classe):
    recuar = random.randint(0, 12)
    print('Opção selecionada: Recuar')
    if recuar == 1:
      print(f'Enquanto {self.classe} recuava por um beco escuro, foi surpreendido por um golpe fatal pelas costas e caiu sem vida no chão.')
    elif recuar >= 2 and recuar <= 5:
      print(f'O {self.classe} recebeu um golpe critico enquanto recuava ficando gravemente ferido.')
    elif recuar >= 6 and recuar <= 10:
      print(f'O {self.classe} sofreu algum dano, mas resistiu e viverá para se vingar outro dia.')
    else:
      print('Você tem sentidos afiados, pressentiu o perigo de longe e recuou antes que fosse tarde.')

herois = [
  heroi('Guerreiro','Impacto de Tyr'),
  heroi('Mago','Ira de Thor'),
  heroi('Monge','Punho Supremo de Asura'),
  heroi('Ninja', 'Kunai Explosiva'),
  heroi('Arqueiro', 'Rajada de Flechas'),
  heroi('Mercenário', 'Lâminas Destruidoras')
]

atacante = random.choice(herois)
inimigo = random.choice(herois)

atacante.atacarOutroHeroi(inimigo)

atacante.usoPocao(atacante)

atacante.recuar(atacante)
#Algoritimo produzido por Railson Doglas, com uso de história baseada na franquia de God of War, feito só para fins educativos e sem fins lucrativos.
# A ideia de uma aplicação dessa forma é para caso fosse adicionado mais elementos de personagens, mapa e monstros, o algoritimo não precisasse ser atualizado, é só o database.
#já que o pandas poderia ler os database de um arquivo de fora.

import pandas as pd
# from google.colab import output

#E Aqui criei os DB das informações que vou usar no programa.

Personagens = pd.DataFrame({'Personagem': ['Kratos','Atena','Hércules', 'Afrodite'],
                             'Liberados': ['Libarado','Finalizar no modo Dificil','Finalizar no modo Deus','Finalizar no modo Titã'],
                             'Lore': ['É um espartano com sede de poder que, para salvar sua vida, é forçado a servir o deus Olímpico Ares.', 
                                      'A Deusa da Sabedoria, mentora e aliada de Kratos.', 'Um semi-deus e meio-irmão de Kratos.', 
                                      'Deusa do Amor. Ajuda Kratos ao dar poder a cabeça de Medusa morta,'],
                             'Classe': ['Espartano', 'Deusa','Herói','Deusa']}, 
                             columns = ['Personagem', 'Liberados', 'Lore', 'Classe'])

historia_mapa = pd.DataFrame({'Nome_do_Continente': ['Ilha da Criaçã', 'Barriga da Hidra', 'Esparta'],
                                       'Lore': ['Onde o Rei Bárbaro, que fugiu do Submundo, e querendo vingança, encontra e confronta Kratos na Ilha da Criação.',
                                                'Onde Kratos encontra Capitão do Bote, e começão uma batalha sangrete dentro da barriga da monstruosa Hidra',
                                                'Objeto de fascínio por ser uma gigantesca cidade onde Kratos vai encontrar os mais diversos inimigo.']},
                                      columns = ['Nome_do_Continente', 'Lore'])

Monstros = pd.DataFrame({'Monstro': ['Rei Bárbaro','Capitão do Bote','Callisto', 'Ceryx'],
                             'Lore': ['Comandante de um horda de bárbaros que ameaçava um exército inimigo Espartano.',
                                      'O Capitão do Bote encontra Kratos em várias ocasiões, e em seus encontros pronto para mata-lo.',
                                      'A mãe de Kratos e Deimos. Punida pelos deuses por revelar a identidade do pai de seus filhos, Callisto é transformada em uma besta que Kratos deve matar.',
                                      'O filho do deus Hermes e um mensageiro do Olimpo. Tenta avisar Kratos sobre as consequências de sua jornada sangrenta'],
                             'Classe': ['Bárbaro', 'Guerreiro', 'Besta', 'Semideus']}, 
                             columns = ['Monstro', 'Vida', 'Tipo', 'Elemento'])

#E então tomei a decisão de criar umas funções sendo:

#Vai exibir na tela a história do game.
def hsitoria(): 
  print('''
  Após Kratos se tornar o novo deus da guerra, passa a guiar os soldados de Esparta, liderando-os sobre várias batalhas e destruindo várias cidades.
  Antes de descer do Olimpo para ajudar seus guerreiros espartanos a destruir a cidade de Rodes, Kratos é avisado por Atena sobre as consequências de seus atos.
  Sem escutá-la, ele salta do Olimpo para Rodes e, ao chegar, uma águia retira parte do poder de Kratos e o deposita em uma estátua gigante (o Colosso de Rodes).
  Kratos, com muita raiva e acreditando ser Atena a responsável, vai em busca de derrotar o colosso para provar para os deuses do Olimpo que ele merece ser um deus.
  Nisso, Zeus, num aparente gesto de generosidade, oferece a Kratos a arma que acabou com a Grande Guerra e derrotou os titãs, a Lâmina do Olimpo. Somente com ela,
  Kratos conseguiria derrotar o Colosso.
  ''')

# função para a criação de entras das opçeõs de cada entrada do submenu
def menu(dataframe, key, opcoes):
  for index, nome in enumerate(dataframe[key]): # enumera cada entrada do submenu
    print(str(index) + " - " + nome)
    opcoes.append(str(index) + " - " + nome)
  print(str(index+1) + " - Voltar para o Menu Principal")
  opcoes.append(str(index+1) + " - Voltar para o Menu Principal")   #vai salvar essas entradas para uso futuro


# função apra exibição de informações do mapa do jogo
def mapa():
  opcao = 0
  while True: 
    opcao = int(input('Selecione um mapa: '))
    if opcao < (len(opcoes) - 1):
      #output.clear()
      print(f'''
      Em {historia_mapa['Nome_do_Continente'][opcao]}
      
      {historia_mapa['Lore'][opcao]}
      ''')
      a = "\n"
      print(a.join(opcoes))
    elif opcao == (len(opcoes) - 1):
      #output.clear()
      break
    else:
      #output.clear()
      print('Opção invalida')
      a = "\n"
      print(a.join(opcoes))
      
# função apra exibição das informações dos personagens
def personagens():
  opcao = 0
  while True:
    opcao = int(input('Selecione um Personagem: '))
    if opcao < (len(opcoes) - 1):
      #output.clear()
      print(f'''
      O persongagem {Personagens['Personagem'][opcao]}
      Tem a História:
      {Personagens['Lore'][opcao]}

      Classe: 
      {Personagens['Classe'][opcao]}

      Liberado pra Jogar? 
      {Personagens['Liberados'][opcao]}
      ''')
      a = "\n"
      print(a.join(opcoes))
    elif opcao == (len(opcoes) - 1):
      #output.clear()
      break
    else:
      #output.clear()
      print('Opção invalida')
      a = "\n"
      print(a.join(opcoes))
      
# função apra exibição das informações dos monstros
def monstros():
  opcao = 0
  while True:
    opcao = int(input('Selecione um Monstro: '))
    if opcao < (len(opcoes) - 1):
      #output.clear()
      print(f'''
      O {Monstros['Monstro'][opcao]}

      É um inimigo onde:
      {Monstros['Lore'][opcao]}

      Classe: {Monstros['Classe'][opcao]}
      ''')
      a = "\n"
      print(a.join(opcoes))
    elif opcao == (len(opcoes) - 1):
      #output.clear()
      break
    else:
      #output.clear()
      print('Opção invalida')
      a = "\n"
      print(a.join(opcoes))
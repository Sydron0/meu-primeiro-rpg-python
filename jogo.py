
import os # (Operating System): Para conversar com o seu Windows e mandar ele limpar a tela (os.system('cls')), por exemplo.
import time # Para controlar o tempo e fazer o jogo "dormir" por alguns milissegundos.
import sqlite3 # Traz a ferramenta oficial do Python para lidar com o banco de dados SQLite.

conexao = sqlite3.connect('rpg.db') # Cria a ponte entre o Python e o arquivo do banco. Se o arquivo não existir, ele cria.
cursor = conexao.cursor() # Cria o "mensageiro" que vai levar os comandos SQL até o banco e trazer as respostas.


def digitar(texto): # def é utilizado para criar comandos próprios, assim como o comando "print" do próprio python. def: Vem de Define (Definir). É a palavra que avisa ao Python: "Ei, estou criando um comando novo que não existe no seu dicionário".
    for letra in texto: # Para cada letra dentro do texto. for: Significa Para. É o que chamamos de Laço de Repetição (Loop). Ele diz ao computador para repetir uma ação várias vezes. in: Significa Em ou Dentro de. Lendo a frase toda: for letra in texto: -> "Para cada letra que estiver dentro da variável texto, faça o seguinte:"
        print(letra, end='', flush=True) # Imprime a letra sem pular linha. letra: É apenas o nome de uma variável temporária que nós inventamos na hora. Poderia se chamar x ou batata. O for vai pegar um pedaço do texto e guardar dentro dessa caixa temporária a cada repetição. end='': O comando print original do Python tem um segredo: no final de tudo que ele imprime, ele joga um \n (quebra de linha) invisível. O end (Fim) permite mudar isso. Ao colocar end='' (aspas vazias, sem espaço), dizemos: "No fim do print, não coloque nada, mantenha o cursor colado na mesma linha". flush=True: Flush significa "Dar descarga" ou "Esvaziar". O Windows tenta ser inteligente e guarda os textos numa memória temporária (Buffer) para jogar na tela tudo de uma vez e economizar processamento. Como queremos letra por letra, o flush=True (Esvaziar = Verdadeiro) obriga o Windows a jogar a letra na tela imediatamente, sem esperar.
        if letra in ['&']: # [] (Colchetes): No Python, colchetes criam uma Lista (Array). É como uma variável que guarda várias coisas ao mesmo tempo, separadas por vírgula.
            time.sleep(2)
            
        else:
            time.sleep(0.04) # Espera 0.04 segundos antes da próxima letra. 
    print() # Pula uma linha quando terminar a frase toda.

time.sleep(1) # Pausar 1 segundo
os.system('cls') # Limpar a tela

digitar("\nQual seu nome, Herói?") # Se eu não quiser que alguma informação do input seja jogada na tela de uma vez, eu deixo ele em branco e coloco um print ou comando antes dele.
nome_jogador = input("> ") # Se o input é uma resposta que vai ser guardada na variável, esse input fica na própria variável.

# SELECT: Comando SQL para buscar dados. *: Curinga que significa "Todas as colunas". WHERE: Filtro "Onde". ?: Placeholder de segurança.
comando_sql = """
    SELECT * FROM jogador WHERE nome = ?""" # ? = O Placeholder (Marcador de Posição). É o espaço em branco seguro que o cursor vai preencher com a variável que passarmos na Tupla, evitando o ataque de *SQL Injection*.
cursor.execute(comando_sql, (nome_jogador,)) # Executa o comando específicado no parentese.
                                             # A tupla (nome_jogador,) não pode ficar dentro do comando SQL, tem que ser colocado diretamente no execute. A vírgula é obrigatória quando a tupla tem só 1 item.

resultados = cursor.fetchall() # Fetchall é o comando do cursor que significa "Busque todos". Ele pega tudo que o `SELECT` achou e devolve no formato de uma Lista []

if len(resultados) == 0: # len() Vem de "Length" (Tamanho). Ferramenta do Python que conta quantos itens existem dentro de uma lista. == 0: Compara se o tamanho da lista é zero. Se for zero, significa que o banco procurou o nome e não achou ninguém (é um jogador novo).
    comando_sql = """ 
        INSERT INTO jogador (nome, vida, nivel) VALUES (?, ?, ?)""" # Insere uma nova linha na tabela
    
    cursor.execute(comando_sql, (nome_jogador, 100, 1)) # Executa o comando específicado no parentese.

    conexao.commit() # O "Salvar" definitivo. Confirma as alterações no disco rígido.
    
    id_jogador = cursor.lastrowid # Verifica o ID da última linha criada.

    vida = 100 # Variável criada por mim com um valor específicado para ser usada no jogo agora.
    nivel = 1 # Variável criada por mim com um valor específicado para ser usada no jogo agora.

else:
    digitar(f'\nSave Encontrado. ')
    time.sleep(2)
    digitar(f'\nCarregando...' )
    time.sleep(3)
    
    # resultados[0]: Pega o primeiro item (posição 0) da lista que veio do banco. Ex: (1, 'Anderson', 100, 1)
    linha = resultados[0] 
    
    # linha[2]: Pega o terceiro item da tupla (posição 2), que é a coluna 'vida' no banco de dados.
    vida = linha[2] 
    
    # linha[3]: Pega o quarto item da tupla (posição 3), que é a coluna 'nivel' no banco de dados.
    nivel = linha[3] 
    
    id_jogador = linha[0] # Pega o primeiro item da tupla que, no caso, é o ID.
    
    

inventario = [] # [] Significa Lista ou Array. Uma caixa grande, pronta para receber vários itens. 
                # Como eu coloco um item dentro dessa lista sem apagar o que já tem lá? Nós usamos um "feitiço" das listas chamado .append() (que significa "anexar" ou "acrescentar ao final").
                # inventario.append("Porção de Cura"). Agora você tem 1 item.
                # inventario.append("Chave"). Agora você tem 2 itens.

os.system('cls')

digitar(f"\nBem-vindo a Jornada, {nome_jogador}") # O "f" dentro do print serve para chamar uma variável através de {}.

digitar(f"\n--- SEUS STATUS ---\n \nVida = {vida}\n \nNível = {nivel}") # \n serve para pular a linha (o mesmo que apertar enter). Se usando no início do print, ele da um "enter" antes de imprimir o texto.

time.sleep(2)
os.system('cls')

digitar(f"\nVocê está caminhando por uma floresta e de repente se depara com uma caverna. ")

time.sleep(2)

os.system('cls')

digitar("\nVocê deseja entrar na caverna?")
escolha = input("> ")

os.system('cls')

if escolha == "Sim": # Sinal de igual "=" significa RECEBE, dois sinais de igual "==" significa COMPARAR se alguna coisa é igual a outra.
    vida_urso = 40
    digitar(f"\nVocê entra na caverna e se depara com um Urso! Vida: {vida_urso} ")
    
    
    
    while True: # O while repete algo enquanto uma condição for verdadeira. Cria o loop infinito. Tudo que tem TAB abaixo dele vai repetir.
        digitar(f"\nO que você faz? (1 - Atacar | 2 - Fugir | 3 - Cantar)")
        acao = input("> ")
        
                
        os.system('cls')
        
        if acao == "1":
            digitar(f"\nVocê ataca o urso! ")
            digitar(f'\nO Urso recebe 20 de dano. ')
            vida_urso = vida_urso - 20
            digitar(f'\nA Vida do Urso agora é {vida_urso}. ')
            
            
            if vida_urso <= 0:
                digitar(f"\nVocê venceu! ")
                time.sleep(2)
                inventario.append("Pele de Urso")
                os.system('cls')
                digitar(f'\nVocê recebeu "Pele de Urso"! ')
                
                comando_sql = """
                    INSERT INTO inventario (id_jogador, nome_item) VALUES (?, ?)""" # Insere uma nova linha na tabela.
                cursor.execute(comando_sql, (id_jogador, "Pele de Urso")) # Executa o comando entre ().
                conexao.commit()
                             
                digitar(f'\nSeu inventário: {inventario}. ')
                time.sleep(2)
                digitar(f'\nFim de Jogo! ')
                time.sleep(3)
                os.system('cls')
                break
                                          
            time.sleep(2)
            os.system('cls')
            
            digitar(f'\nO Urso contra-ataca! ')
            digitar(f'\nVocê recebe 20 de dano. ')
            vida = vida - 20
            digitar(f"\nSua Vida agora é {vida}. ")
            
            comando_sql = """
                UPDATE jogador SET vida = ? WHERE nome = ?""" # Comando para atualizar a vida e o nome que vão ser passados na tupla no execute.
                                                              # REGRA: Nunca faça um UPDATE sem WHERE, se fizer, toda a tabela vai ser atualizada.
            cursor.execute(comando_sql, (vida, nome_jogador)) # As informações da tupla tem que ser na ordem exata da variável executada (comando_sql)
            conexao.commit()
            
            time.sleep(2)
            os.system('cls')
            
            if vida <= 0:
                digitar(f"\nVocê não resistiu aos ferimentos. Você morre! ")
                time.sleep(2)
                digitar(f'\nFim de Jogo! ')
                time.sleep(3)
                os.system('cls')
                break # Mas como saímos desse pesadelo? Usando a palavra mágica break (Quebrar). Quando o Python lê break, ele destrói o loop e o jogo continua para baixo.
                
          
        elif acao == "2":
            digitar(f"\nVocê tenta correr, mas o urso é mais rápido e te alcança.\n \nCom a velocidade, o ataque do urso é mais forte, você recebe 100 de dano! ")
            vida = vida - 100
                        
            digitar(f"\nSua vida desceu para {vida}. Você morre! ")
            time.sleep(2)
            digitar(f'\nFim de Jogo! ')
            time.sleep(3)
            os.system('cls')
            break
            
        elif acao == "3":
            digitar(f"\nVocê começa a cantar! & & & ... ")
            digitar(f"\nO urso dorme... ")
            time.sleep(2)
            digitar(f"\nVocê consegue fugir! ")
            time.sleep(2)
            digitar(f'\nFim de Jogo! ')
            time.sleep(3)
            os.system('cls')
            break
                
        
        else:
            digitar(f"\nVocê desmaia e o urso come você! ")
            vida = vida - 100
        
            time.sleep(1)
            digitar(f"\nVocê morre! ")
            time.sleep(2)
            digitar(f'\nFim de Jogo! ')
            time.sleep(3)
            os.system('cls')
            break
        
else:
    digitar(f"\nVocê entrelaça o rabo entre as pernas e vai para casa. Fim! ")
    time.sleep(2)
    digitar(f'\nFim de Jogo! ')
    time.sleep(3)
    os.system('cls')
    
    
conexao.close() # Fecha a ponte. Regra de ouro: abriu, usou, fechou.
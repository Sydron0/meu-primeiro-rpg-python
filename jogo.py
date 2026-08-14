import os # (Operating System): Para conversar com o seu Windows e mandar ele limpar a tela (os.system('cls')), por exemplo.
import time # Para controlar o tempo e fazer o jogo "dormir" por alguns milissegundos.

def digitar(texto): # def é utilizado para criar comandos próprios, assim como o comando "print" do próprio python. def: Vem de Define (Definir). É a palavra que avisa ao Python: "Ei, estou criando um comando novo que não existe no seu dicionário".
    for letra in texto: # Para cada letra dentro do texto. for: Significa Para. É o que chamamos de Laço de Repetição (Loop). Ele diz ao computador para repetir uma ação várias vezes. in: Significa Em ou Dentro de. Lendo a frase toda: for letra in texto: -> "Para cada letra que estiver dentro da variável texto, faça o seguinte:"
        print(letra, end='', flush=True) # Imprime a letra sem pular linha. letra: É apenas o nome de uma variável temporária que nós inventamos na hora. Poderia se chamar x ou batata. O for vai pegar um pedaço do texto e guardar dentro dessa caixa temporária a cada repetição. end='': O comando print original do Python tem um segredo: no final de tudo que ele imprime, ele joga um \n (quebra de linha) invisível. O end (Fim) permite mudar isso. Ao colocar end='' (aspas vazias, sem espaço), dizemos: "No fim do print, não coloque nada, mantenha o cursor colado na mesma linha". flush=True: Flush significa "Dar descarga" ou "Esvaziar". O Windows tenta ser inteligente e guarda os textos numa memória temporária (Buffer) para jogar na tela tudo de uma vez e economizar processamento. Como queremos letra por letra, o flush=True (Esvaziar = Verdadeiro) obriga o Windows a jogar a letra na tela imediatamente, sem esperar.
        if letra in ['&']: # [] (Colchetes): No Python, colchetes criam uma Lista (Array). É como uma variável que guarda várias coisas ao mesmo tempo, separadas por vírgula.
            time.sleep(2)
            
        else:
            time.sleep(0.04) # Espera 0.04 segundos antes da próxima letra. 
    print() # Pula uma linha quando terminar a frase toda.

print()
time.sleep(1)
os.system('cls')

digitar("\nQual seu nome, Herói?") # Se eu não quiser que alguma informação do input seja jogada na tela de uma vez, eu deixo ele em brando e coloco um print ou comando antes dele.
nome_jogador = input("> ") # Se o input é uma resposta que vai ser guardada na variável, esse input fica na própria variável.

vida = 100

nivel = 1

os.system('cls')

digitar(f"\nBem-vindo a Jornada, {nome_jogador}") # O "f" dentro do print serve para chamar uma variável através de {}.

digitar(f"\n--- SEUS STATUS ---\n \nVida = {vida}\n \nNível = {nivel}") # \n serve para pular a linha (o mesmo que apertar enter). Se usando no início do print, ele da um "enter" antes de imprimir o texto.

time.sleep(2)
os.system('cls')

digitar(f"\nVocê está caminhando por uma floresta e de repente se depara com uma caverna.\n")

time.sleep(2)

os.system('cls')

digitar("\nVocê deseja entrar na caverna?")
escolha = input("> ")

os.system('cls')

if escolha == "Sim": # Sinal de igual "=" significa RECEBE, dois sinais de igual "==" significa COMPARAR se alguna coisa é igual a outra.
    digitar(f"\nVocê entra na caverna e se depara com um Urso! ")
    
    while True: # O while repete algo enquanto uma condição for verdadeira. Cria o loop infinito. Tudo que tem TAB abaixo dele vai repetir.
        digitar(f"\nO que você faz? (1 - Atacar | 2 - Fugir | 3 - Cantar)")
        acao = input("> ")
        
                
        os.system('cls')
        
        if acao == "1":
            digitar(f"\nVocê ataca o urso mas não faz efeito, pois você é muito fraco. ")
            digitar(f"\nVocê recebe um contra-ataque. 20 de dano! ")
            vida = vida - 20
            
            digitar(f"\nSua vida desceu para {vida}. ")
            
            time.sleep(2)
            
            os.system('cls')
            
            if vida <= 0:
                digitar(f"\nVocê não resistiu aos ferimentos. Você morre! ")
                break # Mas como saímos desse pesadelo? Usando a palavra mágica break (Quebrar). Quando o Python lê break, ele destrói o loop e o jogo continua para baixo.
                
          
        elif acao == "2":
            digitar(f"\nVocê tenta correr, mas o urso é mais rápido e te alcança.\n \nCom a velocidade, o ataque do urso é mais forte, você recebe 100 de dano! ")
            vida = vida - 100
                        
            digitar(f"\nSua vida desceu para {vida}. Você morre! " )
            break
            
        elif acao == "3":
            digitar(f"\nVocê começa a cantar! & & & ... ")
            digitar(f"O urso dorme... ")
            time.sleep(1)
            digitar(f"Você consegue fugir! ")
            break
                
        
        else:
            digitar(f"\nVocê desmaia e o urso come você! ")
            vida = vida - 100
        
            time.sleep(1)
            digitar(f"\nVocê morre! ")
            break
        
else:
    digitar(f"\nVocê entrelaça o rabo entre as pernas e vai para casa. Fim!")
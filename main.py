from os import system
from googletrans import Translator

# ======== FILES ===================
portuguese = open('README.md', 'w+', 1, 'utf-8')
english = open('README-en.md', 'w+', 1, 'utf-8')

# ======== Tranlator ===================
translator = Translator()

# ======== Utils ===================

def create_image(alt, path):
    return f"![{alt}]({path})"

def write_file(message, translate):
    portuguese.write(f'{message}\n\n')
    if translate:
        message = translator.translate(message).text
    english.write(f'{message}\n\n')

def write_title(text, order):
    write_file(f'{"#"*order} {text}', order != 1)

def write_lista(txt):
    write_file(f'- {txt}', False)

def write_link(txt, url):
    return f'[{txt}]({url})'

# ======== Criar Seções ===================
def create_outdoor(): 
    system('cls')   
    title = input('Qual o nome do projeto: ')
    descricao = input('Descreva brevemente o projeto: ')
    image = create_image(title, './readme-images/main-image.png')
    write_title(title, 1)
    write_file(image, False)
    write_file(descricao, True)

def create_sobre():
    system('cls')   
    explicacao = input("Explique mais sobre o projeto (O que ele faz, usando o que): ")
    write_title("Sobre", 2)
    write_file(explicacao, True)


def create_tecnologias():
    system('cls')   
    lista_tecnologias = input("Quais tecnologias e linguagens foram usadas (separe-as por vírgula): ").split(', ')
    write_title('Tecnologias', 2)
    for tec in lista_tecnologias:
        write_lista(tec)


def create_documentation():
    system('cls')   
    write_title("APIs e Bibliotecas", 2)
    resposta = input('Foi usada alguma biblioteca ou alguma api foi consumida (S/N): ').upper()
    if resposta != 'S':
        return 
    print("As informações devem ser insiridas de uma API/lib de cada vez!!")
    while True:
        api_lib = input("Digite o nome da API/lib: ")
        link = input("Digite o link da documentação da API/lib: ")
        write_lista(write_link(api_lib, link))
        resposta = input('Deseja continuar (S/N): ').upper()
        if resposta != 'S':
            break


create_outdoor()
write_file('---', False)
create_sobre()
write_file('---', False)
create_tecnologias()
write_file('---', False)
create_documentation()
write_file('---', False)

portuguese.close()
english.close()
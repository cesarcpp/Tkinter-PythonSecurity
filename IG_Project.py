import hashlib
import os
import phonenumbers
import random
import string
import time
from tkinter import *
from phonenumbers import geocoder


def verificar_ip():
    print('-' * 60)
    ip_host = input("Digite o IP ou Host a ser verificado: ")
    time.sleep(2)
    os.system(f' ping -n 4 {ip_host} ')
    print('-' * 60)

def gerar_senha():
    def gerar():
        pegar_dado = vsenha.get()
        tamanho = int(pegar_dado)
        chars = string.ascii_letters + string.digits + '!@#$%&*-+=§^?/|\ç'
        rnd = random.SystemRandom()
        senha_aleatoria["text"] = "".join(rnd.choice(chars) for i in range(tamanho))

    janela_2 = Tk()
    janela_2.title("Gerador de Senhas")
    janela_2.geometry("300x200")
    janela_2.configure(background="#F0F8FF")
    janela_2.maxsize(300, 200)
    janela_2.minsize(300, 200)

    Label(janela_2, text="Informe o tamanho da senha desejada:", anchor=W, background="#00BFFF",
          font="-weight bold -size 9").place(x=10, y=10, width=250, height=30)
    vsenha = Entry(janela_2, background="#C0C0C0")
    vsenha.place(x=10, y=40, width=30, height=20)

    Button(janela_2, text="Gerar", command=gerar).place(x=10, y=70, width=50, height=20)

    senha_aleatoria = Label(janela_2, text="")
    senha_aleatoria.place(x=10, y=100, width=80, height=20)

    janela_2.mainloop()

def verifica_telefone():
    def verificar():
        tel = vtel.get()
        phone = phonenumbers.parse(tel)
        time.sleep(1)
        res_tel["text"] = "O número informado é de " + geocoder.description_for_number(phone, 'pt')

    janela_3 = Tk()
    janela_3.title("Verificador de Telefone")
    janela_3.geometry("300x200")
    janela_3.configure(background="#F0F8FF")
    janela_3.maxsize(300,200)
    janela_3.minsize(300,200)

    Label(janela_3, text="Informe o telefone a ser verificado:", anchor=W, background="#00BFFF", font="-weight bold -size 9").place(x=10, y=10, width=210, height=30)

    vtel = Entry(janela_3,background="#C0C0C0")
    vtel.insert(0, "Ex: +551140088922")
    vtel.place(x=10, y=40, width=110, height=20)

    Button(janela_3, text="Verificar", command=verificar).place(x=10, y=70, width=50, height=20)

    res_tel = Label(janela_3, text="")
    res_tel.place(x=10, y=90, width=250, height=30)
    
    janela_3.mainloop()

def gerar_hashs():
    print('-' * 60)
    string = input("Digite o texto a ser gerado a Hash: ")
    menu = int(input(''' #MENU - ESCOLHA O TIPO DE HASH #
                                       [1] md5
                                       [2] Sha1
                                       [3] Sha256
                                       [4] Sha512

                                       Digite o número do hash a ser gerado: '''))
    time.sleep(2)
    if menu == 1:
        resultado = hashlib.md5(string.encode('utf-8'))
        print("O Hash da string por MD5 é: ", resultado.hexdigest())
    elif menu == 2:
        resultado = hashlib.sha1(string.encode('utf-8'))
        print("O Hash da string por SHA1 é: ", resultado.hexdigest())
    elif menu == 3:
        resultado = hashlib.sha256(string.encode('utf-8'))
        print("O Hash da string por SHA256 é: ", resultado.hexdigest())
    elif menu == 4:
        resultado = hashlib.sha512(string.encode('utf-8'))
        print("O Hash da string por SHA256 é: ", resultado.hexdigest())
    else:
        print("Ocorreu um erro, tente novamente")
        print('-' * 60)


janela = Tk()
janela.geometry("240x300")
janela.title("System")
janela.config(padx=20, pady=10)
janela.configure(background="#A9A9A9")
janela.maxsize(240, 300)
janela.minsize(240, 300)

texto_apresentacao = Label(janela, text="Olá! Seja bem-vindo(a)", font="-weight bold")
texto_apresentacao.grid(column=0, row=0, padx=10, pady=5)

texto_orientacao = Label(janela, text="Escolha uma das opções abaixo:", font=" -size 7")
texto_orientacao.grid(column=0, row=1, padx=10, pady=5)

ip = Button(janela, text="Verificar IP", command=verificar_ip, background="#FFD700")
ip.grid(column=0, row=2, padx=10, pady=5)

senha = Button(janela, text="Gerar Senha", command=gerar_senha, background="#FFD700")
senha.grid(column=0, row=3, padx=10, pady=5)

tel = Button(janela, text="Verificar Telefone", command=verifica_telefone, background="#FFD700")
tel.grid(column=0, row=4, padx=10, pady=5)

hashs = Button(janela, text="Gerar Hash", command=gerar_hashs, background="#FFD700")
hashs.grid(column=0, row=5, padx=10, pady=5)

janela.mainloop()
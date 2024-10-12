# Made By: newbiebel
# Lembre se de instalar as bibliotecas necessárias, sendo elas:
# pip install customtkinter 
# pip install qrcode
# pip install pillow

#-----------------------------------------------------------------------------

import customtkinter as ctk #Importando o customtkinter
import qrcode #Importando a biblioteca qrcode
from tkinter import filedialog, messagebox #filedialog é uma biblioteca para tratar com salvamento e abertura de arquivos, messagebox para uma caixa de mensagem
from PIL import Image, ImageTk # Python Image Libraly (Ou Pillow) é uma biblioteca para manipular imagens
#-----------------------------------------------------------------------------

#Funções 
def gerarQR():
    global codigoQR
    link = url.get()
    if link:
        codigoQR = qrcode.make(link)
        salvar.configure(state=ctk.NORMAL)
        codigoQR = codigoQR.resize((250, 250))
        criarImagem = ImageTk.PhotoImage(codigoQR)
        imagem.configure(image=criarImagem)
        imagem.image = criarImagem
            
    else:
        messagebox.showwarning('ERRO!','Nenhum link inserido, por favor insira um Link')
        codigoQR = None
        salvar.configure(state=ctk.DISABLED)
        imagem.configure(image='')
    
    
def salve():
    origemArquivo = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("Arquivos PNG", "*.png"), ("Todos os arquivos", "*.*")])
    if origemArquivo and codigoQR:
        codigoQR.save(origemArquivo)

#-----------------------------------------------------------------------------

#Criação da janela e definição de titulo       
janela = ctk.CTk('black')
janela.minsize(600, 480)
janela.maxsize(600, 480)
ctk.set_appearance_mode('dark')
janela.title('Gerador de QR Code')
janela.iconbitmap("YouTube_23392.ico")
#-----------------------------------------------------------------------------

#Labels, Entry e Buttons
titulo = ctk.CTkLabel(janela,text='Gerador de QR Code',font=('Arial',25,'bold'), text_color='white')
titulo.pack(padx= 10,pady = 10)

url = ctk.CTkEntry(janela,placeholder_text='Cole aqui a URL desejada',width=350)
url.pack(padx = 20, pady = 15)

gerar = ctk.CTkButton(janela,text='Gerar QR Code',command=gerarQR,width=180,height=30, fg_color="darkred", text_color="white", hover_color="red")
gerar.place(x=100,y=130)

salvar = ctk.CTkButton(janela,text='Salvar QR Code',command=salve,state=ctk.DISABLED,width=180,height=30, fg_color="darkred", text_color="white",hover_color="red")
salvar.place(x=320,y=130)

imagem = ctk.CTkLabel(janela,text='')
imagem.place(x=180,y=200)

#-----------------------------------------------------------------------------

#Inicialização da variavel e da janela
codigoQR = None
janela.mainloop()

#-----------------------------------------------------------------------------

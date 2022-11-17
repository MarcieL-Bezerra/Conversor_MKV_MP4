import sys
import tkinter as tk
from tkinter import ttk
import tkinter.filedialog as fdlg
import tkinter.messagebox as tkMessageBox
from tkinter import *
from conversor import Conversor

def ConverteVideo():
	
    try:
        #aqui seleciona os arquivos
        #nomedoarquivo = TxtOrigem.get()
        #path = fdlg.askopenfilenames()
        #df = pd.DataFrame()
        #aqui seleciona a pasta a ser colocada o novo arquivo
        TxtDestino.config(state='normal')
        TxtOrigem.config(state='normal')
        comboFormato.config(state='normal')
        TxtOrigem.delete(0,"end")
        TxtDestino.delete(0,"end")

        LblStatus.grid(row=11,column=1)
        LblStatus.configure(text = "Aguarde ... ...")
        tkMessageBox.showinfo("Selecionar Pasta", message= "Selecione Pasta de Origem!")
        opcoes = {}                # as opções são definidas em um dicionário
        opcoes['initialdir'] = ''    # será o diretório atual
        opcoes['parent'] = tinicial
        opcoes['title'] = 'Selecione Pasta para salvar!'
        caminhoOrigem = fdlg.askdirectory(**opcoes)

        TxtOrigem.insert(0,caminhoOrigem)
        

        #aqui seleciona a pasta a ser colocada o novo arquivo
        tkMessageBox.showinfo("Selecionar Pasta", message= "Selecione Pasta de Destino!")
        opcoes = {}                # as opções são definidas em um dicionário
        opcoes['initialdir'] = ''    # será o diretório atual
        opcoes['parent'] = tinicial
        opcoes['title'] = 'Selecione Pasta de destino!'
        caminhoFinal = fdlg.askdirectory(**opcoes)

        TxtDestino.insert(0,caminhoFinal)

        TxtDestino.config(state='disabled')
        TxtOrigem.config(state='disabled')
        comboFormato.config(state='disabled')
        tinicial.update()

        chamando = Conversor()
        chamando.origem = caminhoOrigem
        chamando.destino = caminhoFinal
        chamando.formato ="." + comboFormato.get()

        if (chamando.origem  and chamando.destino):
            chamando.ExecultaConversao()
        else:
            tkMessageBox.showinfo("Erro Caminhos", message= "Verifique os caminhos!")
            sys.exit()
        # df.to_excel(caminhoFinal +'/'+ nomedoarquivo +"-"+ data_atual + '.xlsx', index=False)
        
        LblStatus.configure(text = "Finalizado")
        tkMessageBox.showinfo("Finalizado", message= "Finalizado verifique em: " + caminhoFinal)
        TxtDestino.config(state='normal')
        TxtOrigem.config(state='normal')
        comboFormato.config(state='normal')
        TxtOrigem.delete(0,"end")
        TxtDestino.delete(0,"end")
    except :
        tkMessageBox.showinfo("Erro2", message= "Tente Novamente!")
        LblStatus.configure(text = "Tente novamente")
        TxtDestino.config(state='normal')
        TxtOrigem.config(state='normal')
        comboFormato.config(state='normal')
        TxtOrigem.delete(0,"end")
        TxtDestino.delete(0,"end")
                
	


tinicial = tk.Tk()
tinicial.geometry("800x550+200+100")
tinicial.title("Conversor de Vídeos")
tinicial.resizable(width=False, height=False)
tinicial['bg'] = 'Cornsilk'
tinicial.iconphoto(True, PhotoImage(file='./arquivos/convert.png'))
image=PhotoImage(file='./arquivos/convert.png')

robozinho = Label(tinicial, image = image,width=780, height=440,bg ="white")
robozinho.grid(rowspan=10,columnspan =10,pady=10, padx=10)

cmdCadastrar=Button(tinicial,bd=8,bg = 'SKyBlue1',fg='black',text='Selecionar',font=('arial',14,'bold'),
	command = ConverteVideo).grid(row=12,column=1)

LblOrigem=Label(tinicial,bd=4,bg = 'SKyBlue1',fg='black',text='Origem',font=('arial',10,'bold'),height=1).grid(row=11, column=3)
TxtOrigem=Entry(tinicial,bd=4,bg = 'white',fg='black',font=('arial',10,'bold'),width=50,)
TxtOrigem.grid(row=11, column=4)
# TxtOrigem.insert(0,"Relatorio-Excell")

LblDestino=Label(tinicial,bd=4,bg = 'SKyBlue1',fg='black',text='Destino',font=('arial',10,'bold'),height=1).grid(row=12, column=3)
TxtDestino=Entry(tinicial,bd=4,bg = 'white',fg='black',font=('arial',10,'bold'),width=50,)
TxtDestino.grid(row=12, column=4)

LblFormato=Label(tinicial,bd=4,bg = 'SKyBlue1',fg='black',text='Formato',font=('arial',10,'bold'),height=1).grid(row=11, column=5)
comboFormato = ttk.Combobox(tinicial,width=9,values=["mp4","mkv"],font=('arial',10,'bold'))
comboFormato.grid(row=12,column=5)
comboFormato.current(0)

LblStatus=Label(tinicial,bd=4,bg = 'SKyBlue1',fg='black',text='',font=('arial',10,'bold'),height=1)

tinicial.mainloop()



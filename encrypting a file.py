# encrypting a file
import os,webbrowser
from tkinter import *
from tkinter import filedialog
root=Tk()
root.geometry('600x300')
bg=PhotoImage(file=r'C:\Users\Engr M2j\Desktop\public repo\Encrypter-Decrypter-Software\logo.png')
root.iconphoto(False,bg)
frameCon=Frame(root)
frameBu=Frame(root,pady=20)
frameSocial=Frame(root,relief= 'sunken', pady=50)
frameAct=Frame(frameBu,pady=20)
root.title('File Encrypter/Decrypter software by Sule Muhammed Abba-TopTech Script')
from cryptography.fernet import Fernet
# fileLoc=''
def callbackF(url):
    webbrowser.open_new(url)
buttonL=Button(frameSocial,text='LinkedIn', command=lambda :callbackF('https://www.linkedin.com/in/sule-muhammed-abba-b-eng-hcia-a83a8714b/'))
buttonY=Button(frameSocial,text='YouTube', command=lambda :callbackF('https://www.youtube.com/channel/UCC3kkjehaQyQ1w0jaz6Md6A'))
buttonG=Button(frameSocial,text='GitHub', command=lambda :callbackF('https://github.com/muhacolee4'))
buttonS=Button(frameSocial,text='Stack Overflow', command=lambda :callbackF('https://stackoverflow.com/users/18455227/engr-sule-muhammed-abba'))
buttonC=Button(frameSocial,text='Contract me', command=lambda :callbackF('https://api.whatsapp.com/send/?phone=%2B2348168737533&text=chatting+from+Encryter/Decrypter+software'))


pwd=os.getcwd()
def selectFile():
    global fileLoc
    fileName=filedialog.askopenfilename(initialdir=pwd,title='Select file',filetypes=(('Text files','*.txt*'),('All files','*.*')))
    labelEplorer.configure(text='selected file path: '+fileName)
    fileLoc=fileName
    print(fileLoc)
labelEplorer=Label(frameCon,text='File not selected',relief= 'sunken', bg= "white", width=100,height=10)
buttonBrowse=Button(frameBu,text="select file",command=selectFile)
# fileExtension=r'.docx'
def encrypt():
    print(fileLoc)
    print(pwd)
    file,extention=os.path.splitext(fileLoc)
    key=os.environ['key']
    with open(str(file)+str(extention),'rb') as fileToBeEncrypted:
        old=Fernet(key).encrypt(fileToBeEncrypted.read())
    fileSaveAs=filedialog.asksaveasfilename(title='Save encrypted file as')
    with open(str(fileSaveAs)+str(extention),'wb')as newfile:

     newfile.write(old)
     labelEplorer.configure(text='File encrypted successfully. Select a new file to encrypt or decrypt')
     
buttonEncrypt=Button(frameAct,text='Encrypt',command=encrypt)

#decrypt code
def decrypt():
    key=os.environ['key']
    file,extention=os.path.splitext(fileLoc)

    with open(str(file)+str(extention),'rb') as fileToBeDecrypted:
        old=Fernet(key).decrypt(fileToBeDecrypted.read())
    fileSaveAs=filedialog.asksaveasfilename(title='Save encrypted file as')

    with open(str(fileSaveAs)+str(extention),'wb')as newfile:
        newfile.write(old)
    labelEplorer.configure(text='File decrypted successfully. Select a new file to encrypt or decrypt')
frameSocial.pack()
buttonDecrypt=Button(frameAct,text='Decrypt',command=decrypt)

frameCon.pack()
buttonL.grid(row=0,column=0)
buttonY.grid(row=0,column=1)
buttonS.grid(row=0,column=2)
buttonC.grid(row=0,column=3)
buttonG.grid(row=0,column=4)

labelEplorer.pack()
buttonBrowse.pack()
frameBu.pack()
frameAct.pack()


buttonEncrypt.grid(row=0,column=0)
buttonDecrypt.grid(row=0,column=1)
root.mainloop()
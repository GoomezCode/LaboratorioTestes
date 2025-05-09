import customtkinter as ctk

ctk.set_appearance_mode("dark")

def validarLogin():
    usuario = inputUsuario.get()
    senha = inputSenha.get()

    if usuario == "Daniel" and senha == "20081009":
        resultado.configure(text="Login efetuado com sucesso", text_color="green")
    
        
        



app = ctk.CTk()
app.title("Sistema De Login Isaac")
app.geometry("300x300")

txtUsuario = ctk.CTkLabel(app, text="Usuario")
txtUsuario.pack(pady=10)

inputUsuario = ctk.CTkEntry(app, placeholder_text="Digite o seu Usuario")
inputUsuario.pack()

txtSenha = ctk.CTkLabel(app, text="Senha")
txtSenha.pack(pady=10)

inputSenha = ctk.CTkEntry(app, placeholder_text="Digite sua senha")
inputSenha.pack(pady=10)

btnLogin = ctk.CTkButton(app, text="login", command=validarLogin())
btnLogin.pack(pady=10)

resultado = ctk.CTkLabel(app, text='')
resultado.pack(pady=10)

app.mainloop()
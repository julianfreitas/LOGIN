usuarios = []  ##ESTRUTURA DE DADOS
executar = True


  ##INICIO DA APLICAÇÃO

def inicio():
    global  executar
    while executar:
      print("1_Efetuar registro")
      print("2_sair")
      opcao = input()
      if(opcao == "1"):
        print("ok, vamos lá")
        break
      elif(opcao == "2"):
        print("bye")
        executar = False
      else:
       print("opção invalida")
    
 
     
     ##REGISTRAR USUARIOS
     
def registar():
    if not executar:
        return 
    novo_usuario = input("digite um novo usuario\n")
    if novo_usuario in usuarios:
            print("usuario ja existe")
    else:
        nova_senha = input("digite uma senha\n")
        
        usuarios.append({"usuario": novo_usuario, "senha":nova_senha})
        print("usuario registrado com sucesso!!")    
    
    
    ##AUTENTICAR USUARIOS
    
    
def autenticar():
    if not executar:
        return
    usuario_input = input("digite seu usuario\n")
    senha_input = input("digite sua senha\n")
    
    
    for usuario in usuarios:
     if usuario["usuario"] == usuario_input and usuario["senha"] == senha_input:
        print("logado com sucesso!!")
        return  
    else:
        print("erro, usuario e/ou senha erradas")
        autenticar()
    



inicio()
registar()
autenticar()
    
    
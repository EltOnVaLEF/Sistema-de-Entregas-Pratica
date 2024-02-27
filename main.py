import modules
from time import sleep
import datetime

Usuario_Atual = "Nenhum"
#INICIO DO PROGRAMA -----------------------------------------------------------
while True:
    print (f'Usuario Atual: {Usuario_Atual}')
    modules.Tittle('SISTEMA DE ENTREGAS')
    modules.Menu('USUARIO','EVENTOS','SAIR')
    modules.Line ('SISTEMA DE ENTREGAS')
    Resp = modules.Answers ('Escolha sua opção |',3)
    modules.Loading()
#AREA DO USUARIO -----------------------------------------------------------------------
    if Resp == 1: 
        while True:
            modules.Tittle('USUARIO')
            modules.Menu('LOGIN','CADASTRAR','MEUS EVENTOS','VOLTAR')
            modules.Line('USUARIO')
            Resp = modules.Answers('Escolha sua opção |',4)
            modules.Loading
#LOGIN ----------------------------------------------------------------------------------
            if Resp == 1: 
                modules.Tittle('LOGIN') 
                while True:
                    Entrar_User = str(input('Usuario: '))
                    Entrar_Senha = str(input('Senha: '))
                    if modules.login (Entrar_User,Entrar_Senha):
                        modules.Line('Login efetuado com sucesso!')
                        print ('Login efetuado com sucesso!')
                        modules.Line('Login efetuado com sucesso!')
                        modules.Loading()
                        Usuario_Atual = Entrar_User
                        break
                    else:
                        modules.Line('USUARIO OU SENHA INCORRETOS')
                        print ('USUARIO OU SENHA INCORRETOS')
                        modules.Line('USUARIO OU SENHA INCORRETOS')
                        modules.Loading()
                        break
#CADASTRO ----------------------------------------------------------------------------
            elif Resp == 2: 
                modules.Tittle('CADASTRO')
                while True:
                        User = str(input('Usuario: ')).strip()
                        if User == "":
                            print ("ERRO... DIGITE UM VALOR VALIDO!") 
                        else:
                            break
                while True:
                        Email = str(input('Email: ')).strip()
                        if Email == "":
                            print ("ERRO... DIGITE UM VALOR VALIDO!")
                        else:
                            break
                while True:            
                        Password = str(input('Senha: ')).strip()
                        if Password == "":
                            print ("ERRO... DIGITE UM VALOR VALIDO!")
                        else:
                            break
                try:
                    with open('user.data','a') as User_Cadastro:
                        User_Cadastro.write(User)
                    with open('email.data', 'a') as Email_Cadastro:
                        Email_Cadastro.write(Email)
                    with open('password.data', 'a') as Password_Cadastro:
                        Password_Cadastro.write(Password)
                    print ('USUARIO CADASTRADO COM SUCESSO!')
                    modules.Loading()
                    break
                except:
                    print ('UM ERRO OCORREU DURANTE O PROCESSO, TENTE NOVAMENTE')
                    break  
 #MEUS EVENTOS --------------------------------------------------------------------------
            elif Resp == 3:
                while True:
                    modules.Tittle('MEUS EVENTOS')
                    if Usuario_Atual == "Nenhum":
                        print ('Por favor, realize o Login para acessar está area.')
                        modules.Line('MEUS EVENTOS')
                        break
                    else:
                        try:
                            with open (f'user-data/{Usuario_Atual}.data', 'r') as User_Data:
                                if User_Data != '':
                                    for user_event in User_Data:
                                        print (user_event.strip())
                                    modules.Line('MEUS EVENTOS')
                                    while True:
                                        Resp = input('Você deseja cancelar sua inscrição em algum evento? [s/n] |-> ')
                                        if Resp in 'Ss':
                                            with open (f'user-data/{Usuario_Atual}.data', 'r') as User_Data:
                                                quantidade_eventos = 0
                                                contador = 1
                                                lista_de_eventos = []
                                                for user_event in User_Data:
                                                    print (f'{contador} | {user_event.strip()}')
                                                    quantidade_eventos +=1
                                                    contador +=1
                                                    lista_de_eventos.append(user_event.strip())
                                                while True:
                                                    try:
                                                        Resp = int(input('Qual evento deseja cancelar? |-> '))
                                                        if Resp <= 0:
                                                            print ('Digite um valor valido!')
                                                        elif Resp > quantidade_eventos:
                                                            print ('Digite um valor valido')
                                                        else:
                                                            modules.Remover_Eventos(Usuario_Atual,lista_de_eventos[Resp-1])
                                                            break
                                                    except:
                                                        print ('Digite um valor valido!')
                                        elif Resp in 'Nn':
                                            break
                                        else:
                                            print ('Digite um valor valido')
                                    break
                                else:
                                    print('O usuario não está registrado para nenhum evento')
                                    break
                        except Exception as e:
                            print (e)
                            print ('O usuario não está registrado para nenhum evento.')
                            break
            #VOLTAR 
            elif Resp == 4:
                modules.Line('USUARIO')
                break
            else:
                print ("ERRO... DIGITE UM VALOR VALIDO!") 
 #AREA DOS EVENTOS -----------------------------------------------------------------------
    elif Resp == 2:
        while True:
            modules.Tittle("EVENTOS")
            modules.Menu("REGISTRAR EVENTO",'LISTA DE EVENTOS','VOLTAR')
            modules.Line('EVENTOS')
            Resp = modules.Answers('Escolha sua opção |',3)
            if Resp == 1:
                while True:
                    modules.Tittle('REGISTRO DE EVENTOS')
                    modules.Event_Register()
                    break
            elif Resp == 2:
                modules.Tittle('LISTA DE EVENTOS')
                modules.Line('LISTA DE EVENTOS')
                try:
                    with open ('event.data', 'r') as event_name:
                        current_date = datetime.datetime.now()
                        for event in event_name:
                                if 'Data e Hora' in event:
                                    data_do_evento_str = event.split(': ')[1]
                                    data_do_evento_str = data_do_evento_str.strip()
                                    data_do_evento = datetime.datetime.strptime(data_do_evento_str,'%Y-%m-%d %H:%M:%S')
                                    status_evento = modules.Event_Status(data_do_evento)
                                    print (f'{event.strip()} | {status_evento}')
                                else:
                                    print (f'{event.strip()}')
                        if Usuario_Atual != 'Nenhum':
                            while True:
                                modules.Line('LISTA DE EVENTOS')
                                Resp = input ('Você deseja se registrar para algum evento? [s/n] |-> ')
                                if Resp in 'Ss':
                                    modules.User_Events(Usuario_Atual)
                                elif Resp in 'Nn':
                                    break
                                else:
                                    modules.Line('LISTA DE USUARIO')
                                    print ('Digite um valor valido! [s/n]')       
                                
                except Exception as e:
                    print (e)
                    print ('NÃO EXISTEM EVENTOS REGISTRADOS.')
                modules.Line('EVENTOS REGISTRADOS')
            elif Resp == 3:
                break
#FINALIZAR O PROGRAMA ----------------------------------------------------------------------
    elif Resp == 3:
        break
    else:
        print ('')
        print ('ERRO... DIGITE UM VALOR VALIDO!')
    
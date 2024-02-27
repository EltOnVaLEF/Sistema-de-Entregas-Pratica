from time import sleep
import datetime

def Tittle(tittle_text:str):
    tam = len(tittle_text) + 10
    print ('='*tam)
    print (f'     {tittle_text}')
    print ('='*tam)


def Menu (*options:str):
    cont = 1
    for name in options:
        print (f'{cont} | {name}')
        cont += 1
    return (len(options))


def Line(Tittle:str):
    tam = len(Tittle) + 10
    print ('='*tam)


def Answers(Text:str,Options_Limiter:int):
    resp = input (f'{Text} ').strip()
    try:
        resp = int(resp)
        if resp > Options_Limiter:
            print ("ERRO... DIGITE UM VALOR VALIDO!")
        elif resp <= 0:
            print ("ERRO... DIGITE UM VALOR VALIDO!")
        elif resp is None:
            print ("ERRO... DIGITE UM VALOR VALIDO!") 
        else:
            return (resp)
    except:
        print ("ERRO... DIGITE UM VALOR VALIDO!")


def Loading():
    Line('Carregando...')
    print ('Carregando...')
    sleep (1)
    

def login(usuario, senha):
    with open ('user.data','r') as User_List:
        Usuarios = User_List.readlines()
    with open('password.data','r') as Password_List:
        Senhas = Password_List.readlines()
    for user_line, pass_line in zip(Usuarios,Senhas):
        if usuario == user_line.strip() and senha == pass_line.strip():
            return True
        return False


def Event_Register():
    #CRIANDO VARIAVEIS ----------------------
    event_name = str
    event_type = str
    event_date_time = str
    event_address = str
    event_description = str
    #COMEÇO DO REGISTRO ------------------------------
    while True:
        event_name = str(input('Nome do evento: '))
        if event_name != '':
            break
        else:
            print('Preencha o campo.')
    Line('REGISTRO DE EVENTOS')
    print ('QUAL O TIPO DO EVENTO? ')
    Line('REGISTRO DE EVENTOS')
    Menu ('Social','Corporativo', 'Academico','Cultural','Esportivo','Caridade','Religioso','Entretenimento','Educacional')
    Line('REGISTRO DE EVENTOS')
    resp = Answers('|-> ',9)
    if resp == 1:
        event_type = 'Social'
    elif resp == 2:
        event_type = 'Corporativo'
    elif resp == 3:
        event_type = 'Academico'
    elif resp == 4:
        event_type = 'Cultural'
    elif resp == 5:
        event_type = 'Esportivo'
    elif resp == 6:
        event_type = 'Caridade'
    elif resp == 7:
        event_type = 'Religioso'
    elif resp == 8:
        event_type = 'Entretenimento'
    elif resp == 9:
        event_type = 'Educacional'
    Line('REGISTRO DE EVENTOS')
    while True:
        event_address = str(input('Qual o endereço? '))
        if event_address != '':
            break
        else:
            print('Preencha o campo!')
    Line('REGISTRO DE EVENTOS')
    while True:
        event_date_time_register = input ('Qual a data é a hora do evento? (Certifique-se de digitar em formato DD/MM/AAAA HH:MM): ')
        try:
            event_date_time = datetime.datetime.strptime(event_date_time_register,'%d/%m/%Y %H:%M')
            break
        except:
            print ('Formato digitado invalido!\nCertifique-se de digitar em formato DD/MM/AAAA HH:MM!')
    Line('REGISTRO DE EVENTOS')
    event_description = str(input('Qual a descrição do evento? '))
    try:
        with open ('event.data','a') as Event_Table:
            Event_Table.write(f'Evento: {event_name}\nCategoria: {event_type}\nEndereço: {event_address}\nData e Hora: {event_date_time}\nDescrição: {event_description}\n{"-" * 30}\n')
            print ('EVENTO REGISTRADO COM SUCESSO')
            Line('EVENTOS')
            Loading()
    except:
        print('UM ERRO INESPERADO OCORREU DURANTE O REGISTRO, TENTE NOVAMENTE.')
    Line('REGISTRO DE EVENTOS')


def Event_Status(event_date):
    current_date = datetime.datetime.now()
    if event_date < current_date:
        return '(O evento já ocorreu)'
    elif event_date > current_date:
        return '(O evento ainda vai ocorrer)'
    elif event_date == current_date:
        return '(O evento está ocorrendo)'
    

def User_Events(Usuario):
    c = 1
    Events_Name_Cuted = []
    while True:
        Line('LISTA DE USUARIO')
        c = 1
        with open ('event.data','r') as Events:
            Events_Limiter = Events.read().strip().split("-" * 30)
            quantidade_eventos = len(Events_Limiter)-1
        with open ('event.data', 'r') as Events_Name:
            for event in Events_Name:
                if 'Evento: ' in event:
                    Events_Name_Cuted.append(event.strip())
            for name in Events_Name_Cuted:
                if c == quantidade_eventos + 1:
                    break
                print (f'{c} | {name}')
                c += 1
            Resp = Answers('Em qual evento deseja se inscrever? |-> ', quantidade_eventos)
            while True:
                confirm = input(f'Você deseja se inscrever no {Events_Name_Cuted[Resp-1]}? [s/n] |-> ')
                if confirm in 'Nn':
                    Loading()
                    break
                elif confirm in 'Ss':
                        with open (f'user-data/{Usuario}.data', 'r') as User_Table_Events:
                            linhas = User_Table_Events.readlines()
                            verfi = False
                            for events in linhas:
                                if events in linhas:
                                    print ('Você já está registrado neste evento.')
                                    verfi = True
                                    break
                            if verfi == True:
                                break
                        with open (f'user-data/{Usuario}.data', 'a') as User_Table_Data:
                            User_Table_Data.write(f'{Events_Name_Cuted[Resp-1]}\n')
                            print ('O usuario foi inscrito com sucesso.')
                            Line('LISTA DE EVENTOS')
                            Loading()
                            break
                else:
                    Line('LISTA DE EVENTOS')
                    print('Digite um valor valido! [s/n]')
                    Line('LISTA DE EVENTOS')
                
        break

            
def Remover_Eventos(Usuario,evento_remover):
    try:
        with open (f'user-data/{Usuario}.data','r') as User_Data_Base:
            linhas = User_Data_Base.readlines()
        with open (f'user-data/{Usuario}.data','w') as User_Data_Base:
            verif = False
            for linha in linhas:
                if evento_remover.strip() not in linha.strip():
                    User_Data_Base.write(linha)
                else:
                    verif = True
                    if verif:
                        print (f'O evento {evento_remover} foi removido da lista')
                        Line('MEUS EVENTOS')
                    else:
                        print (f'O evento não pode ser removido.')
                        Line ('MEUS EVENTOS')
    except Exception as e:
        print ('Um erro ocorreu durante o processo')
        print (e)


                    
                




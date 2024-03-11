#Titulo
#Botao iniciar chat
    #Clicou no botao
    #aparecer pop up / modal
    #Bem vindo ao MyWhats
        #campo: escreva seu nome no chat
        #Esreva seu nome no chat
#chat
#Embaixo do chat
#Digite sua msg
    #Botao de enviar

#flet - framework - Conjunto de ferramentas p resolver um problema
#pip install flet

import flet as ft

def main(pagina): #funcao principal
    texto = ft.Text('MyWhats')

    chat = ft.Column()
    nome_usuario = ft.TextField(label= 'Escreva seu nome no chat') #escrever nome


    def enviar_mensagem_tunel(mensagem):
        texto_mensagem = ft.Text(mensagem)#add msg p tds os usuarios
        chat.controls.append(texto_mensagem)
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel) #enviar mensagem pra todos com o site aberto

    def enviar_mensagem(evento):
        print('Enviar mensagem')
        pagina.pubsub.send_all(f"{nome_usuario.value}: {campo_mensagem.value}")#rodar a funcao para mandar pra todos os usuarios
        #adicione a mensagem no chat
        
        #limpe o campo mensagem
        campo_mensagem.value = ''
        pagina.update()#edicao visual no codigo



    


    campo_mensagem = ft.TextField(label='Digite sua mesagem', on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton('Enviar', on_click=enviar_mensagem)
    linha_enviar = ft.Row([campo_mensagem, botao_enviar]) #colocar as duas coisas numa linha só

    def entrar_chat(evento):
        print('Entrar no chat')
        #fechar popup
        popup.open = False
        #tirar o botao iniciar chat
        pagina.remove(botao_iniciar)
    #tirar o botao MyWhats
        pagina.remove(texto)
        #criar o chat
        pagina.add(chat)
        pagina.pubsub.send_all((f'{nome_usuario.value} entrou no chat'))
        #campo de digitar msg
        pagina.add(linha_enviar)
        #criar botao de enviar
        
        pagina.update()

    titulo_popup = ft.Text('Bem vindo ao MyWhats') #apaece texto escrito
    botao_entrar = ft.ElevatedButton('Entrar no chat', on_click=entrar_chat)

    popup = ft.AlertDialog(
        open = False, 
        modal= True,
        title = titulo_popup,
        content= nome_usuario,
        actions = [botao_entrar] #precisa dp [] -- Lista de ações
    ) #criar popup


    def abrir_popup(evento):
        pagina.dialog = popup #qual popup abrir 
        popup.open = True #abrir popup
        #sempre que editar a página, depois que a pg ja tover c arregada, rodar a pagina p ser atualisada qd ttiver uma edicao
        pagina.update()#atualisa a pagina sem precisar de f5
    botao_iniciar = ft.ElevatedButton('Iniciar chat', on_click=abrir_popup)

    pagina.add(texto)
    pagina.add(botao_iniciar)


    

ft.app(target=main,  view=ft.WEB_BROWSER, port=8000) #criar o app chamando a função principal main
import flet as ft

def main(page):
    
    title = ft.Text("Chat")
    
    window_title = ft.Text("Welcome to the chat!")
    username_field = ft.TextField(label = "Write your name")
    
    chat = ft.Column()
    
    def send_message_tunel(message):
        chat_text = ft.Text(message)
        chat.controls.append(chat_text)
        page.update()
        
        
    page.pubsub.subscribe(send_message_tunel)
    
    def send_message(event):
        message_text = message_field.value
        username = username_field.value
        message = f"{username}: {message_text}"
        page.pubsub.send_all(message)
        message_field_value = ""
        page.update()

 
    message_field = ft.TextField(label = "Type your message", on_submit = send_message)
    send_message_button = ft.ElevatedButton("Send", on_click = send_message)
    
    message_line = ft.Row([message_field, send_message_button])
    def enter_chat(event):
        page.remove(title)
        page.remove(start_button)
        window.open = False
        page.add(chat)
        page.add(message_line)
        message = f"{username_field.value} entered the chat"
        page.pubsub.send_all(message)
        page.update()

    enter_chat_button = ft.ElevatedButton("Enter chat", on_click = enter_chat)
    
    window = ft.AlertDialog(
        title = window_title,
        content = username_field,
        actions = [enter_chat_button])
    
    def start_chat(event):
        page.dialog = window
        window.open = True
        page.update()
        
    start_button = ft.ElevatedButton("Start Chat", on_click = start_chat)
    
    page.add(title)
    page.add(start_button)

ft.app(main, view = ft.WEB_BROWSER)

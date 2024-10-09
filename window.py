from tkinter import *
import pywhatkit as kit
from datetime import datetime, timedelta


def btn_clicked():
    numero = entry0.get()
    if not numero.startswith('+'):
        numero = '+55' + numero
    mensagem = entry2.get("1.0", "end-1c")

    # Obter o horário atual e adicionar 2 minutos
    agora = datetime.now() + timedelta(minutes=1)
    hora = agora.hour
    minuto = agora.minute

    kit.sendwhatmsg(numero, mensagem, hora, minuto)
    print(f"Mensagem enviada para {numero} às {hora}:{minuto} com a mensagem: {mensagem}")

window = Tk()

window.geometry("640x480")
window.configure(bg="#ffffff")
canvas = Canvas(
    window,
    bg="#ffffff",
    height=480,
    width=640,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)

background_img = PhotoImage(file="background.png")
background = canvas.create_image(320.0, 240.0, image=background_img)

entry0_img = PhotoImage(file="img_textBox0.png")
entry0_bg = canvas.create_image(432.0, 178.5, image=entry0_img)

entry0 = Entry(bd=0, bg="#ffffff", highlightthickness=0)
entry0.place(x=278.0, y=156, width=308.0, height=43)

entry1_img = PhotoImage(file="img_textBox1.png")
entry1_bg = canvas.create_image(432.0, 270.5, image=entry1_img)

entry1 = Entry(bd=0, bg="#ffffff", highlightthickness=0)
entry1.place(x=278.0, y=248, width=308.0, height=43)

entry2_img = PhotoImage(file="img_textBox2.png")
entry2_bg = canvas.create_image(432.0, 406.0, image=entry2_img)

entry2 = Text(bd=0, bg="#ffffff", highlightthickness=0)
entry2.place(x=278.0, y=340, width=308.0, height=130)

img0 = PhotoImage(file="img0.png")
salvar = Button(image=img0, borderwidth=0, highlightthickness=0, command=btn_clicked, relief="flat")
salvar.place(x=409, y=95, width=198, height=48)

window.resizable(False, False)
window.mainloop()

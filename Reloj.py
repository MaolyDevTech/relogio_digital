import tkinter as tk
import time
from tkinter import messagebox

app_window = tk.Tk()
app_window.title("Relógio Digital")
app_window.geometry("510x150")
app_window.resizable(1, 1)
app_window.option_add('*Font', 'Boulder 68 bold')

text_font = ("Boulder", 68, 'bold')
background = "#a2e000"
foreground = "#570600"
border_width = 25

# Título da janela para melhor usabilidade
app_window.title("Relógio Digital")

label = tk.Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width)
label.grid(row=0, column=1)

def toggle_idioma():
    if label["text"] == "Relógio Digital":
        label.config(text="Digital Clock")
        toggle_button.config(text="Mudar para Português")
    else:
        label.config(text="Relógio Digital")
        toggle_button.config(text="Switch to English")

def aumentar_contraste():
    # Função para aumentar o contraste do texto
    # Você pode implementar isso conforme necessário
    pass

def definir_alarme():
    alarme_hora = entry_hora.get()
    try:
        alarme_hora = time.strptime(alarme_hora, "%H:%M")
        alarme_hora = time.strftime("%H:%M", alarme_hora)
        messagebox.showinfo("Alarme definido", f"Alarme definido para {alarme_hora}")
    except ValueError:
        messagebox.showerror("Erro", "Formato de hora inválido. Use HH:MM")

toggle_button = tk.Button(app_window, text="Mudar para Inglês", command=toggle_idioma)
toggle_button.grid(row=1, column=1)

# Botão para aumentar contraste (usabilidade)
contraste_button = tk.Button(app_window, text="Aumentar Contraste", command=aumentar_contraste)
contraste_button.grid(row=2, column=1)

# Adicionando um campo de entrada para definir o alarme
entry_hora = tk.Entry(app_window)
entry_hora.grid(row=3, column=1)
entry_hora_label = tk.Label(app_window, text="Definir Alarme (HH:MM):")
entry_hora_label.grid(row=3, column=0)

def digital_clock():
    time_live = time.strftime("%H:%M:%S")
    label.config(text=time_live)
    label.after(200, digital_clock)

digital_clock()
app_window.mainloop()

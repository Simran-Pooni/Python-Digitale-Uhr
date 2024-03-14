import tkinter as tk
import time

# main window erstellen
mw = tk.Tk()
mw.title("Digitale Uhr")

def zeit():
    aktuelle_uz = time.strftime('%H:%M:%S')
    uzFeld.config(text=aktuelle_uz)
    uzFeld.after(1000, zeit)

# Feld für die Uhrzeit
uzFeld = tk.Label(mw, font=("Century", 80), bg="white", fg="pink")
uzFeld.pack()

# Uhrzeit aktualisieren
zeit()


mw.mainloop()
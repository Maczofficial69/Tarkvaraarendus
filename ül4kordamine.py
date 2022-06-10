from tkinter import * # impordib

def save_info():
    firstname_info = firstname.get() # saab esinime info
    lastname_info = lastname.get() # saab perekonnanime info
    age_info = age.get() # saab vanuse info
    print(firstname_info, lastname_info, age_info) # prindib nende info

    file = open("user.txt", "w") # teeb/avab faili user.txt
    file.write(firstname_info) # kirjutab esinime info
    file.write(lastname_info) # Kirjutab perekonnanime info
    file.write(age_info) # kirjutab vanuse info
    file.close() # close'b faili
    print (" User ", firstname_info, " has been registered successfully") # Prindib selle teksti

# KUSTUTAB ENTRY
    firstname_entry.delete(0, END)
    lastname_entry.delete(0, END)
    age_entry.delete(0, END)


screen = Tk() # screen töötab tkinteriga
screen.geometry("500x500") # ekraani parameetrid
screen.title("Python Form") # pealkiri ekraanil
heading = Label(text = "Python Form", bg = "grey", fg = "black", width = "500", height = "500") # seab akna texti värvid jms.
heading.pack ()

firstname_text = Label(text = "Firstname * ",) # seab firstname teksti
lastname_text = Label(text = "Lastname * ",) # seab lastname teksti
age_text = Label(text = "Age * ") # seab vanuse teksti
firstname_text.place(x = 15, y = 70) # seab esinime teksti asukoha
lastname_text.place(x = 15, y = 140) # seab perenime teksti asukoha
age_text.place(x = 15, y = 210) # seab vanuse teksti asukoha

firstname = StringVar() # esinimi on string
lastname = StringVar () # perenimi on string
age = IntVar () # vanus on number

firstname_entry = Entry(textvariable = firstname, width = "30") # esinime entry on muutuja firstname
lastname_entry = Entry(textvariable = lastname, width = "30") # perenime entry on muutuja lastname
age_entry = Entry(textvariable = age, width = "30") # vanuse entry on muutuja vanus

firstname_entry.place (x = 15, y = 100) # firstname entry koordinaadid
lastname_entry.place(x = 15, y = 180) # lastname entry koordinaadid
age_entry.place(x= 15, y = 240) # vanuse koordinaadid


register = Button(text = "Register", width = "500", height = "2", command = save_info, bg = "grey") # Register nupu laius värv jne.
register.place(x = 15, y = 290) # register nupu koordinaadid


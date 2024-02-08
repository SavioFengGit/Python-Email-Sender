# Importa il modulo smtplib che fornisce le funzioni per comunicare con i server di posta elettronica
import smtplib

# Imposta le variabili sender, receiver, password, subject e body con i dati della email da inviare
sender = "sender@gmail.com@gmail.com"
receiver = "receiver@gmail.com"
password = "password" #se gmail devi generare il token e inserirlo qui
subject = "soggetto dell'email"
body = "Corpo dell'email da creare, magari convincente per far cliccare un link"

# Crea la stringa del messaggio, usando il formato header + corpo, e inserendo le variabili nelle posizioni appropriate
message = f"""From: Mr. Rossi{sender}
To: Mr. Bianchi{receiver}
Subject: {subject}\n
{body}
"""

# Crea un oggetto server che si connette al server SMTP di Gmail, usando la porta 587
server = smtplib.SMTP("smtp.gmail.com", 587)
# Avvia il protocollo TLS (Transport Layer Security) per criptare la comunicazione con il server
server.starttls()

# Usa un blocco try-except per gestire le possibili eccezioni
try:
    # Effettua il login al server SMTP usando le credenziali dell'account Gmail del mittente
    server.login(sender,password)
    # Stampa un messaggio di conferma sul terminale
    print("Logged in...")
    # Invia la email al destinatario, usando il metodo sendmail del server e passando il mittente, il destinatario e il messaggio
    server.sendmail(sender, receiver, message)
    # Stampa un messaggio di conferma sul terminale
    print("Email has been sent!")

# Se si verifica un'eccezione di tipo SMTPAuthenticationError, significa che il login non è andato a buon fine
except smtplib.SMTPAuthenticationError:
    # Stampa un messaggio di errore sul terminale
    print("unable to sign in")


#Author Xiao Li Savio Feng
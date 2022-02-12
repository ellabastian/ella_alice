# added import getpass
import getpass

# changed PIN variable to string
PIN = '4567'
attempt = 1
while attempt <= 3:
    # removed int from input
    # entered_PIN = getpass.getpass(prompt='Password: ')
    entered_PIN = getpass.getpass(prompt='Enter your PIN: ')
    if entered_PIN == PIN:
        print("PIN correct")
        # need a break here, otherwise, will continue loop even if PIN is correct
        break
    else:
        print("PIN incorrect; attempts remaining:", int(3 - attempt))
    attempt = attempt + 1
print("END")
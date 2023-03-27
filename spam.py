import requests
import time

payload = {
    'content': """
    Yay
    https://youtube.com/shorts/zsPBd_wxRBw?feature=share
    """
}

header = {
    'authorization': "ODgyNTQ4ODE5NzAxNjY5ODk5.GOn2K5.viKw-73ozMaBBmndfj0LdIgxk12OZ7oOnelwCU"
}

while True:
    r = requests.post('https://discord.com/api/v9/channels/1089460007042568252/messages', data=payload, headers=header)
    time.sleep(30)  # wait for 5 minutes before sending the next message


#######################################################################

# All the disord servers

# https://discord.com/api/v9/channels/967752137012551700/messages - just me

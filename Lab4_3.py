from datetime import datetime
from time import sleep

for a in range(5):
    print(f'Сейчас {datetime.now().strftime('%H:%M:%S')}')
    sleep(1)
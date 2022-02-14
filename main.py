import random, shutil, sys, time

MIN_STREAM_LENGHT = 6
MAX_STREAM_LEANGHT = 14
PAUSE = 0.1
STREAM_SHARS = ['0', '1']

# Плотность
DENSITY = 0.02

# Получаем размер окна терминала
WIDHT = shutil.get_terminal_size()[0]
WIDHT -= 1

print('The matrix. Created ZQRey')
print('Нажмите Ctrl-C что бы выйти')
time.sleep(2)

try:
    columns = [0] * WIDHT
    while True:
        for i in range(WIDHT):
            if columns[i] == 0:
                if random.random() <= DENSITY:
                    columns[i] = random.randint(MIN_STREAM_LENGHT, MAX_STREAM_LEANGHT)

            if columns[i] > 0:
                print(random.choice(STREAM_SHARS), end='')
                columns[i] -= 1
            else:
                print(' ', end='')
        print()
        sys.stdin.flush()
        time.sleep(PAUSE)
except KeyboardInterrupt:
    sys.exit()
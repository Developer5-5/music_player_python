# this program created by alireza.re (  :)ikiler:)  )

from pygame import mixer


mixer.init()
mixer.music.load('your addres mp3 file copy here example C:\\Users\\alireza\\Desktop\\eminem.mp3')
mixer.music.set_volume(0.7)
mixer.music.play()

while True:
    print('Press "p" to pause , "r" to resume')
    print('Press "e" to exit the program')
    query = input(' ')
    if query == 'p':
        mixer.music.pause()
    elif query == 'r':
        mixer.music.unpause()
    elif query == 'e':
        mixer.music.stop()
        break
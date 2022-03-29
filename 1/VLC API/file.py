from time import sleep

import pafy
import vlc


url = 'https://www.youtube.com/watch?v=p3j2NYZ8FKs'
video = pafy.new(url)
best = video.getbest()
playurl = best.url


Instance = vlc.Instance()
player = Instance.media_player_new()
Media = Instance.media_new(playurl)
Media.get_mrl()
player.set_media(Media)
player.play()
Media.add_option('start-time=120.0')
Media.add_option('run-time=10.0')
sleep(10)
while player.is_playing():
    sleep(1)

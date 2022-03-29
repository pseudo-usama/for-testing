from time import sleep
import vlc


sound = vlc.MediaPlayer('F:/songs/Gimme More.mp3')


vlc_instance = vlc.Instance()
player = vlc_instance.media_player_new()
media = vlc_instance.media_new(sound)
player.set_media(media)
player.play()
sleep(1.5)
duration = player.get_length() / 1000
sleep(duration)

# import modules
import threading
import random
from pynput.keyboard import Key, Listener
import wx
import wx.adv

# class untuk menampung keyboard listener.
class KBSoundThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.onPress = None
        self.onRelease = None

    def run(self):
        with Listener(
                on_press=self.onPress,
                on_release=self.onRelease) as listener:
            listener.join()

# class untuk memainkan suara keyboard.
class KBSound:
    def __init__(self):
        self.running = False
        self.randomized = False
        self.soundArray = []
        self.counter = 0

    # saat KBSoundThread mendeteksi keyboard di-press.
    def onPress(self, key):
        self.playSound()
        return self.running

    # saat KBSoundThread mendeteksi keyboard di-release.
    def onRelease(self, key):
        return self.running

    # tambahkan WAV ke list.
    def addSound(self, path):
        self.soundArray.append(wx.adv.Sound(path))

    # jalankan service ini.
    def startService(self):
        if len(self.soundArray) <= 0:
            return

        self.running = True

        thr = KBSoundThread()
        thr.onPress = self.onPress
        thr.onRelease = self.onRelease

        thr.start()

    # hentikan service ini.
    def stopService(self):
        self.running = False

    # ambil WAV selanjutnya dari list.
    def nextSound(self):
        if len(self.soundArray) <= 0:
            return

        nxs = self.soundArray[self.counter]
        self.counter += 1
        if self.counter >= len(self.soundArray):
            self.counter = 0
        return nxs

    # ambil random WAV selanjutnya dari list.
    # dilakukan jika randomize dicentang.
    def nextRandomSound(self):
        if len(self.soundArray) <= 0:
            return

        return random.choice(self.soundArray)

    # implementasi mainkan suara WAV.
    def playSound(self):
        if len(self.soundArray) <= 0:
            return

        sndToplay = None
        if self.randomized == True:
            sndToplay = self.nextRandomSound()
        else:
            sndToplay = self.nextSound()

        sndToplay.Play(wx.adv.SOUND_ASYNC)

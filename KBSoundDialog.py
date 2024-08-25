import wx
import os
import webbrowser

from BaseDialog import BaseDialog
from KBSound import KBSound

# subclass dari BaseDialog.
# sebagai satu-satunya dialog yang muncul pada aplikasi ini.
class KBSoundDialog (BaseDialog):
    def __init__(self):
        BaseDialog.__init__(self, None)

        # event binding.
        #self.m_buttonTraktir.Bind(wx.EVT_BUTTON, self.onButtonTraktir)

        self.m_checkBoxRandomize.Bind(wx.EVT_CHECKBOX, self.onCheckRandomize)
        self.m_buttonStartStop.Bind(wx.EVT_BUTTON, self.onButtonStartStop)
        self.m_buttonClearList.Bind(wx.EVT_BUTTON, self.onButtonClearList)
        self.m_buttonAddSoundWAV.Bind(wx.EVT_BUTTON, self.onButtonAddSoundWAV)

        # inisialisasi.
        self.kbSound = KBSound()
        self.isStarted = False
        self.soundPathArray = []

    def __del__(self):
        pass

    def onButtonTraktir(self, e):
        print("onButtonTraktir")
        webbrowser.open("https://rebrand.ly/sfr-traktir")
        pass

    # ketika Randomize dicentang atau tidak dicentang.
    def onCheckRandomize(self, e):
        self.kbSound.randomized = e.IsChecked()

    # saat tombol Add Sound WAV diklik.
    def onButtonAddSoundWAV(self, e):
        openFileDialog = wx.FileDialog(
            self, "Open", "", "", "WAV files (*.wav)|*.wav", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

        openFileDialog.ShowModal()
        path = openFileDialog.GetPath()
        openFileDialog.Destroy()

        print(path)

        self.kbSound.addSound(path)
        self.soundPathArray.append(path)
        self.updateListBox()

    # saat tombol Clear List diklik.
    def onButtonClearList(self, e):
        self.kbSound.soundArray.clear()
        self.soundPathArray.clear()
        self.updateListBox()

    # saat tombol Start/Stop ditekan.
    def onButtonStartStop(self, e):
        if self.isStarted == True:
            self.isStarted = False
            self.m_buttonStartStop.SetLabelText("Start")
            self.kbSound.stopService()
        else:
            self.isStarted = True
            self.m_buttonStartStop.SetLabelText("Stop")
            self.kbSound.startService()

    # implementasi refresh List Box.
    def updateListBox(self):
        self.m_listBoxSoundWAV.Clear()

        for path in self.soundPathArray:
            self.m_listBoxSoundWAV.AppendItems(os.path.basename(path))

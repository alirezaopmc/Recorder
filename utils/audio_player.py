import PySide6.QtMultimedia as qtm
import PySide6.QtCore as qtc

import pathlib
import os

class AudioPlayer:
    def __init__(self, path_provider):
        self.path_provider = path_provider
        self.player = qtm.QMediaPlayer()

    def setAudioOutput(self, output):
        self.audioOutput = output
        self.player.setAudioOutput(self.audioOutput)
    
    def play(self):
        filename = self.path_provider.get_current_active_audio()
        print(filename)
        path = pathlib.Path(qtc.QDir.currentPath()) / "records" / filename
        self.player.setSource(qtc.QUrl.fromLocalFile(path))
        self.player.play()
    
    def pause(self):
        self.player.pause()

    def isPlaying(self):
        return self.player.isPlaying()
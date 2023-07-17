import PySide6.QtCore as qtc
import PySide6.QtWidgets as qtw
import PySide6.QtGui as qtg
import PySide6.QtMultimedia as qtm

import utils

import sys
import os


from ui.main_ui import Ui_RecorderWidget

class BaregheRecorderWidget(qtw.QWidget, Ui_RecorderWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.recorder = utils.AudioRecorder()
        self.player = utils.AudioPlayer(self)

        # for  action in ['play', 'record', 'stop']:
        #     getattr(self, f'pb_{action}').clicked.connect(getattr(self.recorder, action))
        self.audio_i_map = {}
        k = 0
        for audio_input_dev in qtm.QMediaDevices.audioInputs():
            item = audio_input_dev.description()
            self.audio_i_map[item] = k
            k += 1
            self.cl_audio_input.addItem(item)
        self.cl_audio_input.currentIndexChanged.connect(self.audio_input_changed_listener)
        self.audio_input_changed_listener()

        self.audio_o_map = {}
        k = 0
        for audio_output_dev in qtm.QMediaDevices.audioOutputs():
            item = audio_output_dev.description()
            self.audio_o_map[item] = k
            k += 1
            self.cl_audio_output.addItem(item)
        self.cl_audio_output.currentIndexChanged.connect(self.audio_output_changed_listener)
        self.audio_output_changed_listener()
        
        self.setup_player()

        self.pb_play_n_pause.clicked.connect(self.play_n_pause)
        self.pb_record.clicked.connect(self.record)
        self.pb_stop.clicked.connect(self.stop)

    def audio_input_changed_listener(self):
        device = qtm.QMediaDevices.audioInputs()[self.cl_audio_input.currentIndex()]
        self.recorder.setAudioInput(qtm.QAudioInput(device))

    def audio_output_changed_listener(self):
        device = qtm.QMediaDevices.audioOutputs()[self.cl_audio_output.currentIndex()]
        self.player.setAudioOutput(qtm.QAudioOutput(device))

    def setup_player(self):
        self.update_player_files()

    def update_player_files(self):
        self.cl_player_files.clear()
        records = os.listdir('records')
        records = list(filter(lambda s: s.endswith('m4a'), records))
        records.sort(reverse=True)
        self.cl_player_files.addItems(records)
    
    def get_current_active_audio(self):
        filename = self.cl_player_files.currentText()
        return filename

    def record(self):
        if self.recorder.recorder.recorderState() != qtm.QMediaRecorder.RecorderState.RecordingState:
            self.recorder.record()
            self.pb_record.setEnabled(False)
            self.pb_stop.setEnabled(True)
    
    def stop(self):
        if self.recorder.recorder.recorderState != qtm.QMediaRecorder.RecorderState.StoppedState:
            self.recorder.stop()
            self.pb_stop.setEnabled(False)
            self.pb_record.setEnabled(True)
            self.update_player_files()

    def play_n_pause(self):
        if self.player.isPlaying():
            self.pb_play_n_pause.setText("Play")
            self.player.pause()
        else:
            self.pb_play_n_pause.setText("Pause")
            self.player.play()
            # self.player.
            # self.pb_record.setDisabled(True)
            # self.pb_stop.setDisabled(True)
    
if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    window = BaregheRecorderWidget()
    window.show()

    sys.exit(app.exec())
import PySide6.QtMultimedia as qtm
import PySide6.QtCore as qtc

import pathlib
import os
import datetime

class AudioRecorder:
    def __init__(self):
        self.session = qtm.QMediaCaptureSession()
        self.audioInput = qtm.QAudioInput(qtm.QMediaDevices.audioInputs()[0])
        self.setAudioInput(self.audioInput)
        self.recorder = qtm.QMediaRecorder()
        format = qtm.QMediaFormat(qtm.QMediaFormat.FileFormat.MP3)
        format.setAudioCodec(qtm.QMediaFormat.AudioCodec.MP3)
        self.recorder.setMediaFormat(format)
        self.recorder.setQuality(qtm.QMediaRecorder.Quality.HighQuality)
        # self.recorder.setOutputLocation(qtc.QUrl.fromLocalFile(os.fspath(os.path.join(self.get_path(), '.mp3'))))
        self.session.setRecorder(self.recorder)

    def setAudioInput(self, input):
        self.audioInput = input
        self.session.setAudioInput(input)
    
    def get_path(self):
        time_str = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        filename = pathlib.Path(qtc.QDir.currentPath()) / "records" / time_str
        return filename
    
    def record(self):
        self.recorder.setOutputLocation(qtc.QUrl.fromLocalFile(os.fspath(self.get_path())))
        self.recorder.record()
    
    def stop(self):
        self.recorder.stop()


# from queue import Queue
# from enum import Enum
# import pyaudio

# class AudioRecorder:
#     class STATE(Enum):
#         Init=0
#         Recording=1
#         Pause=2
#         Stop=3

#     def __init__(self, save_strategy):
#         self.save_strategy = save_strategy
#         self.stream = None
#         self.sample_format=pyaudio.paInt16
#         self.state = AudioRecorder.STATE.Init
#         self.lock = threading.Lock()
#         self.chunk = 1024
#         self.rate = 44100
#         self.channels = 1
#         self.frames = Queue()

#         self.thread = threading.Thread(target=self.run)#, args=[self])
#         self.thread.start()

#     def get_frames(self):
#         frames = []
#         while not self.frames.empty():
#             frames.append(self.frames.get())
#         return frames
    
#     def record(self):
#         self.set_state(AudioRecorder.STATE.Recording)

#     def _record(self):
#         self.pa = pyaudio.PyAudio()
#         self.stream = self.pa.open(
#             format=self.sample_format,
#             channels=self.channels,
#             rate=self.rate,
#             input=True,
#             frames_per_buffer=self.chunk,
#         )
#         self.init_metadata()
#         self.state = AudioRecorder.STATE.Recording
#         self.lock.acquire()
#         while self.state == AudioRecorder.STATE.Recording:
#             self.lock.release()
#             data = self.stream.read(self.chunk)
#             self.frames.put(data)
#             self.lock.acquire()

#     def init_metadata(self):
#         self.metadata = {
#             'time': datetime.datetime.now()
#         }

#     def set_state(self, state):
#         self.lock.acquire()
#         self.state = state
#         self.lock.release()
    
#     def get_state(self):
#         self.lock.acquire()
#         state = self.state
#         self.lock.release()
#         return state

#     def save(self):
#         # wf = wave.open(self.save_strategy.get_path(self.metadata), 'wb')
#         wf = wave.open('output.wav', 'wb')
#         wf.setnchannels(self.channels)
#         wf.setsamplewidth(self.pa.get_sample_size(self.sample_format))
#         wf.setframerate(self.rate)
#         wf.writeframes(b''.join(self.get_frames()))
#         wf.close()

#     def stop(self):
#         self.set_state(AudioRecorder.STATE.Stop)

#     def _stop(self):
#         self.set_state(AudioRecorder.STATE.Init)
#         self.stream.stop_stream()
#         self.stream.close()
#         self.pa.terminate()
#         self.save()

#     def pause(self):
#         self.set_state(AudioRecorder.STATE.Pause)

#     def _pause(self):
#         self.set_state(AudioRecorder.STATE.Pause)

#     def resume(self):
#         # self.set_state(AudioRecorder.STATE.)
#         pass

#     def _resume(self):
#         self.set_state(AudioRecorder.STATE.Recording)

#     def run(self):
#         debug=True
#         while True:
#             if self.get_state() == AudioRecorder.STATE.Init:
#                 if debug: print('Init')
#                 pass
#             elif self.get_state() == AudioRecorder.STATE.Recording:
#                 if debug: print('Recording')
#                 self._record()
#             elif self.get_state() == AudioRecorder.STATE.Pause:
#                 if debug: print('Pause')
#                 pass
#             elif self.get_state() == AudioRecorder.STATE.Stop:
#                 if debug: print('Stop')
#                 self._stop()
#                 self.set_state(AudioRecorder.STATE.Init)
#             else:
#                 pass
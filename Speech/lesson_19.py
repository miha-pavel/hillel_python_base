from pydub import AudioSegment

mp3_file = AudioSegment.from_file('./Speech/mp3_file.mp3')
print('mp3_file: ', mp3_file)
import re

from deepaffects.realtime.util import chunk_generator_from_file, get_deepaffects_client
from scipy.io.wavfile import read as read_wav

TIMEOUT_SECONDS = 200
apikey = "g0X3fWgLA9HWcezCoXqyGbS8FtXZMJJa"

# Set is_youtube_url True while streaming from youtube url
is_youtube_url = False
languageCode = "en-Us"
encoding = "wav"

# DeepAffects realtime Api client
client = get_deepaffects_client()


def find_emotion(file_path):
    try:
        try:
            sampling_rate, _ = read_wav(file_path)  # enter your filename
            print(sampling_rate)
        except:
            sampling_rate = 8000

        metadata = [
            ('apikey', apikey),
            ('encoding', encoding),
            ('samplerate', str(sampling_rate)),
            ('languagecode', languageCode)
        ]

        responses = client.IdentifyEmotion(
            # Use chunk_generator_from_file generator to stream from local file
            chunk_generator_from_file(file_path, buffer_size=10000),
            # Use chunk_generator_from_url generator to stream from remote url or youtube with is_youtube_url set to true
            # chunk_generator_from_url(file_path, is_youtube_url=is_youtube_url),
            TIMEOUT_SECONDS, metadata=metadata)

        # responses is the iterator for all the response values
        for response in responses:
            print("Received message", response)
            emotion = re.search('(?<=emotion:.")(.*)(?=")', str(response), re.IGNORECASE)
            return emotion.group(1) or "neutral"
    except:
        print("Error getting emotion")
        return "neutral"


from pydub import AudioSegment
from pydub.playback import play


def duplicate_wav(audio_in_file, audio_out_file):
    # create 1 sec of silence audio segment
    # one_sec_segment = AudioSegment.silent(duration=3000)  #duration in milliseconds

    # read wav file to an audio segment
    song = AudioSegment.from_wav(audio_in_file)

    # Add above two audio segments
    final_song = song

    while final_song.duration_seconds < 3:
        final_song += final_song

    # Either save modified audio
    final_song.export(audio_out_file, format="wav")

from pathlib import Path
from array import array
from enum import Enum
import wave

class CONFIG(Enum):
    MIXING="UP"
    SCALING="UP"
    SAMPLING="UP"

    TARGET_MIXING = 2 # stereo has 2 channels
    TARGET_SCALING = 2 # ...bytes(int16/16-bit)
    TARGET_FRAMERATE = 48 * 1000 # (48kHz since default SAMPLING is UP)
    

def main():
    BASE_DIR = Path("samples")

    main_audio_path = BASE_DIR / "425a9.wav"
    chime_audio_path = BASE_DIR / "chimes/accurate.wav"

    with wave.open(str(main_audio_path), "rb") as main_audio, \
        wave.open(str(chime_audio_path), "rb") as chime_audio:

        # checking if both are equal channel (stereo/mono):
        if main_audio.getnchannels() == chime_audio.getnchannels():
            # now since we have equal channels, we check sample-width is equal
            if main_audio.getsampwidth() == chime_audio.getsampwidth():
                # now we have equal bit depth, we check framerate is equal
                if main_audio.getframerate() == chime_audio.getframerate():
                    main_num = raw_to_num_stereo(main_audio.readframes(main_audio.getnframes()))
                    chime_num = raw_to_num_stereo(chime_audio.readframes(chime_audio.getnframes()))

                    MAX_DIVISOR = 32768.0
                    main_num = normalize(main_num, MAX_DIVISOR)
                    chime_num = normalize(chime_num, MAX_DIVISOR)
                    
                else:
                    # [#A] TODO Do upsampling or downsampling
                    # [#B] TODO provide option/config for either of the up/down-sampling
                    pass
                pass
            else:
                # [#A] TODO Do upscaling or downscaling
                # [#B] TODO provide option/config for either of the up/down-scaling
                pass
        else:
            # [#A] TODO Do down-mixing(quality reduce) or up-mixing(quality-preserved)
            # [#B] TODO provide option/config for either of the up/down-mixing
            pass


def get_duration(frames, framerate):
    return frames / framerate

def raw_to_num_stereo(raw_bytes):
    num = array('h', raw_bytes)
    return num

def normalize(num, divisor):
    num = array('f', (sample / divisor for sample in num))
    return num

def index_to_seconds(index, framerate, channel):
    # MONO: index / framerate for mono

    # STEREO: index / framerate * 2 for stereo since stereo has both L & R side!
    #       : index / framerate * number_of_channel(s)

    return index / (framerate * channel)

if __name__ == "__main__":
    main()
from pathlib import Path
import wave

def main():
    BASE_DIR = Path("samples")

    main_audio_path = BASE_DIR / "425a9.wav"
    chime_audio_path = BASE_DIR / "chimes/accurate.wav"

    with wave.open(str(main_audio_path), "rb") as main_audio, \
        wave.open(str(chime_audio_path), "rb") as chime_audio:
        print("Duration of main_audio", get_duration(main_audio.getnframes(), main_audio.getframerate()), "seconds")
        print("Duration of chime_audio", get_duration(chime_audio.getnframes(), chime_audio.getframerate()), "seconds")

def get_duration(frames, framerate):
    return frames / framerate

if __name__ == "__main__":
    main()
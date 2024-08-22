import os
import tempfile
from pydub import AudioSegment
from pydub.playback import play

def manipulate_audio(input_path, output_path):
    try:
        # Memuat file audio
        audio = AudioSegment.from_file(input_path)
        print("✅ Audio berhasil dimuat")

        # Operasi Pemotongan dengan validasi durasi
        start_time = 5000  # dalam milidetik
        end_time = 20000   # dalam milidetik
        if end_time > audio.duration_seconds * 1000:
            end_time = int(audio.duration_seconds * 1000)
        cropped_audio = audio[start_time:end_time]
        print("✅ Pemotongan audio berhasil")

        # Operasi Pengaturan Volume dengan validasi
        volume_increase = 6  # Ubah nilai ini sesuai kebutuhan
        if volume_increase > 0:
            louder_audio = cropped_audio + volume_increase
        else:
            louder_audio = cropped_audio
        print("✅ Pengaturan volume berhasil")

        # Simpan audio hasil manipulasi ke direktori dalam direktori home pengguna
        output_dir = os.path.join(os.path.expanduser("~"), "Documents", "audio_output")
        os.makedirs(output_dir, exist_ok=True)
        temp_output_path = os.path.join(output_dir, "result.wav")
        louder_audio.export(temp_output_path, format='wav')
        print("✅ Konversi format berhasil")

        # Operasi Pemutaran Audio
        print("🔊 Memutar audio hasil manipulasi...")
        play(louder_audio)

    except Exception as e:
        print(f"❌ Terjadi kesalahan: {e}")

if __name__ == "__main__":
    manipulate_audio('The Drum.mp3', 'result.mp3')
from pydub import AudioSegment
from pydub.playback import play
import tempfile
import os

def manipulate_audio(input_path, output_path):
    try:
        # Memeriksa apakah ffmpeg tersedia
        if not (os.system('ffmpeg -version') == 0 and os.system('ffprobe -version') == 0):
            raise EnvironmentError("ffmpeg atau ffprobe tidak ditemukan di PATH")

        # Memuat file audio
        audio = AudioSegment.from_file(input_path)
        print("✅ Audio berhasil dimuat")

        # Operasi Pemotongan dengan validasi durasi
        if len(audio) > 10000:
            clipped_audio = audio[:10000]  # Mendapatkan 10 detik pertama
            clipped_audio.export('clipped_' + output_path, format='mp3')
            print("✅ Pemotongan berhasil")

            # Operasi Penggabungan
            combined_audio = audio + clipped_audio
            combined_audio.export('combined_' + output_path, format='mp3')
            print("✅ Penggabungan berhasil")
        else:
            raise ValueError("Durasi audio terlalu pendek untuk dipotong 10 detik")

        # Operasi Konversi Format
        audio.export('result.wav', format='wav')
        print("✅ Konversi format berhasil")

        # Operasi Pengaturan Volume dengan validasi
        if audio.dBFS < -10:
            louder_audio = audio + 10  # Meningkatkan volume sebesar 10dB
            louder_audio.export('louder_' + output_path, format='mp3')
            print("✅ Pengaturan volume berhasil")
        else:
            print("🔊 Volume audio sudah cukup tinggi, pengaturan volume dilewati")
            louder_audio = audio

        # Operasi Pemutaran Audio menggunakan file sementara
        with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as tmpfile:
            louder_audio.export(tmpfile.name, format='wav')
            print("🔊 Memutar audio hasil manipulasi...")
            play(AudioSegment.from_wav(tmpfile.name))
        
        os.remove(tmpfile.name)  # Menghapus file sementara secara manual setelah diputar

    except PermissionError as pe:
        print(f"❌ Kesalahan izin: {pe}")
    except Exception as e:
        print(f"❌ Terjadi kesalahan: {e}")

if __name__ == "__main__":
    manipulate_audio('The Drum.mp3', 'result.mp3')

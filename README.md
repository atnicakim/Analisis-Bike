Proyek ini menganalisis data peminjaman sepeda berdasarkan berbagai faktor seperti cuaca, musim, dan tren harian. Hasil analisis divisualisasikan dalam dashboard interaktif menggunakan Streamlit.

Persyaratan
Sebelum menjalankan proyek, pastikan Anda memiliki Python dan pustaka yang diperlukan. Anda bisa menginstalnya dengan:
pip install -r requirements.txt

Jalankan Dashboard di Lokal
1. Buka terminal dan arahkan ke folder dashboard.
2. Jalankan perintah berikut:
   streamlit run app.py

Deploy ke Streamlit Cloud
1. Buat Repository GitHub
   - Pastikan struktur folder sesuai.
   - Push kode proyek ke GitHub.
2. Buat Aplikasi di Streamlit Cloud
   - Buka Streamlit Cloud dan login.
   - Klik "New App" → Pilih repository GitHub proyek ini.
   - Pilih branch utama dan tentukan app.py sebagai main file.
   - Klik "Deploy".
3. Cek URL Aplikasi
   - Setelah berhasil deploy, catat URL aplikasi yang diberikan.
   - Simpan di url.txt.
   
URL Dashboard:
https://bike-sharing-analysis-mika.streamlit.app/

Hasil Analisis
1. Tren Peminjaman Sepeda: Pola musiman menunjukkan peningkatan peminjaman pada bulan tertentu.
2. Pengaruh Cuaca: Cuaca buruk berpengaruh negatif terhadap jumlah peminjaman.

Lisensi
Dataset berasal dari Capital Bikeshare System, Washington D.C., dan digunakan untuk analisis akademik.

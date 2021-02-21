# Hotel Room Price Determination Based on Dynamic Pricing Model
Project ini dibuat sebagai kontribusi data scientist untuk program UN Sustainable Development Goals 2030. 

![Dynamic Pricing](https://user-images.githubusercontent.com/66118303/102737528-3ccbea80-437a-11eb-813d-0bbcdb87361d.png)

Kontributor dalam project ini:

- Faisal Faturohman
- Elien Hanjani Pramitha
- Khayrussyifa Putri Ramadhani
- Nadya Syahrita Maghfirah

Link Youtube:
https://youtu.be/sj7V8fQjWBM

## Dataset
Dataset diambil dari data hotel yang ada pada aplikasi Online Travel Agent. Harga dan tanggal pada dataset tidak real masih berdasarkan asumsi dari review pelanggan Hotel Ibis Trans Studio Bandung. Nantinya ketika mendapatkan data real dai hotel maka akan lebih meminimalisr error yang terjadi.

## Alur Sistem
![Alur](https://user-images.githubusercontent.com/66118303/102738979-5b33e500-437e-11eb-8cc3-83b332db59c4.png)

## Cara Penggunaan
1. Clone atau download repository ini.
2. Pastikan terdapat Anaconda.
3. Aktifkan environment anaconda:
`conda create -n namaenv pip python=3.7`
4. Buat environment terlebih dahulu:
`conda activate namaenv`
5. Install library di folder ini jangan lupa arahin cmdnya ke folder ini:
`pip install -r req.txt`
6. Jika ingin melakukan tes maka buka Jupyter Notebooknya dengan buka cmd pada folder lalu ketikan:
`jupyter notebook`
7. Pilih Jupyter Notebook yang ingin digunakan
8. Atau bisa langsung menjalankan aplikasi dengan cara:
`flask run`
9. Jika ingin langsung melihat pengecekan harga sesuai dengan demand yang diinginkan hotel maka bisa langsung menuju web kami:
`https://hoteldynamicpricing.online/`

## Output
Output dari program akan menghasilkan prediksi harga berdasarkan demand yang diharapkan.

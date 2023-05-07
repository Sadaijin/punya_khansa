import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title = "by : Khansa")
with st.sidebar:
        pilihan = option_menu('Menu', ["Total Dissolved Solid", 'Total Suspended Solid', 'Total Solid', 'Kalkulator TDS', 'Kalkulator TSS',                                        'Kalkulator TS', 'About Us'],
                                      icons = ['book-half','book-half','book-half','calculator','calculator','calculator','people-fill'], menu_icon="menu-down" )
    
    
if pilihan == 'Total Dissolved Solid' :

    st.title("TOTAL DISSOLVED SOLID")

    st.header("Prinsip Kerja")
    st.markdown("""Analisis Total Dissolved Solid atau residu terlarut dalam air permukaan dilakukan dengan cara menimbang berat residu sampel yang lolos dari kertas saring berpori< 0,45 μm dan telah dikeringkan pada suhu 103-105°C hingga diperoleh bobot tetap.""")

    st.header("Tujuan Praktikum : Mengetabui kadar Toral Dissolved solid dalam laratan")

    st.header("Alat dan Bahan")
    st.markdown("""
    1. Pinggan penguap yang terbuat dari porselen atau platina atau silica berkualitas tinggi
    2. Penangas air
    3. Oven untuk pemanasan pada suhu 103-105°C 
    4. Desikator
    5. Neraca analitik
    6. Pipet volumetrik 25 ml
    7. Cawan Goch atau alat penyaring lain yang dilengkapi pengisap atau penekan
    8. Kertas saring berpori 0,45 μm
    9. Tempat khusus untuk menaruh kertas saring
    10. Penjepit""")

    st.header("Cara Kerja")
    st.markdown("""
    1. Timbang pinggan penguap kosong yang telah di pansakan di oven menggunakan neraca analitik
    2. Kocok sampel air permukaan
    3. Saring sampel air
    4. Pipet 25 ml filtrat hasil penyaringan dan masukkan ke dalam pinggan penguap kosong yang telah ditimbang
    5. Panaskan dengan penangas air hingga kering, setelah kering lap bagian luar pinggan dengan alkohol
    6. Masukkan pinggan penguap ke dalam oven dan panaskan pada suhu 103-105°C selama 1 jam
    7. Keluarkan pinggan penguap dan masukkan ke dalam desikator selama 15 menit atau sampai dingin
    8. Timbang pinggan penguap yang sudah dingin.""")

    st.header("Perhitungan")

    st.latex(r'''
        Bobot TDS \left(\frac{mg}{ml}\right) = 
        \frac{\left(A-B\right) 1000}{volume sampel \left(ml\right)}
        ''')

    st.markdown("""Keterangan: \n
    A = Berat cawan berisi residu terlatur dalam (mg) \n
    B = Berat cawan kosong (mg) \n
    1000 = Konversi dari mL ke L""")
    
elif pilihan == "Total Suspended Solid" :
    import streamlit as st

    st.title("TOTAL SUSPEND SOLID")

    st.header("Prinsip Kerja")
    st.markdown("""Total suspended solid atau padatan tersuspensi total (TSS) adalah residu dari padatan total yang tertahan oleh saringan   dengan ukuran partikel maksimal 2μm atau lebih besar dari ukuran partikel koloid. """)

    st.header("Tujuan Praktikum : Untuk mengetahui total padatan tersuspensi")

    st.header("Alat dan Bahan")
    st.markdown("""
    1. Timbang pinggan penguap kosong yang telah dipanaskan di oven menggunakan neraca analitik
    2. Kocok sampel air permukaan
    3. Pipet 25 ml sampel air dan masukkan ke dalam pinggan penguap kosong yang telah ditimbang
    4. Panaskan dengan penangas air hingga kering, setelah kering lap bagian luar pinggan penguap dengan alkohol
    5. Masukkan pinggan penguap kedalam oven dan panaskan pada suhu 103-105°C selama 1 jam
    6. Keluarkan pinggan penguap dan masukkan menit atau sampai dingin kedalam desikator sela 19/73
    7. Timbang pinggan penguap yang sudah dingin.""")
    
# st.header("Cara Kerja")
# st.markdown("""1. Timbang pinggan penguap kosong yang telah dipanaskan di oven menggunakan neraca analitik
# 2. Kocok sampel air permukaan
# 3. Pipet 25 ml sampel air dan masukkan ke dalam pinggan penguap kosong yang telah ditimbang
# 4. Panaskan dengan penangas air hingga kering, setelah kering lap bagian luar pinggan penguap dengan alkohol
# 5. Masukkan pinggan penguap kedalam oven dan panaskan pada suhu 103-105°C selama 1 jam
# 6. Keluarkan pinggan penguap dan masukkan menit atau sampai dingin kedalam desikator sela 19/73
# 7. Timbang pinggan penguap yang sudah dingin.""")

    st.header("Perhitungan")

    st.latex(r'''
        Bobot TSS \left(\frac{mg}{ml}\right) = 
        \frac{\left(A-B\right) 1000}{volume sampel \left(ml\right)}
        ''')

    st.markdown("""Keterangan: \n
    A = Berat cawan berisi residu (mg) \n
    B = Berat cawan kosong (mg) \n
    1000 = Konversi dari mL ke L""")

elif pilihan == 'Total Solid' :
  
    st.title("TOTAL SOLID")

    st.header("Prinsip Kerja")
    st.markdown("""Pengujian Total Solid atau residu total dilakukan dengan cara menimbang berat contoh yang telah dikeringkan pada suhu 103-105 C hingga diperoleh bobot tetap.""")

    st.header("Tujuan Praktikum : Mengetahui kadar total solid dalam larutan")

    st.header("Alat dan Bahan")
    st.markdown("""
    1. Pinggan penguap yang terbuat dari porselen atau tinggi platina atau silica berkualitas
    2. Penangas air 
    3. Oven untuk pemanasan pada suhu 103-105°C
    4. Desikator
    5. Neraca analitik
    6. Pipet volumetrik 25 mL
    7. Penjepit""")

    st.header("Cara Kerja")
    st.markdown("""
    1. Timbang pinggan penguap kosong yang telah dipanaskan di oven menggunakan neraca analitik
    2. Kocok sampel air permukaan
    3. Pipet 25 ml sampel air dan masukkan ke dalam pinggan penguap kosong yang telah ditimbang
    4. Panaskan dengan penangas air hingga kering, setelah kering lap bagian luar pinggan penguap dengan alkohol
    5. Masukkan pinggan penguap kedalam oven dan panaskan pada suhu 103-105°C selama 1 jam
    6. Keluarkan pinggan penguap dan masukkan menit atau sampai dingin kedalam desikator sela 19/73
    7. Timbang pinggan penguap yang sudah dingin.""")

    st.header("Perhitungan")

    st.latex(r'''
        Bobot TS \left(\frac{mg}{ml}\right) = 
        \frac{\left(A-B\right) 1000}{volume sampel \left(ml\right)}
        ''')

    st.markdown("""Keterangan: \n
    A = Berat cawan berisi residu (mg) \n
    B = Berat cawan kosong (mg) \n
    1000 = Konversi dari mL ke L""")

elif pilihan == 'Kalkulator TDS' :

    st.title("""Perhitungan TDS""")

    st.write('---')
    st.title('TDS')

    A = st.number_input('Masukkan berat cawan (g)')
    B = st.number_input('Masukkan nilai berat sampel pada cawan (g)')
    V = st.number_input('Masukkan volume sampel (mL)')

    tombol = st.button('Hitung nilai TDS')

    if tombol:
        nilai_TDS = ((B-A*1000)/(V/1000))
        st.success(f'Nilai TDS adalah {nilai_TDS}')

elif pilihan == 'Kalkulator TSS' :

    st.title("""Perhitungan TSS""")

    st.write('---')
    st.title('TSS')

    A = st.number_input('Masukkan nilai berat kertas saring (g) atau berat cawan + kertas saring')
    B = st.number_input('Masukkan nilai berat sampel pada kertas saring (g) atau berat cawan sampel + kertas saring residu setelah pemanasan')
    V = st.number_input('Masukkan nilai volume sampel (mL)')

    tombol = st.button('Hitung nilai TSS')

    if tombol:
        nilai_TSS = ((B-A*1000)/(V/1000))
        st.success(f'Nilai TSS adalah {nilai_TSS}')

elif pilihan == 'Kalkulator TS' :
  
    st.title('Perhitungan TS')

    st.write('---')
    st.title('TS')


    A = st.number_input('Masukkan nilai berat cawan akhir + residu(g)')
    B = st.number_input('Masukkan nilai berat cawan (g)')
    V = st.number_input('Masukkan nilai volume (mL)')

    tombol = st.button('Hitung nilai TS')

    if tombol:
        nilai_TS = ((A-B*1000)/(V/1000))
        st.success(f'Nilai TS adalah {nilai_TS}')

else :

    st.title("About Us")

    st.markdown("""Assalammualaikum wr.wb.
    Perkenalkan kami dari mahasiswa/i Politeknik AKA Bogor, memperkenalkan webapss perhitungan parameter lingkungan yang telah berhasil kami buat. 
    Khususnya guna memenuhi nilai mata kuliah Logika Pemrograman Komputer dan kebermanfaatan di industri dalam menghitung parameter lingkungan (TSS,TS dan TDS).

    Tim Penyusun:
    1. Aldira Naswa Syahwalia (NIM 2260003)
    2. Khansa Nur Shafiyah (NIM 2260025)
    3. Nizmi Amalia Samtika (NIM 2260036)
    4. Rivia Sekar Notiyanti (NIM 2260047)
    5. Nadya Nafis (NIM 2020356)

    Sekian,
    Semoga web apps ini bermanfaat bagi kalian para pengguna.
    Wassalammualaikum wr.wb.""")


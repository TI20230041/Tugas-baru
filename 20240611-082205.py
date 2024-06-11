def create_map():
    # Membuat peta dengan titik pusat di koordinat tertentu
    peta = folium.peta(lokasi=[-
    peta =  folium.peta(menemukan

    peta = folium.Bu

    peta = fo

    pe
6.200000, 106.816666], zoom_mulai=10)

    

  
# Menambahkan marker ke peta
    folium.penanda(
        lokasi=[-
    folium.penanda(
        lokasi=[-

    folium.penanda(
        lokasi

    folium.penanda(
   

    folium.Merusak

    fo
6.200000, 106.816666],
        muncul=
        p

 
'Jakarta',
        ikon=folium.Ikon(ikon=
        ikon=folium.Ikon

        ikon=foll

        
'info-tanda')
    ).tambahkan_(peta)

    
    ).tambahkan_(peta)

   

    ).tambahkan_(peta)


    ).tambahkan_(peta

    ).tambahkan_

    ).a

  
# Menyimpan peta ke file HTML
    peta.menyimpan(
    p
'peta.html')

    

   
mencetak("Peta telah dibuat dan disimpan sebagai peta.html")

if __nama__ == "__utama__":
    buat_peta() 
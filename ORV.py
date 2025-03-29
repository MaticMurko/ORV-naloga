import cv2 as cv
import numpy as np
import time as time

def zmanjsaj_sliko(slika, sirina, visina):
    return    cv.resize(slika, (sirina, visina))

def obdelaj_sliko_s_skatlami(slika, sirina_skatle, visina_skatle, barva_koze) -> list:
    x=0 
    y=0
    height, width,channels = slika.shape
    rezultat = []
    while y<height:
        vrstica = []
        x=0
        while x<width:
            skatla = slika[y:y+visina_skatle, x:x+sirina_skatle]
            x+=sirina_skatle
            vrstica.append(prestej_piklse_z_barvo_koze(skatla,barva_koze))
        rezultat.append(vrstica)
        y+=visina_skatle
    return rezultat

def prestej_piklse_z_barvo_koze(slika, barva_koze) -> int:
    spodnja_meja, zgornja_meja =barva_koze
    range=cv.inRange(slika,spodnja_meja,zgornja_meja) 
    koza=cv.countNonZero(range)
    return koza

def doloci_barvo_koze(slika,levo_zgoraj,desno_spodaj) -> tuple:
    x1, y1 = levo_zgoraj
    x2, y2 = desno_spodaj
    kva = slika[y1:y2, x1:x2]

    mean_color = np.mean(kva, axis=(0, 1))  #izačuna povprečje za vse barvne kanale posebaj 
    std_color = np.std(kva, axis=(0, 1)) #izračuna standarni odklon za vse barvne kanale posebaj
    
    spodnja_meja = np.maximum(mean_color - std_color, 0).astype(np.uint8)
    zgornja_meja = np.minimum(mean_color + std_color, 255).astype(np.uint8)

    return spodnja_meja, zgornja_meja

def nariši_kvadratke_na_sliko(slika, polje, sirina_skatle, visina_skatle):
    y = 0
    for row in range(len(polje)):
        x = 0
        for col in range(len(polje[row])):
            if polje[row][col] > sirina_skatle*visina_skatle*0.30: #preveri če v škatli večkot 30% pikslov barve koze
                top_left = (x, y)
                bottom_right = (x + sirina_skatle, y + visina_skatle)
                cv.rectangle(slika, top_left, bottom_right, (0, 255, 0), 1)
            x += sirina_skatle
        y += visina_skatle

if __name__ == '__main__':
    #Pripravi kamero
    kamera = cv.VideoCapture(0)
    # Preverimo, če je kamera pravilno naložena
    if not kamera.isOpened():
        print('Kamera ni bila odprta.')
    else:
        while True:
            # Preberemo sliko iz kamere
            ret, slika = kamera.read()
            slika=zmanjsaj_sliko(slika,260,300)
            cv.rectangle(slika, (120,100), (150,120), (0,255,0), 1)
            cv.imshow('Kamera', cv.flip(slika,1))
            key=cv.waitKey(1) & 0xFF
            if key == ord('t'):
                spodnja_meja, zgornja_meja = doloci_barvo_koze(slika, (120, 100), (150, 120))
                break

            # Če pritisnemo tipko 'q', zapremo okno
            if key == ord('q'):
                break
        # Zapremo okno
        kamera.release()
        cv.destroyAllWindows()

    kamera = cv.VideoCapture(0)
    if not kamera.isOpened():
        print('Kamera ni bila odprta.')
    else:
        last_time = time.time()  # začeten cas
        fps=0
        while True:
            if cv.waitKey(1) & 0xFF == ord('q'):
                    break
            ret, slika = kamera.read()
            slika=zmanjsaj_sliko(slika,260,300)

            polje=obdelaj_sliko_s_skatlami(slika,13,15,(spodnja_meja,zgornja_meja))

            current_time = time.time()
            fps =1/(current_time-last_time)
            last_time = current_time 
 

            slika=cv.flip(slika,1)
            cv.putText(slika, f"FPS: {int(fps)}", (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1)
            cv.imshow('Kamera',slika)
        kamera.release()
        cv.destroyAllWindows()  
    pass
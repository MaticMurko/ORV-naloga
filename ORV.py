import cv2 as cv
import numpy as np

def zmanjsaj_sliko(slika, sirina, visina):
    return    cv.resize(slika, (sirina, visina))

def obdelaj_sliko_s_skatlami(slika, sirina_skatle, visina_skatle, barva_koze) -> list:
    '''Sprehodi se skozi sliko v velikosti škatle (sirina_skatle x visina_skatle) in izračunaj število pikslov kože v vsaki škatli.
    Škatle se ne smejo prekrivati!
    Vrne seznam škatel, s številom pikslov kože.
    Primer: Če je v sliki 25 škatel, kjer je v vsaki vrstici 5 škatel, naj bo seznam oblike
      [[1,0,0,1,1],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,1]]. 
      V tem primeru je v prvi škatli 1 piksel kože, v drugi 0, v tretji 0, v četrti 1 in v peti 1.'''
    pass

def prestej_piklse_z_barvo_koze(slika, barva_koze) -> int:
    '''Prestej število pikslov z barvo kože v škatli.'''
    pass

def doloci_barvo_koze(slika,levo_zgoraj,desno_spodaj) -> tuple:

    pass
    

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
           
            cv.imshow('Kamera', cv.flip(slika,1))
            key=cv.waitKey(1) & 0xFF
            if key == ord('t'):
               
                break

            # Če pritisnemo tipko 'q', zapremo okno
            if key == ord('q'):
                break
        # Zapremo okno
        kamera.release()
        cv.destroyAllWindows()
    pass
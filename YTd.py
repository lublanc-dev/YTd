#Importamos la librería pytube
from pytube import YouTube

print("\nInserta el link del vídeo:")
link=input()
yt = YouTube(link)

print("\nQuieres descargar únicamente el audio?: (y/n)   **el formato de descarga será mp4 en todo caso**")
f=input()
if f=="y":
    print("\nDetalles del vídeo","\n")
    print("Título:   ",yt.title)
    print("Nº de visitas:  ",yt.views)
    print("Duración:  ",yt.length,"segundos")

    yt.streams.get_audio_only().download()
    
    print("\nDescarga completada!! (Revise la carpeta en la que está guardado este archivo para ver tu descarga)")
    print()

else:
    print("\nDetalles del vídeo","\n")
    print("Título:   ",yt.title)
    print("Nº de visitas:  ",yt.views)
    print("Duración:  ",yt.length,"segundos")

    yt.streams.get_highest_resolution().download()
    print("\nDescarga completada!! (Revisa tu carpeta de descargas)")
    print()

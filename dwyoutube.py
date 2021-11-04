from pytube import YouTube

url = str(input("Informe a url do video a ser baixado: "))
print("Fazendo Download... Aguarde")
video = YouTube(url)
stream = video.streams.get_highest_resolution()
stream.download(output_path="videosBaixados")
print("\nDownload Concluido")

while True:
    x = int(input("\nQuer baixar outro video? Informe 1 para (SIM) ou 0 para (NÃO): "))
    if x == 1:
        url = str(input("Informe a url do video a ser baixado: "))
        print("\nFazendo Download... Aguarde")
        video = YouTube(url)
        stream = video.streams.get_highest_resolution()
        stream.download(output_path="videosBaixados")
        print("\nDownload Concluido")
    else:
        break
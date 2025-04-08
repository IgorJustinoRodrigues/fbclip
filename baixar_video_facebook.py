import os
import sys
import subprocess
from yt_dlp import YoutubeDL

# Caminho fixo do ffmpeg
ffmpeg_path = r"C:\ffmpeg-7.1\bin\ffmpeg.exe"

def baixar_video(url, nome_arquivo='video_baixado.mp4'):
    print("🔽 Baixando vídeo do Facebook...")
    ydl_opts = {
        'outtmpl': nome_arquivo,
        'format': 'bestvideo+bestaudio/best',
        'ffmpeg_location': ffmpeg_path,
        'merge_output_format': 'mp4'
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return nome_arquivo if os.path.exists(nome_arquivo) else None

def cortar_com_ffmpeg(entrada, saida, inicio=None, fim=None):
    print("✂️  Cortando vídeo com FFmpeg...")

    comando = []

    if inicio:
        comando += [ffmpeg_path, '-ss', inicio]
    else:
        comando += [ffmpeg_path]

    comando += ['-i', entrada]

    if inicio and fim:
        # Calcular duração
        h1, m1, s1 = map(int, inicio.split(':'))
        h2, m2, s2 = map(int, fim.split(':'))
        total_inicio = h1 * 3600 + m1 * 60 + s1
        total_fim = h2 * 3600 + m2 * 60 + s2
        duracao = total_fim - total_inicio
        h, m, s = duracao // 3600, (duracao % 3600) // 60, duracao % 60
        duracao_str = f"{h:02}:{m:02}:{s:02}"
        comando += ['-t', duracao_str]

    comando += ['-c', 'copy', saida]

    print("Executando:", ' '.join(comando))
    subprocess.run(comando)

def formatar_tempo(minuto, segundo):
    minutos = int(minuto)
    segundos = int(segundo)
    horas = minutos // 60
    minutos = minutos % 60
    return f"{horas:02}:{minutos:02}:{segundos:02}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python baixar_video_facebook.py <URL> [min_ini seg_ini min_fim seg_fim]")
        sys.exit(1)

    url = sys.argv[1]
    inicio = fim = None

    if len(sys.argv) >= 6:
        min_ini, seg_ini = sys.argv[2], sys.argv[3]
        min_fim, seg_fim = sys.argv[4], sys.argv[5]
        inicio = formatar_tempo(min_ini, seg_ini)
        fim = formatar_tempo(min_fim, seg_fim)

    arquivo_origem = baixar_video(url)
    if arquivo_origem:
        nome_saida = "video_cortado.mp4" if inicio and fim else "video_completo.mp4"
        cortar_com_ffmpeg(arquivo_origem, nome_saida, inicio, fim)

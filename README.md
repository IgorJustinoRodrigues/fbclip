# 📥 fbclip

Script simples e funcional em Python para baixar vídeos **públicos** do Facebook e cortar trechos específicos usando `yt-dlp` + `ffmpeg`.

---

## ✅ Requisitos

- Python 3.7 ou superior
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- FFmpeg

### Instalar dependências do Python:

```bash
pip install yt-dlp
```

---

## 🔧 Instalação do FFmpeg

Este projeto depende do FFmpeg para cortar os vídeos após o download.

### 🔹 Windows

1. Acesse: [https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/)
2. Baixe a versão **"Release full build"**
3. Extraia em um local como `C:\ffmpeg`
4. No script, altere a linha:

```python
ffmpeg_path = r"C:\ffmpeg\bin\ffmpeg.exe"
```

> Ou, opcionalmente, adicione `C:\ffmpeg\bin` à variável de ambiente **PATH** do sistema.

### 🔹 macOS

```bash
brew install ffmpeg
```

### 🔹 Linux (Debian/Ubuntu)

```bash
sudo apt update
sudo apt install ffmpeg
```

---

## 🚀 Como usar

### 📥 Baixar o vídeo completo

```bash
python baixar_video_facebook.py "<URL do vídeo do Facebook>"
```

### ✂️ Baixar e cortar um trecho do vídeo

```bash
python baixar_video_facebook.py "<URL>" <min_inicio> <seg_inicio> <min_fim> <seg_fim>
```

**Exemplo:** cortar de 45:00 a 48:00:

```bash
python baixar_video_facebook.py "https://www.facebook.com/algumperfil/videos/1234567890123456" 45 0 48 0
```

---

## 📂 Arquivos gerados

- `video_baixado.mp4`: vídeo original baixado do Facebook
- `video_completo.mp4`: se nenhum corte for aplicado
- `video_cortado.mp4`: se o corte for realizado com sucesso

---

## 💡 Dicas

- O vídeo precisa estar **público** no Facebook
- O corte é feito com `-c copy` (sem recodificação), o que torna o processo muito rápido
- Os tempos devem ser passados como `<min> <seg>` para início e fim

---

## 👨‍💻 Autor

Projeto mantido por Igor Justino Rodrigues.

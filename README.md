# 📥 Video Downloader

## 📝 Opis

**Video Downloader** to prosta aplikacja GUI napisana w Pythonie, która umożliwia pobieranie filmów z różnych źródeł
wideo online. Aplikacja wykorzystuje bibliotekę `yt-dlp` do pobierania wideo i audio oraz łączenia ich w jeden plik MP4.
Interfejs użytkownika oparty na `tkinter` pozwala na łatwe wprowadzanie URL wideo, wybór lokalizacji zapisu oraz
śledzenie postępu pobierania.

## 🚀 Funkcje

- **📹 Pobieranie Wideo**: Pobiera wideo z najlepszą dostępną jakością.
- **🎵 Pobieranie Audio**: Pobiera audio z najlepszą dostępną jakością.
- **🔗 Łączenie Wideo i Audio**: Automatycznie łączy strumienie wideo i audio w jeden plik MP4.
- **🖥️ Prosty interfejs GUI**: Użytkownik może wprowadzić URL wideo, wybrać lokalizację zapisu i śledzić postęp
  pobierania w intuicyjnym interfejsie.

## 📋 Wymagania

- **Python 3.x**
- **yt-dlp**: Biblioteka do pobierania wideo
- **ffmpeg**: Narzędzie do łączenia wideo i audio (opcjonalne, ale zalecane)
- **tkinter**: Biblioteka GUI (wbudowana w standardową bibliotekę Pythona)

## 🛠️ Instalacja

### Krok 1: Skopiuj repozytorium

Możesz skopiować repozytorium, używając narzędzia `git`, lub po prostu pobrać i rozpakować pliki ręcznie.

```bash
git clone https://github.com/twoj-repo/video-downloader.git
```

### Krok 2: Zainstaluj wymagane zależności

Przejdź do katalogu projektu i zainstaluj wymagane biblioteki:

```bash
pip install -r requirements.txt
```

### Krok 3: Instalacja `ffmpeg`

`ffmpeg` jest wymagane do łączenia plików wideo i audio. Możesz zainstalować `ffmpeg` za pomocą menedżera pakietów:

- **Windows**: Pobierz [ffmpeg](https://ffmpeg.org/download.html) i dodaj do zmiennej środowiskowej PATH.
- **macOS**: Użyj `Homebrew`:

```bash
brew install ffmpeg
```

- **Linux**: Użyj menedżera pakietów, np. na Ubuntu:

```bash
sudo apt update && sudo apt install ffmpeg
```

## 💻 Użycie

1. **Uruchomienie aplikacji**
   Uruchom aplikację za pomocą Pythona:

```bash
   python main.py
```

2. **Wprowadzenie URL**
    - Wprowadź URL wideo w polu tekstowym „Enter the video URL”.

3. **Wybór lokalizacji zapisu**
    - Kliknij „Browse”, aby wybrać lokalizację, w której chcesz zapisać pobrany plik wideo.

4. **Rozpoczęcie pobierania**
    - Kliknij przycisk „Download”, aby rozpocząć pobieranie. Status pobierania będzie wyświetlany w oknie aplikacji.

5. **Zakończenie**
    - Po zakończeniu pobierania i łączenia plików wideo i audio, pasek postępu osiągnie 100%, a status wyświetli
      komunikat „Download completed!”.
    - Możesz zamknąć aplikację, klikając przycisk „Close”.

## 🐛 Problemy

Jeśli napotkasz jakiekolwiek problemy, upewnij się, że:

- `yt-dlp` jest poprawnie zainstalowane i działa.
- `ffmpeg` jest zainstalowany i dostępny w ścieżce systemowej.
- URL wideo jest poprawny i dostępny.

## 📜 Licencja

Ten projekt jest licencjonowany na podstawie licencji MIT – zobacz plik [LICENSE](LICENSE) po więcej szczegółów.

## 👤 Autor

Stworzony przez [Sebastian Ledzianowski](https://github.com/sebastianLedzianowski).
# AuraTranscribe

Local-first AI transcription app powered by Whisper Small. Supports 13 audio & video formats, batch processing with pause/resume/cancel, and exports to .txt — wrapped in a minimal, light-driven desktop UI.

## Features

- Offline transcription using [faster-whisper](https://github.com/SYSTRAN/faster-whisper) (Whisper Small model)
- Supports English and Spanish
- 13 audio & video formats: `.mp3`, `.wav`, `.ogg`, `.flac`, `.m4a`, `.wma`, `.aac`, `.opus`, `.mp4`, `.mkv`, `.avi`, `.mov`, `.webm`
- Batch processing with pause, resume, and cancel
- Export transcriptions to `.txt`
- Browser-based UI served from a local FastAPI backend
- Auto-downloads the Whisper model on first run with integrity verification
- Auto-shutdown when the browser tab is closed

## Quick Start

### From source

```bash
# Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python main.py
```

The app opens automatically in your default browser at `http://127.0.0.1:47821`.

### From release (.exe)

1. Download `AuraTranscribe-windows-x64.zip` from the [Releases](../../releases) page
2. Extract the zip
3. Run `AuraTranscribe.exe`

No installation required. The app opens in your default browser and shuts down automatically when you close the tab.

## Build

To build the standalone `.exe`:

```bash
pip install pyinstaller
pyinstaller auratranscribe.spec --noconfirm
```

Output will be in `dist/AuraTranscribe/`.

## Architecture

- **Backend**: FastAPI + uvicorn (Python), bundled with PyInstaller
- **Frontend**: Static HTML/CSS/JS served by FastAPI
- **Transcription**: faster-whisper (CTranslate2) running locally
- **Audio processing**: FFmpeg (bundled via static-ffmpeg)

## License

MIT

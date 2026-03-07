# auratranscribe.spec
import static_ffmpeg
import os
import sys

# Get static-ffmpeg binary paths
ffmpeg_path = os.path.join(os.path.dirname(static_ffmpeg.__file__), "bin")

# Anaconda stores some DLLs outside the venv; bundle them explicitly
anaconda_bin = os.path.join(sys.base_prefix, "Library", "bin")

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[
        (os.path.join(anaconda_bin, 'ffi.dll'), '.'),
        (os.path.join(anaconda_bin, 'libbz2.dll'), '.'),
        (os.path.join(anaconda_bin, 'sqlite3.dll'), '.'),
    ],
    datas=[
        ('frontend', 'frontend'),
        (ffmpeg_path, 'static_ffmpeg/bin'),
    ],
    hiddenimports=[
        'uvicorn.logging',
        'uvicorn.loops',
        'uvicorn.loops.auto',
        'uvicorn.protocols',
        'uvicorn.protocols.http',
        'uvicorn.protocols.http.auto',
        'uvicorn.protocols.websockets',
        'uvicorn.protocols.websockets.auto',
        'uvicorn.lifespan',
        'uvicorn.lifespan.on',
        'faster_whisper',
        'ctranslate2',
        'av',
        'av._core',
        'av.audio',
        'av.video',
    ],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='AuraTranscribe',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    icon='frontend/assets/icon.ico',
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    name='AuraTranscribe',
)

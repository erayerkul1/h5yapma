# -*- mode: python ; coding: utf-8 -*-
# PyInstaller spec file for Load Extraction Tool

import sys
import os
from PyInstaller.utils.hooks import collect_all, collect_submodules

# ── Collect pyNastran (has many dynamic imports) ─────────────────────────────
pynastran_datas, pynastran_binaries, pynastran_hiddenimports = collect_all('pyNastran')

# ── Collect h5py (needs HDF5 shared libs) ────────────────────────────────────
h5py_datas, h5py_binaries, h5py_hiddenimports = collect_all('h5py')

# ── Collect pandas ────────────────────────────────────────────────────────────
pandas_datas, pandas_binaries, pandas_hiddenimports = collect_all('pandas')

block_cipher = None

a = Analysis(
    ['LOAD_EXTRACTION_CQUAD_BUSH_H5_V2.py'],
    pathex=[],
    binaries=h5py_binaries + pynastran_binaries + pandas_binaries,
    datas=h5py_datas + pynastran_datas + pandas_datas,
    hiddenimports=(
        h5py_hiddenimports
        + pynastran_hiddenimports
        + pandas_hiddenimports
        + collect_submodules('numpy')
        + [
            'tkinter',
            'tkinter.filedialog',
            'tkinter.messagebox',
            'tkinter.scrolledtext',
            'h5py._hl',
            'h5py._hl.files',
            'h5py._hl.group',
            'h5py._hl.dataset',
            'h5py.defs',
            'h5py.utils',
            'h5py.h5ac',
            'h5py.h5z',
            'h5py._errors',
            'h5py._conv',
            'h5py.version',
            'pyNastran.bdf.bdf',
            'pyNastran.utils.numpy_utils',
            'pyNastran.bdf.cards.elements.shell',
            'pyNastran.bdf.cards.properties.shell',
            'pyNastran.bdf.cards.elements.bush',
            'pyNastran.bdf.cards.coordinateSystems',
            'pandas',
            'numpy',
            'scipy',
            'scipy.spatial.transform._rotation_groups',
            'pkg_resources.py2_warn',
        ]
    ),
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'matplotlib',
        'IPython',
        'jupyter',
        'notebook',
        'PIL',
        'cv2',
        'PyQt5',
        'PyQt6',
        'PySide2',
        'PySide6',
        'wx',
        'gi',
        'gtk',
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='LoadExtractionTool',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,          # GUI uygulama — konsol penceresi açılmaz
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,              # İkon eklemek için: icon='icon.ico'
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='LoadExtractionTool',
)

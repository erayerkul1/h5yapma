import subprocess
import sys

cmd = [
    sys.executable, "-m", "PyInstaller",
    "--onefile",
    "--windowed",
    "--name", "LoadExtractionTool",
    "--collect-all", "h5py",
    "--collect-all", "pyNastran",
    "--collect-all", "pandas",
    "--exclude-module", "win32com",
    "--exclude-module", "pythoncom",
    "--exclude-module", "pywintypes",
    "--exclude-module", "matplotlib",
    "--exclude-module", "IPython",
    "LOAD_EXTRACTION_CQUAD_BUSH_H5_V2.py"
]

subprocess.run(cmd, check=True)

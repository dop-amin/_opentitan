import os
import re
import subprocess
import sys
import tempfile
from typing import Dict, List, Optional, Set, TextIO, Tuple
import argparse

from shared.toolchain import find_jasminc

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("files", type=str, help="jasminc target")
    parser.add_argument("-o", "--output", type=str, help="output jasmin arguments")
    args = parser.parse_args()
    
    jasminc = find_jasminc()
    print(jasminc)

    default_args = [
        '-arch otbn'
    ]

    # with tempfile.TemporaryDirectory(suffix='.otbn-jasminc') as tmpdir:
    cmd = [jasminc] + ['-arch', 'otbn'] + [args.files] + ["-o", args.output] + ["-pasm"]
    print(cmd)
    try:
        return subprocess.run(cmd).returncode
    except FileNotFoundError:
        sys.stderr.write('Unknown command: {!r}.\n'.format(jasminc))
        return 127

if __name__ == '__main__':
    sys.exit(main())

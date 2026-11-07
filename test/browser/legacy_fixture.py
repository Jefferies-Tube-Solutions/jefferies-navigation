# The immutable v1 browser harness uses the original custom-element and YAML names.
from contextlib import contextmanager
from io import BytesIO
from pathlib import Path
import subprocess
import tarfile
import tempfile

V1_SOURCE='25291186b07bfee81b8877fe731e00a417d56c12'

@contextmanager
def legacy_fixture():
    files=subprocess.check_output(['git','archive',V1_SOURCE,'test','docs/assets'])
    with tempfile.TemporaryDirectory() as directory:
        with tarfile.open(fileobj=BytesIO(files)) as archive:
            archive.extractall(directory,filter='data')
        yield Path(directory)/'test/browser'

"""Safety checks for original-image selection and refusal before creating output."""
import hashlib
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import patcher as installer


class PatcherTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.gdi = self.root/'original.gdi'
        self.gdi.write_text('3\n1 0 4 2352 "first track.bin" 0\n2 600 0 2352 track02.raw 0\n3 45000 4 2352 track03.bin 0\n', 'utf8')
        for name in ('first track.bin', 'track02.raw', 'track03.bin'):
            (self.root/name).write_bytes(b'original')
        self.out = self.root/'output'
        self.manifest = dict(tracks={name:dict(bytes=8, before_sha256=hashlib.sha256(b'original').hexdigest())
            for name in ('track01.bin', 'track02.raw', 'track03.bin')},
            patch=dict(file='delta.xdelta', bytes=10, sha256='0'*64))

    def tearDown(self):
        self.temporary.cleanup()

    def test_quoted_names(self):
        _, tracks = installer.original_tracks(self.gdi)
        self.assertEqual(tracks['track01.bin'].name, 'first track.bin')

    def test_parent_escape_rejected(self):
        self.gdi.write_text(self.gdi.read_text('utf8').replace('first track.bin', '../outside.bin'), 'utf8')
        with self.assertRaisesRegex(ValueError, '같은 폴더'):
            installer.original_tracks(self.gdi)

    def test_absolute_track_rejected(self):
        self.gdi.write_text(self.gdi.read_text('utf8').replace('first track.bin', 'C:/outside.bin'), 'utf8')
        with self.assertRaisesRegex(ValueError, '같은 폴더'):
            installer.original_tracks(self.gdi)

    def test_wrong_track_layout_rejected(self):
        self.gdi.write_text(self.gdi.read_text('utf8').replace('3 45000', '3 45001'), 'utf8')
        with self.assertRaisesRegex(ValueError, '트랙 구성'):
            installer.original_tracks(self.gdi)

    def test_existing_output_untouched(self):
        self.out.mkdir(); marker = self.out/'keep.txt'; marker.write_text('keep', 'utf8')
        with patch.object(installer, 'read_manifest', return_value=self.manifest):
            with self.assertRaisesRegex(ValueError, '이미 있습니다'):
                installer.apply(self.gdi, self.out)
        self.assertEqual(marker.read_text('utf8'), 'keep')

    def test_wrong_original_hash_creates_nothing(self):
        self.manifest['tracks']['track03.bin']['before_sha256'] = '0'*64
        before = (self.root/'track03.bin').read_bytes()
        with patch.object(installer, 'read_manifest', return_value=self.manifest):
            with self.assertRaisesRegex(ValueError, '원본 해시'):
                installer.apply(self.gdi, self.out)
        self.assertFalse(self.out.exists())
        self.assertEqual((self.root/'track03.bin').read_bytes(), before)

    def test_bad_payload_creates_nothing(self):
        payload = self.root/'delta.xdelta'; payload.write_bytes(b'bad delta!')
        with patch.object(installer, 'read_manifest', return_value=self.manifest):
            with self.assertRaisesRegex(ValueError, '패치 파일 해시'):
                installer.apply(self.gdi, self.out, payload)
        self.assertFalse(self.out.exists())


if __name__ == '__main__':
    unittest.main()

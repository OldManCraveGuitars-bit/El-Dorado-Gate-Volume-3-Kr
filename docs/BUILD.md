# EXE 패처 재빌드

이 저장소는 배포 패처·설명·검증 자료를 제공합니다. 아래 과정은 Windows x64 패처를 만드는 방법입니다.

1. Python 3.13과 PyInstaller 6.22.3을 준비합니다.
2. [xdelta3 3.2.1 Windows x64](https://github.com/jmacd/xdelta/releases/tag/v3.2.1)의 `xdelta3.exe`를 준비합니다.
3. v0.8 릴리스의 `track03-v0.8.xdelta`를 준비합니다. ZIP에도 포함되어 있습니다.
4. 저장소 루트에서 아래 명령을 실행합니다.

```powershell
python -m pip install pyinstaller==6.22.3
python tools/test_patcher.py
.\tools\build-patcher.ps1 -Xdelta C:\tools\xdelta3.exe -Patch C:\patch\track03-v0.8.xdelta
```

빌드 스크립트는 엔진과 패치의 SHA-256을 `hashes.json`과 비교한 뒤,
패치·엔진·매니페스트·라이선스를 내장한 `dist/El-Dorado-Gate-Volume-3-Kr-v0.8-Patcher.exe`를 만듭니다.
최종 사용자는 Python이나 xdelta3를 따로 설치할 필요가 없습니다.
도구·운영체제·빌드 시점에 따라 재빌드 EXE 자체의 해시는 달라질 수 있습니다.
패치가 생성해야 하는 게임 트랙과 GDI 해시는 `hashes.json`에 고정되어 있습니다.

검사한 원본 GDI는 3트랙 구조이며 트랙 시작 LBA는 `0 / 600 / 45000`입니다.
게임 이미지 파일 자체는 이 저장소에서 배포하지 않습니다.

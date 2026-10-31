# El-Dorado-Gate-Volume-3-Kr

**엘도라도 게이트 Vol.3 · 드림캐스트 한글 패치 v0.85**

일본판 **Vol.3 v1.001**용 한글 패치입니다. 대사·시스템·아이템·브라우저·오프닝·추가 콘텐츠를 번역하고,
원래 다운로드 상품 77종을 오프라인에서 구매할 수 있도록 설정했습니다.
Vol.1의 검토된 공통 번역·그림·글꼴·제작 도구를 재사용하고 Vol.3 전용 내용과 배치를 따로 맞췄습니다.
공개 버전은 **v0.85**, 내부 검증 빌드는 **v0.30**입니다.

<img src="https://raw.githubusercontent.com/OldManCraveGuitars-bit/El-Dorado-Gate-Volume-3-Kr/v0.85/screenshots/title.png" width="640" alt="엘도라도 게이트 Vol.3 한글 타이틀">

## 다운로드

**[v0.85 릴리스](https://github.com/OldManCraveGuitars-bit/El-Dorado-Gate-Volume-3-Kr/releases/tag/v0.85)**

| 파일 | 용도 |
| --- | --- |
| [El-Dorado-Gate-Volume-3-Kr-v0.85-Patcher.exe](https://github.com/OldManCraveGuitars-bit/El-Dorado-Gate-Volume-3-Kr/releases/download/v0.85/El-Dorado-Gate-Volume-3-Kr-v0.85-Patcher.exe) | **Windows 64비트용 단독 EXE 패처. 이 파일만 받아도 적용할 수 있습니다.** |
| [El-Dorado-Gate-Volume-3-Kr-v0.85.zip](https://github.com/OldManCraveGuitars-bit/El-Dorado-Gate-Volume-3-Kr/releases/download/v0.85/El-Dorado-Gate-Volume-3-Kr-v0.85.zip) | EXE·설명·스크린샷·해시·라이선스·수동 적용용 xdelta를 묶은 패키지 |
| [SHA256SUMS-v0.85.txt](https://github.com/OldManCraveGuitars-bit/El-Dorado-Gate-Volume-3-Kr/releases/download/v0.85/SHA256SUMS-v0.85.txt) | EXE·ZIP·xdelta 배포 파일의 SHA-256 |

패치 데이터와 xdelta3 엔진은 EXE 안에 들어 있습니다. **Python이나 별도 패치 도구 설치가 필요 없습니다.**
원본 게임 GDI와 세 트랙은 사용자가 준비합니다. 배포물은 패치와 도구이며 원본·완성 게임 이미지, BIOS, VMU 저장 파일을 포함하지 않습니다.

## 적용 방법

1. 일본판 **Eldorado Gate Vol. 3 v1.001 (2000)(Capcom)(NTSC)(JP)[!]**의 원본 3트랙 GDI를 준비합니다.
2. EXE 패처를 실행하고 **원본 GDI**를 선택합니다. GDI가 가리키는 트랙 세 개가 같은 폴더에 있어야 합니다.
3. **새 출력 폴더**를 지정합니다. 출력 드라이브에 약 1.3GB 이상의 여유 공간이 필요합니다.
4. **한글 패치 적용**을 누르면 원본 해시 검사 → 패치 → 결과 해시 검사 → 나머지 트랙 복사가 진행됩니다.
5. 새 폴더의 **`El-Dorado-Gate-Volume-3-Kr-v0.85.gdi`**를 실행합니다. 완성된 GDI와 트랙 3개를 함께 유지하세요.

패처는 원본을 읽고 결과를 새 폴더에 만듭니다. 기존 출력 폴더를 덮어쓰지 않으며,
지원 대상과 해시가 다른 이미지에는 적용하지 않습니다. 오류가 나면 아래의 원본 SHA-256과 비교하세요.
지원 대상은 일본판 v1.001 원본입니다. 이미 패치한 이미지에 추가로 적용하는 업데이트 방식이 아닙니다.

## v0.85 변경 내용

- **시나리오 시작 제목 2장**: `수몰된 도시로`, `파멜라의 기억`을 Vol.1 내부 빌드 **1.7.13**과 같은 **바탕체(BatangChe)**로 교체했습니다. 같은 반각 공백·금색 명암·1px 그림자를 사용합니다.
- **잘림과 좌표**: 첫 제목은 원래 타일 19칸 안에 맞춰 22px, 두 번째는 28px로 렌더링했습니다. 글자와 그림자를 자르지 않고 원래 좌표·앵커·애니메이션을 유지했습니다.
- **상태 배지**: 혼란을 포함한 `독·혼·마·사·공·방·염·속·회` 9개를 실제 Vol.1 최신 디스크와 대조했습니다. 12×12 칸의 테두리·그림자·글씨 픽셀이 같으며 원래 고정 슬롯 18개도 유지합니다.
- **상태창 제목**: 공백 없는 **특수능력**을 유지하고 기본 번역 데이터도 맞췄습니다. 원작 네 글자 영역과 같은 96px입니다.
- **단독 EXE 패처**: 버전·내장 매니페스트·패치 데이터·Windows 파일 정보를 v0.85로 맞추고, 새 EXE를 실제 일본판 원본 GDI에 적용해 세 트랙과 GDI 해시를 대조했습니다.

실제 GDI에서는 제목 그림 두 장 이외의 **패치 파일 58개**, 등록된 번역 **17,199개**, 기존 한글 글꼴 **1,043칸**이 이전 v0.8과 같습니다. 기존 대사 검수·추가 콘텐츠·오프라인 다운로드 상점·엔딩 44페이지를 포함합니다.
편집기 EXE 0.1.11에서도 새 제목과 상태 표시를 비교·수정할 수 있으며, 현재 데이터의 실제 Tk 미리보기와 배치 검사를 통과했습니다.

아래는 **실제 ROM 자산의 비교 이미지이며 실행 스크린샷은 아닙니다.** 왼쪽부터 일본어 원본, 이전 한국어 비트맵, 새 바탕체입니다.

![시나리오 제목 바탕체 변경 비교](https://raw.githubusercontent.com/OldManCraveGuitars-bit/El-Dorado-Gate-Volume-3-Kr/v0.85/docs/images/chapter-font-v085.png)

[제목·상태·특수능력 검증](https://github.com/OldManCraveGuitars-bit/El-Dorado-Gate-Volume-3-Kr/blob/v0.85/docs/chapter-font-verification.json) · [검수 이미지 출처](https://github.com/OldManCraveGuitars-bit/El-Dorado-Gate-Volume-3-Kr/blob/v0.85/docs/asset-review-provenance.json)

## 이전 v0.8 변경 내용

Vol.1의 최근 내부 빌드 **1.7.12**를 대조해 Vol.3에 해당하는 누락과 배치 문제를 보완했습니다.

- **본문·추가 콘텐츠 119곳**: 실제 폰트 크기, 영문·문장부호의 전각 폭, 반각 공백, 최대 9글자의 동적 이름 삽입을 고려해 문장과 줄바꿈을 정리했습니다.
- **상태 표시 18곳 / 배지 9개**: 길게 적혀 있던 `(혼란)`, `(기절)` 등을 원작 한 칸에 맞는 `독·혼·마·사·공·방·염·속·회`로 바꿨습니다. 원래 네모·그림자와 고정 글자 슬롯을 유지합니다.
- **장비 비교 8개 렌더러**: 반각 공백 때문에 어긋났던 비교 괄호를 맞추고 `+`/`-`와 비교 불가 표시 `****`를 보존했습니다.
- **권·화 및 수집 수치**: 별도로 그리는 숫자 위치를 공백 폭에 맞게 보정했습니다. 수집 개수·플래그·아이템 수치는 바꾸지 않았습니다.
- **특수능력 제목**: 띄어쓰기를 줄여 원래 네 글자 영역 안에 표시합니다.
- **엔딩 2종 44페이지**: 원래 페이지 순서·앵커·그림을 유지하면서 역할명과 제작진 이름, 마지막 `한글화 기타 깎는 노인` 크레딧을 반영했습니다.
- **편집기 0.1.11**: 실제 글자 크기와 삽입 이름을 포함한 폭·높이 검사를 추가하고, 상태 배지와 전체 엔딩 페이지 미리보기를 연결했습니다.

이전 v0.8에서 수정한 텍스트 레코드는 **총 138개(본문·추가 콘텐츠 119 + 상태 표시 18 + 제목 1)**입니다.
등록된 17,199개 문구의 새 배치 검사 오류는 0개이며, 실제 GDI에서 대사 4,972개와 포인터 5,137개, 추가 콘텐츠 338개와 엔딩 그림 44개를 다시 대조했습니다.
v0.8 당시 패치 파일 60개 중 해당 수정과 관계없는 **47개는 v0.75와 바이트까지 같습니다.**

![특수능력 제목과 상태 화면](https://raw.githubusercontent.com/OldManCraveGuitars-bit/El-Dorado-Gate-Volume-3-Kr/v0.85/screenshots/status-v08.png)

아래 두 이미지는 **실행 스크린샷이 아닌, 실제 ROM 자산을 확대한 검수 이미지**입니다.
상태 배지의 원래 테두리와 픽셀 글씨, 마지막 크레딧을 확인할 수 있습니다.

![상태 배지 자산](https://raw.githubusercontent.com/OldManCraveGuitars-bit/El-Dorado-Gate-Volume-3-Kr/v0.85/docs/images/status-badges-v08.png)
![마지막 엔딩 크레딧 자산](https://raw.githubusercontent.com/OldManCraveGuitars-bit/El-Dorado-Gate-Volume-3-Kr/v0.85/docs/images/ending-credit-v08.png)

엔딩까지의 실제 진행 검증은 하지 않았습니다. 인명 4건은 확정된 가나·로마자 자료가 없어 일반적인 독음으로 임시 표기했으며 [인명 독음 검토 기록](https://github.com/OldManCraveGuitars-bit/El-Dorado-Gate-Volume-3-Kr/blob/v0.85/docs/credit-reading-notes.json)에 남겼습니다.
[Vol.1 최근 수정 대조·검증 기록](https://github.com/OldManCraveGuitars-bit/El-Dorado-Gate-Volume-3-Kr/blob/v0.85/docs/vol1-recent-verification.json)을 함께 제공합니다.

## 한글화 내용

| 항목 | 반영 내용 |
| --- | --- |
| 대사·시스템 | 4,972개 레코드. 중복을 묶은 원문·번역 4,006쌍을 대조하고 문맥·말투·호칭·줄 길이와 따옴표를 검수 |
| 추가 콘텐츠 | 용어·인물·줄거리·몬스터의 제목·본문 **338개**, 메뉴·배너 그림의 문구 **14개** |
| 아이템·적 이름 | 아이템명 레코드 10,941개, 적 이름 112개. 아이템 수에는 등급·변형별 반복 레코드가 포함됨 |
| 브라우저 | 텍스트 823개, 메뉴·설정·키보드 안내 등 이미지 문구 419개와 한글 배경 로고 |
| 저장·고정 메시지 | 날짜 글자 3개, VMU 파일 설명 6개, 아이템 획득 등의 짧은 메시지 조각 4개 |
| 오프닝 | 화면 문구 21개·노랫말 9개, 총 **30개 자막** 및 한글 로고. 원래 ADX 음성 섹터 유지 |
| UI·그림 | 한글 타이틀과 메뉴, 챕터 제목 2장·서적 광고 4장, 엔딩 2종 44페이지의 역할명·제작진 이름·한글화 크레딧. 설정 X/Y 정렬 및 상점 제목 폭 수정 |

적용 항목은 합계 **17,199개 레코드**이며, 추출·등록 목록에서 반영되지 않은 번역 항목은 0개입니다.
비언어 데이터·이벤트 명령 등은 검토 후 원본을 유지합니다. 이 수치는 게임 전체 원문 추출이나 모든 장면 검증의 완료를 뜻하지 않습니다.

### 추가 콘텐츠

게임 용어 **31항목**, 인물 **42항목**, 제1~6화 줄거리 **31페이지**, 몬스터 설명 **107개**를 번역했습니다.
용어 사전의 강조색과 커서·속성·장비 그림 기호를 유지하고, 페이지 그림 번호·목록 순서·원래 파일 크기를 보존합니다.
추가 콘텐츠 입구의 게임 사전·몬스터 도감·게임 정보 버튼도 한글로 표시합니다.

| 추가 콘텐츠 메뉴 | 사전·줄거리·인물 소개 |
| --- | --- |
| <img src="https://raw.githubusercontent.com/OldManCraveGuitars-bit/El-Dorado-Gate-Volume-3-Kr/v0.85/screenshots/extra-menu.png" width="320" alt="추가 콘텐츠 메뉴"> | <img src="https://raw.githubusercontent.com/OldManCraveGuitars-bit/El-Dorado-Gate-Volume-3-Kr/v0.85/screenshots/encyclopedia-menu.png" width="320" alt="사전·줄거리·인물 소개"> |

| 용어 사전 | 인물 소개 |
| --- | --- |
| <img src="https://raw.githubusercontent.com/OldManCraveGuitars-bit/El-Dorado-Gate-Volume-3-Kr/v0.85/screenshots/dictionary.png" width="320" alt="용어 사전"> | <img src="https://raw.githubusercontent.com/OldManCraveGuitars-bit/El-Dorado-Gate-Volume-3-Kr/v0.85/screenshots/character.png" width="320" alt="인물 소개"> |

| 줄거리 소개 | 몬스터 도감 |
| --- | --- |
| <img src="https://raw.githubusercontent.com/OldManCraveGuitars-bit/El-Dorado-Gate-Volume-3-Kr/v0.85/screenshots/story.png" width="320" alt="줄거리 소개"> | <img src="https://raw.githubusercontent.com/OldManCraveGuitars-bit/El-Dorado-Gate-Volume-3-Kr/v0.85/screenshots/monster-gallery.png" width="320" alt="몬스터 도감"> |


도감의 `????????`는 불러온 저장 데이터에서 아직 열리지 않은 항목입니다. 공개 패치에서 도감을 강제로 개방하지 않습니다.

### 오프라인 다운로드 상점

Vol.3에 들어 있던 다운로드 상품 **77종: 무기 33 · 방어구 25 · 액세서리 19**를 이용합니다.
게임의 다운로드 상점 담당 NPC와 원래 대화를 마친 뒤 구매하는 방식입니다.
외부 DLC 파일이나 인터넷 연결은 필요하지 않으며 **원래 가격·능력치·효과를 유지**합니다.
아이템을 인벤토리에 자동 지급하지 않습니다.

정상 게임 진행에서 배틀 아머를 400z에 판매하고 에어 레이피어를 원래 가격 100z에 구매했습니다.
남은 300z와 구매품을 VMU에 저장한 뒤 새 부팅으로 다시 불러와 보존되는 것을 확인했습니다.

| 오프라인 다운로드 상점 | 정상 가격으로 구매한 에어 레이피어 |
| --- | --- |
| <img src="https://raw.githubusercontent.com/OldManCraveGuitars-bit/El-Dorado-Gate-Volume-3-Kr/v0.85/screenshots/download-shop.png" width="320" alt="오프라인 다운로드 상점"> | <img src="https://raw.githubusercontent.com/OldManCraveGuitars-bit/El-Dorado-Gate-Volume-3-Kr/v0.85/screenshots/purchased-item.png" width="320" alt="정상 가격으로 구매한 에어 레이피어"> |


### 작은 글씨·좌표·화면 배치

시나리오 시작 제목은 **바탕체(BatangChe)**를 사용합니다. 광고·작은 메뉴 그림 글씨에는 **전기칩 한글 12px 원본 비트맵**과 정수 배율을 사용했습니다.
광고·추가 콘텐츠 메뉴의 글자를 맞추고, 설정 화면의 X/Y 겹침과
오우거 스톤 교환소 제목이 장식을 침범하는 문제를 수정했습니다.
추가 콘텐츠 사전 배너의 제목 잘림과 메뉴의 영어 잔상도 제거했습니다.

| 설정 화면 좌표 수정 | 브라우저 환경 설정 |
| --- | --- |
| <img src="https://raw.githubusercontent.com/OldManCraveGuitars-bit/El-Dorado-Gate-Volume-3-Kr/v0.85/screenshots/options.png" width="320" alt="설정 화면 좌표 수정"> | <img src="https://raw.githubusercontent.com/OldManCraveGuitars-bit/El-Dorado-Gate-Volume-3-Kr/v0.85/screenshots/browser.png" width="320" alt="브라우저 환경 설정"> |

| 한글 타이틀 | 메인 메뉴 |
| --- | --- |
| <img src="https://raw.githubusercontent.com/OldManCraveGuitars-bit/El-Dorado-Gate-Volume-3-Kr/v0.85/screenshots/title.png" width="320" alt="한글 타이틀"> | <img src="https://raw.githubusercontent.com/OldManCraveGuitars-bit/El-Dorado-Gate-Volume-3-Kr/v0.85/screenshots/main-menu.png" width="320" alt="메인 메뉴"> |


스크린샷은 실제 에뮬레이터 출력이며 AI로 만들거나 글자를 덧씌운 이미지가 아닙니다.
스크린샷 13장은 이전 v0.25~v0.29 및 v0.75 검수 때 촬영한 화면입니다. v0.85의 새 실행 캡처로 표시하지 않습니다. 이번에 바뀐 제목 그림은 위 ROM 자산 비교로 제공합니다.
각 캡처의 실제 빌드와 SHA-256은 [스크린샷 출처](https://github.com/OldManCraveGuitars-bit/El-Dorado-Gate-Volume-3-Kr/blob/v0.85/docs/screenshot-provenance.json)에 기록했습니다.

## 검증 범위

- 원본 게임 파일 **923개**를 크기·SHA-256으로 검사했습니다. 변경 60개, 원본 내용 유지 863개입니다.
- 변경 **15,389개 섹터**의 EDC/ECC와 원본 트랙 보존을 확인했습니다.
- 추가 콘텐츠 문자열 338개를 실제 GDI에서 다시 읽고, 페이지·그림 번호와 그림의 글자 영역 밖 픽셀을 대조했습니다.
- 한글 글꼴 1,043칸의 번호·픽셀을 유지했습니다. 원본 한 칸짜리 상태 배지 9개는 네모와 그림자를 보존해 한글로 바꿨습니다.
- 편집기 통합 검사 **17개**, 최근 이식 회귀 검사 **7개**, 패처 안전 검사 **7개**를 통과했습니다.
- 공개 EXE의 GUI와 내장 패치·엔진을 확인하고, **실제 원본 GDI에 적용한 결과 트랙 3개의 해시가 검증된 빌드와 일치**하는 것을 확인했습니다.
- Vol.3 원본의 트랙 배치(두 번째 트랙 LBA 600)를 유지합니다. 이전 v0.8에서 새 부팅·정상 VMU 불러오기·한글 상태 화면을 확인했습니다. v0.85는 제목 그림만 바꾼 실제 GDI와 EXE 적용 결과를 검사했으며, 새 부팅 검증은 하지 않았습니다.
- 기존 정상 진행에서 전투·아이템 획득·VMU 저장/불러오기·다운로드 상품 구매, 브라우저 메뉴와 주소 입력/삭제를 확인했습니다.

**7·8장 전체와 엔딩까지의 완주, 실기 구동, 모든 이미지·영상·추가 콘텐츠 페이지의 실제 재생 검증은 완료하지 않았습니다.**
오프닝 전체 디코딩·타이밍·원래 음성 보존은 검사했으며, 30개 자막 각각의 실제 재생과 모든 짧은 조사 문구의 사용 문맥은 추가 확인이 필요합니다.

[검증 요약](https://github.com/OldManCraveGuitars-bit/El-Dorado-Gate-Volume-3-Kr/blob/v0.85/docs/verification.json) · [EXE 패처 검증](https://github.com/OldManCraveGuitars-bit/El-Dorado-Gate-Volume-3-Kr/blob/v0.85/docs/patcher-verification.json) · [변경된 60개 게임 파일의 전후 해시](https://github.com/OldManCraveGuitars-bit/El-Dorado-Gate-Volume-3-Kr/blob/v0.85/docs/changed-files-sha256.json)

## SHA-256

| 파일 | 원본 SHA-256 | v0.85 적용 후 SHA-256 |
| --- | --- | --- |
| `track01.bin` | `e100c442c927b313e282aa2a34659bc3aeae5f27cf173640c2a9bd913d2b8499` | `e100c442c927b313e282aa2a34659bc3aeae5f27cf173640c2a9bd913d2b8499` |
| `track02.raw` | `cd7c82d88f21e4ebb32a94c65f15f625df871c933d6d78cbf85c671778a6ffca` | `cd7c82d88f21e4ebb32a94c65f15f625df871c933d6d78cbf85c671778a6ffca` |
| `track03.bin` | `ae452974db251a6ca20901c2fd1779f919e8ae157c3546284f9f0ad79baa365a` | `9ef09d7c76e9a898a02ba428a13889418f9c664c1bde25842608332b8f729334` |

출력 GDI SHA-256: `025516557d49e1835e7eb8571e09244b64db190cf3981ead555c54b1924ca19f`

패처 EXE SHA-256: `90f15de0285e142e7a123a628c0d5ddf8797ca6fb364c8956516dd13dd95b81e`

패치 데이터 SHA-256: `b0011bcff0c0fb73ccb0b2e251bb20d536957db77aa7f6ba254556faef801b7d`

[전체 해시·파일 크기](https://github.com/OldManCraveGuitars-bit/El-Dorado-Gate-Volume-3-Kr/blob/v0.85/hashes.json) · [배포 파일과 트랙 해시](https://github.com/OldManCraveGuitars-bit/El-Dorado-Gate-Volume-3-Kr/blob/v0.85/docs/HASHES.md) · [배포 파일 체크섬](https://github.com/OldManCraveGuitars-bit/El-Dorado-Gate-Volume-3-Kr/releases/download/v0.85/SHA256SUMS-v0.85.txt)

Windows PowerShell에서 다운로드한 파일을 확인할 수 있습니다.

```powershell
Get-FileHash -Algorithm SHA256 .\El-Dorado-Gate-Volume-3-Kr-v0.85-Patcher.exe
```

## 패처 소스와 라이선스

[패처 소스](https://github.com/OldManCraveGuitars-bit/El-Dorado-Gate-Volume-3-Kr/blob/v0.85/tools/patcher.py)와 [빌드 스크립트](https://github.com/OldManCraveGuitars-bit/El-Dorado-Gate-Volume-3-Kr/blob/v0.85/tools/build-patcher.ps1), [안전 검사](https://github.com/OldManCraveGuitars-bit/El-Dorado-Gate-Volume-3-Kr/blob/v0.85/tools/test_patcher.py)를 공개합니다.
패처는 Vol.1에서 사용한 MIT 라이선스 도구를 Vol.3 데이터·트랙 배치·내장 패치에 맞게 변경했습니다.
[패처 재빌드 방법](https://github.com/OldManCraveGuitars-bit/El-Dorado-Gate-Volume-3-Kr/blob/v0.85/docs/BUILD.md)을 참고하세요.

xdelta3 3.2.1은 [공식 릴리스](https://github.com/jmacd/xdelta/releases/tag/v3.2.1)의 Windows x64 엔진을 사용합니다.
시나리오 제목은 Windows 바탕체의 래스터 결과만 포함하며 해당 폰트 파일은 배포하지 않습니다.
새 패처 코드와 재사용한 패처 코드는 MIT, xdelta3는 Apache 2.0, 갈무리·MaruMinya·전기칩 글꼴은 SIL OFL 1.1을 따릅니다.
Python·Tcl/Tk·PyInstaller와 글꼴·엔진의 고지문은 [licenses](https://github.com/OldManCraveGuitars-bit/El-Dorado-Gate-Volume-3-Kr/tree/v0.85/licenses/) 및 EXE의 **라이선스** 버튼에서 확인할 수 있습니다.
원작 게임·캐릭터·그림·상표의 권리는 각 권리자에게 있습니다.

ZIP SHA-256: `c4ecf5f10c97362bd36c41a0b43c8717c53513638d6ad303ac52ea4f6262802e`

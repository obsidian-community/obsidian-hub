---
aliases:
- 
tags: 
- 
publish: true
---

%% ----- Badges ----- %%

![Downloads](https://img.shields.io/badge/downloads-90-573E7A?style=for-the-badge&logo=)
![GitHub last commit](https://img.shields.io/github/last-commit/towishy/Owen-Graphite?color=573E7A&label=last%20update&logo=github&style=for-the-badge)
![GitHub issues by-label](https://img.shields.io/github/issues/towishy/Owen-Graphite/help%20wanted?color=573E7A&logo=github&style=for-the-badge) 
![GitHub Repo stars](https://img.shields.io/github/stars/towishy/Owen-Graphite?color=573E7A&logo=github&style=for-the-badge)

%% ----- Badges ----- %%

%% ----- Do not edit this section ----- %%

# Owen Graphite

Repository: [GitHub](https://github.com/towishy/Owen-Graphite)
Designed by: [[towishy]]
Modes: [[Dark-mode themes|dark]], [[Light-mode themes|light]]



![screenshot](https://github.com/towishy/Owen-Graphite/raw/HEAD/screenshots/light.png)

%% ----- Do not edit anything above this line ----- %% 

%% Does the repository or author have any sponsoring links? Uncomment the next line and add them to the author's note. If they don't, please delete the placeholder tag: #placeholder/author %%
%% ![[towishy#Sponsor this author]] %%


## Features

- [[Themes with Friendly Settings|Friendly settings]]: Supports the [[obsidian-style-settings|Style Settings]] plugin

## Customization Options (Style Settings Plugin) 

**읽기와 본문**: 
- 본문 폰트 크기: 본문(p, li 등) 기본 글자 크기
- 본문 줄간격
- 본문 최대 폭
- 헤더 강조 색상

**표와 코드**: 
- 표 모던 스타일 강화: 표 헤더, 첫 컬럼, hover, PDF border를 보고서형 톤으로 강화
- PDF 블록 분할 방지 강화: callout, 표, mermaid, 코드블록, 이미지가 페이지 중간에서 잘리는 것을 완화

**보고서와 PDF**: 
- 보고서 모드 (헤더 자동 넘버링 + 본문 들여쓰기 + 세리프): 표지/넘버링/들여쓰기/세리프 본문을 한 번에 적용
- PDF Compact Report: PDF 출력 시 제목·본문·callout·표·참고 문헌 간격을 압축해 공백을 줄이고 정보 밀도를 높입니다.
- PDF 보고서 가시성 강화: PDF 출력에서 문서 상태 라벨, callout, 문서 끝 신호의 대비를 높입니다. 제목 계층과 표 디자인은 변경하지 않습니다.
- PDF 고객 전달용 화면 가시성: 메일, Teams, 브라우저 미리보기에서 바로 읽히도록 제목 위계, 본문·표 크기, callout 구분, 라벨 톤을 조정합니다.
- PDF 고객 전달 권장 프리셋: 고객 공유용 PDF에 맞춰 본문·표·callout·코드·링크를 한 번에 읽기 좋은 톤으로 조정합니다.
- PDF 글자 크기: PDF 출력에서 본문, 목록, callout, 코드, 헤더/푸터 라벨 크기를 조정합니다. 제목 계층과 표 디자인은 변경하지 않습니다.
- PDF 링크 출력 방식: PDF export에서 외부 URL을 본문 뒤에 표시할지, 숨길지, 참고문헌 중심으로 정리할지 선택합니다.
- 본문 세리프 글꼴: 본문만 Noto Serif KR로 전환 (긴 보고서 가독성)
- 첫 줄 들여쓰기: 한국 보고서 스타일 1em 들여쓰기
- 헤더 자동 넘버링 (1. 1.1 1.1.1)
- 드롭 캡 (첫 문단 첫 글자 크게)
- 간격 프리셋
- 액센트 컬러 프리셋
- 코드블록 테마

**워크스페이스와 접근성**: 
- 시선 보호 모드 (베이지 배경)
- OS 다크 모드 자동 추종: 시스템 다크 모드일 때 자동으로 다크 테마 변수 적용
- 데스크톱 Glass 강도: 데스크톱 UI chrome의 투명 유리/그림자 강도를 조정합니다. Reduced는 blur를 줄여 배터리와 저성능 환경에 적합합니다.
- 데스크톱 Hover 움직임: 버튼, 메뉴 항목, 설정 row의 hover/press lift 움직임을 조정합니다. Off는 움직임 없이 색과 그림자만 유지합니다.
- 한글/CJK 폰트 +0.5px 자동 보정

**PDF 헤더/푸터 작은 라벨**: PDF 출력에만 첫 페이지 헤더와 마지막 페이지 푸터 라벨을 표시합니다. 화면 Reading View에는 노출하지 않습니다.
- 첫 페이지 헤더 라벨 표시: PDF 첫 페이지 상단에 한 줄 라벨을 표시합니다. 끄면 문구나 프리셋이 있어도 출력하지 않습니다.
- 마지막 페이지 푸터 라벨 표시: PDF 마지막 콘텐츠 아래 중앙에 한 줄 라벨을 표시합니다. 끄면 문구나 프리셋이 있어도 출력하지 않습니다.
- PDF 라벨 구성: 단일 라벨은 기존처럼 한 문구만 표시합니다. Key/Value는 `Prepared by` + `Owen Lee`처럼 붙어 있는 1쌍으로 표시합니다.
- **공통 구성**: 
    - 헤더/푸터 빠른 문구: 직접 문구를 비워둘 때 쓰는 출력용 조합입니다. 직접 입력한 헤더/푸터 문구가 있으면 입력값이 우선됩니다.
    - 헤더/푸터 글자 색상: 두 라벨 공통 글자 색상입니다. 기본값은 출력물에 어울리는 graphite 톤입니다.
    - 헤더/푸터 라벨 스타일: PDF 엔진에서 안정적인 표면만 제공합니다. 위치나 페이지 흐름은 바꾸지 않습니다.
    - 헤더/푸터 라벨 크기: 글자와 내부 여백을 조정합니다. 출력 안정성을 위해 두 단계만 제공합니다.
- **헤더 설정**: 
    - 헤더 Key 색상: 첫 페이지 헤더의 왼쪽 key 영역 색상입니다. 예 `Prepared by` 쪽 색상입니다.
    - 헤더 Value 색상: 첫 페이지 헤더의 오른쪽 value 영역 색상입니다. 예 `Owen Lee - Sr. CSA` 쪽 색상입니다.
    - 첫 페이지 헤더 1번 Key 문구: 단일 라벨에서는 전체 문구, Key/Value에서는 1번 왼쪽 key입니다. 예 `Prepared by`.
    - 첫 페이지 헤더 1번 Value 문구: Key/Value 구성에서 1번 오른쪽 value로 표시됩니다. 예 `Owen Lee` 또는 `Sr. CSA`. 단일 라벨 구성에서는 사용하지 않습니다.
    - 첫 페이지 헤더 2번 Key/Value 표시: 기존 Key/Value 1쌍 구성에서 두 번째 key/value 쌍만 추가로 켭니다. PDF 라벨 구성에서 `Key/Value 2쌍`을 선택해도 같은 출력이 적용됩니다.
    - 헤더 2번 Key 색상: 첫 페이지 헤더의 2번 key segment 색상입니다. 예 `Reviewed by` 쪽 색상입니다.
    - 헤더 2번 Value 색상: 첫 페이지 헤더의 2번 value segment 색상입니다. 예 `Graphite QA` 쪽 색상입니다.
    - 첫 페이지 헤더 2번 Key 문구: 2번 key segment입니다. 예 `Reviewed by`.
    - 첫 페이지 헤더 2번 Value 문구: 2번 value segment입니다. 예 `Design QA` 또는 `2026-05-17`.
    - 첫 페이지 헤더 위치: 첫 페이지 헤더 라벨 위치를 선택합니다. Key/Value 구성에서는 두 segment가 같은 기준점에 붙어서 배치됩니다. 마지막 페이지 푸터는 안정성을 위해 중앙 하단으로 고정됩니다.
- **푸터 설정**: 
    - 푸터 Key 색상: 마지막 페이지 푸터의 왼쪽 key segment 색상입니다. 예 `Confidential` 쪽 색상입니다.
    - 푸터 Value 색상: 마지막 페이지 푸터의 오른쪽 value segment 색상입니다. 예 `End of Document` 쪽 색상입니다.
    - 마지막 페이지 푸터 Key 문구: 단일 라벨에서는 전체 문구, Key/Value에서는 왼쪽 key입니다. 예 `Confidential`.
    - 마지막 페이지 푸터 Value 문구: Key/Value 구성에서 오른쪽 value로 표시됩니다. 예 `Internal Use Only` 또는 `End of Document`. 단일 라벨 구성에서는 사용하지 않습니다.


%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/02%20-%20Community%20Expansions/02.05%20All%20Community%20Expansions/Themes/Owen%20Graphite.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/02%20-%20Community%20Expansions/02.05%20All%20Community%20Expansions/Themes/Owen%20Graphite.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>

---
aliases:
- 
tags: 
- 
publish: true
---

%% ----- Badges ----- %%

![Downloads](https://img.shields.io/badge/downloads-322-573E7A?style=for-the-badge&logo=)
![GitHub last commit](https://img.shields.io/github/last-commit/amdhj22/rbr.obsidian?color=573E7A&label=last%20update&logo=github&style=for-the-badge)
![GitHub issues by-label](https://img.shields.io/github/issues/amdhj22/rbr.obsidian/help%20wanted?color=573E7A&logo=github&style=for-the-badge) 
![GitHub Repo stars](https://img.shields.io/github/stars/amdhj22/rbr.obsidian?color=573E7A&logo=github&style=for-the-badge)

%% ----- Badges ----- %%

%% ----- Do not edit this section ----- %%

# RBR

Repository: [GitHub](https://github.com/amdhj22/rbr.obsidian)
Designed by: [[amdhj22]]
Modes: [[Dark-mode themes|dark]]



![screenshot](https://github.com/amdhj22/rbr.obsidian/raw/HEAD/screenshot.png)

%% ----- Do not edit anything above this line ----- %% 

%% Does the repository or author have any sponsoring links? Uncomment the next line and add them to the author's note. If they don't, please delete the placeholder tag: #placeholder/author %%
%% ![[amdhj22#Sponsor this author]] %%


## Features

- [[Themes with Friendly Settings|Friendly settings]]: Supports the [[obsidian-style-settings|Style Settings]] plugin

## Customization Options (Style Settings Plugin) 

**Accent**: 
- Primary accent color: 활성/선택 항목 강조에 쓰일 메인 색.
RBR 기본 룰은 Kerb Red. 커서는 별개 — 아래 Cursor 옵션 참고.


**Headings**: 
- Heading style: h1~h3 색상 패턴.
  Trio        : h1=accent · h2=yellow · h3=white (RBR 기본)
  Mono        : 모든 헤딩이 본문 색 (강조 최소화)
  Accent only : h1만 accent, 나머지는 본문 색


**Cursor**: 
- Cursor color: 에디터 커서 색.
  RB Yellow  : RBR 기본 — 항상 주목 픽셀
  RB Warm    : 한 단계 덜 자극적인 따뜻한 노랑
  Follow accent : 위 Primary accent를 따라감


**Tab indicator**: 
- Active tab indicator: 활성 탭 강조 방식.
  Top    : 위쪽에 accent 색 띠 (RBR 기본)
  Bottom : 아래쪽 띠
  Fill   : 탭 전체 배경에 accent 옅게 깔기


**Typography**: 
- Code font size: 코드 블록과 인라인 코드의 폰트 크기 (em).
- Highlight intensity: ==하이라이트== 배경 alpha. 검색 매치도 같은 값을 사용.
0.10 = 거의 안 보임, 0.60 = 강한 강조.


**Auto hide**: 마우스를 올렸을 때만 보이도록 UI 요소를 숨긴다.
호버가 없는 모바일에서는 자동 비활성.

- Auto hide tab bar: 탭 헤더 바를 숨기고 상단/타이틀바에 호버하면 펼침.
- Auto hide status bar: 하단 상태바를 가는 띠로 줄이고 호버 시 펼침.
- Auto hide left ribbon: 좌측 리본 메뉴를 가는 띠로 줄이고 호버 시 펼침.
- Auto hide vault profile: 좌측 사이드바 하단의 vault 프로필 영역 숨김. 사이드바 호버 시 펼침.
- Hover delay before expanding: 호버 후 펼쳐지기까지 대기 시간 (ms).
커서가 잠깐 지나가는 것만으로 깜빡이지 않게 하는 hover-intent 지연.
0 = 즉시 펼침, 100 = 살짝만 확인(기본), 400+ = 의도적으로 머무를 때만.

- Expand/collapse animation duration: 자동 숨김 영역이 펼쳐지고 닫히는 애니메이션 길이 (ms).
짧을수록 가볍고 스냅함. 기본 80ms. 더 스냅하게 60까지 내릴 수 있음.
layout-property transition 비용을 줄여 마우스 hover 시
메인 스레드 부담을 직접 낮춤.

- Tab strip top hover zone (above strip): 접힌 탭 strip 위쪽(타이틀바 방향) hover 영역의 높이 (px).
아래쪽 hover 영역은 "펼친 탭 높이"에 자동으로 맞춰지므로 이 값과
무관하다 — 이 슬라이더는 위쪽 밴드/타이틀바 트리거 높이만 조절.
메인 에디터/좌우 사이드 패널 strip 모두에 적용.

- Expanded ribbon width (= hover hit zone): 접힌 ribbon 위로 마우스를 올렸을 때 펼쳐지는 폭 (px).
hover hit zone 이 이 값과 항상 동일하게 맞춰짐 — 즉 "펼쳐질 리본이
차지할 자리"가 그대로 hover 영역이 된다. 그 자리에 마우스를 올리면
리본이 딱 그 자리로 펼쳐짐.
값을 키우면 리본이 더 넓게 펼쳐지면서 hover 영역도 같이 넓어짐.
아이콘은 hit zone 밴드 위에 있어서 폭을 키워도 클릭은 안 막힘.
주의: 접힌 6px 를 넘는 hover 밴드 구간의 클릭은 ribbon 으로 캡처됨.

- Expanded status bar height (= hover hit zone): 상태 바가 hover 시 펼쳐지는 높이 (px). hover hit zone 이 이 값과
동일하게 맞춰져 "펼쳐질 자리"가 그대로 hover 영역이 된다 — 리본과
같은 방식. 값을 키우면 상태 바가 더 높게 펼쳐지고 hover 영역도
같이 넓어짐.


**Card layout**: 워크스페이스 패널을 카드처럼 분리해서 표시.
여백 + 둥근 모서리 + 부드러운 그림자가 추가된다.

- Enable card layout: 카드 레이아웃 켜기/끄기.
- Card corner radius: 카드 모서리 라운딩 (px).
- Card gap: 카드 사이 간격 (px).


%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/02%20-%20Community%20Expansions/02.05%20All%20Community%20Expansions/Themes/RBR.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/02%20-%20Community%20Expansions/02.05%20All%20Community%20Expansions/Themes/RBR.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>

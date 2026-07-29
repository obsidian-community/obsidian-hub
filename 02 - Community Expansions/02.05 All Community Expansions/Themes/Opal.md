---
aliases:
- 
tags: 
- 
publish: true
---

%% ----- Badges ----- %%

![Downloads](https://img.shields.io/badge/downloads-279-573E7A?style=for-the-badge&logo=)
![GitHub last commit](https://img.shields.io/github/last-commit/cyriusweng/opal-theme?color=573E7A&label=last%20update&logo=github&style=for-the-badge)
![GitHub issues by-label](https://img.shields.io/github/issues/cyriusweng/opal-theme/help%20wanted?color=573E7A&logo=github&style=for-the-badge) 
![GitHub Repo stars](https://img.shields.io/github/stars/cyriusweng/opal-theme?color=573E7A&logo=github&style=for-the-badge)

%% ----- Badges ----- %%

%% ----- Do not edit this section ----- %%

# Opal

Repository: [GitHub](https://github.com/cyriusweng/opal-theme)
Designed by: [[cyriusweng]]
Modes: [[Dark-mode themes|dark]], [[Light-mode themes|light]]



![screenshot](https://github.com/cyriusweng/opal-theme/raw/HEAD/screenshot.png)

%% ----- Do not edit anything above this line ----- %% 

%% Does the repository or author have any sponsoring links? Uncomment the next line and add them to the author's note. If they don't, please delete the placeholder tag: #placeholder/author %%
%% ![[cyriusweng#Sponsor this author]] %%


## Features

- [[Themes with Friendly Settings|Friendly settings]]: Supports the [[obsidian-style-settings|Style Settings]] plugin

## Customization Options (Style Settings Plugin) 

**配色**: 
- 主强调色: 链接、选中、焦点等核心交互色。
- 副强调色: 第二强调色，用于次级高亮、渐变的另一端。默认青。
- 强调色鲜艳度: 1=原样，小于 1 更灰更沉，大于 1 更艳。老引擎不支持时自动忽略。
- 浅色底色温: 给浅色背景掺入的色调（暖灰选桃、冷灰选蓝、紫灰选紫）。要配合下面的强度才生效。
- 深色底色温: 给深色背景掺入的色调。要配合下面的强度才生效。
- 底色温强度: 上面色温掺进背景的比例。0=纯中性灰（默认），越大染色越明显。
- 面板分层强度: 侧栏/卡片这些「面」相对正文背景的明暗差。100=正常分层（默认），越小越扁平、越贴近背景。
- 代码块底色
- 高亮主色: 荧光笔高亮的基准色（波浪线/辉光都取自它）。
- 高亮风格: 霓虹波浪=波浪下划线+辉光（默认）。纯色底=传统荧光块。柔和底=淡色块。裁字=只给字上色。
- 标题配色: 彩虹多色=每级一色（默认）。同色渐变=一色族由亮到暗。单色=都用主色。逐级自定=用下面 6 个色钮。关闭=退回正文色。
- 标签配色: 首字母伪哈希=按标签首字母散成 26 色（默认）。语义=只给紧急/完成等词库上色，其余统一。单色=统一。
- 未创建笔记的链接样式: 指向还不存在笔记的链接怎么显示。虚线（默认）/ 变灰 / 模糊 / 加问号角标。

**字体**: 
- 正文字体: 填字体名即可（多个用英文逗号隔开）。把 Inter 换成你要的，如 Beiruti。后面自动接系统中文兜底。
- 标题字体: 标题专用字体。留 Inter 或换成你的展示字体。
- 代码/等宽字体
- 界面字体: 侧栏、菜单、标签页等界面文字的字体。
- 正文字号
- 正文行高
- 正文字间距
- 粗体不上色: 默认粗体是桃色。打开后粗体回退成正文色，只加粗不变色。
- 代码字体特性: 高级项。填 OpenType 特性，如 "liga" 1, "calt" 1 开连字，"zero" 1 斜杠零。留 normal 则默认。

**标题分级**: 
- H1 字号
- H2 字号
- H3 字号
- H4 字号
- H5 字号
- H6 字号
- H1 字重
- H2 字重
- H3 字重
- H4 字重
- H5 字重
- H6 字重
- 标题下划线: 标题的下边线，可与下面的「标题前缀」叠加。渐变下划线（默认，各级自身色淡出）/ 单线底边 / 无。
- 标题前缀: 标题前的标记，可与上面的「标题下划线」叠加。无（默认）/ 悬挂井号（左侧露出
- H1 颜色（逐级自定时用）
- H2 颜色（逐级自定时用）
- H3 颜色（逐级自定时用）
- H4 颜色（逐级自定时用）
- H5 颜色（逐级自定时用）
- H6 颜色（逐级自定时用）

**布局尺寸**: 
- 正文行宽: 一行最多多宽（可读宽度）。最常调的一项。
- 表格铺满行宽: 打开后表格占满可用宽度，不再被行宽夹窄。
- 图表超宽改横向滚动: 默认超出行宽的 Mermaid 图会等比缩放适应行宽。打开此项改为保持原大小、超宽部分横向滚动查看。
- 段落间距
- 首行缩进排版: 打开后段落首行缩进两字、段间不留空（书本式）。关闭则段间留空、不缩进（网页式，默认）。
- 列表缩进
- 编辑区上下边距
- 图片圆角
- 图片最大宽度
- 图片投影: 打开后图片带柔和投影，像浮起的照片。
- 背景纹理: 编辑区背景纹理。无（默认）/ 点阵 / 方格纸 / 横线纸。
- 圆角大小
- 圆角形状: 超椭圆=iOS 式更柔的角（默认；老引擎自动退标准圆角）。标准圆角 / 凹角 scoop / 斜角 bevel。

**界面线条与边框**: 
- 全局边框粗细: 卡片、输入框、表格、菜单等所有描边的统一粗细。
- 全局边框颜色
- 分隔线风格: 正文分隔线（---）的样式。渐隐（默认）/ 实线 / 虚线 / 圆点 / 双线。
- 显示面板分隔边框: 打开后相邻面板之间画出分隔线，边界更清楚。默认关（靠留白区分）。
- 文件树缩进参考线: 侧栏文件树每层缩进画一条竖参考线（默认开）。关闭则只靠缩进。
- 正文列表缩进线: 正文里多级列表每层画竖参考线，看清层级。默认关。
- 焦点环风格: 输入框/按钮获得焦点时的提示。描边（默认）/ 发光 / 无。
- 滚动条粗细
- 表格边框: 仅横线（默认）/ 全框（每格描边）/ 无框。

**元素开关**: 
- 去掉链接下划线: 打开后所有链接不带下划线，只用颜色区分。
- 代码块自动换行: 打开后长代码行自动折行，不再横向滚动。
- 代码连字: 打开后代码里连字合成合字（需字体支持）。
- 关闭表格斑马纹: 默认偶数行有淡色底。打开此项取消斑马纹。
- 高亮当前行: 打开后光标所在行有淡强调色底，便于定位。
- 聚焦暗化: 打开后非当前段落变淡，只有正在写的那段清晰。
- 复选框回退原生: 打开后不用自定义状态样式，退回系统原生复选框。
- 列表符号: 分层形状=按深度 ●○▪– 变形+单色（默认）。彩虹循环=形状不变、按深度换色。单色圆点=各级都用同色实心圆点。
- 关闭氛围背景光晕: 编辑区背后默认有极淡角落光晕。打开此项关掉它。

**皮肤与动效**: 
- 表面质感: 实底=性能/可读最佳（默认）。毛玻璃=通透。液态玻璃=最有质感最吃性能。系统开「减少透明度」自动退实底。
- 界面设计语言: 整体控件观感。中性（默认）/ Cupertino（圆润+轻投影）/ Fluent（微亮描边）/ Material（实底+明确阴影）。
- Callout 皮肤: 融合款=软底+左条+轻抬升（默认）。硬阴影 / 描边 / HUD发光 / 反色标题条 / 折角纸片。
- 文件夹着色: 彩虹脊柱=顶层循环色+子树继承（默认）。编号分区=按 00/10/20 前缀分色。单色 / 关闭。
- 动效总取向: 一个旋钮统管全站微动效。关=全静态。微=更轻更慢。标准=克制快顺（默认）。活泼=幅度大带回弹。系统开「减少动态」自动全关。
- 入场动效: 开笔记时整篇淡入一次。去模糊合焦（默认）/ 平滑平移 / 弹性过冲。
- 复古皮肤: 整套复古外壳。无（默认）/ 合成波 / 绿磷终端 / 琥珀CRT / 数字雨。

**打印导出**: 
- 导出保留暗色: 默认导出转纸面浅色（省墨可读）。打开后保留暗底（需在导出设置里开 printBackground）。
- 打印正文字体: 导出时正文换成。衬线（默认，纸面易读）/ 不置换 / 打字机。
- 打印段落对齐: 两端对齐+首行缩进（默认，书本式）/ 齐左。


%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/02%20-%20Community%20Expansions/02.05%20All%20Community%20Expansions/Themes/Opal.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/02%20-%20Community%20Expansions/02.05%20All%20Community%20Expansions/Themes/Opal.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>

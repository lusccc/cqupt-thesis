\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{cqupt_thesis}


\DeclareOption*{\PassOptionsToClass{\CurrentOption}{ctexbook}}
\ProcessOptions\relax
%  咱们重邮模板是oneside的！
\LoadClass[a4paper,UTF8,oneside, openany, zihao=-4,AutoFakeBold]{ctexbook}

\RequirePackage{float}
\RequirePackage{amsmath}
%https://tex.stackexchange.com/questions/43835/conflict-between-amsthm-and-some-other-package
\RequirePackage{amsthm}
\let\proof\relax
\let\endproof\relax
\RequirePackage{pifont}
% 解图表目录引用编号顺序问题
\RequirePackage{notoccite}
% 加入hyperref超链接参考
\RequirePackage{hyperref}
% fancyhdr 宏包提供了方便使用的命令用于设置页眉、页脚。
\RequirePackage{fancyhdr}
\RequirePackage{titletoc}
% 加入判断支持
\RequirePackage{ifthen}
% 此宏包提供图形支持。
\RequirePackage{graphicx}
% 颜色
\RequirePackage{xcolor}
\RequirePackage{multirow}
\RequirePackage{array}
\RequirePackage{setspace}
\usepackage{booktabs}
\RequirePackage{enumitem}
%TODO pdfpages 宏包便于我们插入扫描后的授权说明和声明页 PDF 文档。
\RequirePackage{pdfpages}
\includepdfset{fitpaper=true}

% 以下是一些文档默认设置：
\RequirePackage{geometry}%使用geometry调整边距
\geometry{a4paper,papersize={21cm,29.7cm}}
%http://www.ctex.org/documents/packages/layout/geometry.htm
\geometry{left=3.5cm,right=2.45cm,top=3.1cm,bottom=2.4cm,footskip=0.14cm,headsep=0.75cm,headheight=1.5cm}

% 页眉页脚、线
\pagestyle{fancy}
\renewcommand\headrulewidth{0.8pt}

% 字体、段落设置
\RequirePackage{xeCJK}
\xeCJKsetup{CheckSingle=true} % 首字不放行尾，似乎不太有用
\punctstyle{hangmobanjiao} % 行末半角，使得中文标点符号后的距离和word一致
\setmainfont{Times New Roman}
\setCJKmainfont[AutoFakeBold=1.8,ItalicFont=KaiTi]{SimSun}
\newCJKfontfamily\cuheiti{heiti}[AutoFakeBold=1.8]
\newCJKfontfamily\cusongti{SimSun}[AutoFakeBold=1.8]
\setmonofont[Mapping=tex-text]{Consolas}
% ！封面至声明页 行距设为1.5，注意不等同于word的1.5倍行距
\linespread{1.5}\selectfont

% 这些命令用于设定各项文档信息的具体内容。
\newcommand\@classifiedindex{}
\newcommand\@udc{}
\newcommand\@statesecrets{}
\newcommand\@paperno{}
\newcommand\@cntitle{}
\newcommand\@cnsubtitle{}
\newcommand\@cnsubsubtitle{}
\newcommand\@entitle{}
\newcommand\@ensubtitle{}
\newcommand\@ensubsubtitle{}
\newcommand\@stuno{}
\newcommand\@name{}
\newcommand\@degreeclass{}
\newcommand\@major{}
\newcommand\@supervisor{}
\newcommand\@completedate{}
\newcommand\@cnkeywords{}
\newcommand\@enkeywords{}
\newcommand\classifiedindex[1]{\renewcommand\@classifiedindex{#1}}
\newcommand\udc[1]{\renewcommand\@udc{#1}}
\newcommand\paperno[1]{\renewcommand\@paperno{#1}}
\newcommand\statesecrets[1]{\renewcommand\@statesecrets{#1}}
\newcommand\cntitle[1]{\renewcommand\@cntitle{#1}}
\newcommand\cnsubtitle[1]{\renewcommand\@cnsubtitle{#1}}
\newcommand\cnsubsubtitle[1]{\renewcommand\@cnsubsubtitle{#1}}
\newcommand\entitle[1]{\renewcommand\@entitle{#1}}
\newcommand\ensubtitle[1]{\renewcommand\@ensubtitle{#1}}
\newcommand\ensubsubtitle[1]{\renewcommand\@ensubsubtitle{#1}}
\newcommand\stuno[1]{\renewcommand\@stuno{#1}}
\newcommand\name[1]{\renewcommand\@name{#1}}
\newcommand\degreeclass[1]{\renewcommand\@degreeclass{#1}}
\newcommand\major[1]{\renewcommand\@major{#1}}
\newcommand\supervisor[1]{\renewcommand\@supervisor{#1}}
\newcommand\completedate[1]{\renewcommand\@completedate{#1}}
\newcommand\cnkeywords[1]{\renewcommand\@cnkeywords{#1}}
\newcommand\enkeywords[1]{\renewcommand\@enkeywords{#1}}

\newcommand{\makecoverINFOcell}[1]{
    \hspace{3mm}\CJKunderline[depth=0.8em]{\makebox[10.06cm][c]{ \zihao{-3}\textbf{#1}}}
}

\newcommand{\makecover}{

    \begin{titlepage}
        \zihao{-4}
        \vspace*{-2mm}
%        \hspace{1.57cm}\parbox[b]{15.37cm}{
        \hspace{0.599cm}\parbox[b]{15.37cm}{
            \makebox[2.65cm][c]{\textbf{分类号}}
            %1.5mm, 1.1mm是单元格边距
            \hspace{1mm}\CJKunderline[thickness=1.3pt,]{\makebox[2.97cm][c]{\textbf{\@classifiedindex}}}\hspace{1.2mm}
            \makebox[3cm][c]{\textbf{密级}}
            \hspace{1.1mm}\CJKunderline[thickness=1.3pt,]{\makebox[4.39cm][c]{\textbf{\@statesecrets}}}
            \\[-0.1mm]
            \makebox[2.65cm][c]{\textbf{UDC}}
            \hspace{1.5mm}\CJKunderline[thickness=1.3pt,]{\makebox[2.97cm][c]{\textbf{\@udc}}}\hspace{1.3mm}
            \makebox[3cm][c]{\textbf{学位论文编号}}
            \hspace{1.1mm}\CJKunderline[thickness=1.3pt,]{\makebox[4.39cm][c]{\textbf{\@paperno}}}
        }


        \zihao{2}
        \vspace{2.35cm}
        \hspace{1.379cm}\textbf{重庆邮电大学硕士学位论文}

        \zihao{-4}
        \vspace{2.56cm}
        \hspace{0.36cm}
        \renewcommand{\arraystretch}{1.228}
%        \begin{tabular}{p{1.7cm} c<{\rule[2mm]{0pt}{7mm}}}
        \begin{tabular}{p{1.7cm} c}
            \makebox[1.7cm][l]{\textbf{中文题目}} & \makecoverINFOcell{\@cntitle}       \\
            \ifthenelse{\equal{\@cnsubtitle}{}}{}{
                & \makecoverINFOcell{\@cnsubtitle}    \\
            }
            \ifthenelse{\equal{\@cnsubsubtitle}{}}{}{
                & \makecoverINFOcell{\@cnsubsubtitle} \\
            }
            \makebox[1.7cm][l]{\textbf{英文题目}} & \makecoverINFOcell{\@entitle}       \\
            \ifthenelse{\equal{\@ensubtitle}{}}{}{
                & \makecoverINFOcell{\@ensubtitle}    \\
            }
            \ifthenelse{\equal{\@ensubsubtitle}{}}{}{
                & \makecoverINFOcell{\@ensubsubtitle} \\
            }
            \makebox[1.7cm][s]{\textbf{学号}}   & \makecoverINFOcell{\@stuno}         \\
            \makebox[1.7cm][s]{\textbf{姓名}}   & \makecoverINFOcell{\@name}          \\
            \makebox[1.7cm][s]{\textbf{学位类别}} & \makecoverINFOcell{\@degreeclass}   \\
            \makebox[1.7cm][s]{\textbf{学科专业}} & \makecoverINFOcell{\@major}         \\
            \makebox[1.7cm][s]{\textbf{指导教师}} & \makecoverINFOcell{\@supervisor}    \\
            \makebox[1.7cm][s]{\textbf{完成日期}} & \makecoverINFOcell{\@completedate}  \\
        \end{tabular}
    \end{titlepage}
}

\newcommand{\makestatement}{
        {
        \clearpage
        \thispagestyle{empty}
        \setlength{\baselineskip}{25pt}
        \vspace*{-1.35cm}
        \begin{center}
            \heiti\zihao{-2} 独\hspace{0.5em}创\hspace{0.5em}性\hspace{0.5em}声\hspace{0.5em}明
        \end{center}
        \vspace{-0.5mm}
        \renewcommand{\CJKglue}{\hskip 0pt plus 0.08\baselineskip} % 字距调整至和word一样
        \par 本人声明所呈交的学位论文是本人在导师指导下进行的研究工作及取得的研究成果。尽我所知，除了文中特别加以标注和致谢的地方外，论文中不包含他人
    已经发表或撰写过的研究成果，也不包含为获得\CJKunderline[thickness=0.6pt,depth=0.12em]{\quad 重庆邮电大学\quad}或其他单位的
    学位或证书而使用过的材料。与我一同工作的人员对本文研究做出的贡献均已在论文中作了明确的说明并致以谢意。
        \\
        \par  作者签名：\hspace{5.5cm}  日期：\hspace{1.32cm} 年\hspace{0.54cm} 月\hspace{0.54cm} 日

        \vspace{3.71cm}
        \begin{center}
            \heiti\zihao{-2} \textbf{学位论文版权使用授权书}
        \end{center}
        \vspace{1.4mm}
        % 服了，上面25磅，这里24磅，
        \setlength{\baselineskip}{24pt}
        \renewcommand{\CJKglue}{\hskip 0pt plus 0.08\baselineskip}
%        \renewcommand{\CJKglue}{\hskip -0.2pt plus 0.08\baselineskip}
        % 注意 1个\quad = 1em = 2个word中文空格
        \par  本人完全了解\CJKunderline[thickness=0.6pt,depth=0.12em]{\hspace{1.5em}重庆邮电大学\hspace{1.5em}}有权保留、使用学位论文纸质版和电子版
    的规定，即学校有权向国家有关部门或机构送交论文，允许论文被查阅和借阅等。
    本人授权\CJKunderline[thickness=0.6pt,depth=0.12em]{\hspace{1.5em}重庆邮电大学\hspace{1.5em}}可以公布本学位论文的全部或部分内容，可编入有
    关数据库或信息系统进行检索、分析或评价，可以采用影印、缩印、扫描或拷贝
    等复制手段保存、汇编本学位论文。
        \par（注：保密的学位论文在解密后适用本授权书。）
        \par \vspace{26pt}
        \par 作者签名：\hspace{5.5 cm}导师签名：
        \vspace{4pt}
        \par 日期:\qquad\qquad 年\hspace{1.5em} 月\hspace{1.5em} 日 \hspace{2.02cm} 日期:\hspace{1.26cm} 年\hspace{1.5em} 月\hspace{1.5em} 日
    }
}

%摘要及之后中文的正文，小四1.5倍行距等同的linespread=1.62
%https://www.jianshu.com/p/9c0d74d741dd
\linespread{1.62}\selectfont
\renewcommand{\CJKglue}{\hskip 0pt plus 0.08\baselineskip} % 0.08字距调整至和word一样

% CTEX设置各级标题对齐方式，字号，字体及前后段间距
%使用 fixskip 来抑制标题的额外间距。这里的 beforeskip 和 afterskip
%是与 Word 样例对比后通过尝试得出的。
\renewcommand{\theparagraph}{(\arabic{paragraph})}
\ctexset{
    chapter= {
        pagestyle={fancy},
        format+={\rm\zihao{3}\heiti\bfseries},
        number={\arabic{chapter}},
        numberformat={\normalfont},
%        aftername={\hspace{\ccwd}},
        aftername={\hspace{0.5em}},
        beforeskip={19pt},
        afterskip={33pt},
        fixskip=true
    },
    section={
        format+={\rm\zihao{-3}\heiti\bfseries\flushleft},
        numberformat={\normalfont},
        aftername={\hspace{0.5em}},
%        aftername={\hspace{\ccwd}},
        beforeskip={13pt},
        afterskip={13pt}
    },
    subsection={
        format+={\zihao{4}\rm\heiti\flushleft},
        numberformat={\normalfont},
        aftername={\hspace{0.5em}},
%        aftername={\hspace{\ccwd}},
        beforeskip={13pt},
        afterskip={13pt}
    },
    subsubsection={
        format+={\cusongti\bfseries},
        number={\hspace{\ccwd}\hspace{\ccwd}\arabic{subsubsection}.},
        aftername={\hspace{0.3em}},
%        number={\hspace{\ccwd}\hspace{\ccwd}\arabic{subsubsection}.},
%        aftername={\quad},
        beforeskip={0pt},
        afterskip={0pt}
    }
}

%https://www.shangmayuan.com/a/80b54c9f1c574f5982b1f69b.html
\newcommand{\makefancyhf}[1]{
    \fancyhf{}
    \fancyhead[L]{\songti\zihao{5} 重庆邮电大学硕士学位论文 \vspace{0.22cm}}
    \fancyhead[R]{\songti\zihao{5} #1 \hspace{0.2cm} \vspace{0.22cm}}
    \fancyfoot[CO,CE]{\zihao{-5}\thepage}
}

\newenvironment{cnabstract}{
    \clearpage
    \pagenumbering{Roman}
    \makefancyhf{摘要}
    \vspace*{-0.78cm}
    \begin{center}
        \heiti\zihao{3}
        摘要
    \end{center}
    \vspace{0.23cm}
    \par
    \renewcommand{\CJKglue}{\hskip -0.22pt plus 0.01\baselineskip} % 0.01表示汉字间距离可伸缩
}
{
    \vspace{21pt}\par
    {\textbf{\cusongti{关键词：}}} \@cnkeywords
}

\newenvironment{enabstract}{
    \clearpage
    \makefancyhf{Abstract}
%    \vspace*{-0.667cm}
%    \begin{center}
%        \zihao{3}
%        \textbf{Abstract}
%    \end{center}
%    \vspace*{0.28cm}
    \chapter*{Abstract}
    \par
    % word中英文的1.5倍行距对应的是1.44
    \linespread{1.44}\selectfont
    }
    {
    \vspace{21pt}\par
    {\textbf{\cusongti{Keywords: }}} \@enkeywords
}

% ------开始设置 目录样式
% 使用hyperref宏包去除索引上的颜色标记
\RequirePackage{hyperref}
\hypersetup{pdfborder=0 0 0}
% 把表录、图录、参考文献 加入目录
\usepackage[nottoc,notlot,notlof]{tocbibind}


% 使用tocloft宏包修改目录样式
\RequirePackage[subfigure]{tocloft} % 兼容subfigure
%\renewcommand{\cftdot}{$\cdot$}
\renewcommand{\cftdotsep}{0.5}
%\setlength{\cftbeforechapskip}{10pt}

\renewcommand{\cftchapleader}{\cftdotfill{\cftchapdotsep}}
\renewcommand{\cftchapdotsep}{\cftdotsep}

% 控制目录内容的行距
%\renewcommand\cftchapafterpnum{\vskip      -18pt}
%\renewcommand\cftsecafterpnum{\vskip       -18pt}
%\renewcommand\cftsubsecafterpnum{\vskip    1pt}
\setlength{\cftbeforechapskip}  {0em}
\renewcommand\cftchappagefont{\normalfont}

% 目录两字标题的设置，toc
\renewcommand\contentsname{目录}
\renewcommand{\cfttoctitlefont}{\hfill\zihao{3}\rm\heiti}
\renewcommand{\cftbeforetoctitleskip}{8pt}%此处魔改 目录 大标题行距
\renewcommand{\cftaftertoctitleskip}{10pt}
\renewcommand{\cftaftertoctitle}{\hfill}%相当于均匀排布、居中

% 目录内容章、节 lof lob 设置
\renewcommand{\cftchapfont}{\normalfont}
\renewcommand{\cftsecfont}{\normalfont}
\renewcommand\listfigurename{图录}
\renewcommand\listtablename{表录}
\renewcommand{\cftloftitlefont}{\hfill\zihao{3}\rm\heiti}
\renewcommand{\cftlottitlefont}{\hfill\zihao{3}\rm\heiti}
\renewcommand{\cftafterloftitle}{\hfill}
\renewcommand{\cftafterlottitle}{\hfill}
\renewcommand{\cftbeforeloftitleskip}{8pt}%此处魔改 表录、图录 大标题行距，下同
\renewcommand{\cftbeforelottitleskip}{8pt}
\renewcommand{\cftafterloftitleskip}{10pt}
\renewcommand{\cftafterlottitleskip}{10pt}

\setcounter{secnumdepth}{3}     % 设定章节计数深度
\setcounter{tocdepth}{2}        % 设置目录计数深度

% 调整序号和标题名称之间的空隙为word中的一个空格， 调整缩进
%\setlength\cftchapnumwidth{-100cm}
%这个不行https://gitee.com/wuzhouhui/awk/blob/8a8c3a25d8191d9808339aeb7358366bbbd245aa/latex_src/preamble.tex
%\settowidth\cftchapnumwidth{第十章} % 最宽的可能编号
%这个行
\renewcommand{\cftchapaftersnumb}{\hspace{-0.45em}}
\setlength\cftsecnumwidth{0.5em}
\setlength\cftsubsecnumwidth{0.5em}
\setlength\cftsecindent{0.7cm}% Indent
\setlength\cftsubsecindent{1.43cm}% Indent

% 使得 点线与页码数字 之间的空隙减少
%https://tex.stackexchange.com/questions/196416/dotted-leader-does-not-reach-the-page-number-in-toc
\usepackage{everypage}
\usepackage{calc}
\AddEverypageHook{\addtocontents{toc}{
    \protect\cftsetpnumwidth{\widthof{\thepage}-0.02em}
}}

% ------结束设置 目录样式

\newcommand{\maketoc}{
    \clearpage
    \makefancyhf{目录}
    \tableofcontents
    \thispagestyle{fancy}
}

\newcommand{\makefigtablist}{
    \clearpage
    \makefancyhf{图录}
    \listoffigures
%    \addcontentsline{toc}{chapter}{图录}
    \thispagestyle{fancy}

    \clearpage
    \makefancyhf{表录}
    \listoftables
%    \addcontentsline{toc}{chapter}{表录}
    \thispagestyle{fancy}
    \clearpage
}
\usepackage{ragged2e}
\newcolumntype{P}[1]{>{\RaggedRight\hspace{0pt}}p{#1}} % 固定宽度列、居左
\newcommand\makecommenttable[1]{
    \addcontentsline{toc}{chapter}{注释表}
    \makefancyhf{注释表}
    \chapter*{注释表}
    \vspace{-0.7cm}
    \renewcommand{\arraystretch}{1.6}
    \begin{table}[H]
        \hspace{-9pt}
%    \centering
        \begin{tabular}{P{1.8cm}P{13cm}}
            #1\\
        \end{tabular}
    \end{table}
    \clearpage
}


%数学环境
\RequirePackage{unicode-math}
\newtheoremstyle{theoremdd}% name of the style to be used
{0pt}% measure of space to leave above the theorem. E.g.: 3pt
{0pt}% measure of space to leave below the theorem. E.g.: 3pt
{\normalfont}% name of font to use in the body of the theorem
{0pt}% measure of space to indent
{\bfseries}% name of head font
{}% punctuation between head and body
{ }% space after theorem head; " " = normal interword space
{\thmname{#1}\thmnumber{ #2}\thmnote{ (#3)}}
\theoremstyle{theoremdd}

\newtheorem*{proof}{证明}
%\theoremseparator{：}
\newtheorem{assumption}{假设}[chapter]
\newtheorem{definition}{定义}[chapter]
\newtheorem{proposition}{命题}[chapter]
\newtheorem{lemma}{引理}[chapter]
\newtheorem{theorem}{定理}[chapter]
\newtheorem{axiom}{公理}[chapter]
\newtheorem{corollary}{推论}[chapter]
\newtheorem{exercise}{练习}[chapter]
\newtheorem{example}{例}[chapter]
\newtheorem{remark}{注释}[chapter]
\newtheorem{problem}{问题}[chapter]
\newtheorem{conjecture}{猜想}[chapter]

% 支持显示代码
\RequirePackage{listings}
% 排版算法
\usepackage{algorithm}
\usepackage{algorithmicx}
\floatname{algorithm}{算法}
\usepackage{algpseudocode}
\renewcommand{\algorithmicrequire}{\textbf{输入:}}
\renewcommand{\algorithmicensure}{\textbf{输出:}}

% 图、表 格式
%\captionsetup[table]{position=top,belowskip=6bp,aboveskip=0bp,singlelinecheck=true}
%\captionsetup[figure]{position=bottom,belowskip=0bp,aboveskip=6bp}
\RequirePackage[font=small,]{caption}
\captionsetup[table]{skip=0pt}
\captionsetup[figure]{skip=0pt}
\usepackage{etoolbox}
\AtBeginEnvironment{tabular}{\zihao{5}}
\AtEndEnvironment{tabular}{\vspace{-0.08cm}}%缩小表格后间隔
\AtBeginEnvironment{figure}{\zihao{5}}
\AtEndEnvironment{figure}{\vspace{-0.08cm}}
\usepackage{subfigure}
%\AtBeginEnvironment{subfigure}{\zihao{5}}
%\renewenvironment{table}%
%  {\zihao{5}
%   \@float{table}}
%  {\end@float}



\newcommand\initmaincontent{
    \fancyhf{}
    \pagestyle{fancy}
    \pagenumbering{arabic}
    \fancyhead[L]{\songti\zihao{5} 重庆邮电大学硕士学位论文 \vspace{0.21cm}}
    \fancyhead[R]{\songti\zihao{5} \leftmark \vspace{0.21cm}}
    \fancyfoot[CO,CE]{\vspace{0.004cm}\zihao{-5}\thepage}
}

%脚注https://www.cnblogs.com/ahhylau/p/4588939.html
\RequirePackage[bottom,perpage,hang]{footmisc}
% 生成带圈的脚注数字，最多处理到 10。
\newcommand\thu@circled[1]{%
    \ifnum#1 >10\relax
    \thu@error{%
        Too many footnotes in this page.
        Keep footnote less than 10%
    }%
    \fi
    {\ding{\the\numexpr\value{#1}+171\relax}}%
}
\renewcommand{\thefootnote}{\zihao{6}\ding{\numexpr171+\value{footnote}}}
\renewcommand{\thempfootnote}{\zihao{6}\ding{\numexpr171+\value{footnote}}}

%定义脚注分割线，字号（宋体小五），以及悬挂缩进（1.5 字符）。
%https://tex.stackexchange.com/questions/198150/move-footnoterule-to-right
%                           左缩进                             分割线宽度          分割线粗细     前后间隔
\def\footnoterule{\moveright0.8cm\vbox{\vskip0\p@\hrule\@width0.35\textwidth\@height0.6\p@\vskip3\p@}}
%https://tex.stackexchange.com/questions/96116/is-this-the-right-way-to-format-foot-notes/96401#96401
\setlength{\footnotesep}{16pt}
\usepackage{scrextend}
\deffootnote[2em]{0em}{2em}{\thefootnotemark}
\let\origfootnote\footnote
\renewcommand{\footnote}[1]{
    \begingroup
%    \vspace{0.9em}
    \origfootnote{
        \linespread{1.6}
        \selectfont\zihao{6}#1
        \vspace{3.5em}
    }%
    \endgroup
}

% 定义 \incite 命令，用于如“文献[1]”这样的引用
\newcommand*{\incite}{}
\DeclareRobustCommand*{\incite}[1]{
    \begingroup
% \romannumeral-`\x
    \setcitestyle{numbers}
    \hspace{-1em}~\cite{#1}\hspace{-0.3em}
    \endgroup
}


% GBT7714-2015引用格式
\RequirePackage[sort&compress]{gbt7714}
% 使用natbib宏包修改参考文献段间距
\RequirePackage{natbib}
\setlength{\bibsep}{0pt}
% 定义参考文献环境
\newenvironment{reference}{
    \bibliographystyle{gbt7714-numerical}
    \cleardoublepage
    \zihao{5}}{
}



\newcommand{\beginappendix}{
    \appendix
    \addtocontents{toc}{\protect\setcounter{tocdepth}{0}}
}


\newenvironment{acknowledgements}{%
    \cleardoublepage
    \chapter*{致谢}%
    \addcontentsline{toc}{chapter}{致谢}
    \markboth{致谢}{}
    }{%
}


\newenvironment{mastermainwork}{%
    \clearpage
    \@mainmatterfalse
%    \thu@chapter*{\thu@resume@name}%
    \ctexset{
        chapter = {
            numbering = false,
        },
        section = {
            format = \cusongti\zihao{-4}\bfseries,
            numbering = false,
            beforeskip={0pt},
            afterskip={0pt},
        },
    }%
    \chapter*{攻读硕士学位期间从事的科研工作及取得的成果}

    \addcontentsline{toc}{chapter}{攻读硕士学位期间从事的科研工作及取得的成果}
    \markboth{攻读硕士学位期间从事的科研工作及取得的成果}{}
    }{}
\newlist{achievements}{enumerate}{1}
\setlist[achievements]{
    label = [\arabic*],
    align = left,
    leftmargin = 10mm,
    topsep = -0bp,
    parsep = 0bp,
    partopsep = 0bp,
    itemsep = 0bp,
    labelsep = !,
    before = {},
    after = {\newline},
}

%\newenvironment{publications}{%
%    \begin{achievements}%
%    }{%
%    \end{achievements}%
%}

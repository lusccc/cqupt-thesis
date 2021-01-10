\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{cqupt_thesis}

% 加载key value options
\RequirePackage{xkeyval}

\def\approval{0}
\def\colortitle{0}
\def\secret{0}

\DeclareOption{doctor}{\def\thesistype{0}}
\DeclareOption{master}{\def\thesistype{1}}
\DeclareOption{approval}{\def\approval{1}}
\DeclareOption{color}{\def\colortitle{1}}
\DeclareOption{secret}{\def\secret{1}}
\DeclareOption{academic}{\def\degreetype{0}}
\DeclareOption{professional}{\def\degreetype{1}}



\DeclareOption*{\PassOptionsToClass{\CurrentOption}{ctexbook}}
\ProcessOptions\relax
\LoadClass[a4paper,UTF8,twoside, openright, zihao=-4,]{ctexbook}


% 解图表目录引用编号顺序问题
\RequirePackage{notoccite}
% 加入hyperref超链接参考
\RequirePackage{hyperref}
% fancyhdr 宏包提供了方便使用的命令用于设置页眉、页脚。
\RequirePackage{fancyhdr}
% 加入判断支持
\RequirePackage{ifthen}
% 此宏包提供图形支持。
\RequirePackage{graphicx}
% 颜色
\RequirePackage{xcolor}
\RequirePackage{multirow}
\RequirePackage{array}
%\RequirePackage{syntonly}
%\syntaxonly
%font
\RequirePackage{xeCJK}
\setmainfont{Times New Roman}
\setCJKmainfont[AutoFakeBold=1.8,ItalicFont=KaiTi]{SimSun}

%\newCJKfontfamily\bsong{SimSun}[AutoFakeBold]
%\newcommand{\bfs}[1]{\textbf{#1}}
\setmonofont[Mapping=tex-text]{Consolas}

%使用geometry调整边距
\RequirePackage{geometry}
\geometry{a4paper,papersize={21cm,29.7cm}}
\geometry{left=2.5cm,right=2.5cm,top=3cm,bottom=3cm,headsep=0.32cm,footskip=1cm}
% bottom为2.5 + 0.5cm，考虑到footer的高度，这样与word一致


\def\label@cntitle{题目}

% 这些命令用于设定各项文档信息的具体内容。
\newcommand\@classifiedindex{}
\newcommand\@udc{}
\newcommand\@paperno{}
\newcommand\@statesecrets{}
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

% 判断论文类别，定义不同论文名称
\ifthenelse{\equal{\thesistype}{1}}{
    \def\thesisname{硕士研究生学位论文}
    \def\CHSauthortype{研究生}
    \def\ENGauthortype{Postgraduate}
    \def\TypeAbbr{MSc Degree}
}{}

\newcommand\hwbox[3]{
    \begin{minipage}[c][#1]{#2}
        #3
    \end{minipage}
}

% 定义\fillinblank命令，用下划线填充指定的空间。
\newcommand{\fillinblank}[2]{
    \CJKunderline[thickness=0.8pt,depth=2em]{\makebox[#1]{#2}}
}

\newcommand\coveritembox[1]{
    \vspace{-4mm}
    \hspace{3mm}\CJKunderline[depth=0.8em]{\makebox[10.06cm][c]{\zihao{-3}\textbf{#1}}}
}
\newcolumntype{V}{>{\centering\arraybackslash}m{3em}}
\newcommand{\makecover}{

    \begin{titlepage}
        \zihao{-4}
        \vspace*{-2mm}
        \hspace{1.57cm}\parbox[b]{15.37cm}{
            \makebox[2.65cm][c]{\textbf{分类号}}
            %1.5mm, 1.1mm是单元格边距
            \hspace{1.5mm}\CJKunderline[thickness=1.3pt,]{\makebox[2.97cm][c]{\textbf{\@classifiedindex}}}\hspace{1.3mm}
            \makebox[3cm][c]{\textbf{密级}}
            \hspace{1.1mm}\CJKunderline[thickness=1.3pt,]{\makebox[4.39cm][c]{\textbf{\@statesecrets}}}
            \\[1mm]
            \makebox[2.65cm][c]{\textbf{UDC}}
            \hspace{1.5mm}\CJKunderline[thickness=1.3pt,]{\makebox[2.97cm][c]{\textbf{\@udc}}}\hspace{1.3mm}
            \makebox[3cm][c]{\textbf{学位论文编号}}
            \hspace{1.1mm}\CJKunderline[thickness=1.3pt,]{\makebox[4.39cm][c]{\textbf{\@paperno}}}
        }


        \zihao{2}
        \vspace{2.55cm}
        \hspace{2.35cm}\textbf{重庆邮电大学硕士学位论文}

        \zihao{-4}
        \vspace{2.7cm}
        \hspace{1.47cm}
        \renewcommand{\arraystretch}{1.38}
        \begin{tabular}{p{1.7cm}c}
            \makebox[1.7cm][l]{\textbf{中文题目}}
            &
            \hspace{3mm}\CJKunderline[depth=0.8em]{\makebox[10.06cm][c]{\zihao{-3}\textbf{\@cntitle}}}
            \\
            \ifthenelse{\equal{\@cnsubtitle}{}}{}{
                &
                \hspace{3mm}\CJKunderline[depth=0.8em]{\makebox[10.06cm][c]{\zihao{-3}\textbf{\@cnsubtitle}}}
%                \coveritembox{\@cnsubtitle}
                \\
            }
            \ifthenelse{\equal{\@cnsubsubtitle}{}}{}{
                &
                \hspace{3mm}\CJKunderline[depth=0.8em]{\makebox[10.06cm][c]{\zihao{-3}\textbf{\@cnsubsubtitle}}}
                \\
            }
            \makebox[1.7cm][l]{\textbf{英文题目}}
            &
            \hspace{3mm}\CJKunderline[depth=0.8em]{\makebox[10.06cm][c]{\zihao{-3}\textbf{\@entitle}}}
            \\
            \ifthenelse{\equal{\@ensubtitle}{}}{}{
                &
                \hspace{3mm}\CJKunderline[depth=0.8em]{\makebox[10.06cm][c]{\zihao{-3}\textbf{\@ensubtitle}}}
                \\
            }
            \ifthenelse{\equal{\@ensubsubtitle}{}}{}{
                &
                \hspace{3mm}\CJKunderline[depth=0.8em]{\makebox[10.06cm][c]{\zihao{-3}\textbf{\@ensubsubtitle}}}
                \\
            }
            \makebox[1.7cm][s]{\textbf{学号}}
            &
            \hspace{3mm}\CJKunderline[depth=0.8em]{\makebox[10.06cm][c]{\zihao{-3}\textbf{\@stuno}}}
            \\
            \makebox[1.7cm][s]{\textbf{姓名}}
            &
            \hspace{3mm}\CJKunderline[depth=0.8em]{\makebox[10.06cm][c]{\zihao{-3}\textbf{\@name}}}
            \\
            \makebox[1.7cm][s]{\textbf{学位类别}}
            &
            \hspace{3mm}\CJKunderline[depth=0.8em]{\makebox[10.06cm][c]{\zihao{-3}\textbf{\@degreeclass}}}
            \\
            \makebox[1.7cm][s]{\textbf{学科专业}}
            &
            \hspace{3mm}\CJKunderline[depth=0.8em]{\makebox[10.06cm][c]{\zihao{-3}\textbf{\@major}}}
            \\
            \makebox[1.7cm][s]{\textbf{指导教师}}
            &
            \hspace{3mm}\CJKunderline[depth=0.8em]{\makebox[10.06cm][c]{\zihao{-3}\textbf{\@supervisor}}}
            \\
            \makebox[1.7cm][s]{\textbf{完成日期}}
            &
            \hspace{3mm}\CJKunderline[depth=0.8em]{\makebox[10.06cm][c]{\zihao{-3}\textbf{\@completedate}}}
        \end{tabular}
    \end{titlepage}
}
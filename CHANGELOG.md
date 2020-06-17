---

CHANGELOG.md
Copyright 2020 R. Langner

This work may be distributed and/or modified under the
conditions of the LaTeX Project Public License, either version 1.3
of this license or (at your option) any later version.
The latest version of this license is in
  http://www.latex-project.org/lppl.txt
and version 1.3 or later is part of all distributions of LaTeX
version 2005/12/01 or later.

This work has the LPPL maintenance status `maintained'.

The Current Maintainer of this work is R. Langner.

This work consists of all files listed in MANIFEST.md.

---

# Clean Thesis changelog

The latest version of this file can be found at the master branch of the
*Clean Thesis* [repository](https://github.com/derric/cleanthesis).

## Latest Dev
- ...

## v0.4.1
- Updated copyright year

## v0.4.0
- Fixed compatibility to new version of KOMA script
- Fixed code for headline/title styles (e.g., removed use of package titlesec)
- Fixed code for footer style (e.g., removed use of package fancyhdr)
- Fixed compatibility to new version of biblatex (e.g., obsolete options)
- Fixed an issue with page breaks at headings (thanks @guillerodriguez)
- Added style for part sections (often used for books)
- Added new package options: quotation style, bibliography sorting, 
- Changed alignment of titles from justified to left aligned
- Changed the documentation according the updates
- Changed file structure of the repository in order to improve the development and release process
- Example: several improvements, such as location of appendix, use of subsubsections and paragraphs, long section titles, listings, pdf bookmark for toc, or separate config file

## v0.3.1
- re-licensed cleanthesis using the LPPL 1.3, http://www.latex-project.org/lppl.txt
- moved documentation into a separate subfolder (doc/)
- Example: change specific version number to a more general value (My First Draft).

## v0.3
- Created this changelog text file
- Switched to markdown files (README, CHANGELOG)
- Added a sub-section in the example thesis
- Fixed README. Corrected copyright statement (year), wording and link to classicthesis (moschlar)
- Fixed broken package option/parameter colorize (hrzbrg)
- Fixed changing font size of the document to small caused by a bug in the titlepage (matthieu-lapeyre)
- Fixed documentation. Added missing descriptions for package options: hangfigurecaption, hangsection, hangsubsection, colorize, and colortheme
- Fixed line height for the title on the very first title page (Riin)
- Fixed colored title on title page, even if color mode is bw
- New package option bibfile: allows you to link/use arbitrary bibtex files
- New package option bibstyle: allows you to set a citation and bibliography style

## v0.2.3
- Fixed line breaks for long chapter headlines (caused text overlapping)
- Fixed wrong file names to the main latex file for the example document

## v0.2.2
- Fix: added address for postcards
- Doc: improved acknowledgments, added André Miede

## v0.2.1
- Fix: make horizontal line longer (just a bit)
- Fix: update my address (new)
- Change: add my name to the colophon
- Change: copyright years
- Feature: new package option for citation management tool (bib engine), biber or bibtex
- Doc: add first people to acknowledgments

## v0.2
- Fix: label widths in the lof and lot (list of figures, list of tables)
- Feature: more flexible/new package options
- Feature: improved color management, introduction of color themes (currently two)
- Doc: Initial documentation (package options)

## v0.1
- Initial public beta version

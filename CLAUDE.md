# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is the content repository for **BYU CCE 270 - Computational Methods**, a course that teaches Excel, Python fundamentals, and advanced Python libraries for data analysis. The course is structured into three main units:

- **Unit 1**: Excel-based computational methods (data analysis, lookups, pivot tables, charts, Gantt charts)
- **Unit 2**: Introduction to Python (variables, lists, loops, conditionals, dictionaries, functions)
- **Unit 3**: Advanced Python (file I/O, APIs/gspread, matplotlib, numpy, pandas, ipywidgets)

## Documentation System

The course content is built using **MkDocs** and hosted on Read the Docs at https://byu-cce270.readthedocs.io/

### Building and Serving Documentation

To build and serve the documentation locally:

```bash
# Install dependencies
pip install -r docs/requirements.txt

# Serve documentation locally (auto-reloads on changes)
mkdocs serve

# Build static site
mkdocs build
```

The MkDocs configuration is in `mkdocs.yml` at the repository root.

## Repository Structure

```
docs/
├── unit1/          # Excel-based exercises (*.xlsx files, *.md instructions)
├── unit2/          # Python fundamentals (*.ipynb notebooks, *.md instructions)
├── unit3/          # Advanced Python (*.ipynb notebooks, *.md instructions, *.csv data)
├── old_unit2_copy/ # Archived content from previous semester
├── old_unit3_copy/ # Archived content from previous semester
├── bonus/          # Additional content (Python/Excel integration, local Python setup)
├── resources/      # Course resources (textbooks, TA info, grading policy)
├── css/            # Custom styling for documentation
├── js/             # JavaScript for MathJax configuration
├── images/         # Image assets
└── requirements.txt # Python dependencies for building docs
```

## Content Organization Pattern

Each topic follows a consistent three-part structure:
- **Reading** (`*_read.md`): Pre-class reading assignments with references to textbooks
- **In Class** (`*_class.md`): In-class exercises and activities
- **Homework** (`*_hw.md`): Homework assignments

Supporting materials include:
- Jupyter notebooks (`.ipynb`) for Python units (Unit 2 and 3)
- Excel workbooks (`.xlsx`) for Unit 1
- Data files (`.csv`) for exercises in Unit 3

## Key Technologies

- **MkDocs**: Static site generator using `readthedocs` theme
- **Python Markdown extensions**: Math rendering (MathJax), task lists, admonitions, emoji support
- **Google Colab**: Primary environment for Python instruction (Unit 2 and 3)
- **Jupyter Notebooks**: Exercise and homework starter files
- **Read the Docs**: Hosting platform (builds specified in `readthedocs.yml`)

## Important Notes for Content Editing

1. **Navigation structure**: All course content must be registered in the `nav` section of `mkdocs.yml` to appear in the documentation
2. **File naming convention**: Starter workbooks follow the pattern `(Starter-Workbook)-[Type]-[Topic].xlsx` or `.ipynb`
3. **Markdown files**: May contain embedded MathJax (LaTeX) expressions for mathematical notation
4. **Links**: Many internal links use relative paths like `../../resources/textbooks/textbooks.md`
5. **Old content**: The `old_unit2_copy/` and `old_unit3_copy/` directories contain archived material from previous semesters—avoid modifying these unless explicitly requested
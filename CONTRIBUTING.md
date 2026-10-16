# Contributing

Thank you for helping improve this GATE CS previous-year paper archive.

## What to contribute

Useful contributions include reporting broken or unreadable PDFs, correcting file names, fixing documentation, and improving the study workflow. Please do not add unofficial solutions or answer keys without clearly identifying their source and status.

## Before adding or replacing a paper

1. Confirm the year and paper/session label from a reliable source.
2. Open the PDF and check that its pages are readable and the document is complete.
3. Use the existing naming convention: `YYYY_CS.pdf` or `YYYY_CS1.pdf` / `YYYY_CS2.pdf`.
4. Check that you have permission to redistribute the document and include an official source link where possible.
5. Run the local validation script:

   ```bash
   python scripts/check_papers.py
   ```

6. Update the paper index in `README.md` if the archive changes.

The current index expects 24 files for 2007–2026. If adding a new year or correcting the archive's expected inventory, update the script's expected file list, README index, and this note together.

## Reporting a problem

Open a [GitHub Issue](https://github.com/Vikram2005-byte/gate-cs-previous-year-papers/issues) and include the file name, what is wrong, and—if available—a link to the official source. Do not attach copyrighted material unless redistribution is permitted.

## Pull request checklist

- [ ] I checked the paper's year/session and readability.
- [ ] I used the established filename format.
- [ ] I checked redistribution permissions or only changed documentation/code.
- [ ] I updated the README/index if needed.
- [ ] The paper validation script passes, where applicable.

## Scope and licensing

This is an independent study archive and is not affiliated with GATE or any IIT. Contributors are responsible for ensuring that material they submit may legally be shared. No license is implied for third-party papers by this repository's documentation.

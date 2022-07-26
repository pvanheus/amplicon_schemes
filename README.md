# Amplicon Schemes for PrimalSeq sequencing

This repository describes primer schemes for PrimalScheme amplicon sequencing.

The `schemes.yml` describes known amplicon schemes (in YAML format). It follows a schema described by `schemes-schema.json`. The `incomplete-schemes.yml` file describes schemes
that are known but where information is still
incomplete.

[ajv](https://github.com/ajv-validator/ajv-cli) can be used to validate the `schemes.yml`:

```bash
ajv --spec=draft2020 --errors=text -s schemes-schema.json -d schemes.yml
```

Shield: [![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

This work is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg

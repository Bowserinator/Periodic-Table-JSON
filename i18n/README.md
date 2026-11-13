# Translations (i18n)

Translations of element names, categories, and phases into multiple languages.

## File format

Each language has its own JSON file following the naming convention `{language}-{REGION}.json` (e.g., `es-ES.json`) or `{language}.json` for languages without regional variants (e.g., `ca.json`).

Language codes follow [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) and region codes follow [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).

### Structure

```json
{
  "meta": {
    "language": "es-ES",
    "language_name": "Spanish (Spain)",
    "native_name": "Castellano",
    "translator": "GitHub username or name",
    "last_updated": "2026-03-31",
    "source": "References used for the translation",
    "completeness": {
      "names": true,
      "categories": true,
      "phases": true,
      "summaries": false
    }
  },
  "names": {
    "1": "Hidrógeno",
    "2": "Helio",
    "3": "Litio"
  },
  "categories": {
    "diatomic nonmetal": "no metal diatómico",
    "noble gas": "gas noble"
  },
  "phases": {
    "Gas": "Gas",
    "Liquid": "Líquido",
    "Solid": "Sólido"
  }
}
```

### Fields

| Field | Required | Description |
|-------|----------|-------------|
| `meta` | Yes | Metadata about the translation |
| `meta.language` | Yes | Language code (ISO 639-1 + optional ISO 3166-1 region) |
| `meta.language_name` | Yes | Language name in English |
| `meta.native_name` | Yes | Language name in its own language |
| `meta.translator` | Yes | Who made the translation |
| `meta.last_updated` | Yes | Date of last update (YYYY-MM-DD) |
| `meta.source` | Yes | References used (e.g., "IUPAC + RAE") |
| `meta.completeness` | Yes | Which sections are complete |
| `names` | Yes | Element names indexed by atomic number (1-119) |
| `categories` | Yes | Translation of the 15 element categories |
| `phases` | Yes | Translation of the 3 phases (Gas, Liquid, Solid) |
| `summaries` | No | Element summaries indexed by atomic number (future) |

### Key conventions

- **Names** are indexed by atomic number as strings (`"1"`, `"2"`, ..., `"119"`)
- **Categories** use the original English category as the key
- **Phases** use the original English phase as the key

## Available translations

| Language | Code | File | Translator |
|----------|------|------|------------|
| Spanish (Spain) | `es-ES` | [es-ES.json](es-ES.json) | Cubel89 |

## Contributing a new language

1. Copy an existing translation file (e.g., `es-ES.json`) and rename it with the appropriate language code
2. Update the `meta` section with your language details
3. Translate all 119 element names, 15 categories, and 3 phases
4. Use official nomenclature from your country's chemical society or IUPAC when available
5. Open a pull request with your translation

### Quality guidelines

- Use official chemical nomenclature from recognized institutions (IUPAC, national chemistry societies)
- Ensure proper diacritics and special characters for your language
- Do not use machine translation without manual review by a native speaker
- Verify elements 113-119 (named in 2016) have their official translated names

### Recommended sources

- [IUPAC Nomenclature](https://iupac.org/what-we-do/nomenclature/)
- [Wikipedia](https://wikipedia.org) in the target language
- [Ptable.com](https://ptable.com) (supports 40+ languages)
- [Elementymology](https://elements.vanderkrogt.net/multidict.php) (80+ languages)
- National chemistry societies and language academies

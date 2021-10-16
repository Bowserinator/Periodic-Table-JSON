# Periodic-Table-JSON
A json of the entire periodic table. Feel free to use it in your projects.

Temperatures such as boiling points and melting points are given in degrees kelvin.  Densities are given in g/l for gases and g/cm³ for solids and liquids and molar heat in (mol*K).
Information that is missing is represented as null. Some elements may have an image link to their spectral bands.

All elements have a three sentence summary from Wikipedia.

**Electron configuration** is given as a string, with each orbital separated by a space.  **Electron configuration semantic** is given as a string, this is the short-hand version of the electron configuration. Elements with a semantic electron configuration marked with a "*" mean that the electron configuration has not yet been confirmed. **Electron shells** are given as an array, the first item is the number of electrons in the first shell, the 2nd item is the number of electrons in the second shell, and so on.

Both **ionization energy** and **first electron affinities** are given as the energy required to *detach* an electron from the anion.  Ionization energies are given as an array for successive ionization energy.

A link to the source where the information was from is provided in each element under the key "source".

Here's an example of how it's formatted:
```json
{
	"elements" : [{
		"name": "Hydrogen",
		"symbol": "H",
		"number": 1,
		"period": 1,
		"category": "diatomic nonmetal ",
		"atomic_mass": 1.008,
		"appearance": "colorless gas",
		"phase": "Gas",
		"melt": 13.99,
		"boil": 20.271,
		"density": 0.08988,
		"discovered_by": "Henry Cavendish",
		"molar_heat": 28.836,
		"source":"https://en.wikipedia.org/wiki/Hydrogen",
		"named_by": "Antoine Lavoisier",
		"spectral_img": "https://en.wikipedia.org/wiki/File:Hydrogen_Spectra.jpg",
		"summary": "Hydrogen is a chemical element with chemical symbol H and atomic number 1. With an atomic weight of 1.00794 u, hydrogen is the lightest element on the periodic table. Its monatomic form (H) is the most abundant chemical substance in the Universe, constituting roughly 75% of all baryonic mass.",
		"ypos": 1,
		"xpos": 1,
		"shells": [
			1
		],
		"electron_configuration": "1s1",
		"electron_configuration_semantic": "1s1",
		"electron_affinity": 72.769,
		"electronegativity_pauling": 2.20,
		"ionization_energies": [
			1312.0
		],
		"cpk-hex": "ffffff"
	}]
}
```

## Additional Formats

Besides the original JSON file `PeriodicTableJSON.json`, the data is provided in the following additional formats:

- As a lookup table for easy indexing in `periodic-table-lookup.json`.

- As a CSV file (one row per element and one column per property, where some subfields are flattened to strings) in `periodicTableCSV.csv`.

These files are generated from the original data via scripts in the directory `scripts`.

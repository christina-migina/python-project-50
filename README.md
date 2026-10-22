[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=christina-migina_python-project-50&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=christina-migina_python-project-50)[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=christina-migina_python-project-50&metric=bugs)](https://sonarcloud.io/summary/new_code?id=christina-migina_python-project-50)[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=christina-migina_python-project-50&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=christina-migina_python-project-50)[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=christina-migina_python-project-50&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=christina-migina_python-project-50)[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=christina-migina_python-project-50&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=christina-migina_python-project-50)[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=christina-migina_python-project-50&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=christina-migina_python-project-50)[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=christina-migina_python-project-50&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=christina-migina_python-project-50)[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=christina-migina_python-project-50&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=christina-migina_python-project-50)[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=christina-migina_python-project-50&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=christina-migina_python-project-50)
[![Python CI](https://github.com/christina-migina/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/christina-migina/python-project-50/actions/workflows/pyci.yml)

# Gendiff

Difference Evaluator is a program that determines the differences between two data structures. This is a popular problem with many online services available for its solution, such as http://www.jsondiff.com/. A similar mechanism is used when displaying test results or automatically tracking changes in configuration files.

## Dependencies

* Windows 10 / macOS / Linux
* Python 3.10+
* uv package manager

## Installation

### 1. Clone the repository
```bash
git clone git@github.com:christina-migina/python-project-50.git
cd python-project-50
```

### 2. Install dependencies
```bash
make install
```

### 3. Build and install the package globally
```bash
make build
make package-install
```

## Usage

### 4. Comparison of plain files
1. **Stylish Formatter (Default)**
```bash
uv run gendiff file1.json file2.json
uv run gendiff file1.yaml file2.yaml
```
[![asciicast](https://asciinema.org/a/1269465.svg)](https://asciinema.org/a/1269465)[![asciicast](https://asciinema.org/a/1269467.svg)](https://asciinema.org/a/1269467)
2. **Plain Formatter**
```bash
uv run gendiff --format plain file1.json file2.json
uv run gendiff --format plain file1.yaml file2.yaml
```
[![asciicast](https://asciinema.org/a/1269468.svg)](https://asciinema.org/a/1269468)
3. **JSON Formatter**
```bash
uv run gendiff --format json file1.json file2.json
uv run gendiff --format json file1.yaml file2.yaml
```

[![asciicast](https://asciinema.org/a/1269469.svg)](https://asciinema.org/a/1269469)
[![asciicast](https://asciinema.org/a/1269470.svg)](https://asciinema.org/a/1269470)

### 5. Comparison of nested files
1. **Stylish Formatter (Default)**
```bash
uv run gendiff file1_tree.json file2_tree.json
uv run gendiff file1_tree.yaml file2_tree.yaml
```

[![asciicast](https://asciinema.org/a/1269471.svg)](https://asciinema.org/a/1269471)
[![asciicast](https://asciinema.org/a/1269472.svg)](https://asciinema.org/a/1269472)

2. **Plain Formatter**
```bash
uv run gendiff --format plain file1_tree.json file2_tree.json
uv run gendiff --format plain file1_tree.yaml file2_tree.yaml
```

[![asciicast](https://asciinema.org/a/1269473.svg)](https://asciinema.org/a/1269473)

3. **JSON Formatter**
```bash
uv run gendiff --format json file1_tree.json file2_tree.json
uv run gendiff --format json file1_tree.yaml file2_tree.yaml
```

[![asciicast](https://asciinema.org/a/1269477.svg)](https://asciinema.org/a/1269477)
[![asciicast](https://asciinema.org/a/1269478.svg)](https://asciinema.org/a/1269478)

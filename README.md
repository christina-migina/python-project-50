[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=christina-migina_python-project-50&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=christina-migina_python-project-50)[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=christina-migina_python-project-50&metric=bugs)](https://sonarcloud.io/summary/new_code?id=christina-migina_python-project-50)[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=christina-migina_python-project-50&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=christina-migina_python-project-50)[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=christina-migina_python-project-50&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=christina-migina_python-project-50)[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=christina-migina_python-project-50&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=christina-migina_python-project-50)[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=christina-migina_python-project-50&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=christina-migina_python-project-50)[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=christina-migina_python-project-50&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=christina-migina_python-project-50)[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=christina-migina_python-project-50&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=christina-migina_python-project-50)[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=christina-migina_python-project-50&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=christina-migina_python-project-50)

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
[![asciicast](https://asciinema.org/a/0g8VyUo55aENklOA.svg)](https://asciinema.org/a/0g8VyUo55aENklOA)

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

### 4. Run Gendiff via CLI
```bash
uv run gendiff path/to/file1.json path/to/file2.json
```
[![asciicast](https://asciinema.org/a/r74IpMBhcGzybJgf.svg)](https://asciinema.org/a/r74IpMBhcGzybJgf)
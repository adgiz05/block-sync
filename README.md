# Block Sync

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
<!-- [![PyPI version](https://badge.fury.io/py/block_sync.svg)](https://badge.fury.io/py/block_sync) -->

Block Sync is a tool that allows you to synchronize code blocks defined in your Jupyter notebooks with your Python source files. Thanks to special tags in the notebooks, you can automatically update specific sections of your code, making maintenance and code reuse much easier.

## Functionality

The package consists of the following modules:

- **`config.py`**: Loads the project configuration from a YAML file.
- **`notebook.py`**: Parses a Jupyter notebook to extract code blocks delimited by tags such as `# <block_name>` and `# </block_name>`.
- **`updater.py`**: Updates source files by replacing the existing code blocks with the new extracted code.
- **`main.py`**: The main script that integrates all functionalities and runs the synchronization process.

## Project Structure

```
block_sync/
├── block_sync/           # Main package
│   ├── __init__.py       # Public API of the package
│   ├── config.py         # Configuration loading functions
│   ├── notebook.py       # Notebook parsing functions
│   └── updater.py        # File updating functions
├── main.py                # Entry script for executing the synchronization
├── config.yaml           # Project configuration file
├── pyproject.toml        # Packaging configuration (PEP 517)
├── README.md             # This file
└── LICENSE               # Project license (MIT, in this case)
```

## Installation

You can install Block Sync directly from the repository:

```bash
git clone https://github.com/adgiz05/block_sync.git
```

## Configuration

The `config.yaml` file is essential for Block Sync to function properly. In it you define:

- **NB**: The path to the Jupyter notebook that contains the code blocks.
- **SRC**: The base path for the source files to be updated.
- **SYNCS**: A mapping between the block names and their location in the source code (e.g., `module.submodule.blockname`).

Example `config.yaml`:

```yaml
NB: "/path/to/notebook.ipynb"
SRC: "/path/to/source_files"
SYNCS:
  block1: "module1.block1"
  block2: "module2.submodule.block2"
```

## Usage

### Running Manually

To run the synchronization process, simply execute the main script:

```bash
python main.py
```

The script will perform the following tasks:

1. **Load the configuration** from `config.yaml`.
2. **Parse the notebook** specified to extract the code blocks.
3. **Update the source files** according to the mapping defined in `SYNCS`.

### Integration in VSCode

If you work in VSCode, you can set up the **Run on Save** extension to automatically execute the script when you save a notebook. For example, in your `settings.json`:

```json
{
  "emeraldwalk.runonsave": {
    "commands": [
      {
        "match": ".*\\.ipynb$",
        "cmd": "python /path/to/your/project/main.py",
        "cwd": "/path/to/your/project"
      }
    ]
  },
  "emeraldwalk.runonsave.debug": true
}
```

With this configuration, every time you save a notebook, the synchronization process will be triggered.

## Example Usage

Below is a real code example demonstrating how to use Block Sync programmatically:

```python
# Code in the notebook
# <add>
def add(a, b)
    return a + b
# </add>
```
Now just set the same clause in the desired script and Block Sync will link the code.
```python
# Imagine this is src/ops.py
# <add>

# </add>
```
In the config.yaml set:
```yaml
SYNCS:
    - "add" : "ops.add"
```

## License

This project is distributed under the [MIT License](LICENSE).

## Contact

If you have any questions, suggestions, or issues, feel free to open an issue in the repository or contact me at [adrian.giron@upm.es](mailto:adrian.giron@upm.es).

---

Enjoy Block Sync and feel free to contribute to make it even better!

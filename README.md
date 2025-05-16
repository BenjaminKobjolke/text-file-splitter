# Text File Splitter

A Python project to split text files based on a configurable separator.

## Setup

1. Clone the repository.
2. Run `install.bat` to create a virtual environment and install dependencies.

## Usage

Run the `run.bat` script with the following arguments:

```bash
run.bat --input "path/to/your/input.txt" --output "path/to/your/output_folder"
```

-   `--input`: Path to the text file you want to split.
-   `--output`: Path to the folder where the split files will be saved. The folder will be created if it doesn't exist.

## Configuration

The separator string can be configured in the `settings.ini` file:

```ini
[Settings]
separator = ---
```

Change the value of `separator` to your desired string. The default is `---`.

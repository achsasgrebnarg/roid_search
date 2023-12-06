This command-line package uses `textract` to extract data from documents within a specified folder for a given regex pattern and saves the extracted data into a tab-separated values (TSV) file.

### Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/achsasgrebnarg/roid_search.git
    ```

2. Navigate to the project directory:

    ```bash
    cd roid_search
    ```

3. Install the package:

    ```bash
    pip install .
    ```

## Usage

Run the `roid_search` command directly in the terminal with the following arguments:

```bash
roid_search --document_folder <path_to_folder> --pattern <regex_pattern> --output_file <output_file_name>
```

### Command-line arguments:

- `--document_folder`: Path to the folder containing the documents from which data needs to be extracted.
- `--pattern`: The regex pattern used to extract the desired data from the documents.
- `--output_file`: The name of the output file to store the extracted data in (excluding file extension).

### Example:

```bash
roid_search --document_folder ./documents --pattern "your_regex_pattern_here" --output_file extracted_data
```

This will process the documents in the `./documents` folder using the specified regex pattern and save the extracted data to a file named `extracted_data.tsv`.

## Dependencies

- `textract`: For extracting text content from various document formats.

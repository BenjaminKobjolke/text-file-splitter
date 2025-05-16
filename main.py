import argparse
import logging
import os
from classes.config_manager import ConfigManager
from classes.file_handler import FileHandler
from classes.file_splitter import FileSplitter

def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    parser = argparse.ArgumentParser(description="Split a text file based on a separator.")
    parser.add_argument("--input", required=True, help="Path to the input text file.")
    parser.add_argument("--output", required=True, help="Path to the output folder.")

    args = parser.parse_args()

    config_manager = ConfigManager()
    separator = config_manager.get_separator()
    logging.info(f"Using separator: '{separator}'")

    file_handler = FileHandler()
    content = file_handler.read_file(args.input)

    if content is None:
        return

    file_splitter = FileSplitter(separator)
    sections = file_splitter.split_content(content)

    if not sections:
        logging.warning("No sections found in the input file.")
        return

    total_sections = len(sections)
    logging.info(f"Found {total_sections} sections.")

    for i, section in enumerate(sections):
        output_filename = file_splitter.generate_output_filename(args.output, i, total_sections)
        file_handler.write_file(output_filename, section)
        logging.info(f"Wrote section {i + 1} to {output_filename}")

    logging.info("Splitting complete.")

if __name__ == "__main__":
    main()

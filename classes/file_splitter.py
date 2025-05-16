import os

class FileSplitter:
    def __init__(self, separator):
        self.separator = separator

    def split_content(self, content):
        sections = content.split(self.separator)
        return [self._clean_section(section) for section in sections]

    def _clean_section(self, section):
        lines = section.splitlines()
        # Remove empty lines from the start
        while lines and not lines[0].strip():
            lines.pop(0)
        # Remove empty lines from the end
        while lines and not lines[-1].strip():
            lines.pop()
        return "\n".join(lines)

    def generate_output_filename(self, output_dir, index, total_sections):
        num_digits = len(str(total_sections))
        filename = f"{index + 1:0{num_digits}}.txt"
        return os.path.join(output_dir, filename)

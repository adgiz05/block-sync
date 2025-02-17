import nbformat
import re

def parse_notebook_blocks(nb_path):
    """
    Extract code blocks from a Jupyter Notebook based on custom delimiters.

    The notebook is scanned for code cells with blocks defined like:
        # <block_name>
        ... code ...
        # </block_name>

    Blocks spanning multiple cells are concatenated.

    Parameters:
        nb_path (str or Path): Path to the Jupyter Notebook file.

    Returns:
        dict: A dictionary mapping block names to their corresponding code.
    """
    nb = nbformat.read(nb_path, as_version=4)
    blocks = {}

    for cell in nb.cells:
        if cell.cell_type != 'code':
            continue

        lines = cell.source.splitlines(keepends=True)
        current_block_name = None
        current_block_lines = []

        for line in lines:
            start_match = re.match(r'\s*#\s*<([^/].*?)>\s*', line)
            end_match = re.match(r'\s*#\s*</(.*?)>\s*', line)

            if start_match:
                if current_block_name:
                    blocks.setdefault(current_block_name, []).append(''.join(current_block_lines))
                current_block_name = start_match.group(1).strip()
                current_block_lines = []
            elif end_match:
                end_name = end_match.group(1).strip()
                if current_block_name == end_name:
                    blocks.setdefault(current_block_name, []).append(''.join(current_block_lines))
                    current_block_name = None
                    current_block_lines = []
                else:
                    # Mismatched block names; ignoring this end tag.
                    pass
            else:
                if current_block_name:
                    current_block_lines.append(line)

        if current_block_name:
            blocks.setdefault(current_block_name, []).append(''.join(current_block_lines))
            current_block_name = None
            current_block_lines = []

    for key, fragments in blocks.items():
        blocks[key] = '\n'.join(fragments)

    return blocks
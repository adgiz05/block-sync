import os
import re

def _update_file_block(file_path, block_name, new_code):
    """
    Update a specific code block in a file with new code.

    This function searches for a code block in the file, where the block is delimited by:
        # <block_name>
        ... (existing code) ...
        # </block_name>
    If the block is found, it replaces the entire block (including delimiters) with the new code.
    Otherwise, it prints a message indicating that the block is not defined.

    Parameters:
        file_path (str): Path to the file that should be updated.
        block_name (str): The name of the block to update.
        new_code (str): The new code to be inserted into the block.
    """
    # Compile a regex pattern to find the block with the given block_name.
    # The pattern uses DOTALL so that the '.' character matches newline characters.
    pattern = re.compile(
        rf'(#\s*<{block_name}>.*?#\s*</{block_name}>)',
        re.DOTALL
    )

    # Open the file and read its current content.
    with open(file_path, 'r', encoding='utf-8') as f:
        original_content = f.read()

    # Create the new block with delimiters and the new code.
    replacement = f"# <{block_name}>\n{new_code}# </{block_name}>"

    # Check if the block exists in the file.
    if re.search(pattern, original_content):
        # If found, replace the existing block with the new block.
        updated_content = re.sub(pattern, replacement, original_content)
    else:
        # If the block is not found, print a warning and exit the function.
        print(f"The block ({block_name}) is not defined in the source file.")
        return

    # Write the updated content back to the file.
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)

    # Print a confirmation message.
    print(f"Block '{block_name}' updated in {file_path}")

def update_file_blocks(src_path, blocks, syncs):
    """
    Update multiple code blocks in their corresponding files.

    This function iterates over the blocks provided in the 'blocks' dictionary.
    For each block, it determines the corresponding source file and block mapping using the
    'syncs' dictionary, then calls _update_file_block to update the block in the file.

    Parameters:
        src_path (str): Base directory path where source files are located.
        blocks (dict): Dictionary mapping block names to their new code.
        syncs (dict): Dictionary mapping block names to their file mapping, which should be in
                      a format like 'module.submodule.blockname'. The last part represents the block
                      name in the file, while the preceding parts form the file path.
    """
    # Iterate over each block defined in the blocks dictionary.
    for block, source in blocks.items():
        try:
            # Retrieve the corresponding file mapping for the current block.
            block_mapping = syncs[block]
        except KeyError:
            # If no mapping exists for the block, print a warning and skip it.
            print(f"Block '{block}' does not correspond to any mapping.")
            continue

        # Extract the block identifier from the mapping.
        # The block name is expected to be the last segment in a dot-separated string.
        obj_block = block_mapping.split('.')[-1]

        # Construct the relative file path by joining all segments except the last one,
        # then appending a '.py' extension.
        relative_file_path = '/'.join(block_mapping.split('.')[:-1]) + '.py'

        # Combine the base source path with the relative file path to get the full file path.
        full_file_path = os.path.join(src_path, relative_file_path)

        # Update the block in the file using the helper function.
        _update_file_block(full_file_path, obj_block, source)

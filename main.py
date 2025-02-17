import os
from pathlib import Path
from block_sync.config import load_config
from block_sync.notebook import parse_notebook_blocks
from block_sync.updater import update_file_blocks

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(CURRENT_DIR, 'config.yaml')

def main():
    """
    Main routine to load configuration, parse the notebook for code blocks,
    and update the corresponding source files.
    """
    config = load_config(CONFIG_PATH)
    nb_path = Path(config['NB'])
    src_path = Path(config['SRC'])
    syncs = config.get('SYNCS', {})

    blocks = parse_notebook_blocks(nb_path)
    update_file_blocks(src_path, blocks, syncs)

if __name__ == '__main__':
    main()

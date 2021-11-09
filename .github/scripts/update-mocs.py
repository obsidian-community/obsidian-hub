import os
import sys
import argparse

from make_mocs import DirectoryMoc, filter_directories


class VaultMoc:
    """
    Top-level class, to manage MOCs for all the directories in an entire vault.

    For now, the path to the vault is hard-coded, as there is some code
    in make_mocs.py that knows that the root of the vault is in a parent of the
    directory containing this script.
    """

    def update_all_mocs(self, args):
        directory = '../..'
        for root, dirs, files in os.walk(directory):
            filter_directories(dirs)
            dirs.sort()
            directory_moc = DirectoryMoc(root, dirs, files)
            directory_moc.generate_moc()


def main(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser(
        description="Create and update MOCs, mimicking Zoottelkeeper output"
    )
    # parser.add_argument("-v", "--verbose", action="store_true", default=False)

    args = parser.parse_args(argv)

    vault_moc = VaultMoc()
    vault_moc.update_all_mocs(args)


if __name__ == "__main__":
    main()

from collections import defaultdict
from glob import glob

def main() -> None:
    found_conflict = False
    all_markdown_paths = glob("../../*.md") + glob("../../**/*.md")

    paths_by_lower_path = defaultdict(list)
    for path in all_markdown_paths:
        paths_by_lower_path[path.lower()].append(path)

    for lower_path, original_paths in paths_by_lower_path.items():
        #print(f"count={len(original_paths)} - {lower_path}")
        if len(original_paths) == 1:
            # No conflict.
            continue

        found_conflict = True
        print("Conflict!")
        for path in original_paths:
            print(f"\t{path}")

    if found_conflict:
        exit(1)

if __name__ == '__main__':
    main()


import os
import sys

def main(root_path):
    combined_content = []
    traverse_directory(root_path, combined_content)
    script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    output_file = os.path.join(script_dir, "combined_output.md")
    write_combined_markdown(combined_content, output_file)

def traverse_directory(path, combined_content, level=1):
    for item in sorted(os.listdir(path)):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            combined_content.append(f"{'#' * level} {item}\n\n")
            traverse_directory(item_path, combined_content, level + 1)
        elif item.endswith('.md'):
            process_markdown_file(item_path, combined_content, level)

def process_markdown_file(file_path, combined_content, level):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    combined_content.append(f"{'#' * level} {file_name}\n\n")
    
    lines = content.split('\n')
    for line in lines:
        if line.startswith('#'):
            hashes, title = line.split(' ', 1)
            new_level = len(hashes) + level
            combined_content.append(f"{'#' * new_level} {title}\n")
        else:
            combined_content.append(line + '\n')
    
    combined_content.append('\n')

def write_combined_markdown(content, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        file.writelines(content)

if __name__ == "__main__":
    root_path = "/Users/woji/Dev/python/md_from_directory/documentation"
    main(root_path)
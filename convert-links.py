# Markdown and HTML links converter. Licenced under MIT, by Gordon Stevens (https://github.com/gordonstevens/convert-markdown-links)
import re, sys, os, argparse

def convert_markdown_to_href(markdown_text, add_blank_target):
  markdown_link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
  matches = markdown_link_pattern.findall(markdown_text)
  if add_blank_target:
    converted_text = markdown_link_pattern.sub(r'<a href="\2" target="_blank">\1</a>', markdown_text)
  else:
    converted_text = markdown_link_pattern.sub(r'<a href="\2">\1</a>', markdown_text)
  return converted_text, len(matches)

def convert_href_to_markdown(html_text):
  href_link_pattern = re.compile(r'<a\s+(?:[^>]*?\s+)?href="([^"]*)"(?:[^>]*?\s+)?target="_blank"[^>]*>(.*?)</a>|<a\s+(?:[^>]*?\s+)?href="([^"]*)"[^>]*>(.*?)</a>')
  matches = href_link_pattern.findall(html_text)
  converted_text = href_link_pattern.sub(lambda match: f'[{match.group(2) or match.group(4)}]({match.group(1) or match.group(3)})', html_text)
  return converted_text, len(matches)

def validate_input_content(content, is_markdown):
  if is_markdown:
    if not re.search(r'\[.*?\]\(.*?\)', content):
      print("Warning: The input file does not appear to contain Markdown links.")
  else:
    if not re.search(r'<a\s+href=".*?"', content):
      print("Warning: The input file does not appear to contain HTML links.")

def main():
  parser = argparse.ArgumentParser(
    description="Convert between Markdown links and HTML links.",
    usage="%(prog)s -in INPUT -out OUTPUT (-m | -n) [-b]",
    formatter_class=argparse.RawTextHelpFormatter
  )
  parser.add_argument('-in', '--input', required=True, help="Path to the input file.")
  parser.add_argument('-out', '--output', required=True, help="Path to the output file.")
  parser.add_argument('-b', '--blank', action='store_true', help="Add target='_blank' to HTML links (only works with -n).")
  group = parser.add_mutually_exclusive_group(required=True)
  group.add_argument(
    '-m', '--markdown',
    action='store_true',
    help="""Convert HTML links to Markdown links.
    Example:
      Input:  <a href="https://example.com">Example</a>
      Output: [Example](https://example.com)"""
  )
  group.add_argument(
    '-n', '--normal',
    action='store_true',
    help="""Convert Markdown links to normal HTML links.
    Example:
      Input:  [Example](https://example.com)
      Output: <a href="https://example.com">Example</a>"""
  )
  args = parser.parse_args()

  input_file = args.input
  output_file = args.output
  add_blank_target = args.blank
  to_markdown = args.markdown
  to_normal = args.normal

  # Validate flag dependencies
  if add_blank_target and not to_normal:
    print("Warning: The -b/--blank flag is ignored when converting HTML to Markdown.")

  # Check if output file already exists
  if os.path.exists(output_file):
    response = input(f"The file '{output_file}' already exists. Overwrite? (y/n): ").strip().lower()
    if response != 'y':
      print("Operation canceled.")
      sys.exit(0)

  try:
    # Read the input file
    try:
      with open(input_file, 'r', encoding='utf-8') as file:
        input_content = file.read()
    except FileNotFoundError:
      print(f"Error: The input file '{input_file}' does not exist.")
      sys.exit(1)
    except UnicodeDecodeError:
      print(f"Error: The input file '{input_file}' could not be decoded as UTF-8.")
      sys.exit(1)
    except Exception as e:
      print(f"Error: An unexpected error occurred while reading the file: {e}")
      sys.exit(1)

    # Validate input content
    validate_input_content(input_content, to_normal)

    # Perform the conversion
    if to_markdown:
      output_content, num_links = convert_href_to_markdown(input_content)
      operation = f"converted {num_links} HTML links to Markdown links"
    elif to_normal:
      output_content, num_links = convert_markdown_to_href(input_content, add_blank_target)
      operation = f"converted {num_links} Markdown links to HTML links"

    # Write the output file
    try:
      with open(output_file, 'w', encoding='utf-8') as file:
        file.write(output_content)
    except Exception as e:
      print(f"Error: An unexpected error occurred while writing to the file: {e}")
      sys.exit(1)

    print(f"Successfully {operation} and saved to {output_file}")

  except KeyboardInterrupt:
    print("\nProcess interrupted by the user.")
    sys.exit(1)

if __name__ == "__main__":
  main()

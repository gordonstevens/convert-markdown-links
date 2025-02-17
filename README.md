# Markdown ↔ HTML Link Converter
A Python script for the command line interface of your operating system to convert between Markdown links and HTML links.

The script supports:

> Converting Markdown links to HTML links (-n or --normal).
> Converting HTML links to Markdown links (-m or --markdown).
> Adding target="_blank" to HTML links (-b or --blank).

### Prerequisites:

Ensure you have Python 3.x installed. You can check by running:

python --version

> If Python 3 is not installed, download it from [python.org](https://www.python.org/).

### Download the Script:

Download the script convert_links.py from the repository.

### Run the Script:

Open a terminal or command prompt.
Navigate to the directory where convert_links.py is located.
Run the script using Python:

python convert_links.py -h

This will display the help message and confirm that the script is working.

### Usage

Basic Usage
The script requires the following arguments:

-in or --input: Path to the input file.

-out or --output: Path to the output file.

One of the following mutually exclusive options:

-m or --markdown: Convert HTML links to Markdown links.

-n or --normal: Convert Markdown links to HTML links.

> Optional:
> -b or --blank: Add target="_blank" to HTML links (only works with -n, as default Markdown does not support opening in a new tab or window).

### Examples

1. Convert Markdown Links to HTML Links
Input File (input.md):

```Here is a link to [Google](https://www.google.com) and another to [GitHub](https://github.com).```

#### Command:

```python convert_links.py -in input.md -out output.html -n```
Output File (output.html):

```Here is a link to <a href="https://www.google.com">Google</a> and another to <a href="https://github.com">GitHub</a>.```

2. Convert HTML Links to Markdown Links
Input File (input.html):

```<p>Here is a link to <a href="https://www.google.com">Google</a> and another to <a href="https://github.com" target="_blank">GitHub</a>.</p>```

#### Command:

```python convert_links.py -in input.html -out output.md -m```
Output File (output.md):

```<p>Here is a link to [Google](https://www.google.com) and another to [GitHub](https://github.com).</p>```

3. Add target="_blank" to HTML Links

Input File (input.md):

```Here is a link to [Google](https://www.google.com) and another to [GitHub](https://github.com).```

#### Command:

```python convert_links.py -in input.md -out output.html -n -b```

Output File (output.html):

```Here is a link to <a href="https://www.google.com" target="_blank">Google</a> and another to <a href="https://github.com" target="_blank">GitHub</a>.```

### Options

Flag	Description
-in, --input	Path to the input file (required).
-out, --output	Path to the output file (required).
-m, --markdown	Convert HTML links to Markdown links.
-n, --normal	Convert Markdown links to HTML links.
-b, --blank	Add target="_blank" to HTML links (only works with -n).

### Error Handling

The script includes error handling to make this a smoother experiences. Here are some common scenarios:

#### Input File Not Found:

If the input file does not exist, the script will exit with an error:

Error: The input file 'input.md' does not exist.

#### Output File Already Exists:

If the output file already exists, the script will prompt the user to confirm overwriting:

The file 'output.html' already exists. Overwrite? (y/n):

#### Invalid File Encoding:

If the input file is not UTF-8 encoded, the script will exit with an error:

Error: The input file 'input.md' could not be decoded as UTF-8.

#### No Links Found:

If the input file does not contain any links, the script will issue a warning:

Warning: The input file does not appear to contain Markdown links.

#### Keyboard Interrupt:

If the user interrupts the script (e.g., with Ctrl+C), it will exit gracefully:

Process interrupted by the user.

### License

This project is licensed under the MIT License. See the LICENSE file for details.

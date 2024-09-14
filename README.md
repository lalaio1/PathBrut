
# 🛠️ Directory Bruter

![DirectoryBrutser])

**Directory Bruter** is a powerful tool for directory brute-forcing on web servers. It helps to discover hidden directories and files by making HTTP requests with a list of potential directory names and extensions.

![DirectoryBruter](https://raw.githubusercontent.com/lalaio1/PathBrut/main/1.png)

## 📋 Features

- 🚀 Multi-threaded for fast execution.
- 📂 Supports custom wordlists for flexible scanning.
- 🌐 Configurable HTTP headers with random User-Agent.
- 💾 Option to save results to a file.
- 🛠️ Verbose mode for detailed logs and errors.

## 🛠️ Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/lalaio1/PathBrut.git
   ```

2. **Navigate to the directory:**

   ```bash
   cd PathBrut
   ```

3. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

To use Directory Bruter, run the script with the necessary arguments. Here's a basic example:

```bash
python PathBrut.py -u http://example.com -w /path/to/wordlist.txt -t 10 -o -v -e .php,.html
```

## 📜 Arguments

| Argument      | Description                                                   | Default    |
|---------------|---------------------------------------------------------------|------------|
| `-u`, `--url` | Target URL (e.g., `http://example.com`)                       | Required   |
| `-w`, `--wordlist` | Path to the wordlist file                                  | Required   |
| `-t`, `--threads` | Number of threads to use (default is 1)                    | 1          |
| `-o`, `--output` | Save results to a file                                     | Disabled   |
| `-v`, `--verbose` | Verbose mode (show detailed logs and errors)               | Disabled   |
| `-e`, `--extensoes` | List of extensions to try (e.g., `.php,.exe,.bak`)         | None       |

### Example Commands

1. **Basic Scan:**

   ```bash
   python PathBrut.py -u http://example.com -w /path/to/wordlist.txt
   ```

2. **Scan with Custom Threads and Verbose Output:**

   ```bash
   python PathBrut.py -u http://example.com -w /path/to/wordlist.txt -t 5 -v
   ```

3. **Scan with Extensions and Save Results:**

   ```bash
   python PathBrut.py -u http://example.com -w /path/to/wordlist.txt -e .php,.html -o
   ```

## 📂 Examples

### Basic Usage

```bash
python PathBrut.py -u http://example.com -w /path/to/wordlist.txt
```

Output:
```
> Target: http://example.com
-----------------------------------------
[+] 200: http://example.com/admin
[+] 200: http://example.com/login
[-] 404: http://example.com/hidden
```

### Advanced Usage with Extensions and Verbose Mode

```bash
python PathBrut.py -u http://example.com -w /path/to/wordlist.txt -e .php,.html -v
```

Output:
```
> Target: http://example.com
-----------------------------------------
[+] 200: http://example.com/admin.php
[+] 200: http://example.com/login.html
[-] 404: http://example.com/hidden.php
[ERROR] Request failed: http://example.com/unknown.php
```

## 📝 License

This project is licensed under the [MIT License](LICENSE).

## 📞 Contact

For any issues or inquiries, please open an issue on [GitHub](https://github.com/lalaio1/PathBrut/issues).

---

Made with ❤️ by [lalaio1](https://github.com/lalaio1)

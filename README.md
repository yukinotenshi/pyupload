# PyUpload
A simple CLI tool to upload file with direct link

Made for those who are too lazy to open SCP/SFTP

## Installation
```
pip install pyupload
```

## Usage

```
pyupload <filename> --host=<host>
```

## Example
```
pyupload .gitignore --host=catbox

[1674/1674] bytes |====================>|Your link : https://files.catbox.moe/e03ygs.gitignore
```

## Running Tests
```
python3 upload_test.py
```

## Issues? Changes?
Just open an issue/pull requests
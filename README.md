# MSP360 / CloudBerry Backup Agent Configuration Decrypter

This tool decrypts CloudBerry Labs `enginesettings.list` passwords,
namely from the `NetworkCredentials` block.

This repo contains the following:

* `README.md` - This file.
* `enginesettings.list` - A sample configuration file to decrypt.
* `main.py` - The decrypter, as a simple proof of concept (PoC).
* `requirements.txt`- Describes python dependencies required to run the PoC.

## Usage

```bash
poc@pentest ~/cloudberry-decrypt $ python main.py enginesettings.list
\\localhost\networkshare cloudberry 0vagrant
```

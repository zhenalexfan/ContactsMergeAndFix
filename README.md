# Contacts Merge and Fix

## Overview

This is a command-line tool to help you clean, fix and merge contacts records.

**Features:**
* Merge duplicated contacts
* Add phonetic names to Chinese names

**Supported formats:**
* Google Contacts CSV


## Usage

After git clone'ing or downloading the code package, run the code with Python 3.

```
# Prepare the dependency pakages
pip3 install .

# Run `contacts_merge_and_fix` script
python3 -m contacts_merge_and_fix \
  -input <a path to your *.csv file> \
  -output <a path to save the output *csv file to>
```
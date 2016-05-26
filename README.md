# Scraping Screenshots of Google Opinion Rewards Data

Google Opinion Rewards lets you view your reward history within the Android app, but only as an image and with no way to export to a text format. 

Since images of tabular data are a common annoyance it seemed like it could be interesting to use OCR to extract this data and possibly reuse for something else later.

This script uses [tesseract-ocr](https://github.com/tesseract-ocr/tesseract) and python to extract the data from screenshots and format into a csv file.

------------------------
### Note: [tesseract](https://github.com/tesseract-ocr/tesseract) is required in order for this to work.

Instructions for Debian Linux and Mac below. I am not sure if a Windows version of tesseract is available. I briefly tried to find it, but was not very successful.
 
The following will install tesseract on Debian Linux distros including Raspbian for Raspberry Pi:
 
 ```
 sudo apt-get install tesseract-ocr
 ```
 
On Mac, if you have [homebrew](https://github.com/Homebrew/brew) installed you can install tesseract in Terminal with:
```
brew install tesseract
```

 
 This script is written for python 3x, but could easily be modified for python 2x if needed.
 
 The required python packages for the script to work are all standard library and this was able to run on a Raspberry Pi.
 
 --------------------
### To try it out:
* Install tesseract with the instructions above
* [Download and unzip](https://github.com/BenRussert/scrape-rewards/archive/master.zip) 
    or clone this repository:
    ```
    git clone https://github.com/BenRussert/scrape-rewards.git
    ```

* Take screenshots of your rewards history data and put them in the ./screenshots directory (example screenshot below)
    * Don't worry about capturing duplicate rewards entries in the images, they will be removed by the script

* Open a command line and cd to the main scrape-rewards directory, run:
```
python ./get_rewards_data.py
```
* A timestamped csv file will be placed placed in the current directory, this can be opened with any spreadsheet software, text editor, etc.
---
### Optional Arguments:
If you append the -v argument as below and you have [pandas](http://pandas.pydata.org/) installed the csv output will contain additional formatting and date sorting
    * If you have pandas you should use the -v argument
```
python ./get_rewards_data.py -v
```

### Output example:

| date       | reward | cumulative | 
|------------|--------|------------| 
| 2015-05-26 | 0.6    | 6.79       | 
| 2015-05-24 | 0.1    | 6.19       | 
| 2015-05-18 | 0.1    | 6.09       | 
| 2015-05-17 | 0.57   | 5.99       | 
| 2015-05-13 | 0.0    | 5.42       | 
| 2015-05-12 | 0.2    | 5.42       | 
| 2015-05-12 | 0.69   | 5.22       | 
| 2015-05-04 | 0.15   | 4.53       | 
| 2015-04-28 | 0.1    | 4.38       | 
| 2015-04-25 | 0.33   | 4.28       | 
| 2015-04-23 | 0.19   | 3.95       | 
| 2015-04-22 | 0.12   | 3.76       | 
| 2015-04-21 | 0.15   | 3.64       | 
| 2015-04-20 | 0.63   | 3.49       | 
| 2015-04-16 | 0.3    | 2.86       | 
| 2015-04-13 | 0.13   | 2.56       | 
| 2015-04-11 | 0.54   | 2.43       | 
| 2015-04-08 | 0.0    | 1.89       | 
| 2015-04-03 | 0.14   | 1.89       | 
| 2015-04-02 | 0.21   | 1.75       | 
| 2015-03-30 | 0.12   | 1.54       | 
| 2015-03-25 | 0.1    | 1.42       | 
| 2015-03-23 | 0.22   | 1.32       | 
| 2015-03-14 | 0.1    | 1.1        | 
| 2015-03-09 | 0.0    | 1.0        | 
| 2015-03-04 | 1.0    | 1.0        | 
| 2015-03-04 | 0.0    | 0.0        | 

### Example screenshot input:

<a href="url"><img src="./screenshots/Screenshot1.png" align="left" height="430" width="243" ></a>

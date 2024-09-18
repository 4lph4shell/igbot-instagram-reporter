# instagram accounts reporter IGbot

![image](https://github.com/4lph4shell/igbot-instagram-reporter/blob/master/Untitled-design-13.png)

Instagram reporter - is a tool designed to help you report instagram account by your awn account .
You should have number of account (recomended more than 100 ) and some proxy to able report and delete account from instagram.
This tool will be loging to each account one by one and start to choose report aption that you choose in the firdt step .

 we recomend to use it one the Ubuntu 20 servers

# Prerequisited
You should install these requerment in the fist step on your server 
```
 sudo add-apt-repository ppa:deadsnakes/ppa
```
```
 sudo apt update
```
```
sudo apt install firefox
```
```
sudo apt install python3.10
```
```
sudo apt-get install python3-setuptools
```
```
sudo apt-get install python3.10-venv
```
```
python3.10 -m pip install setuptools
```
```
apt-get install python3-setuptools
```
```
python3.10 -m pip install pandas
```
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```
```
python3.10 get-pip.py
```
```
python3.10 -m pip install pandas jsonpickle  dnspython matplot seaborn selenium bs4 webdriver_manager
```
```
python3.10 -m pip install pyarrow
```
```
python3.10 -m pip install --upgrade requests
```
```
python3.10 -m pip install --upgrade urllib3 chardet
```
 # Usage
 
1. **PreSetting**
 
first of all you have to make list of proxys and accounts in the files
 - add your proxys to proxy.txt like     127.0.0.1.8588
 - add your accounts to accounts.txt     in the fist line username and in the second line password
 2. **PreUsage**
   - Processing accounts
   ```
   python3.10 instagram3.py account ./accounts.txt ./accounts.json true
   ```
   It is true, it means that the randomizer is active.
   - Proxies processing
     ```
     python3.10 instagram3.py proxy http ./proxy.txt ./proxy.json
     ```
     - Converting accounts to cookies
       ```
       python3.10 instagram3.py cookie ./accounts.json ./cookies.json null null 2 true false
       ```
From left to right, the second null is the processed proxy file, the number 2 is the number of calls for each account, then let it remain true, then false means randomizer, which is false because we did it in the previous step (initial processing of accounts). 

# Original and final order:
- report
```
python3.10 instagram3.py report username1_to_report,username2_to_report 0,4,0 true ./cookies.json ./proxy.json
```
## Example
The expression 0, 4, 0 from left to right means that the first option is selected first, that is:
- It's posting something that should't be on instagram

 ![image](https://github.com/4lph4shell/igbot-instagram-reporter/blob/master/photo_2024-09-18_19-20-03.jpg)


Then the fifth option (index 4)

![image](https://github.com/4lph4shell/igbot-instagram-reporter/blob/master/photo_2024-09-18_19-20-08.jpg) 

- Nudity or sexual activity
  
Then, in the next question, he chooses the first option (zero index).

The expression true means to block or not

## Use it for good perpeses

The next two files are obtained from the previous steps

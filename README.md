# Simple-Coinbase-Pro-DCA
This is a simple python script to allow for Dollar-Cost-Averaging through the Coinbase Pro market API.

## DISCLAIMER:
This script is available to the public for use in dollar-cost-averaging through the Coinbase Pro API; however, there is absolutely 
no warantee provided with this code and the developer(s) cannot be found liable for ANY AND ALL use of the code. 
	USE THIS CODE AT YOUR OWN FINANCIAL RISK.
	
This script is under active development and suggestions/edits are GREATLY appreciated and encouraged!

--------------------------------------------------------------------------------------------------

## Requirements
The following are requirements for this script:
* cbpro
* schedule
* json
* time

These can be installed individually using Pip or by running: ```pip install -r requirements.txt```


## How to generate a Coinbase Pro API key:

1) Follow one of the following two links depending on your intention. 
	* To use this code for REAL transactions, go to: https://pro.coinbase.com/profile/api
	* To use this code for TEST transactions, go to: https://public.sandbox.pro.coinbase.com/profile/api
		* If this is your first time using the Coinbase Pro sandbox, you may need to connect/authorize your Coinbase account to access this feature. There will be a pop-up if you need to do this.
2) Click "New API Key".
3) Select your portfolio and name the API key (optional).
4) Select the permissions you would like to give to the API key: "View", "Transfer", "Trade".
5) Give the API key a secure Passphrase and KEEP A RECORD of this, as it will not be viewable again.
6) (Optional) Configure IP Whitelisting.
7) Click "Create API Key" and enter your 2FA (if enabled).
8) Copy the API Secret and KEEP A RECORD of this, as it will not be viewable again.
9) Copy the API Public Key above the Nickname. This will be viewable until the key is deleted.

--------------------------------------------------------------------------------------------------

## Script configuration:

Note: Configuration file MUST follow valid JSON standards in order to be read properly by the script. It is NOT recommended to validate the JSON online with your API information as it is sensitive financial informaiton that should NOT be shared.

1) Open "example-config.json" and examine the two provided examples.
2) Open "config.json".
3) Copy your API Public Key into "api-key".
4) Copy your API Secret Key into "api-secret".
5) Copy your API Passphrase into "api-passphrase".
6) Enter a frequency type: "seconds", "minutes", "hours", "days", "day" (for use with a named day), or "weeks". Frequency type must be in DOUBLE quotes.
	* If the frequency type is "seconds", "minutes", "hours", "days", or "weeks":
		* Enter an integer value. 
	* If the frequency type is "day":
		* Enter one of the following strings: "sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday". Day name must be in DOUBLE quotes.
		* Day-type frequency will occur once each week on the selected day.
8) For each recurring purchase:
	* Enter a VALID trading pair from Coinbase Pro in DOUBLE quotes in "trading-pair".
	* Enter a float-type value into "amount" for purchase amount in the QUOTE currency.
		* Example: "BTC-USD" quote currency is USD and will purchase BTC. "USD-BTC" quote currency is BTC and will purchase USD.

--------------------------------------------------------------------------------------------------

## Contributing
Contributions are greatly appreciated for this project! For major changes, please open an issue first to discuss what you would like to change. **DO NOT** push your personal config.json file to the repository as it stores the API information which is sensitive financial information that should NOT be shared.

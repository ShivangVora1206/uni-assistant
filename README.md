# uni-assistant
This is a simple tool to help students keep track of university applications currently available. It is utilizing the uni-assist APIs to fetch the data and display it in a user-friendly manner. The data is displayed in a terminal because it looks cooler.

## config.py
The `config.py` file holds the configuration information which can be updated to your needs. In the `main.py` file there are comments which indicate what some selected configuration values represent.

## filters.py
The `filters.py` file has the filters which are used to filter the data fetched from the uni-assist APIs. The filters are used to filter the data based on the user's preferences.

## main.py
The `main.py` file is the main file which is used to run the application. It fetches the data from the uni-assist APIs and displays it.

## local.json
A lazy db file just to store the data fetched, used to compare newer response from the previous one to identify the difference and see what has changed.


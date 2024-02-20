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

## Sample Output
![alt text](https://github.com/ShivangVora1206/uni-assistant/blob/main/sample_output/uni-assistant-sample-output.png?raw=true)

## Instructions
#### 1. Clone this repo
#### 2. Navigate to the repo in your terminal
#### 3. Run `python main.py`

## Color Code Representation Of Output
***red -> Application not opened yet***
***green -> Application open***
***violet -> New / Difference / Token***
***yellow -> Course Name***
***blue -> Degree Type***

## Note
The ***difference*** part in the output means this data was not present in the previous response, so it is a ***new data***. Assuming the script is run once a day, the data present in the ***difference*** part is the ***new data*** that has been added in the last 24 hours.

Update the `filters.py` file to add your preferences, the university names need to be the same as written on the uni-assist portal. If the university name is not written correctly, the script will not be able to filter the data for that university.
# Money-Management

README

Our app is a money management system which tracks income on a month to month basis, and calculates if certain expenditures are necessary.

We have created 2 parts: A back-end python program, a visual graph depicting the user's balance over a time period.

The back-end python uses natural language processing to distinguish between different styles of text in order to reach a conclusion based on input.

The visual graph uses updated input from the python program to consistently update the graph. The visual graph is a line chart depicting monthly balance across a period
of time.

EXPLANATION

To run the code, you will need to first download some things:
 - PyCharm (Latest Version)
 - The matplotlib Module
 - The textblob Module

To download PyCharm:
- Go to: https://www.jetbrains.com/pycharm/download/#section=windows
- Click the download button and follow the instructions to download.

Once PyCharm is downloaded:
- Download the GitHub code
- Open the .zip file
- Open MoneyManager.py
- Open the Terminal at the bottom

To install the Modules:
- In the Terminal, type the following to update pip:
   python -m pip install -U pip
- Type the following once pip has finished updating:
    python -m pip install -U matplotlib
- This will install all the necessary libraries for matplotlib to function.
- In the terminal, type the following:
    pip install -U textblob
    python -m textblob.download_corpora
- Now wait for the Module to download.
- Excpect several command line statements.

Once all the libraries have finished downloading, you can now run the program.
Make sure your terminal is in the correct path for the program to properly run. 
To run the app, type the following in the terminal:
    python MoneyManager.py

Congratulations! You can now use our program.

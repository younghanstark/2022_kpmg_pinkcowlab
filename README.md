# CO2gather: Automatic CO2 Saving Incentive Manegement Service
[2022 KPMG Ideathon Challenge] Pink Cow Lab. - "CO2gather"

## Overview
This is an API which gets core brandname from random merchant name of credit card log. We're gonna use this API to automatically calculate people's available incentive based on their credit card log.

## API Base URL (Only during the Competition)
[http://20.194.102.148:3000/api/투썸플레이스신촌](http://20.194.102.148:3000/api/투썸플레이스신촌)

You can put the string that you wanna know the core brandname instead of '투썸플레이스신촌'.

## Algorithm Description
![Flow Chart](/assets/flow_chart.png)
As you can seen in flow chart, the solution learns brand name datasets using `make_scores.py`. The 'learn' in our solution means the process computing 'word scores'. Word scores can be defined freely considering characteristics of solution and datasets, we defined our word scores as cohesion probability.

> Cohesion Probability: Prefix(cumulative) product of the probablities of meeting following characters in given string, in the process of making inner string from seperating each characters from a string.

After the learning, `string_processing.py` script gets a random string and it extracts core brand name. I implemented extracting using tokenizing. The script tokenizes given string based on cohesion probablities, and returns decreasingly sorted list based on word scores. At the function call, you can get core brand name by accessing first element of the list.

Since the word score is only based on cohesion probability, the probability that token that has the highest word score and core brand name are the same is significantly high. From `data_lab.py` script, the accuracy of the current solution was 80.501393%.

## Local Requirements
- Node.js, npm (Uses express.js and python-shell but it considers dependencies)
- Python 3, Some Python packages:
    ```shell
    $ pip install numpy
    $ pip install psutil
    $ pip install scipy
    $ pip install scikit-learn
    $ pip install soynlp
    $ pip install openpyxl
    $ pip install pandas
    ```

## How to Run
1. Clone this repository.
2. Satisfy every requirements.
3. Go to local repository folder, run:
    ```shell
    $ cd myapp
    $ nohup npm start &
    ```

## How to Put Datasets
> Datasets: List of brandnames that you wanna detect in random strings
1. Make Excel(.xlsx) file that containing data of brandnames. (Make it into same format with previous files!)
2. Put it to /core/test_data
3. Add that filename to the list 'file_list' in make_scores.py like below(Do not include .xlsx into it!):
    ```python
    file_list = ['purchase_data_7Feb22', 'YOUR NEW FILE NAME']
    ```
4. Run /core/make_scores.py once, then it makes word scores. (You don't need to restart the server.)

It saves the dictionary data into a file(scores_dict.pkl). When the API starts the process, it gets word scores from the **pickle file**. It means, the new brandnames are not gonna be considered unless you run make_scores.py even if you put the new dataset files.

## File Description
- `api.py`: Script that Python shell runs
- `data_lab.py`: Measures accuracy of solution
- `make_scores.py`: Considers every datasets and computes cohesion scores - learning
- `scores_dict.pkl`: Data file containing cohesion scores
- `read_data.py`: Script that reads datasets
- `string_processing.py`: Script that tokenizes given string and extracts core brand name

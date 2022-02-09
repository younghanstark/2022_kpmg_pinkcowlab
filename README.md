# CO2gather
[2022 KPMG Ideathon Challenge] Pink Cow Lab. - "CO2gather"

## Overview
This is an API which gets core brandname from random merchant name of credit card log. We're gonna use this API to automatically calculate people's available incentive based on their credit card log.

## API Base URL (Only during the Competition)
[http://20.194.102.148:3000/api/투썸플레이스신촌](http://20.194.102.148:3000/api/투썸플레이스신촌)

## Local Requirements
```shell
$ pip install numpy
$ pip install psutil
$ pip install scipy
$ pip install scikit-learn
$ pip install soynlp
$ pip install openpyxl
$ pip install pandas
```

## How to Put Datasets
> Datasets: List of brandnames that you wanna detect in random strings
1. Make Excel(.xlsx) file that containing data of brandnames. (Make it into same format with previous files!)
2. Put it to /core/test_data
3. Add that filename to the list 'file_list' in make_scores.py like below(Do not include .xlsx into it!):
    ```python
    file_list = ['purchase_data_7Feb22', 'YOUR NEW FILE NAME']
    ```
4. Run /core/make_scores.py once, then it makes word scores.

It saves the dictionary data into a file(scores_dict.pkl). When the API starts the process, it gets word scores from the **pickle file**. It means, the new brandnames are not gonna be considered unless you run make_scores.py even if you put the new dataset files.
# Repository Contents

This repository has the following files

* Data 
* Metrics 
* Model 
* Patterns & CAPAs
* Testing

## Data 

* **MS** (txt file): This file has the metrics to work with
* **Visualization** (notebook): This file presents a visualisation of the extracted metrics 
* **dataset** (csv file): This file has the labels and metrics
* **repositories**: This file has the list of repositories (and its labels) used to extract the metrics obtained in the **dataset** file. 

## Metrics

This folder has just the metrics used in the project written in individual py files, a more detailed description can be found in the problem formulation section: https://www.overleaf.com/project/61aa26a069ec8372892bdf33

## Model 

This folder contains a txt file with two links to the two models used in the experiment. The first link is to the model (CAPA vs non-CAPA classification task), the second link is to the model (CAPA classification). In both cases three machine learning algorithms were used. 

## Patterns and CAPAs

* **nonCAPAs** (link to csv file): This csv file has the metrics of nonCAPAs repositories to train the first model in the Model folder.
* **chosen_pull_requests** (link to csv file): This file has the chosen pull requests according to the patterns (timestamps) in the file **total_added_result.json** taken from https://github.com/Gci04/tom-pattern-recognition (to see how they were selected please refer to the following notebook https://colab.research.google.com/drive/1yUEz9QcdcYdnFnkeKZc-Xme02HU8q5-6?usp=sharing). 
* **not_chosen_pull_requests.csv** (link to csv file): This csv file has the pull requests that were not chosen (do not match with the patterns, i.e. the complement set)
* **patterns_metrics_data.csv** (link to csv file): This csv file has the metrics of the chosen pull requests (the ones that comply with the patterns), the metrics are the same metrics defined in the folder Metrics. 


## Testing

* **Metrics Unit Test** (notebook): This jupyter notebook imports and tests the individual metrics py files from the folder Metrics.
* **test_metrics** (py file): This script is the imported filed executed by the notebook in this same folder. 


# covid-19-image-classification



## Contacts:

- [Saumya Pandey](https://github.com/saumya-datascience)
- [Tricia Toffey](https://github.com/ttoffey)
- [Jackelyne Gutierrez](https://github.com//Jackelyneg)
- [Okyere Gyebi](https://github.com/Okyere82)

## Table of Contents:



## Purpose
As the world grapples with COVID-19, every ounce of technological innovation and ingenuity harnessed to fight this pandemic brings us one step closer to overcoming it.
 
AI, a core technology of the fourth industrial revolution, has come up as an important non-medical intervention to overcome the current global health crisis, to build next-generation epidemic preparedness, and to move towards a resilient recovery.

Effective screening enables quick and efficient diagnosis of COVID-19 and can mitigate the burden on healthcare systems

 In this project,we propose two Machine learning models to assist in faster screening of COVID 19.
 
 
 ## Model 
Our model(s) aim to predict whether a person has a risk of COVID19 through chest X-rays and  symptom checker.
Once predicted positive the user will have the opportunity to input their zip code and search hospitals within a 15 miles radius.



# List of Data Sources
- [Covid-19 Chest X-ray Images](https://www.kaggle.com/debajyoti1/covid19-classification-x-ray/data) 
- [Covid symptom Database](https://www.kaggle.com/saumya5679/covid-19-prediction-97-eda?select=Covid+Dataset.csv)
- [Hospital data API](https://protect-public.hhs.gov/pages/hospital-utilization)

## Data Scrubbing
- Basic Cleanup:(Symptoms/Hospital)
- Delete nulls
- Drop unnecessary columns 
- Change column names
- Merged different datasets (Hospital/zip)


### Target Variable :(X-ray/Symptoms)
- Covid yes/no
- Converted symptoms and Chest X-rays into Binary labels for 1=possible covid case and 0=No covid case



## Technologies Used:
- Pandas
- JavaScript
- Folium
- Flask
- HTML/CSS
- Bootstrap
- Python
- Web API
- Tensorflow(Keras)
- Sklearn
- Matplotlib

## X-Ray 

![Network](https://github.com/Jackelyneg/covid-19-image-classification/blob/main/Images/network.PNG)
<img src="https://github.com/Jackelyneg/covid-19-image-classification/blob/main/Images/train-val.PNG" width="300" height="300">


![class 1](https://github.com/Jackelyneg/covid-19-image-classification/blob/main/Images/class%200.PNG)

![class 0](https://github.com/Jackelyneg/covid-19-image-classification/blob/main/Images/class%201.PNG)



## Symptoms

### Model Comparison(Symptoms):
<img src="https://user-images.githubusercontent.com/81592631/134608547-3a4eee18-01da-4246-9dc1-799f2c01f316.png" width="600" height="250">

- 5 models were done to the dataset
- Target Variable: Covid yes/no binary classification of 1 = yes, no = 0
- Random Forest has the highest score with an accuracy of .98 and a recall of .99. This model tends to have high accuracy prediction and can handle large numbers of features due to the embedded feature selection in the model generation process.



#### Metric of choice (Symptoms):
Recall:
- Model should have a recall as close to 1 as possible to reduce False Negatives

- Recall is being used as the selected metric because we need the percentage of actual positive results predicted correctly.

#### Top Features for Symptoms Data
<img src="https://github.com/Jackelyneg/covid-19-image-classification/blob/main/Images/symptoms%20weight.PNG" width="300" height="250">

- Using eli5, an explanation of estimator parameters (weights) was returned displaying model weights as an HTML table with the top positive features in the table.

###### Top features for Covid symptoms:
- Breathing Problems
- Dry cough
- Sore throat
- Fever




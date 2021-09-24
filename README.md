# covid-19-image-classification



## Contacts:

- [Saumya Pandey](https://github.com/saumya-datascience)
- [Tricia Toffey](https://github.com/ttoffey)
- [Jackelyne Gutierrez](https://github.com//Jackelyneg)
- [Okyere Gyebi](https://github.com/Okyere82)

## Table of Contents:



## Purpose
The app takes in x-ray of patients and detects weather the lungs are infected with covid 19 or not. To achieve our aim, we are using machine learning image processing algorithms. This part of the app is useful for the technicians to get a speedy outcome. The other part of the project is primarily catered for patients. We will be using another machine learning algorithm where  the patients can enter their symptoms and on that basis the model will detect whether they have covid or not.once detected positive, the  app
lets the person enter the zip code and then find hospitals with beds available for covid 19 patients within 15 miles.
 

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
![val](https://github.com/Jackelyneg/covid-19-image-classification/blob/main/Images/train-val.PNG)

![class 1](https://github.com/Jackelyneg/covid-19-image-classification/blob/main/Images/class%200.PNG)

![class 0](https://github.com/Jackelyneg/covid-19-image-classification/blob/main/Images/class%201.PNG)

<img src="https://github.com/Jackelyneg/covid-19-image-classification/blob/main/Images/xray%20graph.png" width="300" height="250">





## Symptoms
### Data
<img src="https://user-images.githubusercontent.com/81592631/134627210-c77ca715-280e-4b16-8390-a1be5bc9eb9d.png" >

-  In the data set there are symptoms like the ones listed above that will be used as our features
- The column Covid 19 is our target label
- The data consists of 0's and 1's meaning 1: the symptom is present and 0: the symptom is not present
### Model Comparison(Symptoms):

<img src="https://user-images.githubusercontent.com/81592631/134608547-3a4eee18-01da-4246-9dc1-799f2c01f316.png" width="500" height="300">

- 5 models were done to the dataset
- Target Variable: Covid yes/no binary classification of 1 = yes, no = 0
- Random Forest has the highest score with an accuracy of .98 and a recall of .99. This model tends to have high accuracy prediction and can handle large numbers of features due to the embedded feature selection in the model generation process.
#### Metric of choice (Symptoms):
Recall:

- Model should have a recall as close to 1 as possible to reduce False Negatives
- Recall is being used as the selected metric because we need the percentage of actual positive results predicted correctly.
#### Top Features for Symptoms Data

<img src="https://github.com/Jackelyneg/covid-19-image-classification/blob/main/Images/symptoms%20weight.PNG" width="600" height="300">

- Uing eli5, an explanation of estimator parameters (weights) is reutned displaying model weights as an HTML table with the top positive features in the table.
##### Top features for Covid symptoms:

- Breathing Problems
- Dry cough
- Sore throat
- Fever











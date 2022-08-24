
# Running the Model

## CAPA & non-CAPA Classification 

* **Data Loading**: We load the data labeled as CAPA and the non-CAPA elements and merge them in a single dataset to work with. 

* **Preprocessing**: The data has corrupted and/or missing values, we need to clean the data and set the correct format for all the elements entries (integer type, categorical values, timestamps, boolean values, etc).

* **Data Preparation**: The labels are encoded, the features to be used are set, the models to be trained are loaded, the dataset is split into train and test sets.

* **Model Training**: The models are trained. 

* **Model Assessment**: The respective metrics are obtained (confusion matrix, accuracy, precision, recall and f1 scores).

## CAPA Classification 

* **Preprocessing**: Load the [notebook](https://colab.research.google.com/drive/11imVJi9-O7OFrX1yJutDH3Brlkr5MOFC?usp=sharing) to check the procedure on how to the data was cleaned, prepared, and presented as the pair $(X,y)$ to train the model, 

* **Model Training*: Load the [notebook](https://colab.research.google.com/drive/1-QfY-rx7Hi1HP4vyngtcFv1_U8r-8cOa?usp=sharing) to obtain the pipeline to train the model, and to check its performance.

* **Trained Model**: Load the [notebook](https://colab.research.google.com/drive/1sb8_AI7VoGTB5Ntro1ZZSb9YVkLGSdpx?usp=sharing) to use the trained model to test your own pull request. Follow the specifications in the preprocessing notebook to have the same format as ours. 


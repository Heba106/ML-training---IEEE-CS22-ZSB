import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

def data_processing():
    features = ["gender", "age", "hypertension","heart_disease", "ever_married", 
        "work_type", "Residence_type", "avg_glucose_level", "bmi", "smoking_status"]

    # reading data
    data = pd.read_csv('./healthcare-dataset-stroke-data.csv')

    # id column is not a feature  
    data = data.drop(columns=['id'])

    # replace missing data with mean value 
    data['bmi'].fillna(data['bmi'].mean(), inplace=True) 

    # applying feature scaling (mean normalization)
    scale  = ['age', 'avg_glucose_level' , 'bmi', ] 
    data[scale] = (data[scale] - data[scale].mean()) / data[scale].std()

    # classify features with strong data type into numeric groups 
    data['gender'].replace('Male', 0, inplace=True)
    data['gender'].replace('Female', 1, inplace=True)
    data['gender'].replace('Other', 1, inplace=True)

    data["ever_married"].replace("Yes", 1, inplace=True)
    data["ever_married"].replace("No", 0, inplace=True)

    data["work_type"].replace("Private", 0, inplace=True)
    data["work_type"].replace("Self-employed", 1, inplace=True)
    data["work_type"].replace("Govt_job", 2, inplace=True)
    data["work_type"].replace("children", 3, inplace=True)
    data["work_type"].replace("Never_worked", 4, inplace=True)

    data["Residence_type"].replace("Rural", 0, inplace=True)
    data["Residence_type"].replace("Urban", 1, inplace=True)

    data["smoking_status"].replace("formerly smoked", 0, inplace=True)
    data["smoking_status"].replace("never smoked", 1, inplace=True)
    data["smoking_status"].replace("smokes", 2, inplace=True)
    data["smoking_status"].replace("Unknown", 3, inplace=True)

    X = data[features].values
    y = data['stroke'].values
    return X, y

if __name__ == "__main__":
    X , y = data_processing()
    # cut the dataset in half, one is used to train the model 
    # and the other one is used to test the model’s performance on new data (computing accuracy/cost. )
    x_train, x_test, y_train, y_test = train_test_split(X, y,  test_size=0.5)

    # Create a Logistic Regression Object, perform Logistic Regression
    log_reg = LogisticRegression()
    log_reg.fit(x_train, y_train)

    # Perform prediction using the test dataset
    y_pred = log_reg.predict(x_test)

    # calculating accuracy from Confusion Matrix 
    cm=confusion_matrix(y_test, y_pred)
    tp , fp , fn , tn = cm[0 ,0] ,cm[0 ,1] ,cm[1 ,0] ,cm[1 ,1]
    accuracy = ((tp+tn)/(tp+tn+fp+fn))*100
    print("{:.2f}%".format(accuracy))
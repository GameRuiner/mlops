from sklearn.linear_model import LinearRegression
import mlflow
import pickle

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

mlflow.set_tracking_uri("http://mlflow:5000")
mlflow.set_experiment("Linear Regression models")


@data_exporter
def export_data(inputData, *args, **kwargs):
    X_train, df, dv = inputData
    target = 'duration'
    y_train = df[target].values
    lr = LinearRegression()
    with open("preprocessor.b", "wb") as f_out:
        pickle.dump(dv, f_out)
    mlflow.log_artifact("preprocessor.b", artifact_path="preprocessor")
    mlflow.end_run()
    # mlflow.sklearn.autolog()
    with mlflow.start_run():
        lr.fit(X_train, y_train)
        model_info = mlflow.sklearn.log_model(
        sk_model=lr, artifact_path="model")
    print(lr.intercept_)

    return dv, lr
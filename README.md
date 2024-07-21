### Prerequisites

Make sure you have the following dependencies installed:

- [FastAPI](https://fastapi.tiangolo.com/)
- [XGBoost](https://xgboost.readthedocs.io/)
- [scikit-learn](https://scikit-learn.org/stable/)

Install dependencies using the following:

```bash
pip install fastapi
pip install xgboost
pip install scikit-learn
```

### Running the Application

Clone the repository and navigate to the project directory. Run the FastAPI application using:

```bash
uvicorn app:app --reload
```

Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) in your browser to access the FastAPI Swagger documentation and test the routes.

## Code Structure

- `filename.py`: The main Python script containing the FastAPI application.
- `xgb_reg.pkl`: The serialized XGBoost regression model.
- `InputData`: Pydantic model for input validation.
- `/test`: FastAPI route for testing the application.
- `/predict`: FastAPI route for making predictions using the trained model.

## Routes

### Test Route

- **Endpoint:** `/test`
- **Method:** GET
- **Description:** A test route to check if the FastAPI application is running successfully.
- **Response:**
  ```json
  {"message": "It Works!!!"}
  ```

### Prediction Route

- **Endpoint:** `/predict`
- **Method:** POST
- **Description:** Route for making predictions using the trained XGBoost model.
- **Request Body:**
  - `apogee`: Apogee parameter (float)
  - `perigee`: Perigee parameter (float)
  - `incl`: Inclination parameter (float)
  - `arg_perigee`: Argument of perigee parameter (float)
  - `raan`: RAAN (Right Ascension of Ascending Node) parameter (float)
- **Response:**
  ```json
  {"prediction": [float, float, ...]}
  ```

## Model Loading and Scaling

- The XGBoost model (`xgb_reg.pkl`) is loaded using `pickle` during application startup.
- Input data is validated using the Pydantic model `InputData`.
- Input features are converted to a 2D NumPy array and scaled using a `StandardScaler` instance.

## Notes

- Ensure that the path to the `xgb_reg.pkl` file is correct.
- The application runs on `http://127.0.0.1:8000` by default.

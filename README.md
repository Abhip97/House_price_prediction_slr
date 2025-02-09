# House_price_prediction_slr

This project builds a **Simple Linear Regression model** to predict house prices based on the area (square footage). The model is trained using a real-world dataset and follows a step-by-step approach, including data preprocessing, exploratory data analysis (EDA), model training, evaluation, and deployment.

## 📂 Dataset
- **Dataset Name**: Mock House Price Dataset
- **Features**:
  - `area_sq_ft`: Area of the house in square feet (independent variable)
  - `Price`: House price in dollars (dependent variable)
- **Source**: The dataset is generated for learning purposes only

## 📊 Steps in the Project
1. **Data Loading & Preprocessing**
   - Load the dataset
   - Rename columns (`area` → `area_sq_ft`, `amount` → `Price`)
   - Check for and handle missing values
   - Remove outliers using the IQR method
2. **Exploratory Data Analysis (EDA)**
   - Visualize feature distributions
   - Correlation heatmap
3. **Model Building**
   - Train-test split (80-20)
   - Train a **Simple Linear Regression model**
   - Evaluate model using **MSE, RMSE, and R² Score**
4. **Model Deployment**
   - Save the trained model using **Pickle**
   - Deploy via **Streamlit**


## 🚀 Deployment (Optional)
You can deploy the model as a web-based UI using **Streamlit**.


### Streamlit UI
1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## 📈 Model Performance

Mean Squared Error: 108462386.26
Root Mean Squared Error: 10414.53
R-squared Score: 0.97

## 🔗 Project Links
-  attached csv file of the dataset

## 🤝 Contributing
Feel free to fork this repository and contribute by submitting pull requests!




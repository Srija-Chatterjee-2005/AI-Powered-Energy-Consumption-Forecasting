# **⚡ AI-Powered Energy Consumption Forecasting System**
---

AI-powered energy consumption system to forecast energy consumption using machine learning. Includes data preprocessing, feature engineering, model training, and an interactive Streamlit dashboard for real-time predictions. Supports smart cities, energy optimization, and sustainability use cases. An end-to-end Machine Learning project that predicts future electricity usage and visualizes insights through an interactive dashboard.

---

## **📌 A. Project Explanation**
---

### **Energy Consumption Forecasting :** 

Energy forecasting means predicting how much electricity will be used in the future 📊
It helps reduce wastage, save cost 💰, and prevent power failures ⚡

### 🔹 **Technical Explanation :**

This project uses a Multi-Layer Perceptron (MLP) Regressor 🤖 to analyze time-series data and forecast future energy consumption using features like:

⏰ Hour.

📅 Day.

🗓️ Month.

🏷️ Weekend.

### **❗ Problem Statement :**

⚠️ Without proper energy forecasting, systems face:

⚡ Power cuts due to sudden demand spikes.

♻️ Energy wastage from overproduction.

💸 High electricity costs.

📉 Poor planning and inefficient resource use.

### **✅ Solution :**

This project uses an AI-based forecasting model 🤖 to predict future energy demand using historical data.

********🎯 Result:**

--> Better planning.

--> Reduced costs.

--> Efficient energy usage.

--> Stable power supply.

### **🌍 Industry Importance :**

*****Used in:

🏙️ Smart Cities → efficient energy planning.

⚡ Electricity Boards → load balancing.

🏭 Industries → reduce operational cost.

💻 Data Centers → optimize power usage.

🌱 Renewable Energy → plan generation.

### **🔄 Complete Workflow :**

Data Collection → Preprocessing → Feature Engineering → Model Training → Forecasting → Evaluation → Visualization

---

## ** 🛠️ B. Tech Stack Options**
---

This project uses a Multi-Layer Perceptron (MLP) Regressor 🤖, which is a type of neural network capable of learning complex patterns from data.

📊 Pandas & NumPy → for data handling and numerical operations.

🤖 Scikit-learn → to build and train the MLP model.

📈 Matplotlib → for visualizing trends and predictions.

⚙️ Difficulty: Medium.

💻 GPU Requirement: ❌ Not required.

🎯 Outcome: Provides a strong balance between accuracy and simplicity, making it ideal for practical projects and learning.

---

## **✅ C. Selected Approach**
---

We selected MLP Regressor with engineered time-based features because it offers an efficient and practical solution for energy forecasting.

i) Works well for pattern learning : The model can capture non-linear relationships in energy usage across time.

ii) Easy to implement : Using Scikit-learn makes it beginner-friendly and quick to build.

iii) No GPU required : Runs efficiently on standard systems, making it accessible.

iv) Strong GitHub proof : Demonstrates real-world ML concepts like feature engineering, model training, and prediction in a clear and impactful way.

---

## **🧠 D. Project Architecture**
---

 This project follows a modular Machine Learning pipeline where data flows step-by-step from raw input to final predictions and visualization.
 
 *******🔄 Data Flow :**
 
 📊 Energy Data (CSV)
        ↓
🧹 Data Preprocessing
        ↓
🧠 Feature Engineering
        ↓
🤖 Model Training (MLP Regressor)
        ↓
🔮 Energy Prediction
        ↓
📈 Evaluation Metrics
        ↓
🌐 Streamlit Dashboard

*******📦 Modules :**

--- data_preprocessing.py → cleaning & resampling

--- feature_engineering.py → create features

--- model_training.py → train MLP model

--- evaluation.py → calculate metrics

--- app.py → UI dashboard

---

## **📂  E. Folder structure**
---



---

## **💻 F. Installation & Setup**
---

### **🔹1. Install Python :**

👉 Download and install Python (version 3.9 or above)

### **🔹 2. Verify Installation : **

Open terminal / command prompt and run: **python --version**

### **🔹 3. Clone the Repository : **

**git clone https://github.com/Srija-Chatterjee-2005/AI-Powered-Energy-Consumption-Forecasting.git
cd AI-Powered-Energy-Consumption-Forecasting**

### **🔹 4. Create Virtual Environment :**

🪟 Windows : **python -m venv venv
              venv\Scripts\activate**
              
🐧 Mac/Linux : **python3 -m venv venv
                source venv/bin/activate**

✔ After activation, you’ll see (venv) in terminal

### **🔹 5. Install Required Libraries : **

**pip install -r requirements.txt**

✔ This installs:

--> pandas
--> numpy
--> scikit-learn
--> matplotlib
--> streamlit
--> joblib

### **🔹 6. Check Project Structure **

### **🔹 7. Train the Model : **

**python main.py**

✔ This will:

--train the model 🤖

--save model in models/

--save metrics in outputs/

### **🔹 8. Run the Dashboard : **

**python -m streamlit run app.py**

---

## **🔬 G. Virtual Simulation**
---

This project simulates a real-world energy management system ⚡ using historical data.

📊 Dataset acts as smart grid energy logs.

🤖 Model learns usage patterns (hour, day, month, weekend).

🔮 Predicts future energy demand.

📈 Dashboard shows insights and trends.

### **💼 Impact**

✔ Predict peak demand.

✔ Reduce energy wastage.

✔ Optimize energy usage.

✔ Support better decision-making.

---

## **▶️  H. How To Run**
---

**python -m streamlit run app.py**

 OR, 👉 Click here to watch the project demo


https://github.com/user-attachments/assets/6ff77092-1f6b-498c-980b-a1f6ca4af621

---

 ## **📸 I. Outputs**
 ---

 <img width="1502" height="712" alt="output6" src="https://github.com/user-attachments/assets/d19c11d2-9eea-4a08-bee2-3d10a13989e5" />
<img width="1920" height="1020" alt="output5" src="https://github.com/user-attachments/assets/7b009f84-375f-44d2-a50d-69c7bf8f33c4" />
<img width="1920" height="1020" alt="output4" src="https://github.com/user-attachments/assets/1b897645-37ab-48b5-ae88-ac9d50d97905" />
<img width="1920" height="1020" alt="output3" src="https://github.com/user-attachments/assets/dd85f2cd-0ee7-4f4a-8642-e91c60473ed9" />
<img width="1920" height="1020" alt="output2" src="https://github.com/user-attachments/assets/322ebb71-397f-412e-9246-614ca63bb3dd" />
<img width="1920" height="1020" alt="output1" src="https://github.com/user-attachments/assets/9c50d4d2-13fd-48ea-875f-741f78aecfc7" />

---

## **🚀 J. GitHub Upload Steps**
---

### **1. Create repo on GitHub (Public)**
### **2. Open terminal in project folder**
        git init
        git add .
        git commit -m "Initial commit"
### **3. Connect to GitHub**
        git remote add origin https://github.com/Srija-Chatterjee-2005/AI-Powered-Energy-Consumption-Forecasting.git
### **4.Push code**
        git branch -M main
        git push -u origin main
### **⚠️ If error occurs:**
        git pull origin main --allow-unrelated-histories
        git push

---

## **📅 K. Commit Plan**
---

🟢 Day 1: Project setup & folder structure.

🟢 Day 2: Dataset added.

🟢 Day 3: Data preprocessing implemented.

🟢 Day 4: Feature engineering (time features).

🟢 Day 5: Model training (MLP Regressor).

🟢 Day 6: Evaluation metrics added.

🟢 Day 7: Visualization & dashboard (Streamlit).

🟢 Day 8: Final upload (README + screenshots).

---

## **🛠️ L. Troubleshooting**
---

### **i) Module not found error :** 
👉 Run: pip install -r requirements.txt

### **ii) Model not found :** 
👉 Run main.py first to train and save the model

### **iii) Dataset not loading :** 
👉 Check file path (data/energy.csv) and format

### **iv) Streamlit not opening :** 
👉 Run: streamlit run app.py

### **v) Empty graphs / errors :**
👉 Ensure dataset is not empty and preprocessing is correct

---

## **💡 M. Future Improvements**
---

🔴 Implement LSTM / deep learning models.

☁️ Deploy on cloud (AWS / Streamlit Cloud).

🔌 Integrate real-time IoT data.

📊 Add advanced analytics & alerts.

🌐 Improve UI with interactive dashboards.

---

## **👩‍💻 N. Author**
---

### **Srija Chatterjee**

GitHub: https://github.com/Srija-Chatterjee-2005

LinkedIn: https://www.linkedin.com/in/srija-chatterjee-82a539308?utm_source=share_via&utm_content=profile&utm_medium=member_android

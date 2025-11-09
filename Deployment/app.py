import pandas as pd
import numpy as np
import joblib
import time

# --- Page Configuration ---
# Sets the title of the browser tab, the icon, and the layout.
st.set_page_config(
    page_title="Brainwave Emotion Analysis",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="auto"
)

# --- Mock Model ---
# In a real scenario, you would load your trained model.
# Since we don't have the .pkl file, we'll simulate its behavior.
class MockModel:
    def predict(self, data):
        # Simulate prediction - returns a random class (0, 1, or 2)
        return np.random.randint(0, 3, size=len(data))
    
    def predict_proba(self, data):
        # Simulate prediction probabilities
        proba = np.random.rand(len(data), 3)
        return proba / proba.sum(axis=1, keepdims=True)


# Try to load the real model, if it fails, use the mock model
try:
    xgboost_model = joblib.load("xgboost_model.pkl")
except FileNotFoundError:
    st.warning("`xgboost_model.pkl` not found. Using a mock model for demonstration purposes. Predictions will be random.")
    xgboost_model = MockModel()


# --- App Title and Description ---
st.title("🧠 Brainwave Emotion Analysis")
st.markdown("""
    Welcome to the AI-powered emotion prediction tool. 
    Upload a CSV file with EEG data to analyze and predict the emotional state.
""")


# --- Step 1: File Uploader ---
st.header("Step 1: Upload Your Data")
uploaded_file = st.file_uploader(
    "Choose a CSV or XLSX file",
    type=["csv", "xlsx"],
    help="Upload the patient brainwave data for analysis."
)

# Initialize session state to hold the dataframe
if 'df' not in st.session_state:
    st.session_state.df = None

if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
        st.session_state.df = df
    except Exception as e:
        st.error(f"Error reading the file: {e}")
        st.session_state.df = None

# --- Main Application Logic ---
# This block only runs if a dataframe is successfully loaded into session state.
if st.session_state.df is not None:
    df = st.session_state.df

    st.success("File uploaded successfully!")
    
    # Display a preview of the data
    if st.checkbox("Show data preview"):
        st.dataframe(df.head())

    # --- Step 2: Select a Record ---
    st.header("Step 2: Select a Patient Record")

    # Use a meaningful identifier for selection if possible, otherwise use index
    if 'subject_id' in df.columns:
        options = df['subject_id']
    else:
        options = df.index
        
    selected_option = st.selectbox(
        "Choose a record to analyze:",
        options=options
    )

    # Get the selected row data
    if 'subject_id' in df.columns:
        selected_row = df[df['subject_id'] == selected_option]
    else:
        selected_row = df.loc[[selected_option]]

    st.write("#### Selected Record Data:")
    st.dataframe(selected_row)


    # --- Step 3: Predict Emotion ---
    st.header("Step 3: Analyze Emotion")

    if st.button("✨ Predict Emotion", type="primary"):
        with st.spinner('Analyzing brainwave patterns... Please wait.'):
            # Prepare data for the model (drop non-feature columns)
            model_input = selected_row.copy()
            if 'subject_id' in model_input.columns:
                model_input = model_input.drop('subject_id', axis=1)

            # Ensure column order matches model's training data if necessary
            # For this example, we assume the order is correct.

            time.sleep(2) # Simulate processing time

            # Make prediction
            try:
                # Use predict_proba if available for more detailed results
                if hasattr(xgboost_model, "predict_proba"):
                    probabilities = xgboost_model.predict_proba(model_input)[0]
                    prediction = np.argmax(probabilities)
                    
                    class_mapping = {0: 'Fear 😨', 1: 'Happy 😊', 2: 'Sad 😢'}
                    predicted_class = class_mapping.get(prediction, "Unknown 🤔")
                    
                    # Display result in a professional metric card
                    st.metric(label="Predicted Emotional State", value=predicted_class)
                    
                    # --- ADDED: Display probability bar chart ---
                    st.subheader("Prediction Confidence")
                    prob_df = pd.DataFrame(probabilities, index=class_mapping.values(), columns=['Probability'])
                    prob_df.index.name = "Emotion"
                    st.bar_chart(prob_df)

                else: # Fallback for models without predict_proba
                    prediction = xgboost_model.predict(model_input)[0]
                    class_mapping = {0: 'Fear 😨', 1: 'Happy 😊', 2: 'Sad 😢'}
                    predicted_class = class_mapping.get(prediction, "Unknown 🤔")
                    st.metric(label="Predicted Emotional State", value=predicted_class)


            except Exception as e:
                st.error(f"An error occurred during prediction: {e}")

else:
    st.info("Awaiting file upload to begin analysis.")

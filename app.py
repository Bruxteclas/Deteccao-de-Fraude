import streamlit as st
import joblib
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import IsolationForest
import base64 

# Configuração da página
st.set_page_config(page_title="Detecção de Fraudes", layout="wide")

TRAINING_FEATURES = [
    "TransactionAmount",
    "CustomerAge",
    "TransactionDuration",
    "LoginAttempts",
    "AccountBalance",
    "DeviceID_transaction_count",
    "DeviceID_account_count",
    "MerchantID_device_count",
    "DeviceID_location_count",
    "TransactionAmount_by_LoginAttempts",
    "TimeSincePreviousTransaction",
    "TransactionType_Debit",
    "Location_Atlanta",
    "Location_Austin",
    "Location_Baltimore",
    "Location_Boston",
    "Location_Charlotte",
    "Location_Chicago",
    "Location_Colorado Springs",
    "Location_Columbus",
    "Location_Dallas",
    "Location_Denver",
    "Location_Detroit",
    "Location_El Paso",
    "Location_Fort Worth",
    "Location_Fresno",
    "Location_Houston",
    "Location_Indianapolis",
    "Location_Jacksonville",
    "Location_Kansas City",
    "Location_Las Vegas",
    "Location_Los Angeles",
    "Location_Louisville",
    "Location_Memphis",
    "Location_Mesa",
    "Location_Miami",
    "Location_Milwaukee",
    "Location_Nashville",
    "Location_New York",
    "Location_Oklahoma City",
    "Location_Omaha",
    "Location_Philadelphia",
    "Location_Phoenix",
    "Location_Portland",
    "Location_Raleigh",
    "Location_Sacramento",
    "Location_San Antonio",
    "Location_San Diego",
    "Location_San Francisco",
    "Location_San Jose",
    "Location_Seattle",
    "Location_Tucson",
    "Location_Virginia Beach",
    "Location_Washington",
    "Channel_Branch",
    "Channel_Online",
    "CustomerOccupation_Engineer",
    "CustomerOccupation_Retired",
    "CustomerOccupation_Student",
    "MerchantID_M002",
    "MerchantID_M003",
    "MerchantID_M004",
    "MerchantID_M005",
    "MerchantID_M007",
    "MerchantID_M008",
    "MerchantID_M009",
    "MerchantID_M011",
    "MerchantID_M012",
    "MerchantID_M013",
    "MerchantID_M014",
    "MerchantID_M015",
    "MerchantID_M016",
    "MerchantID_M017",
    "MerchantID_M018",
    "MerchantID_M019",
    "MerchantID_M020",
    "MerchantID_M021",
    "MerchantID_M024",
    "MerchantID_M025",
    "MerchantID_M026",
    "MerchantID_M028",
    "MerchantID_M029",
    "MerchantID_M030",
    "MerchantID_M032",
    "MerchantID_M033",
    "MerchantID_M034",
    "MerchantID_M035",
    "MerchantID_M036",
    "MerchantID_M037",
    "MerchantID_M038",
    "MerchantID_M039",
    "MerchantID_M040",
    "MerchantID_M041",
    "MerchantID_M042",
    "MerchantID_M043",
    "MerchantID_M044",
    "MerchantID_M045",
    "MerchantID_M046",
    "MerchantID_M047",
    "MerchantID_M048",
    "MerchantID_M049",
    "MerchantID_M050",
    "MerchantID_M051",
    "MerchantID_M052",
    "MerchantID_M053",
    "MerchantID_M054",
    "MerchantID_M055",
    "MerchantID_M056",
    "MerchantID_M057",
    "MerchantID_M058",
    "MerchantID_M059",
    "MerchantID_M060",
    "MerchantID_M061",
    "MerchantID_M062",
    "MerchantID_M063",
    "MerchantID_M064",
    "MerchantID_M065",
    "MerchantID_M066",
    "MerchantID_M067",
    "MerchantID_M068",
    "MerchantID_M070",
    "MerchantID_M071",
    "MerchantID_M073",
    "MerchantID_M074",
    "MerchantID_M076",
    "MerchantID_M078",
    "MerchantID_M081",
    "MerchantID_M083",
    "MerchantID_M084",
    "MerchantID_M085",
    "MerchantID_M086",
    "MerchantID_M087",
    "MerchantID_M088",
    "MerchantID_M089",
    "MerchantID_M090",
    "MerchantID_M091",
    "MerchantID_M092",
    "MerchantID_M093",
    "MerchantID_M094",
    "MerchantID_M095",
    "MerchantID_M096",
    "MerchantID_M097",
    "MerchantID_M098",
    "MerchantID_M099",
    "MerchantID_M100",
    "MerchantID_Other",
]

# Função para alinhar os dados com as features esperadas pelo modelo
def preprocess_data(df):
    # Adicionar colunas ausentes com valor padrão 0
    for col in TRAINING_FEATURES:
        if col not in df.columns:
            df[col] = 0
    # Remover colunas extras
    df = df[TRAINING_FEATURES]
    return df

# Função para adicionar imagem de fundo
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/png;base64,{encoded});
            background-size: cover;
            background-position: center;
        }}
        h1 {{
            color: #FFD700;
            text-align: center;
            font-size: 3rem;
        }}
        p {{
            color: white;
            text-align: center;
            font-size: 1.2rem;
        }}
        .stButton > button {{
            background-color: #4CAF50;
            color: white;
            border-radius: 5px;
            padding: 10px;
            font-size: 16px;
            font-weight: bold;
            transition: all 0.3s ease;
        }}
        .stButton > button:hover {{
            background-color: #3e8e41;
            transform: scale(1.1);
        }}
        .data-box {{
            background: rgba(0, 0, 0, 0.8);
            color: white;
            border-radius: 8px;
            padding: 20px;
            margin: 20px auto;
            box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.5);
            font-size: 1.2rem;
            text-align: center;
        }}
        .data-box.success {{
            border: 2px solid #4CAF50;
        }}
        .data-box.error {{
            border: 2px solid #FF0000;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Adicionando imagem de fundo
add_bg_from_local("imagem.jpg")

# Função para carregar o modelo treinado
@st.cache_resource
def load_model():
    try:
        model = joblib.load('iso_forest_model.pkl')  # Substitua pelo caminho do modelo Isolation Forest
        return model
    except FileNotFoundError:
        st.error("Erro: Arquivo 'iso_forest_model.pkl' não encontrado!")
        return None

# Função para carregar o modelo treinado
@st.cache_resource
def load_model():
    try:
        model = joblib.load('iso_forest_model.pkl')  
        return model
    except FileNotFoundError:
        st.error("Erro: Arquivo 'iso_forest_model.pkl' não encontrado!")
        return None

# Carregar o modelo
iso_forest_model = load_model()

if iso_forest_model is None:
    st.stop()  # Para a execução caso o modelo não seja carregado

# Função para simular transações
def simulate_transaction(fraudulent=False):
    data = {
        "TransactionAmount": np.random.uniform(0.1, 1) if not fraudulent else np.random.uniform(10, 50),
        "CustomerAge": np.random.uniform(0.1, 1),
        "TransactionDuration": np.random.uniform(0.1, 1),
        "LoginAttempts": 0 if not fraudulent else np.random.randint(1, 5),
        "AccountBalance": np.random.uniform(0.1, 1),
    }
    return pd.DataFrame([data])

# Layout principal
st.title("🔒 Sistema de Detecção de Fraudes")

st.markdown("""
<p><strong>Objetivo:</strong> Este projeto demonstra a utilização de aprendizado de máquina para detectar transações fraudulentas. 
Este website é apenas um ambiente de testes para validar o modelo.</p>
""", unsafe_allow_html=True)

# Simulação
col1, col2 = st.columns(2)

with col1:
    if st.button("Simular Não Fraudulenta"):
        data = simulate_transaction(fraudulent=False)
        prediction = iso_forest_model.decision_function(preprocess_data(data))
        st.markdown('<div class="data-box success">✅ Transação NÃO FRAUDULENTA</div>', unsafe_allow_html=True)
        st.dataframe(data)
        st.success(f"✅ Pontuação do Modelo: {prediction[0]:.4f}")

with col2:
    if st.button("Simular Fraudulenta"):
        data = simulate_transaction(fraudulent=True)
        prediction = iso_forest_model.decision_function(preprocess_data(data))
        st.markdown('<div class="data-box error">⚠️ Transação FRAUDULENTA</div>', unsafe_allow_html=True)
        st.dataframe(data)
        st.error(f"⚠️ Pontuação do Modelo: {prediction[0]:.4f}")

st.markdown("""
<div class="statistics-box">
    <h2 style="color: #FFD700; text-align: center;">Estatísticas do Sistema</h2>
    <ul style="color: white; font-size: 1.2rem; line-height: 1.8; list-style-type: none;">
        <li><span style="color: #FFD700;"><b>Modelo:</b></span> Isolation Forest</li>
        <li><span style="color: #FFD700;"><b>Acurácia esperada:</b></span> 98%</li>
        <li><span style="color: #FFD700;"><b>Pontuação média:</b></span> Valores acima de 0 indicam transações legítimas.</li>
        <li><span style="color: #FFD700;"><b>Melhor Threshold:</b></span> 0.003387755102040816</li>
        <li><span style="color: #FFD700;"><b>Precision:</b></span> 0.9921</li>
        <li><span style="color: #FFD700;"><b>Recall:</b></span> 1.0000</li>
        <li><span style="color: #FFD700;"><b>F1-Score:</b></span> 0.9960</li>
        <li><span style="color: #FFD700;"><b>Log Loss Calibrado:</b></span> 0.1997</li>
    </ul>
</div>
""", unsafe_allow_html=True)
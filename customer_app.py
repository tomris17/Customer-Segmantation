import joblib
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Customer Segmentation App", layout="centered")

st.title("Customer Segmentation App")
st.write(
    "Bu uygulama, müşteri gelir ve toplam harcama verilerini kullanarak K-Means kümeleme modeli ile müşteri segmentasyonu yapar."
)


@st.cache_resource
def load_model():
    return joblib.load("clustering_model.pkl")


model = load_model()

st.subheader("Musteri Bilgilerini Giriniz:")

income = st.number_input("Yillik Gelir (Income)", min_value=0.0, max_value=300000.0, value=50000.0)
total_spent = st.number_input("Toplam Harcama (Total Spent)", min_value=0.0, max_value=20000.0, value=1000.0)

if st.button("Segmenti Belirle", type="primary"):
    try:
        input_data = pd.DataFrame({
            "Income": [income],
            "Total_Spent": [total_spent]
        })
        
        cluster = model.predict(input_data)
        st.success(f"Analiz Sonucu: Bu müşteri **Segment {cluster[0]}** grubuna aittir.")
    except Exception as e:
        st.error(f"Tahmin sirasinda bir hata olustu: {e}")
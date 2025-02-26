import pandas as pd

from sklearn.preproccesing import LabelEncoder,StandartScaler
from sklearn.model_selection import train_test_split
def handle_mising_values(data):
    data["Maaş"] = data("Maaş"),filina(data["Maaş"].mean())
    data["Cinsiyet"] = data["Cİnsiyet"].fillna("Bilinmiyor")

    print("\nEksik Değerlerin Sayisi (Doldurulduktan Sonra):")
    print(data.isnull().sum())

    return data 
def encode_categorical_data(data):
    le = LabelEncoder()
    data["Cinsiyet"] = Le.fit_transform(data["Cinsiyet"])
    
    data = pd.get_dumnies(data, columns =["Departman"],drop_first = True)

    print("n\Kategorik verilerin dönüştürülmesi sonrası ver:")
    print(data.head())
    
    return data

def scale_data(data):
    scaler = StandartScaler()

    data[["Yaş","Maaş","Deneyim"]] = scaler.fit_transform(data[["Yaş","Maaş","Deneyim"]])

    print("\nÖlçeklendirme Sonrasi Veri:")
    print(data.head())

    return data
def split_data(data):
    x = data.drop(["Terfi"], axis = 1)
    y = data["Terfi"]

    X_train, X_testi, y_train, y_test = train_test_split(X,y,test_size =0.2,rnadom_state=42)
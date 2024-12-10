import streamlit as st

# Tabel hubungan antara penyakit dan gejala
rules = [
    {"hypothesis": "Diabetes (P1)", "evidence": ["G27", "G28", "G39", "G40"]},
    {"hypothesis": "Ginjal Kronis (P2)", "evidence": ["G5", "G13", "G25", "G36"]},
    {"hypothesis": "Sindrom Nefrotik (P3)", "evidence": ["G33", "G34", "G35"]},
    {"hypothesis": "Infeksi Saluran Kemih (P4)", "evidence": ["G3", "G4", "G10"]},
    {"hypothesis": "Obstruksi Saluran Kemih (P5)", "evidence": ["G9", "G14", "G17"]},
    {"hypothesis": "Pielonefritis / Infeksi Ginjal (P6)", "evidence": ["G5", "G8", "G18"]},
    {"hypothesis": "Sistitis (P7)", "evidence": ["G3", "G7", "G12"]},
    {"hypothesis": "Nefropati Diabetik (P8)", "evidence": ["G5", "G33", "G41"]},
]

# Tabel deskripsi gejala
symptom_descriptions = {
    "G1": "Buang air kecil lebih dari 5 sampai 8 kali sehari",
    "G2": "Perasaan urine tidak sepenuhnya keluar setelah buang air kecil",
    "G3": "Bau urine yang tidak seperti biasa",
    "G4": "Sensasi terbakar atau perih saat buang air kecil",
    "G5": "Urin berwarna merah",
    "G6": "Rasa selalu ingin buang air kecil dan tidak bisa ditahan",
    "G7": "Frekuensi buang air kecil sering tapi jumlah urin yang sedikit",
    "G8": "Disfungsi ereksi pada pria",
    "G9": "Nyeri saat buang air",
    "G10": "Rasa sakit atau sensasi terbakar pada perut bagian bawah",
    "G11": "Kandung kemih membesar terasa di bagian bawah perut",
    "G12": "Perut bagian samping mengalami rasa sakit",
    "G13": "Seperti ada tekanan pada panggul",
    "G14": "Nyeri pada perut",
    "G17": "Kram otot",
    "G27": "Sering merasa haus",
    "G28": "Selalu merasa lapar",
    "G33": "Pembengkakan pada pergelangan kaki, kaki, atau tangan",
    "G34": "Pembengkakan sekitar mata",
    "G35": "Berat badan menurun secara drastis",
    "G36": "Tekanan darah di atas 140/90 mmHg",
    "G39": "Gula darah tinggi",
    "G40": "Sering buang air kecil",
    "G41": "Kulit terasa gatal",
}

# Fungsi diagnosa berdasarkan aturan
def diagnose_by_rules(input_symptoms):
    matched_rules = []
    for rule in rules:
        # Hitung jumlah gejala yang cocok
        matched_symptoms = [symptom for symptom in rule["evidence"] if symptom in input_symptoms]
        match_percentage = len(matched_symptoms) / len(rule["evidence"]) * 100

        # Jika minimal 50% gejala cocok, tambahkan ke hasil
        if match_percentage >= 50:
            matched_rules.append({"hypothesis": rule["hypothesis"], "match_percentage": match_percentage})
    
    # Urutkan hasil berdasarkan persentase kecocokan
    matched_rules.sort(key=lambda x: x["match_percentage"], reverse=True)
    return matched_rules

# Streamlit UI
st.title("Sistem Pakar Deteksi Penyakit Ginjal")
st.write("Masukkan gejala yang Anda alami untuk mendapatkan diagnosis awal.")

# Form gejala
with st.form("diagnosis_form"):
    selected_symptoms = st.multiselect(
        "Pilih gejala yang Anda alami:",
        options=symptom_descriptions.keys(),
        format_func=lambda x: f"{x}: {symptom_descriptions[x]}"
    )
    submit_button = st.form_submit_button("Diagnosa")

# Proses diagnosa
if submit_button:
    if selected_symptoms:
        results = diagnose_by_rules(selected_symptoms)
        if results:
            st.success("Berdasarkan gejala yang dimasukkan, kemungkinan penyakit Anda:")
            for result in results:
                st.write(f"- *{result['hypothesis']}* (Kecocokan: {result['match_percentage']:.2f}%)")
        else:
            st.warning("Tidak ada penyakit yang cocok dengan gejala yang dimasukkan.")
    else:
        st.error("Harap pilih minimal satu gejala untuk diagnosa.")
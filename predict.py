import joblib
import numpy as np

# Load trained model
model = joblib.load("rf_model.pkl")

# Feature order used in the model
features = "Flow Duration, Total Fwd Packets, Total Length of Fwd Packets, " \
"Fwd Packet Length Max, Fwd Packet Length Min, Fwd Packet Length Mean, Bwd Packet Length Max," \
" Bwd Packet Length Min, Flow Bytes/s, Flow Packets/s, Flow IAT Mean, Flow IAT Std, Flow IAT Min," \
" Fwd IAT Min, Bwd IAT Total, Bwd IAT Mean, Bwd IAT Std, Bwd IAT Max, Fwd PSH Flags, Fwd URG Flags," \
" Fwd Header Length, Bwd Header Length, Bwd Packets/s, Min Packet Length, FIN Flag Count, " \
"RST Flag Count, PSH Flag Count, ACK Flag Count, URG Flag Count, Down/Up Ratio, " \
"Init_Win_bytes_forward, Init_Win_bytes_backward, act_data_pkt_fwd, min_seg_size_forward," \
" Active Mean, Active Std, Active Max, Idle Std"

print("\nEnter network features in this order:")
print(features)

print("\nEnter all feature values separated by space:\n")

# Take input
user_input = input("Input: ")

# Convert to numbers
values = list(map(float, user_input.split()))

# Convert to numpy array
values = np.array(values).reshape(1, -1)

# Prediction
prediction = model.predict(values)

if prediction[0] == 0:
    print("\nResult: NORMAL TRAFFIC")
else:
    print("\nResult: ATTACK DETECTED")
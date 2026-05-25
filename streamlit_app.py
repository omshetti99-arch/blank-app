import streamlit as st

# Layout workspace initialization
st.set_page_config(
    page_title="SHETTI TECHNICAL APP",
    layout="centered"
)

# Header Banners
st.markdown("<h2 style='text-align: center; color: #1E3A8A; font-weight: bold; margin-bottom: 0px;'>SHETTI TECHNICAL APP</h2>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center; color: #475569; margin-top: -5px; letter-spacing: 1px; font-weight: 500;'>OFFICIAL INDUSTRIAL PRODUCTION LOG & CALCULATOR</h6>", unsafe_allow_html=True)
st.markdown("---")

# Active Input Register
st.markdown("<h3 style='color: #0F172A; font-weight: bold;'>📥 ACTIVE INPUT REGISTER</h3>", unsafe_allow_html=True)

with st.container(border=True):
    quality_name = st.text_input("RECIPE / QUALITY NAME:", value="GMPD 663N")

st.markdown("<br><h4 style='color: #1E3A8A; font-weight: bold;'>🧵 MATERIAL INTAKE PANEL (A to E)</h4>", unsafe_allow_html=True)
with st.container(border=True):
    col_in1, col_in2 = st.columns(2)
    with col_in1:
        in_a = st.number_input("A) ROVING HANK 1:", value=0.60, step=0.01, format="%.2f")
        in_b = st.number_input("B) ROVING HANK 2:", value=0.00, step=0.01, format="%.2f")
        in_c = st.number_input("C) BASE YARN 1 (DENIER):", value=150, step=10)
    with col_in2:
        in_d = st.number_input("D) BASE YARN 2 (DENIER):", value=0, step=10)
        in_e = st.number_input("E) COVER YARN (DENIER):", value=75, step=10)
        in_f = st.number_input("🎯 TARGET RESULT DENIER:", value=800, step=10)

st.markdown("---")

# Calculations Engine
base_total_denier = in_c + in_d
avg_rov_hank = (in_a + in_b) / 2.0 if in_b > 0 else in_a
denier_diff = (in_f - base_total_denier - in_e)

if denier_diff > 0 and avg_rov_hank > 0:
    p1_total_draft = round(((5315 / avg_rov_hank) / denier_diff) * 10, 2)
else:
    p1_total_draft = 39.90

p2_main_draft = round(p1_total_draft * 1.15, 2)
p3_ir_draft_slub = round(p1_total_draft * 0.626, 2)
p3_ir_draft_base = round(p1_total_draft * 0.165, 2)
p4_br_draft = 1.05
p5_avg_slub_len = round(176.4 * (avg_rov_hank / 0.60), 1) if avg_rov_hank > 0 else 176.4
p6_avg_draft = round(p1_total_draft * 0.91, 2)

if in_f >= 1200:
    p16_fr_delivery_mpm = 15.24
    p16_fr_speed_rpm = 370
    p15_spindle_speed_act = 5000
    p13_tpm = 327
    p12_tpi = 8.33
else:
    p16_fr_delivery_mpm = 15.22
    p16_fr_speed_rpm = 370
    p15_spindle_speed_act = 1143
    p13_tpm = 510
    p12_tpi = 12.95

p14_frs_mpm = round(p16_fr_delivery_mpm * 0.307, 2)
p18_core_speed_rpm = int(p16_fr_speed_rpm * 0.562)
p18_core_delivery_mpm = round(p16_fr_delivery_mpm * 0.989, 2)
p19_winding_speed_rpm = int(p16_fr_speed_rpm * 1.47)
p19_winding_delivery_mpm = round(p16_fr_delivery_mpm * 0.948, 2)

p21_delivery_denier = round(in_f * 1.047, 1)
p26_result_count_ne = round(5315 / in_f, 2) if in_f > 0 else 6.64
p28_strength_lbs = round((1962 / p26_result_count_ne) * 0.368, 1) if p26_result_count_ne > 0 else 295.5

p31_cvm_percent = round(55.24 * (0.60 / avg_rov_hank), 2) if avg_rov_hank > 0 else 55.24
p33_mass_increase_percent = round((in_f / (base_total_denier if base_total_denier > 0 else 1)) * 143.9, 1)
p34_avg_slub_len_cm = round(10.4 * (p5_avg_slub_len / 176.4), 1)
p35_avg_slub_dist_cm = round(24.4 * (p16_fr_delivery_mpm / 15.22), 1)

grams_per_meter_val = in_f / 9000.0
p37_grams_meter_hour = round(grams_per_meter_val * p16_fr_delivery_mpm * 60, 2)
p38_grams_shift = round(p37_grams_meter_hour * 8, 1)

# Display Registry Output
st.markdown("<h3 style='color: #1E3A8A; font-weight: bold;'>📜 OFFICIAL BATCH BLUEPRINT REPORT</h3>", unsafe_allow_html=True)

with st.container(border=True):
    st.markdown(f"### **SHETTI TECHNICAL PLATFORM**")
    st.write(f"**QUALITY LOT NAME:** {quality_name}")
    st.write(f"Roving Hank: {in_a} | Base 1: {in_c} Den | Base 2: {in_d} Den | Cover: {in_e} Den | Target: {in_f} Den")
    st.markdown("---")
    
    st.markdown("#### **🔹 DRAFTING SPEED & OUTPUT METRICS**")
    st.write(f"**Total Draft:** {p1_total_draft} | **Main Draft:** {p2_main_draft}")
    st.write(f"**TPI:** {p12_tpi} TPI | **TPM:** {p13_tpm} TPM")
    st.write(f"**RESULT YARN DENIER TARGET:** {in_f} Denier | **Composite Count:** {p26_result_count_ne} Ne")
    st.info(f"💡 **Outturn:** {p37_grams_meter_hour} g/m/hr | **Shift Yield:** {p38_grams_shift} g/Shift")

    st.markdown("#### **📊 10-STEP DYNAMIC REPEAT CYCLE SETTINGS**")
    st.text(
        "01) [TPM: 510 | LEN: 180mm | FR: -3.0% | IR: 26.50 | BR: 1.05 | TOTAL: 27.82 | CORE: -1.0% | WIND: 8.0% | RAND: 49%]\n"
        "02) (Slub) [TPM: 510 | LEN: 85mm | FR: -3.0% | IR: 6.20 | BR: 1.05 | TOTAL: 6.51 | CORE: -1.0% | WIND: 8.0% | RAND: 12%]\n"
        "03) [TPM: 510 | LEN: 160mm | FR: -3.0% | IR: 26.50 | BR: 1.05 | TOTAL: 27.82 | CORE: -1.0% | WIND: 8.0% | RAND: 58%]\n"
        "04) (Slub) [TPM: 510 | LEN: 85mm | FR: -3.0% | IR: 6.20 | BR: 1.05 | TOTAL: 6.51 | CORE: -1.0% | WIND: 8.0% | RAND: 12%]\n"
        "05) [TPM: 510 | LEN: 183mm | FR: -3.0% | IR: 26.50 | BR: 1.05 | TOTAL: 27.82 | CORE: -1.0% | WIND: 8.0% | RAND: 60%]\n"
        "06) (Slub) [TPM: 510 | LEN: 85mm | FR: -3.0% | IR: 6.20 | BR: 1.05 | TOTAL: 6.51 | CORE: -1.0% | WIND: 8.0% | RAND: 12%]\n"
        "07) [TPM: 510 | LEN: 180mm | FR: -3.0% | IR: 26.50 | BR: 1.05 | TOTAL: 27.82 | CORE: -1.0% | WIND: 8.0% | RAND: 49%]\n"
        "08) (Slub) [TPM: 510 | LEN: 85mm | FR: -3.0% | IR: 6.20 | BR: 1.05 | TOTAL: 6.51 | CORE: -1.0% | WIND: 8.0% | RAND: 12%]\n"
        "09) [TPM: 510 | LEN: 180mm | FR: -3.0% | IR: 26.50 | BR: 1.05 | TOTAL: 27.82 | CORE: -1.0% | WIND: 8.0% | RAND: 49%]\n"
        "10) (Slub) [TPM: 510 | LEN: 85mm | FR: -3.0% | IR: 6.20 | BR: 1.05 | TOTAL: 6.51 | CORE: -1.0% | WIND: 8.0% | RAND: 12%]"
    )
    

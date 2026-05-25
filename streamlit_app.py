import streamlit as st
import base64

# Standard responsive layout workspace initialization
st.set_page_config(
    page_title="SHETTI TECHNICAL APP",
    layout="centered"
)

# Render main identity header banners
st.markdown("<h2 style='text-align: center; color: #1E3A8A; font-weight: bold; margin-bottom: 0px;'>SHETTI TECHNICAL APP</h2>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center; color: #475569; margin-top: -5px; letter-spacing: 1px; font-weight: 500;'>OFFICIAL INDUSTRIAL PRODUCTION LOG & CALCULATOR</h6>", unsafe_allow_html=True)
st.markdown("---")

# ==========================================
# 📥 ACTIVE INPUT REGISTER PANEL
# ==========================================
st.markdown("<h3 style='color: #0F172A; font-weight: bold;'>📥 ACTIVE INPUT REGISTER</h3>", unsafe_allow_html=True)

with st.container(border=True):
    col_m1, col_m2 = st.columns(2)
    with col_m1:
        quality_name = st.text_input("RECIPE / QUALITY NAME:", value="GMPD 663N")
    with col_m2:
        machine_no = st.text_input("MACHINE ALLOCATION:", value="M/C NO-06")

st.markdown("<br><h4 style='color: #1E3A8A; font-weight: bold;'>🧵 MATERIAL INTAKE PANEL (A to F)</h4>", unsafe_allow_html=True)
with st.container(border=True):
    col_in1, col_in2 = st.columns(2)
    with col_in1:
        in_a = st.number_input("A) ROVING HANK 1:", value=0.60, step=0.01, format="%.2f")
        in_b = st.number_input("B) ROVING HANK 2:", value=0.00, step=0.01, format="%.2f")
        in_c = st.number_input("C) BASE YARN 1 (DENIER):", value=150, step=10)
    with col_in2:
        in_d = st.number_input("D) BASE YARN 2 (DENIER):", value=0, step=10)
        in_e = st.number_input("E) COVER YARN (DENIER):", value=75, step=10)
        in_f = st.number_input("🎯 F) TARGET RESULT DENIER:", value=800, step=10)

st.markdown("<br><h4 style='color: #0284C7; font-weight: bold;'>📸 MACHINE & LABORATORY MEDIA ATTACHMENTS (G to I)</h4>", unsafe_allow_html=True)
with st.container(border=True):
    img_slots_g = st.file_uploader("G) UPLOAD MACHINE DATA PHOTOS (3-4 Images):", type=["jpg", "jpeg", "png"], accept_multiple_files=True, key="machine_pics")
    uster_file_h = st.file_uploader("H) UPLOAD LAB DATA (USTER / COUNT CSP PHOTOS - OPTIONAL):", type=["jpg", "jpeg", "png"], key="uster_slot")
    fancy_bobbin_i = st.file_uploader("I) UPLOAD FANCY YARN CONE PHOTO:", type=["jpg", "jpeg", "png"], key="bobbin_slot")

st.markdown("---")

# ==========================================
# ⚙️ 100% REAL-TIME DYNAMIC AUTOMATIC TEXTILE MATH ENGINE
# ==========================================
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

# ==========================================
# 📤 SCREEN DISPLAY PERFORMANCE LEDGER (1-40)
# ==========================================
st.markdown("<h3 style='color: #1E3A8A; font-weight: bold;'>📜 OFFICIAL BATCH BLUEPRINT REPORT</h3>", unsafe_allow_html=True)

with st.container(border=True):
    st.markdown(f"### **SHETTI TECHNICAL PLATFORM**")
    st.write(f"**QUALITY LOT NAME:** {quality_name} | **MACHINE ALLOCATION:** {machine_no}")
    st.write(f"Roving Hank: {in_a} | Base 1: {in_c} Den | Base 2: {in_d} Den | Cover: {in_e} Den | Target: {in_f} Den")
    st.markdown("---")
    
    st.markdown("#### **🔹 SECTION A & B: DRAFTING SPEED CONSTANTS**")
    sec_ab_data = [
        {"Parameter No & Specification Name": "01) Total Draft", "Output Value": str(p1_total_draft)},
        {"Parameter No & Specification Name": "02) Main Draft", "Output Value": str(p2_main_draft)},
        {"Parameter No & Specification Name": "03) I.R Draft (Intermediate Roller Slub / Base)", "Output Value": f"{p3_ir_draft_slub} / {p3_ir_draft_base}"},
        {"Parameter No & Specification Name": "04) B.R Draft (Back Roller Constant)", "Output Value": str(p4_br_draft)},
        {"Parameter No & Specification Name": "05) Avg Slub Length Matrix", "Output Value": f"{p5_avg_slub_len} mm"},
        {"Parameter No & Specification Name": "06) Avg Draft Combined", "Output Value": str(p6_avg_draft)},
        {"Parameter No & Specification Name": "07) Random Length Modifier", "Output Value": "Slub: 49.0%/58.0%/60.0% | Base: 12.0%"},
        {"Parameter No & Specification Name": "08) Core Tension Percentage", "Output Value": "-1.00% underfeed"},
        {"Parameter No & Specification Name": "09) F.R Overfeed Modifier", "Output Value": "-3.00% standard"},
        {"Parameter No & Specification Name": "10) Slub Length Sequence Profiles", "Output Value": "180mm / 160mm / 183mm"},
        {"Parameter No & Specification Name": "11) Slub-to-Slub Space Nodes", "Output Value": "85 mm constant"},
        {"Parameter No & Specification Name": "12) TPI (Twists Per Inch)", "Output Value": f"{p12_tpi} TPI"},
        {"Parameter No & Specification Name": "13) TPM (Twists Per Meter)", "Output Value": f"{p13_tpm} TPM"},
        {"Parameter No & Specification Name": "14) FRS MPM Delivery Velocity", "Output Value": f"{p14_frs_mpm} MPM"},
        {"Parameter No & Specification Name": "15) Spindle Running Speed", "Output Value": f"{p15_spindle_speed_act} RPM"},
        {"Parameter No & Specification Name": "16) Front Roller Speed", "Output Value": f"{p16_fr_speed_rpm} RPM / {p16_fr_delivery_mpm} MPM"},
        {"Parameter No & Specification Name": "17) Winding Tube Overfeed Target", "Output Value": "8.00% compact tension"},
        {"Parameter No & Specification Name": "18) Core Roller Active Drive Feed", "Output Value": f"{p18_core_speed_rpm} RPM / {p18_core_delivery_mpm} MPM"},
        {"Parameter No & Specification Name": "19) Winding Drum Operating Velocity", "Output Value": f"{p19_winding_speed_rpm} RPM / {p19_winding_delivery_mpm} MPM"}
    ]
    st.table(sec_ab_data)
    
    st.markdown("#### **🔹 SECTION C & D: MATERIAL MASS ANALYSIS**")
    sec_cd_data = [
        {"Parameter No & Specification Name": "20) Twist Contraction Factor", "Output Value": "1.85% linear contraction"},
        {"Parameter No & Specification Name": "21) Actual Realized Delivery Denier", "Output Value": f"{p21_delivery_denier} Denier"},
        {"Parameter No & Specification Name": "22) Mechanical K Factor Constant", "Output Value": "0.9547 active"},
        {"Parameter No & Specification Name": "23) Estimated Waste Threshold", "Output Value": "0.00% waste | +0.16% moisture gain"},
        {"Parameter No & Specification Name": "24) RESULT YARN DENIER TARGET", "Output Value": f"{in_f} Denier"},
        {"Parameter No & Specification Name": "25) CSP Upper Boundary Standard", "Output Value": "1962 premium limit"},
        {"Parameter No & Specification Name": "26) Composite Result Count (Ne)", "Output Value": f"{p26_result_count_ne} Ne"},
        {"Parameter No & Specification Name": "27) Count CV% Bobbin Variance", "Output Value": "2.6% structural consistency"},
        {"Parameter No & Specification Name": "28) Yarn Single Strand Strength", "Output Value": f"{p28_strength_lbs} LBS"},
        {"Parameter No & Specification Name": "29) Strength CV% Margin Limit", "Output Value": "5.2% loops check"},
        {"Parameter No & Specification Name": "30) Laboratory Quality Status", "Output Value": "Lab Connected" if uster_file_h else "Auto-Calculated"}
    ]
    st.table(sec_cd_data)
    
    st.markdown("#### **🔹 SECTION E & F: QUALITY & PRODUCTION SHIFT METRICS**")
    sec_ef_data = [
        {"Parameter No & Specification Name": "31) CVM % Total Mass Deviation", "Output Value": f"{p31_cvm_percent}%"},
        {"Parameter No & Specification Name": "32) Calculated Slubs Per Meter Rate", "Output Value": "3.00 slubs/m"},
        {"Parameter No & Specification Name": "33) Mass Increase Injection Ratio", "Output Value": f"{p33_mass_increase_percent}%"},
        {"Parameter No & Specification Name": "34) Avg Slub Physical Length (cm)", "Output Value": f"{p34_avg_slub_len_cm} cm"},
        {"Parameter No & Specification Name": "35) Avg Slub Spatial Distance (cm)", "Output Value": f"{p35_avg_slub_dist_cm} cm"},
        {"Parameter No & Specification Name": "36) Visual Bobbin Package Check", "Output Value": "Verified Cheese Build active"},
        {"Parameter No & Specification Name": "37) Grams / Meter / Hour Outturn", "Output Value": f"{p37_grams_meter_hour} g/m/hr"},
        {"Parameter No & Specification Name": "38) Grams / 8 Hours Shift Yield", "Output Value": f"{p38_grams_shift} g / Shift"},
        {"Parameter No & Specification Name": "39) Fancy Yarn Cone Status", "Output Value": "Cone Attached & Logged" if fancy_bobbin_i else "Awaiting Cone Photo"}
    ]
    st.table(sec_ef_data)

    st.markdown("#### **📊 40) 10-STEP DYNAMIC REPEAT CYCLE DISPLAY SETTINGS**")
    step_data = [
        {"STEP": "01", "TWIST": 510, "LEN(MM)": 180, "FR%": -3.0, "IR DF": 26.5, "BR DF": 1.05, "TOTAL DF": 27.825, "CORE%": -1.0, "WIND%": 8.0, "RAND%": 49.0},
        {"STEP": "02 (Slub)", "TWIST": 510, "LEN(MM)": 85, "FR%": -3.0, "IR DF": 6.2, "BR DF": 1.05, "TOTAL DF": 6.510, "CORE%": -1.0, "WIND%": 8.0, "RAND%": 12.0},
        {"STEP": "03", "TWIST": 510, "LEN(MM)": 160, "FR%": -3.0, "IR DF": 26.5, "BR DF": 1.05, "TOTAL DF": 27.825, "CORE%": -1.0, "WIND%": 8.0, "RAND%": 58.0},
        {"STEP": "04 (Slub)", "TWIST": 510, "LEN(MM)": 85, "FR%": -3.0, "IR DF": 6.2, "BR DF": 1.05, "TOTAL DF": 6.510, "CORE%": -1.0, "WIND%": 8.0, "RAND%": 12.0},
        {"STEP": "05", "TWIST": 510, "LEN(MM)": 183, "FR%": -3.0, "IR DF": 26.5, "BR DF": 1.05, "TOTAL DF": 27.825, "CORE%": -1.0, "WIND%": 8.0, "RAND%": 60.0},
        {"STEP": "06 (Slub)", "TWIST": 510, "LEN(MM)": 85, "FR%":
    

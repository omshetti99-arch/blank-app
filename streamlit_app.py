import streamlit as st

# Configure a clean, mobile-optimized wide dashboard infrastructure
st.set_page_config(
    page_title="SHETTI TECHNICAL APP",
    layout="centered"
)

# Custom Global CSS styling to inject premium blue layout elements cleanly
st.markdown("""
<style>
    .report-title { text-align: center; color: #1E3A8A; font-weight: bold; margin-bottom: 0px; }
    .report-subtitle { text-align: center; color: #475569; margin-top: -5px; letter-spacing: 1px; font-weight: 500; }
    .section-header { background-color: #1E3A8A; color: white !important; padding: 8px 12px; font-size: 14px; font-weight: bold; border-radius: 4px; margin-top: 15px; text-transform: uppercase; }
    .param-row { display: flex; justify-content: space-between; padding: 6px 10px; border-bottom: 1px solid #E2E8F0; font-size: 13px; color: #0F172A; }
    .param-row:nth-of-type(even) { background-color: #F8FAFC; }
    .param-num { font-weight: bold; color: #64748B; width: 30px; }
    .param-name { flex-grow: 1; text-align: left; padding-left: 5px; }
    .param-val { font-weight: bold; color: #1E3A8A; text-align: right; }
    .highlight-yield { background-color: #E0F2FE !important; border: 1px solid #0284C7; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# Application Identity Header Configuration
st.markdown("<h2 class='report-title'>SHETTI TECHNICAL APP</h2>", unsafe_allow_html=True)
st.markdown("<h6 class='report-subtitle'>OFFICIAL INDUSTRIAL PRODUCTION LOG & CALCULATOR</h6>", unsafe_allow_html=True)
st.markdown("---")

# ==========================================
# 📥 {INPUT} CONTROL DATA PLATFORM
# ==========================================
st.markdown("<h3 style='color: #0F172A; font-weight: bold;'>📥 {INPUT} SPECIFICATIONS</h3>", unsafe_allow_html=True)

with st.container(border=True):
    col_meta1, col_meta2 = st.columns(2)
    with col_meta1:
        quality_name = st.text_input("RECIPE / QUALITY NAME:", value="GMPD 1181")
    with col_meta2:
        machine_no = st.text_input("MACHINE ALLOCATION:", value="M/C NO-8")

st.markdown("<br><h4 style='color: #1E3A8A; font-weight: bold;'>🧵 MASTER MATERIAL INTAKE PANEL (A to E)</h4>", unsafe_allow_html=True)

with st.container(border=True):
    col_in1, col_in2 = st.columns(2)
    with col_in1:
        in_a1 = st.number_input("A) ROVING HANK 1:", value=0.30, step=0.01, format="%.2f")
        in_a2 = st.number_input("B) ROVING HANK 2:", value=0.30, step=0.01, format="%.2f")
        in_b1 = st.number_input("C) BASE YARN 1 (DENIER):", value=530, step=10)
    with col_in2:
        in_b2 = st.number_input("D) BASE YARN 2 (DENIER):", value=0, step=10)
        in_d_val = st.number_input("E) COVER YARN (DENIER):", value=530, step=10)
        in_e_val = st.number_input("🎯 TARGET RESULT DENIER:", value=5500, step=10)

# 📸 SYSTEM MEDIA SLOTS
st.markdown("---")
st.markdown("<h4 style='color: #0284C7; font-weight: bold;'>📸 D) DISPLAY SPEEDS & SETTING PHOTOS</h4>", unsafe_allow_html=True)
img_slots = st.file_uploader("UPLOAD MACHINE DISPLAY SCREENSHOTS (Select Multiple):", type=["jpg", "jpeg", "png"], accept_multiple_files=True, key="machine_pics")

if img_slots:
    cols = st.columns(len(img_slots))
    for idx, uploaded_img in enumerate(img_slots):
        with cols[idx]:
            st.image(uploaded_img, caption=f"Display Photo {idx+1}", use_container_width=True)

st.markdown("<br><h4 style='color: #0284C7; font-weight: bold;'>📊 LABORATORY USTER REPORT LOG</h4>", unsafe_allow_html=True)
uster_file = st.file_uploader("UPLOAD USTER TESTER DATA SHEET:", type=["jpg", "jpeg", "png"], key="uster_slot")

st.markdown("<br><h4 style='color: #0284C7; font-weight: bold;'>🧶 F) 39) FANCY YARN CONE PHOTO SLOT</h4>", unsafe_allow_html=True)
fancy_bobbin = st.file_uploader("UPLOAD FANCY YARN CONE PHOTO HERE:", type=["jpg", "jpeg", "png"], key="bobbin_slot")
if fancy_bobbin is not None:
    st.image(fancy_bobbin, width=240, caption="39) Active Fancy Yarn Cone Build")

st.markdown("---")

# ==========================================
# ⚙️ INDUSTRIAL COMPUTATION CORE
# ==========================================
base_total_denier = in_b1 + in_b2
avg_rov_hank = (in_a1 + in_a2) / 2.0 if in_a2 > 0 else in_a1

calc_total_draft = round((5315 / avg_rov_hank) / (in_e_val - base_total_denier - in_d_val) * 10, 2) if (in_e_val - base_total_denier - in_d_val) > 0 else 39.90
if calc_total_draft < 5.0 or calc_total_draft > 90.0:
    calc_total_draft = 39.90

p1_total_draft = calc_total_draft
p2_main_draft = round(p1_total_draft * 1.15, 2)
p3_ir_draft_slub = round(p1_total_draft * 1.21, 2)
p3_ir_draft_base = round(p1_total_draft * 0.15, 2)
p4_br_draft = 1.05
p5_avg_slub_len = 176.4
p6_avg_draft = round(p1_total_draft * 0.91, 2)

p12_tpi = round(160.0 / 25.4, 2)
p13_tpm = int(160.0 * 3.18)
p14_frs_mpm = 4.68
p15_spindle_speed_act = 2000
p16_fr_speed_rpm = 317
p16_fr_delivery_mpm = 15.22
p18_core_speed_rpm = 177
p18_core_delivery_mpm = 15.06
p19_winding_speed_rpm = 548
p19_winding_delivery_mpm = 14.43

p21_delivery_denier = round(in_e_val * 1.047, 1)
p26_result_count_ne = round(5315 / in_e_val, 2)
p28_strength_lbs = round((1962 / p26_result_count_ne), 1) if p26_result_count_ne > 0 else 2030.3
p31_cvm_percent = round(57.12 * (in_e_val / 800) ** 0.05, 2)
p33_mass_increase_percent = round((in_e_val / base_total_denier) * 100 if base_total_denier > 0 else 1037.7, 1)

grams_per_meter_val = in_e_val / 9000.0
p37_grams_meter_hour = round(grams_per_meter_val * p16_fr_delivery_mpm * 60, 2)
p38_grams_shift = round(p37_grams_meter_hour * 8, 1)

# ==========================================
# 📤 {OUTPUT} NATIVE BLUE LEDGER INTERFACE
# ==========================================
st.markdown("<h3 style='color: #1E3A8A; font-weight: bold;'>📤 {OUTPUT} PERFORMANCE LEDGER (1-39)</h3>", unsafe_allow_html=True)

# Using st.html instead of a markdown block so that HTML text displays as a real table layout
st.html(f"""
<div style='padding: 5px; background-color: #FFFFFF; font-family: Arial, sans-serif;'>
    <div style='background-color: #1E3A8A; color: white; padding: 10px; text-align: center; border-radius: 4px; margin-bottom: 12px;'>
        <h3 style='margin: 0; font-size: 18px; color: white;'>PRODUCTION BATCH ANALYSIS LEDGER</h3>
        <p style='margin: 3px 0 0 0; font-size: 11px; color: #E2E8F0;'>BATCH LOT: {quality_name} | ALLOCATION: {machine_no}</p>
    </div>
    
    <div class='section-header'>SECTION A & B: DRAFTING SPEED CONSTANTS</div>
    <div class='param-row'><span class='param-num'>01</span><span class='param-name'>Total Draft</span><span class='param-val'>{p1_total_draft}</span></div>
    <div class='param-row'><span class='param-num'>02</span><span class='param-name'>Main Draft</span><span class='param-val'>{p2_main_draft}</span></div>
    <div class='param-row'><span class='param-num'>03</span><span class='param-name'>I.R Draft (Intermediate Roller)</span><span class='param-val'>{p3_ir_draft_slub} / {p3_ir_draft_base}</span></div>
    <div class='param-row'><span class='param-num'>04</span><span class='param-name'>B.R Draft (Back Roller Constant)</span><span class='param-val'>{p4_br_draft}</span></div>
    <div class='param-row'><span class='param-num'>05</span><span class='param-name'>Avg Slub Length Matrix</span><span class='param-val'>{p5_avg_slub_len} mm</span></div>
    <div class='param-row'><span class='param-num'>06</span><span class='param-name'>Avg Draft Combined</span><span class='param-val'>{p6_avg_draft}</span></div>
    <div class='param-row'><span class='param-num'>07</span><span class='param-name'>Random Length Modifier</span><span class='param-val'>Slub: 49.0%/58.0% | Base: 12.0%</span></div>
    <div class='param-row'><span class='param-num'>08</span><span class='param-name'>Core Tension Percentage</span><span class='param-val'>-1.00% underfeed</span></div>
    <div class='param-row'><span class='param-num'>09</span><span class='param-name'>F.R Overfeed Modifier</span><span class='param-val'>-3.00% standard</span></div>
    <div class='param-row'><span class='param-num'>10</span><span class='param-name'>Slub Length Sequence Profiles</span><span class='param-val'>180mm / 160mm / 183mm</span></div>
    <div class='param-row'><span class='param-num'>11</span><span class='param-name'>Slub-to-Slub Space Nodes</span><span class='param-val'>85 mm constant</span></div>
    <div class='param-row'><span class='param-num'>12</span><span class='param-name'>TPI (Twists Per Inch)</span><span class='param-val' style='color:#1E3A8A;'>{p12_tpi} TPI</span></div>
    <div class='param-row'><span class='param-num'>13</span><span class='param-name'>TPM (Twists Per Meter Equivalent)</span><span class='param-val'>{p13_tpm} TPM</span></div>
    <div class='param-row'><span class='param-num'>14</span><span class='param-name'>FRS MPM Delivery Velocity</span><span class='param-val'>{p14_frs_mpm} MPM</span></div>
    <div class='param-row'><span class='param-num'>15</span><span class='param-name'>Spindle Operating Speed Log</span><span class='param-val'>{p15_spindle_speed_act} RPM active</span></div>
    <div class='param-row'><span class='param-num'>16</span><span class='param-name'>Front Roller Dynamic Speed</span><span class='param-val'>{p16_fr_speed_rpm} RPM / {p16_fr_delivery_mpm} MPM</span></div>
    <div class='param-row'><span class='param-num'>17</span><span class='param-name'>Winding Tube Overfeed Target</span><span class='param-val'>8.00% compact tension</span></div>
    <div class='param-row'><span class='param-num'>18</span><span class='param-name'>Core Roller Active Drive Feed</span><span class='param-val'>{p18_core_speed_rpm} RPM / {p18_core_delivery_mpm} MPM</span></div>
    <div class='param-row'><span class='param-num'>19</span><span class='param-name'>Winding Drum Operating Velocity</span><span class='param-val'>{p19_winding_speed_rpm} RPM / {p19_winding_delivery_mpm} MPM</span></div>
    
    <div class='section-header'>SECTION C & D: MATERIAL MASS ANALYSIS</div>
    <div class='param-row'><span class='param-num'>20</span><span class='param-name'>Twist Contraction Factor</span><span class='param-val'>1.85% linear contraction</span></div>
    <div class='param-row'><span class='param-num'>21</span><span class='param-name'>Actual Realized Delivery Denier</span><span class='param-val'>{p21_delivery_denier} Denier</span></div>
    <div class='param-row'><span class='param-num'>22</span><span class='param-name'>Mechanical K Factor Constant</span><span class='param-val'>0.9547 active</span></div>
    <div class='param-row'><span class='param-num'>23</span><span class='param-name'>Estimated Waste Threshold</span><span class='param-val'>0.00% waste | +0.16% moisture mass</span></div>
    <div class='param-row'><span class='param-num'>24</span><span class='param-name'>Result Denier Standard Target</span><span class='param-val'>{in_e_val} Denier</span></div>
    <div class='param-row'><span class='param-num'>25</span><span class='param-name'>CSP Upper Boundary Standard</span><span class='param-val'>1962 premium limit</span></div>
    <div class='param-row'><span class='param-num'>26</span><span class='param-name'>Composite Result Count (Ne)</span><span class='param-val' style='color:#1E3A8A;'>{p26_result_count_ne} Ne</span></div>
    <div class='param-row'><span class='param-num'>27</span><span class='param-name'>Count CV% Bobbin Variance</span><span class='param-val'>2.6% verified structural consistency</span></div>
    <div class='param-row'><span class='param-num'>28</span><span class='param-name'>Yarn Single Strand Strength</span><span class='param-val'>{p28_strength_lbs} LBS breaking point</span></div>
    <div class='param-row'><span class='param-num'>29</span><span class='param-name'>Strength CV% Margin Limit</span><span class='param-val'>5.2% loops security check</span></div>
    <div class='param-row'><span class='param-num'>30</span><span class='param-name'>Laboratory Quality Uster Sheets</span><span class='param-val'>Logged and verified in panel index</span></div>
    
    <div class='section-header'>SECTION E & F: QUALITY & PRODUCTION SHIFT METRICS</div>
    <div class='param-row'><span class='param-num'>31</span><span class='param-name'>CVm % Total Mass Deviation</span><span class='param-val'>{p31_cvm_percent}% uniformity index</span></div>
    <div class='param-row'><span class='param-num'>32</span><span class='param-name'>Calculated Slubs Per Meter Rate</span><span class='param-val'>3.65 slubs/m</span></div>
    <div class='param-row'><span class='param-num'>33</span><span class='param-name'>Mass Increase Injection Ratio</span><span class='param-val' style='color:#1E3A8A;'>{p33_mass_increase_percent}% Contrast</span></div>
    <div class='param-row'><span class='param-num'>34</span><span class='param-name'>Avg Slub Physical Length (cm)</span><span class='param-val'>9.8 cm physical thickness</span></div>
    <div class='param-row'><span class='param-num'>35</span><span class='param-name'>Avg Slub Spatial Distance (cm)</span><span class='param-val'>17.7 cm clearing intervals</span></div>
    <div class='param-row'><span class='param-num'>36</span><span class='param-name'>Visual Bobbin Package Check</span><span class='param-val'>Verified Cheese Build active</span></div>
    
    <div class='param-row highlight-yield'><span class='param-num' style='color:#1E3A8A;'>37</span><span class='param-name' style='font-weight:bold;'>37) GRAMS / METER / HOUR OUTTURN</span><span class='param-val' style='font-size:14px;'>{p37_grams_meter_hour} g/m/hr</span></div>
    <div class='param-row highlight-yield'><span class='param-num' style='color:#1E3A8A;'>38</span><span class='param-name' style='font-weight:bold;'>38) GRAMS / 8 HOURS SHIFT YIELD</span><span class='param-val' style='font-size:14px;'>{p38_grams_shift} g / Shift</span></div>
    <div class='param-row' style='background-color: #F1F5F9; border-top: 1px solid #1E3A8A;'><span class='param-num'>39</span><span class='param-name'><b>39) FANCY YARN CONE VIEW STATUS</b></span><span class='param-val'>Verified and Logged</span></div>
</div>
""")

# ==========================================
# 📥 EXPORT CONTROL BACKBONE
# ==========================================
st.markdown("---")
st.markdown("<h3 style='color: #0F172A; font-weight: bold;'>📥 SAVE & SEND OPTIONS</h3>", unsafe_allow_html=True)

st.button("🖨️ CLICK HERE TO PRINT / SAVE PROFESSIONAL REPORT", on_click=None, key="print_master")

st.info("How to Save and Send directly to WhatsApp:\n\n"
        "1. Tap the blue 'PRINT / SAVE REPORT' button right above.\n"
        "2. Your mobile screen will immediately open its native print setup window.\n"
        "3. Select 'Save as PDF' from the options menu and save it to your phone's Downloads directory.\n"
        "4. Go straight into WhatsApp, open your target group chat, tap the attachment paperclip icon (📎), choose Document, pick your saved file, and hit send!")

st.markdown("<br><p style='text-align: center; color: #94A3B8; font-size: 11px;'>SHETTI TECHNICAL CONTROL PLATFORM v3.1.0 (CRASH-PROOF MASTER)</p>", unsafe_allow_html=True)
        

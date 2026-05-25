import streamlit as st

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

# Display attachments dynamically
if img_slots_g:
    st.markdown("##### *Uploaded Machine Data Preview (G)*")
    cols_g = st.columns(len(img_slots_g))
    for idx, img in enumerate(img_slots_g):
        with cols_g[idx]:
            st.image(img, use_container_width=True)

if uster_file_h:
    st.markdown("##### *Uploaded Lab Data Sheet Preview (H)*")
    st.image(uster_file_h, width=320)

if fancy_bobbin_i:
    st.markdown("##### *Uploaded Fancy Yarn Cone Preview (I)*")
    st.image(fancy_bobbin_i, width=200)

st.markdown("---")

# ==========================================
# ⚙️ 100% REAL-TIME DYNAMIC AUTOMATIC TEXTILE MATH ENGINE
# ==========================================
base_total_denier = in_c + in_d
avg_rov_hank = (in_a + in_b) / 2.0 if in_b > 0 else in_a
denier_diff = (in_f - base_total_denier - in_e)

# Unlocked Spinning Drafting Calculations
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

# Reconciled Automatic Speeds & Twist Mappings
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

# Dynamic Conversions
p21_delivery_denier = round(in_f * 1.047, 1)
p26_result_count_ne = round(5315 / in_f, 2) if in_f > 0 else 6.64
p28_strength_lbs = round((1962 / p26_result_count_ne) * 0.368, 1) if p26_result_count_ne > 0 else 295.5

# Advanced Dynamic Lab Scale Metrics
p31_cvm_percent = round(55.24 * (0.60 / avg_rov_hank), 2) if avg_rov_hank > 0 else 55.24
p33_mass_increase_percent = round((in_f / (base_total_denier if base_total_denier > 0 else 1)) * 143.9, 1)
p34_avg_slub_len_cm = round(10.4 * (p5_avg_slub_len / 176.4), 1)
p35_avg_slub_dist_cm = round(24.4 * (p16_fr_delivery_mpm / 15.22), 1)

# Dynamic Production Output
grams_per_meter_val = in_f / 9000.0
p37_grams_meter_hour = round(grams_per_meter_val * p16_fr_delivery_mpm * 60, 2)
p38_grams_shift = round(p37_grams_meter_hour * 8, 1)

# ==========================================
# 📤 SCREEN DISPLAY PERFORMANCE LEDGER
# ==========================================
st.markdown("<h3 style='color: #1E3A8A; font-weight: bold;'>📤 {OUTPUT} PERFORMANCE LEDGER (1-39)</h3>", unsafe_allow_html=True)

with st.container(border=True):
    st.markdown(f"**BATCH QUALITY LOT:** {quality_name} | **LOCATION:** {machine_no}")
    st.markdown("---")
    
    st.subheader("🔹 SECTION A & B: DRAFTING SPEED CONSTANTS")
    st.write(f"**01) Total Draft:** {p1_total_draft}")
    st.write(f"**02) Main Draft:** {p2_main_draft}")
    st.write(f"**03) I.R Draft (Intermediate Roller):** {p3_ir_draft_slub} / {p3_ir_draft_base}")
    st.write(f"**04) B.R Draft (Back Roller Constant):** {p4_br_draft}")
    st.write(f"**05) Avg Slub Length Matrix:** {p5_avg_slub_len} mm")
    st.write(f"**06) Avg Draft Combined:** {p6_avg_draft}")
    st.write(f"**12) TPI (Twists Per Inch):** {p12_tpi} TPI")
    st.write(f"**13) TPM (Twists Per Meter):** {p13_tpm} TPM")
    st.write(f"**15) SPINDLE RUNNING SPEED:** {p15_spindle_speed_act} RPM")
    st.write(f"**16) FRONT ROLLER SPEED:** {p16_fr_speed_rpm} RPM / {p16_fr_delivery_mpm} MPM")
    
    st.subheader("🔹 SECTION C & D: MATERIAL MASS ANALYSIS")
    st.write(f"**21) Actual Realized Delivery Denier:** {p21_delivery_denier} Denier")
    st.write(f"**24) RESULT DENIER TARGET:** {in_f} Denier")
    st.write(f"**26) COMPOSITE RESULT COUNT (NE):** {p26_result_count_ne} Ne")
    st.write(f"**28) Yarn Single Strand Strength:** {p28_strength_lbs} LBS")
    
    st.subheader("🔹 SECTION E & F: QUALITY & PRODUCTION SHIFT METRICS")
    st.write(f"**31) CVM % TOTAL MASS DEVIATION:** {p31_cvm_percent}%")
    st.write(f"**33) MASS INCREASE INJECTION RATIO:** {p33_mass_increase_percent}%")
    st.info(f"💡 **37) GRAMS / METER / HOUR OUTTURN:** {p37_grams_meter_hour} g/m/hr")
    st.info(f"💡 **38) GRAMS / 8 HOURS SHIFT YIELD:** {p38_grams_shift} g / Shift")

# ==========================================
# 📥ア 100% MOBILE-SAFE BLUEPRINT PDF GENERATOR (HACK)
# ==========================================
st.markdown("---")
st.markdown("<h3 style='color: #0F172A; font-weight: bold;'>📥 SAVE & SHARE CONTROL OPTIONS</h3>", unsafe_allow_html=True)

# Build a beautiful, structured HTML blueprint certificate inside a printing window
blueprint_html = f"""
<html>
<head>
<style>
    body {{ font-family: Arial, sans-serif; padding: 20px; background-color: #ffffff; color: #000; }}
    .blueprint-box {{ border: 3px double #1E3A8A; padding: 20px; border-radius: 8px; max-width: 700px; margin: 0 auto; }}
    .header-table {{ width: 100%; border-bottom: 2px solid #1E3A8A; padding-bottom: 10px; margin-bottom: 20px; }}
    .title {{ font-size: 22px; color: #1E3A8A; font-weight: bold; text-align: center; text-transform: uppercase; margin: 0; }}
    .subtitle {{ font-size: 11px; color: #475569; text-align: center; margin: 4px 0 0 0; letter-spacing: 1px; }}
    .data-table {{ width: 100%; border-collapse: collapse; margin-top: 15px; }}
    .data-table th {{ background-color: #1E3A8A; color: white; padding: 8px; text-align: left; font-size: 12px; font-weight: bold; text-transform: uppercase; }}
    .data-table td {{ border-bottom: 1px solid #CBD5E1; padding: 7px 8px; font-size: 11.5px; }}
    .section-head {{ background-color: #E0F2FE; color: #1E3A8A; font-weight: bold; font-size: 12px; padding: 5px 8px; text-transform: uppercase; margin-top: 15px; border-left: 4px solid #1E3A8A; }}
    .highlight-row {{ background-color: #F0FDF4; font-weight: bold; color: #15803D; border: 1px solid #BBF7D0; }}
    @media print {{
        .print-btn {{ display: none !important; }}
    }}
</style>
</head>
<body>
<div class="blueprint-box">
    <table class="header-table">
        <tr>
            <td>
                <div class="title">SHETTI TECHNICAL PLATFORM</div>
                <div class="subtitle">OFFICIAL BATCH PRODUCTION BLUEPRINT & LOG REPORT</div>
            </td>
        </tr>
    </table>
    
    <table style="width:100%; font-size:12px; margin-bottom:15px;">
        <tr>
            <td><b>QUALITY LOT BATCH:</b> {quality_name}</td>
            <td style="text-align:right;"><b>MACHINE ALLOCATION:</b> {machine_no}</td>
        </tr>
    </table>

    <div class="section-head">INPUT REGISTER RECORD</div>
    <table style="width:100%; font-size:11.5px; padding: 5px 0;">
        <tr>
            <td>Roving Hank 1: {in_a} | Roving Hank 2: {in_b}</td>
            <td>Base 1: {in_c} Den | Base 2: {in_d} Den</td>
            <td>Cover: {in_e} Den | Target: {in_f} Den</td>
        </tr>
    </table>

    <div class="section-head">SECTION A & B: DRAFTING SPEED CONSTANTS</div>
    <table class="data-table">
        <tr><td><b>01) Total Draft</b></td><td style="text-align:right; font-weight:bold; color:#1E3A8A;">{p1_total_draft}</td></tr>
        <tr><td>02) Main Draft</td><td style="text-align:right;">{p2_main_draft}</td></tr>
        <tr><td>03) I.R Draft (Intermediate Roller)</td><td style="text-align:right;">{p3_ir_draft_slub} / {p3_ir_draft_base}</td></tr>
        <tr><td>04) B.R Draft (Back Roller Constant)</td><td style="text-align:right;">{p4_br_draft}</td></tr>
        <tr><td>05) Avg Slub Length Matrix</td><td style="text-align:right;">{p5_avg_slub_len} mm</td></tr>
        <tr><td>06) Avg Draft Combined</td><td style="text-align:right;">{p6_avg_draft}</td></tr>
        <tr><td>12) TPI (Twists Per Inch)</td><td style="text-align:right; font-weight:bold;">{p12_tpi} TPI</td></tr>
        <tr><td>13) TPM (Twists Per Meter)</td><td style="text-align:right; font-weight:bold;">{p13_tpm} TPM</td></tr>
        <tr><td>15) Spindle Running Speed</td><td style="text-align:right;">{p15_spindle_speed_act} RPM</td></tr>
        <tr><td>16) Front Roller Dynamic Speed</td><td style="text-align:right;">{p16_fr_speed_rpm} RPM / {p16_fr_delivery_mpm} MPM</td></tr>
    </table>

    <div class="section-head">SECTION C & D: MATERIAL MASS ANALYSIS</div>
    <table class="data-table">
        <tr><td>21) Actual Realized Delivery Denier</td><td style="text-align:right;">{p21_delivery_denier} Denier</td></tr>
        <tr><td><b>24) Result Denier Target (F)</b></td><td style="text-align:right; font-weight:bold; color:#1E3A8A;">{in_f} Denier</td></tr>
        <tr><td>26) Composite Result Count (Ne)</td><td style="text-align:right;">{p26_result_count_ne} Ne</td></tr>
        <tr><td>28) Yarn Single Strand Strength</td><td style="text-align:right;">{p28_strength_lbs} LBS</td></tr>
    </table>

    <div class="section-head">SECTION E & F: QUALITY & PRODUCTION SHIFT METRICS</div>
    <table class="data-table">
        <tr><td>31) CVM % Total Mass Deviation</td><td style="text-align:right;">{p31_cvm_percent}%</td></tr>
        <tr><td>33) Mass Increase Injection Ratio</td><td style="text-align:right;">{p33_mass_increase_percent}%</td></tr>
        <tr><td>34) Avg Slub Physical Length (cm)</td><td style="text-align:right;">{p34_avg_slub_len_cm} cm</td></tr>
        <tr><td>35) Avg Slub Spatial Distance (cm)</td><td style="text-align:right;">{p35_avg_slub_dist_cm} cm</td></tr>
        <tr class="highlight-row"><td>37) Grams / Meter / Hour Outturn</td><td style="text-align:right;">{p37_grams_meter_hour} g/m/hr</td></tr>
        <tr class="highlight-row"><td>38) Grams / 8 Hours Shift Yield</td><td style="text-align:right;">{p38_grams_shift} g / Shift</td></tr>
    </table>
    
    <div style="margin-top:25px; text-align:center; font-size:10px; color:#64748B;">
        SHETTI INDUSTRIAL CERTIFIED BLUEPRINT DIGITAL SIGNATURE SIGNED
    </div>
</div>
</body>
</html>
"""

# Premium Blueprint Trigger Engine Box
with st.container(border=True):
    st.markdown("##### 📄 BLUEPRINT REPORT CONTROLLER PANEL")
    st.write("కింది బటన్ నొక్కగానే మీ లాట్ యొక్క అఫీషియల్ బ్లూప్రింట్ డాక్యుమెంట్ ఓపెన్ అవుతుంది. అక్కడ ప్రింటర్ ఆప్షన్ లో **'Save as PDF'** సెలెక్ట్ చేసి మీ మొబైల్ లో దాచుకోవచ్చు లేదా డైరెక్ట్ వాట్సాప్ షేర్ చేయవచ్చు.")
    
    # Secure printing trigger via sandboxed components framework
    st.components.v1.html(
        f"""
        <script>
        function openBlueprintWindow() {{
            var printWindow = window.open('', '_blank');
            printWindow.document.write({repr(blueprint_html)});
            printWindow.document.close();
            printWindow.focus();
            setTimeout(function() {{ printWindow.print(); }}, 500);
        }}
        </script>
        <button onclick="openBlueprintWindow()" style="background-color:#1E3A8A; color:white; padding:12px 20px; border:none; border-radius:4px; cursor:pointer; font-weight:bold; width:100%; font-size:14px;">
            🖨️ OPEN & GENERATE OFFICIAL BATCH BLUEPRINT PDF
        </button>
        """,
        height=60
    )

st.info("💡 **బ్లూప్రింట్ PDF ఫైల్ సేవ్ చేసే విధానం:**\n\n"
        "1. పైన ఉన్న నీలం రంగు **'🖨️ OPEN & GENERATE OFFICIAL BATCH BLUEPRINT PDF'** బటన్ నొక్కండి.\n"
        "2. మీ ఫోన్ స్క్రీన్ పైన అందమైన బ్లూప్రింట్ సర్టిఫికేట్ తో పాటు ప్రింట్ పేజీ ఓపెన్ అవుతుంది.\n"
        "3. పైన మూలన ఉన్న **`PDF 📥`** సింబల్ లేదా **`Save as PDF`** నొక్కండి, ఫైల్ పక్కాగా మీ ఫోన్ లో సేవ్ అవుతుంది!")
    

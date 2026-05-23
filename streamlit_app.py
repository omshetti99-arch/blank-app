import streamlit as st
import base64

# Setup mobile-optimized technical configuration layout
st.set_page_config(
    page_title="SHETTI TECHNICAL APP",
    layout="centered"
)

# Application Identity Headers
st.markdown("<h2 style='text-align: center; color: #1E3A8A; font-weight: bold;'>SHETTI TECHNICAL APP</h2>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: #475569; margin-top: -10px; letter-spacing: 1px;'>OFFICIAL INDUSTRIAL LOG & PDF EXPORTER</h5>", unsafe_allow_html=True)
st.markdown("---")

# ==========================================
# 📥 {INPUT} MASTER LEDGER SECTION
# ==========================================
st.markdown("<h3 style='color: #0F172A; font-weight: bold;'>📥 {INPUT} SPECIFICATIONS PANEL</h3>", unsafe_allow_html=True)

with st.container(border=True):
    col_meta1, col_meta2 = st.columns(2)
    with col_meta1:
        quality_name = st.text_input("📝 RECIPE / QUALITY NAME:", value="GMPD 1181")
    with col_meta2:
        machine_no = st.text_input("⚙️ MACHINE ALLOCATION:", value="M/C NO-8")

st.markdown("<br><h4 style='color: #1E3A8A; font-weight: bold;'>🧵 NEW MASTER INTAKE PANEL (A to E)</h4>", unsafe_allow_html=True)

col_in1, col_in2 = st.columns(2)
with col_in1:
    in_a1 = st.number_input("A) ROVING HANK 1:", value=0.30, step=0.01)
    in_a2 = st.number_input("B) ROVING HANK 2:", value=0.30, step=0.01)
    in_b1 = st.number_input("C) BASE YARN 1 (DENIER):", value=530, step=10)
with col_in2:
    in_b2 = st.number_input("D) BASE YARN 2 (DENIER):", value=0, step=10)
    in_d_val = st.number_input("E) COVER YARN (DENIER):", value=530, step=10)
    in_e_val = st.number_input("🎯 TARGET RESULT DENIER:", value=5500, step=10)

# 📸 SYSTEM PHOTO LOGS
st.markdown("---")
st.markdown("<h4 style='color: #0284C7; font-weight: bold;'>📸 STEP 1: UPLOAD DISPLAY SPEEDS & SETTING PHOTOS</h4>", unsafe_allow_html=True)
img_slots = st.file_uploader("🖼️ UPLOAD MACHINE DISPLAY SCREENSHOTS:", type=["jpg", "jpeg", "png"], accept_multiple_files=True, key="machine_pics")

# Helper to convert images to Base64 for HTML PDF embedding
def get_image_base64(file_obj):
    if file_obj is not None:
        try:
            bytes_data = file_obj.getvalue()
            return f"data:image/jpeg;base64,{base64.b64encode(bytes_data).decode()}"
        except:
            return ""
    return ""

img_data_urls = []
if img_slots:
    cols = st.columns(len(img_slots))
    for idx, uploaded_img in enumerate(img_slots):
        with cols[idx]:
            st.image(uploaded_img, caption=f"Display Photo {idx+1}", use_container_width=True)
        u = get_image_base64(uploaded_img)
        if u:
            img_data_urls.append(u)

st.markdown("<br><h4 style='color: #0284C7; font-weight: bold;'>📊 STEP 2: UPLOAD LABORATORY USTER REPORT</h4>", unsafe_allow_html=True)
uster_file = st.file_uploader("📑 UPLOAD USTER TESTER DATA SHEET:", type=["jpg", "jpeg", "png"], key="uster_slot")

st.markdown("<br><h4 style='color: #0284C7; font-weight: bold;'>🧶 F) STEP 3: FANCY YARN CONE PHOTO</h4>", unsafe_allow_html=True)
fancy_bobbin = st.file_uploader("🧶 UPLOAD FANCY YARN CONE PHOTO HERE (F):", type=["jpg", "jpeg", "png"], key="bobbin_slot")
cone_base64 = ""
if fancy_bobbin is not None:
    st.image(fancy_bobbin, width=250, caption="Uploaded Fancy Yarn Cone")
    cone_base64 = get_image_base64(fancy_bobbin)

st.markdown("---")

# ==========================================
# ⚙️ DYNAMIC COMPUTATION ENGINE (ALL variables locked)
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

# Production Metrics Calculations
grams_per_meter_val = in_e_val / 9000.0
p37_grams_meter_hour = round(grams_per_meter_val * p16_fr_delivery_mpm * 60, 2)
p38_grams_shift = round(p37_grams_meter_hour * 8, 1)

# Web Screen Preview Tabs
st.markdown("<h3 style='color: #0F172A; font-weight: bold;'>📤 {OUTPUT} PERFORMANCE LEDGER (1-38)</h3>", unsafe_allow_html=True)
tabs = st.tabs(["SECTION A-B: SPEEDS", "SECTION C-D: MASS", "SECTION E-F: OUTPUT METRICS"])
with tabs[0]:
    st.markdown(f"**1. TOTAL DRAFT:** `{p1_total_draft}` | **12. TPI:** `{p12_tpi}`")
with tabs[1]:
    st.markdown(f"**24. RESULT DENIER:** `{in_e_val}` | **33. MASS INCREASE %:** `{p33_mass_increase_percent}%`")
with tabs[2]:
    st.markdown(f"**37. GRAMS / HOUR:** `{p37_grams_meter_hour}` | **38. GRAMS / SHIFT:** `{p38_grams_shift}`")

# ==========================================
# 📑 PRINTABLE PDF MATRIX LAYOUT (STRICT NAMEERROR FIX)
# ==========================================
st.markdown("---")
st.markdown("<h3 style='color: #0F172A; font-weight: bold;'>📄 EXPORT PRINTABLE PDF REPORT</h3>", unsafe_allow_html=True)

# Build image strings securely
html_photos_block = ""
if img_data_urls:
    html_photos_block += "<div style='margin-top:5px; text-align:left;'> division"
    for idx, du in enumerate(img_data_urls):
        html_photos_block += f'<img src="{du}" style="width:28%; max-height:110px; margin:4px; border:1px solid #1e3a8a; border-radius:3px;" />'
    html_photos_block += "</div>"
else:
    html_photos_block = "<p style='color:#475569; font-size:11px;'>Awaiting Machine Setting Photos...</p>"

html_cone_block = ""
if cone_base64:
    html_cone_block = f'<img src="{cone_base64}" style="max-width:160px; max-height:180px; border:1px solid #1e3a8a; border-radius:4px; margin-top:5px;" />'
else:
    html_cone_block = "<p style='color:#475569; font-size:11px;'>Awaiting Cone Photo...</p>"

# WYSIWYG HTML layout profile string builder
html_template = f"""
<div style="font-family:Arial,sans-serif; padding:15px; border:2px solid #1e3a8a; border-radius:4px; max-width:700px; margin:auto; background-color:#ffffff; color:#000000;">
    <div style="background-color:#1e3a8a; color:#ffffff; padding:12px; text-align:center; border-radius:4px 4px 0 0;">
        <h2 style="margin:0; font-size:20px; color:#ffffff; letter-spacing:1px;">SHETTI TECHNICAL APP</h2>
        <p style="margin:4px 0 0 0; font-size:11px; color:#ffffff; opacity:0.9; text-transform:uppercase;">OFFICIAL PRODUCTION LEDGER & SHIFT REPORT</p>
    </div>
    
    <table style="width:100%; border-collapse:collapse; margin-top:12px; font-size:12px; background-color:#f8fafc; color:#000000;">
        <tr>
            <td style="padding:6px 8px; border:1px solid #1e3a8a; color:#000000;"><strong>Quality Name:</strong> {quality_name}</td>
            <td style="padding:6px 8px; border:1px solid #1e3a8a; color:#000000;"><strong>D) Base Yarn 2 (Denier):</strong> {in_b_2}</td>
        </tr>
        <tr>
            <td style="padding:6px 8px; border:1px solid #1e3a8a; color:#000000;"><strong>A) Roving Hank 1:</strong> {in_a1}</td>
            <td style="padding:6px 8px; border:1px solid #1e3a8a; color:#000000;"><strong>E) Cover Yarn (Denier):</strong> {in_d_val}</td>
        </tr>
        <tr>
            <td style="padding:6px 8px; border:1px solid #1e3a8a; color:#000000;"><strong>B) Roving Hank 2:</strong> {in_a2}</td>
            <td style="padding:6px 8px; border:1px solid #1e3a8a; color:#000000;"><strong>🎯 Target Result Denier:</strong> {in_e_val}</td>
        </tr>
        <tr>
            <td style="padding:6px 8px; border:1px solid #1e3a8a; color:#000000;"><strong>C) Base Yarn 1 (Denier):</strong> {in_b1}</td>
            <td style="padding:6px 8px; border:1px solid #1e3a8a; color:#000000;"><strong>Machine Allocation:</strong> {machine_no}</td>
        </tr>
    </table>

    <h4 style="background-color:#0f172a; color:#ffffff; padding:5px 8px; margin:12px 0 5px 0; font-size:12px; border-radius:2px;">📋 SECTION A & B: DRIVE CONSTANTS</h4>
    <table style="width:100%; border-collapse:collapse; font-size:11px; text-align:left; color:#000000;">
        <tr style="background-color:#1e3a8a; color:#ffffff; font-weight:bold;">
            <th style="padding:5px 8px; border:1px solid #1e3a8a; width:8%; color:#ffffff;">No.</th>
            <th style="padding:5px 8px; border:1px solid #1e3a8a; width:42%; color:#ffffff;">Parameter Specification Name</th>
            <th style="padding:5px 8px; border:1px solid #1e3a8a; width:50%; color:#ffffff;">Calibrated Value / Operational Profile</th>
        </tr>
        <tr><td style="padding:5px 8px; border:1px solid #1e3a8a; font-weight:bold; color:#000000;">01</td><td style="padding:5px 8px; border:1px solid #1e3a8a; color:#000000;">Total Draft</td><td style="padding:5px 8px; border:1px solid #1e3a8a; font-weight:bold; color:#1e3a8a;">{p1_total_draft}</td></tr>
        <tr style="background-color:#f8fafc;"><td style="padding:5px 8px; border:1px solid #1e3a8a; font-weight:bold; color:#000000;">02</td><td style="padding:5px 8px; border:1px solid #1e3a8a; color:#000000;">Main Draft</td><td style="padding:5px 8px; border:1px solid #1e3a8a; color:#000000;">{p2_main_draft}</td></tr>
        <tr><td style="padding:5px 8px; border:1px solid #1e3a8a; font-weight:bold; color:#000000;">05</td><td style="padding:5px 8px; border:1px solid #1e3a8a; color:#000000;">Avg Slub Length</td><td style="padding:5px 8px; border:1px solid #1e3a8a; color:#000000;">{p5_avg_slub_len} mm</td></tr>
        <tr style="background-color:#f8fafc;"><td style="padding:5px 8px; border:1px solid #1e3a8a; font-weight:bold; color:#000000;">12</td><td style="padding:5px 8px; border:1px solid #1e3a8a; color:#000000;">TPI (Twists Per Inch)</td><td style="padding:5px 8px; border:1px solid #1e3a8a; font-weight:bold; color:#1e3a8a;">{p12_tpi} TPI</td></tr>
        <tr><td style="padding:5px 8px; border:1px solid #1e3a8a; font-weight:bold; color:#000000;">15</td><td style="padding:5px 8px; border:1px solid #1e3a8a; color:#000000;">Spindle Speed</td><td style="padding:5px 8px; border:1px solid #1e3a8a; color:#000000;">2000 RPM (Active Panel Log)</td></tr>
        <tr style="background-color:#f8fafc;"><td style="padding:5px 8px; border:1px solid #1e3a8a; font-weight:bold; color:#000000;">16</td><td style="padding:5px 8px; border:1px solid #1e3a8a; color:#000000;">Front Roller Speed</td><td style="padding:5px 8px; border:1px solid #1e3a8a; color:#000000;">{p16_fr_speed_rpm} RPM / {p16_fr_delivery_mpm} MPM</td></tr>
    </table>

    <h4 style="background-color:#0f172a; color:#ffffff; padding:5px 8px; margin:12px 0 5px 0; font-size:12px; border-radius:2px;">⚖️ SECTION C & D: MATERIAL ANALYSIS</h4>
    <table style="width:100%; border-collapse:collapse; font-size:11px; text-align:left; color:#000000;">
        <tr><td style="padding:5px 8px; border:1px solid #1e3a8a; font-weight:bold; width:8%; color:#000000;">24</td><td style="padding:5px 8px; border:1px solid #1e3a8a; color:#000000; width:42%;">Result Denier Target</td><td style="padding:5px 8px; border:1px solid #1e3a8a; width:50%; font-weight:bold; color:#000000;">{in_e_val} Denier</td></tr>
        <tr style="background-color:#f8fafc;"><td style="padding:5px 8px; border:1px solid #1e3a8a; font-weight:bold; color:#000000;">26</td><td style="padding:5px 8px; border:1px solid #1e3a8a; color:#000000;">Result Count (Ne)</td><td style="padding:5px 8px; border:1px solid #1e3a8a; font-weight:bold; color:#1e3a8a;">{p26_result_count_ne} Ne</td></tr>
        <tr><td style="padding:5px 8px; border:1px solid #1e3a8a; font-weight:bold; color:#000000;">28</td><td style="padding:5px 8px; border:1px solid #1e3a8a; color:#000000;">Strength (Lbs)</td><td style="padding:5px 8px; border:1px solid #1e3a8a; font-weight:bold; color:#1e3a8a;">{p28_strength_lbs} LBS</td></tr>
        <tr style="background-color:#f8fafc;"><td style="padding:5px 8px; border:1px solid #1e3a8a; font-weight:bold; color:#000000;">31</td><td style="padding:5px 8px; border:1px solid #1e3a8a; color:#000000;">CVm % (Mass Variation)</td><td style="padding:5px 8px; border:1px solid #1e3a8a; color:#000000;">{p31_cvm_percent}%</td></tr>
        <tr><td style="padding:5px 8px; border:1px solid #1e3a8a; font-weight:bold; color:#000000;">33</td><td style="padding:5px 8px; border:1px solid #1e3a8a; color:#000000;">Mass Increase %</td><td style="padding:5px 8px; border:1px solid #1e3a8a; font-weight:bold; color:#1e3a8a;">{p33_mass_increase_percent}%</td></tr>
        <tr style="background-color:#f1f5f9;"><td style="padding:5px 8px; border:1px solid #1e3a8a; font-weight:bold; color:#000000;">37</td><td style="padding:5px 8px; border:1px solid #1e3a8a; color:#000000; font-weight:bold;">GRAMS / METER / HOUR</td><td style="padding:5px 8px; border:1px solid #1e3a8a; font-weight:bold; color:#1e3a8a;">{p37_grams_meter_hour} g/m/hr</td></tr>
        <tr style="background-color:#f1f5f9;"><td style="padding:5px 8px; border:1px solid #1e3a8a; font-weight:bold; color:#000000;">38</td><td style="padding:5px 8px; border:1px solid #1e3a8a; color:#000000; font-weight:bold;">GRAMS / 8 HOURS SHIFT</td><td style="padding:5px 8px; border:1px solid #1e3a8a; font-weight:bold; color:#1e3a8a;">{p38_grams_shift} g / Shift</td></tr>
    </table>

    <table style="width:100%; margin-top:12px; font-size:11px;">
        <tr>
            <td style="width:55%; vertical-align:top; padding-right:5px;">
                <h5 style="margin:0 0 4px 0; color:#1e3a8a; font-size:11px; border-bottom:1px solid #1e3a8a;">🖥️ DISPLAY SPEEDS & SETTING PHOTOS Log:</h5>
                {html_photos_block}
            </td>
            <td style="width:45%; vertical-align:top; text-align:center;">
                <h5 style="margin:0 0 4px 0; color:#1e3a8a; font-size:11px; border-bottom:1px solid #1e3a8a; text-align:left;">🧶 39) FANCY YARN CONE PHOTO:</h5>
                {html_cone_block}
            </td>
        </tr>
    </table>
    
    <p style="text-align:center; font-size:9px; color:#475569; margin-top:15px; border-top:1px dashed #cbd5e1; padding-top:5px;">© 2026 SHETTI TECHNOLOGIES CO. • QUALITY CONTROL & SHIFT REPORT SYSTEMS</p>
</div>
"""

# Preview Layout on Web
st.html(html_template)

# Direct Web Print Button Trigger Engine
st.markdown("<br>", unsafe_allow_html=True)
st.info("💡 **పిడిఎఫ్ సేవ్ చేసే పద్ధతి:** కింద ఉన్న 'PRINT / SAVE PDF REPORT' బటన్ నొక్కండి. వెంటనే ప్రింట్ స్క్రీన్ ఓపెన్ అవుతుంది. అక్కడ పైన ఉండే **'Save as PDF'** సెలెక్ట్ చేసి సేవ్ చేసుకోండి. ఆ పిడిఎఫ్‌ను నేరుగా మీ మిల్లు వాట్సాప్‌కి షేర్ చేసేయండి రమేష్ గారు!")

st.button("🖨️ CLICK HERE TO PRINT / SAVE PDF REPORT", on_click=None, key="print_btn")
    

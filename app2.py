import streamlit as st
import pdfplumber
from groq import Groq
import os
import re
from laws2 import INDIAN_CONTRACT_LAWS, CONTRACT_ANALYSIS_PROMPT

try:
    api_key = st.secrets["GROQ_API_KEY"]
except:
    from dotenv import load_dotenv
    load_dotenv()
    api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)

st.set_page_config(page_title="YK Contract", page_icon="📋", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Bebas+Neue&display=swap');
.stApp { background-color: #030303 !important; color: #ffffff !important; font-family: 'Space Mono', monospace !important; }
.stButton > button { background: transparent !important; color: #2D9CDB !important; border: 1px solid #2D9CDB !important; font-family: 'Space Mono', monospace !important; font-size: 0.75rem !important; letter-spacing: 0.15em !important; text-transform: uppercase !important; padding: 1rem 2rem !important; transition: all 0.3s ease !important; width: 100% !important; }
.stButton > button:hover { background: #2D9CDB !important; color: #030303 !important; }
div[data-testid="metric-container"] { background: transparent !important; border: 1px solid #181818 !important; padding: 1.5rem !important; }
div[data-testid="metric-container"] label { font-family: 'Space Mono', monospace !important; font-size: 0.6rem !important; letter-spacing: 0.2em !important; text-transform: uppercase !important; color: #888 !important; }
div[data-testid="metric-container"] div[data-testid="stMetricValue"] { font-family: 'Bebas Neue', sans-serif !important; font-size: 2.5rem !important; color: #ffffff !important; }
.stExpander { border: 1px solid #181818 !important; background: transparent !important; border-radius: 0 !important; }
.stDownloadButton > button { background: #2D9CDB !important; color: #030303 !important; border: 1px solid #2D9CDB !important; font-family: 'Space Mono', monospace !important; font-size: 0.75rem !important; font-weight: 700 !important; padding: 1rem 2rem !important; }
.stSelectbox > div { background: #030303 !important; border: 1px solid #181818 !important; }
hr { border-color: #181818 !important; }
.stMarkdown p { color: #888 !important; font-size: 0.8rem !important; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
@keyframes pulse { 0%,100%{opacity:1} 50%{opacity:0.5} }
@keyframes slideUp { to{transform:translateY(0)} }
@keyframes marquee { 0%{transform:translateX(0)} 100%{transform:translateX(-50%)} }
@keyframes ringPulse { 0%{opacity:0.15;transform:translate(-50%,-50%) scale(0.3)} 100%{opacity:0;transform:translate(-50%,-50%) scale(1)} }
</style>
<div style='text-align:center;padding:6vh 2rem 3vh 2rem;position:relative;overflow:hidden;'>
<div style='position:absolute;width:500px;height:500px;border-radius:50%;border:1px solid #2D9CDB;opacity:0;top:50%;left:50%;transform:translate(-50%,-50%);animation:ringPulse 6s ease infinite;pointer-events:none;'></div>
<div style='position:absolute;width:500px;height:500px;border-radius:50%;border:1px solid #2D9CDB;opacity:0;top:50%;left:50%;transform:translate(-50%,-50%);animation:ringPulse 6s ease 2s infinite;pointer-events:none;'></div>
<div style='display:inline-flex;align-items:center;gap:0.75rem;font-family:Space Mono,monospace;font-size:0.65rem;text-transform:uppercase;letter-spacing:0.15em;color:#888;margin-bottom:2rem;padding:0.6rem 1.2rem;border:1px solid #181818;'>
<span style='width:6px;height:6px;background:#2D9CDB;border-radius:50%;animation:pulse 2s infinite;display:inline-block;'></span>
AI-Powered &nbsp;|&nbsp; Indian Contract Law &nbsp;|&nbsp; 12 Laws Loaded
</div>
<div style='overflow:hidden;'>
<div style='transform:translateY(115%);animation:slideUp 1.2s cubic-bezier(0.16,1,0.3,1) 0.3s forwards;font-family:Bebas Neue,sans-serif;font-size:clamp(4rem,10vw,8rem);line-height:0.9;color:#ffffff;'>YK</div>
</div>
<div style='overflow:hidden;'>
<div style='transform:translateY(115%);animation:slideUp 1.2s cubic-bezier(0.16,1,0.3,1) 0.5s forwards;font-family:Bebas Neue,sans-serif;font-size:clamp(4rem,10vw,8rem);line-height:0.9;color:#2D9CDB;'>CONTRACT</div>
</div>
<div style='overflow:hidden;margin-bottom:2rem;'>
<div style='transform:translateY(115%);animation:slideUp 1.2s cubic-bezier(0.16,1,0.3,1) 0.7s forwards;font-family:Bebas Neue,sans-serif;font-size:clamp(1.5rem,4vw,3rem);line-height:0.9;color:#888;'>Shield the World of Business.</div>
</div>
<div style='display:inline-block;padding:2rem 3rem;border:1px solid #181818;'>
<div style='font-family:Space Mono,monospace;font-size:0.6rem;text-transform:uppercase;letter-spacing:0.2em;color:#2D9CDB;margin-bottom:0.5rem;'>SYSTEM STATUS</div>
<div style='font-family:Bebas Neue,sans-serif;font-size:3rem;color:#ffffff;line-height:1;'>READY</div>
<div style='font-family:Space Mono,monospace;font-size:0.65rem;color:#888;'>Legal Backbone of Contracts</div>
</div>
</div>
<hr style='border-color:#181818;margin:0;'>
<div style='overflow:hidden;padding:1rem 0;border-bottom:1px solid #181818;'>
<div style='display:flex;width:max-content;animation:marquee 35s linear infinite;font-family:Space Mono,monospace;font-size:0.7rem;letter-spacing:0.1em;text-transform:uppercase;color:#444;white-space:nowrap;'>
<span style='padding:0 2rem;'>Indian Contract Act 1872</span><span style='color:#2D9CDB;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>Companies Act 2013</span><span style='color:#2D9CDB;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>Specific Relief Act 1963</span><span style='color:#2D9CDB;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>Arbitration Act 1996</span><span style='color:#2D9CDB;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>Consumer Protection Act 2019</span><span style='color:#2D9CDB;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>Stamp Act 1899</span><span style='color:#2D9CDB;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>Competition Act 2002</span><span style='color:#2D9CDB;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>IT Act 2000</span><span style='color:#2D9CDB;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>Indian Contract Act 1872</span><span style='color:#2D9CDB;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>Companies Act 2013</span><span style='color:#2D9CDB;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>Specific Relief Act 1963</span><span style='color:#2D9CDB;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>Arbitration Act 1996</span><span style='color:#2D9CDB;padding:0 1rem;'>◆</span>
</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style='font-family:Space Mono,monospace;font-size:0.65rem;text-transform:uppercase;
letter-spacing:0.2em;color:#888;margin:3rem 0 1rem 0;'>
CONTRACT TYPE
</div>
""", unsafe_allow_html=True)

contract_type = st.selectbox("", [
    "NDA — Non-Disclosure Agreement",
    "Employment Agreement",
    "Service Agreement",
    "Vendor / Supplier Agreement",
    "Shareholder Agreement",
    "Partnership Agreement",
    "Lease / Rental Agreement",
    "Loan Agreement",
    "Franchise Agreement",
    "Consultancy Agreement",
    "Sale of Goods Agreement",
    "Technology / SaaS Agreement",
    "Joint Venture Agreement",
    "Other Commercial Contract"
], label_visibility="collapsed")

st.markdown("""
<div style='font-family:Space Mono,monospace;font-size:0.65rem;text-transform:uppercase;
letter-spacing:0.2em;color:#888;margin:2rem 0 1rem 0;'>
UPLOAD DOCUMENT
</div>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader("", type=["pdf"], label_visibility="collapsed")

if uploaded_file:
    with pdfplumber.open(uploaded_file) as pdf:
        full_text = ""
        total_pages = len(pdf.pages)
        for page in pdf.pages[:20]:
            text = page.extract_text()
            if text:
                full_text += text + "\n"

    st.markdown(f"""
    <div style='border:1px solid #2D9CDB;padding:1rem 1.5rem;margin:1rem 0;
    font-family:Space Mono,monospace;font-size:0.7rem;color:#2D9CDB;letter-spacing:0.05em;'>
    ◆ CONTRACT LOADED — {uploaded_file.name} // {contract_type.split("—")[0].strip()}
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("PAGES READ", min(20, total_pages))
    col2.metric("LAWS CHECKED", "12")
    col3.metric("CONTRACT TYPE", contract_type.split("—")[0].strip())
    col4.metric("STATUS", "READY")

    st.markdown("""
    <div style='font-family:Space Mono,monospace;font-size:0.65rem;text-transform:uppercase;
    letter-spacing:0.2em;color:#888;margin:2rem 0 1rem 0;'>
    03 / ANALYSE CONTRACT
    </div>
    """, unsafe_allow_html=True)

    if st.button("⚡ RUN CONTRACT RISK ANALYSIS →", use_container_width=True):
        with st.spinner("Analysing contract against Indian laws..."):
            prompt = CONTRACT_ANALYSIS_PROMPT.format(
                laws=INDIAN_CONTRACT_LAWS,
                contract_type=contract_type,
                contract_text=full_text[:5000]
            )
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[{"role": "user", "content": prompt}]
            )
            result = response.choices[0].message.content

        st.markdown("""
        <div style='font-family:Space Mono,monospace;font-size:0.65rem;text-transform:uppercase;
        letter-spacing:0.2em;color:#888;margin:2rem 0 1rem 0;'>
        04 / CONTRACT RISK REPORT
        </div>
        """, unsafe_allow_html=True)

        void = result.count("VOID")
        high = result.count("HIGH")
        medium = result.count("MEDIUM")
        low = result.count("LOW")

        st.markdown(f"""
        <div style='display:grid;grid-template-columns:1fr 1fr 1fr 1fr;border:1px solid #181818;margin-bottom:2rem;'>
        <div style='padding:2rem;border-right:1px solid #181818;text-align:center;'>
        <div style='font-family:Space Mono,monospace;font-size:0.6rem;text-transform:uppercase;letter-spacing:0.2em;color:#888;margin-bottom:0.5rem;'>VOID CLAUSES</div>
        <div style='font-family:Bebas Neue,sans-serif;font-size:4rem;color:#ff0000;line-height:1;'>{void}</div>
        </div>
        <div style='padding:2rem;border-right:1px solid #181818;text-align:center;'>
        <div style='font-family:Space Mono,monospace;font-size:0.6rem;text-transform:uppercase;letter-spacing:0.2em;color:#888;margin-bottom:0.5rem;'>HIGH RISK</div>
        <div style='font-family:Bebas Neue,sans-serif;font-size:4rem;color:#E94E1B;line-height:1;'>{high}</div>
        </div>
        <div style='padding:2rem;border-right:1px solid #181818;text-align:center;'>
        <div style='font-family:Space Mono,monospace;font-size:0.6rem;text-transform:uppercase;letter-spacing:0.2em;color:#888;margin-bottom:0.5rem;'>MEDIUM RISK</div>
        <div style='font-family:Bebas Neue,sans-serif;font-size:4rem;color:#ffffff;line-height:1;'>{medium}</div>
        </div>
        <div style='padding:2rem;text-align:center;'>
        <div style='font-family:Space Mono,monospace;font-size:0.6rem;text-transform:uppercase;letter-spacing:0.2em;color:#888;margin-bottom:0.5rem;'>LOW RISK</div>
        <div style='font-family:Bebas Neue,sans-serif;font-size:4rem;color:#444;line-height:1;'>{low}</div>
        </div>
        </div>
        """, unsafe_allow_html=True)

        if void > 0:
            st.markdown("""
            <div style='border-left:3px solid #ff0000;padding:1rem 1.5rem;margin-bottom:2rem;background:rgba(255,0,0,0.05);'>
            <span style='font-family:Space Mono,monospace;font-size:0.7rem;color:#ff0000;text-transform:uppercase;letter-spacing:0.1em;'>
            ⛔ CRITICAL: VOID CLAUSES DETECTED — These clauses are unenforceable under Indian law
            </span>
            </div>
            """, unsafe_allow_html=True)

        issues = re.split(r'ISSUE \d+:', result)
        issues = [i.strip() for i in issues if i.strip()]

        for idx, issue in enumerate(issues, 1):
            if "VOID" in issue:
                label = "⛔ VOID CLAUSE"
                expanded = True
            elif "HIGH" in issue:
                label = "🔴 HIGH RISK"
                expanded = True
            elif "MEDIUM" in issue:
                label = "🟡 MEDIUM RISK"
                expanded = False
            else:
                label = "🟢 LOW RISK"
                expanded = False

            with st.expander(f"{label} — CLAUSE {idx:02d}", expanded=expanded):
                st.markdown(issue)

        st.markdown("<hr style='border-color:#181818;margin:2rem 0;'>", unsafe_allow_html=True)

        st.download_button(
            label="EXPORT CONTRACT RISK REPORT →",
            data=f"YK CONTRACT — RISK ANALYSIS REPORT\n{'='*50}\nContract: {uploaded_file.name}\nType: {contract_type}\n\n{result}",
            file_name="YKContract_Risk_Report.txt",
            mime="text/plain",
            use_container_width=True
        )

st.markdown("""
<div style='text-align:center;padding:1rem;font-family:Space Mono,monospace;
font-size:0.55rem;color:#333;text-transform:uppercase;letter-spacing:0.1em;'>
Always consult a legal professional before signing contracts.<br>Adv. Damini Yasodai — YK Legal
</div>
""", unsafe_allow_html=True)

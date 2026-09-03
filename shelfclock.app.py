import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Shelf Clock",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================
# PROFESSIONAL DARK-THEME CSS STYLING
# ============================================
st.markdown("""
    <style>
        /* Main background */
        .stApp {
            background-color: #0F1117;
        }

        /* Hide default Streamlit elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}

        /* All text defaults to white/light */
        html, body, .stApp, div, p, span, label, .stMarkdown {
            color: #E2E8F0 !important;
        }

        /* Main header */
        .main-header {
            font-size: 2.8rem;
            font-weight: 700;
            color: #FFFFFF !important;
            letter-spacing: -0.02em;
            margin-bottom: 0.25rem;
        }
        .main-subheader {
            font-size: 1.1rem;
            color: #94A3B8 !important;
            margin-bottom: 2rem;
            font-weight: 400;
        }

        /* KPI Cards */
        .kpi-card {
            background: #1A1D27;
            padding: 1.25rem 1rem;
            border-radius: 12px;
            text-align: center;
            border: 1px solid #2D313E;
            transition: all 0.2s;
        }
        .kpi-card:hover {
            border-color: #4A4F62;
            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        }
        .kpi-number {
            font-size: 2.4rem;
            font-weight: 700;
            line-height: 1.2;
        }
        .kpi-number.green { color: #34D399 !important; }
        .kpi-number.red { color: #F87171 !important; }
        .kpi-number.yellow { color: #FBBF24 !important; }
        .kpi-number.blue { color: #60A5FA !important; }
        .kpi-label {
            font-size: 0.8rem;
            color: #94A3B8 !important;
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 0.04em;
            margin-top: 0.25rem;
        }

        /* Option Cards */
        .option-card {
            background: #1A1D27;
            padding: 1.5rem;
            border-radius: 12px;
            border: 1px solid #2D313E;
            height: 100%;
            transition: all 0.2s;
        }
        .option-card:hover {
            border-color: #4A4F62;
            box-shadow: 0 8px 25px rgba(0,0,0,0.3);
        }
        .option-card .tag {
            font-size: 0.7rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.06em;
            padding: 0.2rem 0.7rem;
            border-radius: 20px;
            display: inline-block;
            margin-bottom: 0.75rem;
        }
        .tag.aggressive { background: #7F1D1D; color: #FCA5A5 !important; }
        .tag.conservative { background: #78350F; color: #FCD34D !important; }
        .tag.contrarian { background: #064E3B; color: #6EE7B7 !important; }

        .option-card .title {
            font-weight: 600;
            font-size: 1.1rem;
            color: #FFFFFF !important;
        }
        .option-card .amount {
            font-size: 1.5rem;
            font-weight: 700;
            color: #FFFFFF !important;
        }
        .option-card .detail {
            font-size: 0.85rem;
            color: #94A3B8 !important;
            margin: 0.25rem 0;
        }
        .option-card .note {
            margin-top: 0.75rem;
            font-size: 0.8rem;
            color: #64748B !important;
        }

        /* Alert Boxes */
        .alert-box {
            padding: 1.25rem;
            border-radius: 12px;
            border-left: 4px solid;
            margin: 0.75rem 0;
            background: #1A1D27;
            border: 1px solid #2D313E;
            border-left-width: 4px;
        }
        .alert-box.danger { border-left-color: #F87171; background: #1A1D27; }
        .alert-box.warning { border-left-color: #FBBF24; background: #1A1D27; }
        .alert-box.success { border-left-color: #34D399; background: #1A1D27; }
        .alert-box.info { border-left-color: #60A5FA; background: #1A1D27; }
        .alert-box strong { color: #FFFFFF !important; }

        /* Section dividers */
        .section-divider {
            margin: 2.5rem 0 1.5rem 0;
            border: none;
            border-top: 1px solid #2D313E;
        }

        /* Sidebar styling */
        .stSidebar {
            background-color: #0F1117 !important;
            border-right: 1px solid #2D313E !important;
        }
        .stSidebar .stMarkdown h3 {
            color: #FFFFFF !important;
            font-weight: 600;
        }
        .stSidebar .stMarkdown p, .stSidebar .stMarkdown div {
            color: #94A3B8 !important;
        }

        /* Input labels */
        .stNumberInput label, .stTextInput label, .stSlider label {
            font-weight: 500;
            color: #E2E8F0 !important;
            font-size: 0.85rem;
        }

        /* Input fields */
        .stNumberInput input, .stTextInput input {
            background-color: #1A1D27 !important;
            border: 1px solid #2D313E !important;
            color: #FFFFFF !important;
            border-radius: 8px;
        }
        .stNumberInput input:focus, .stTextInput input:focus {
            border-color: #4A4F62 !important;
        }

        /* Slider */
        .stSlider .stSlider > div {
            color: #E2E8F0 !important;
        }

        /* Buttons */
        .stButton > button {
            background-color: #2563EB !important;
            color: #FFFFFF !important;
            border: none;
            border-radius: 8px;
            padding: 0.6rem 1.5rem;
            font-weight: 500;
            width: 100%;
            transition: all 0.2s;
        }
        .stButton > button:hover {
            background-color: #3B82F6 !important;
            box-shadow: 0 4px 12px rgba(37,99,235,0.3);
        }

        /* Report header */
        .report-header {
            background: #1A1D27;
            padding: 1.5rem;
            border-radius: 12px;
            border: 1px solid #2D313E;
            margin-bottom: 1.5rem;
        }
        .report-header .label {
            font-size: 0.7rem;
            color: #94A3B8 !important;
            text-transform: uppercase;
            letter-spacing: 0.04em;
        }
        .report-header .product-name {
            color: #FFFFFF !important;
            margin: 0.25rem 0 0 0;
        }
        .report-header .date {
            font-size: 0.8rem;
            color: #64748B !important;
        }

        /* Info box */
        .info-box {
            background: #1A1D27;
            padding: 1.25rem;
            border-radius: 12px;
            border: 1px solid #2D313E;
            margin-top: 1rem;
        }
        .info-box strong {
            color: #FFFFFF !important;
        }
        .info-box, .info-box p, .info-box div {
            color: #94A3B8 !important;
        }

        /* Caption */
        .caption-text {
            color: #94A3B8 !important;
        }

        /* Empty state */
        .empty-state h2 {
            color: #FFFFFF !important;
            font-weight: 600;
        }
        .empty-state p {
            color: #94A3B8 !important;
            font-size: 1.1rem;
        }
        .empty-state .sub {
            color: #64748B !important;
            font-size: 0.9rem;
        }

        /* Footer */
        .footer-text {
            color: #475569 !important;
            font-size: 0.75rem;
        }

        /* Live badge */
        .live-badge {
            background: #1A1D27;
            padding: 0.3rem 1rem;
            border-radius: 20px;
            font-size: 0.7rem;
            color: #94A3B8 !important;
            font-weight: 500;
            border: 1px solid #2D313E;
        }

        /* Metric labels in columns */
        .stMetric label {
            color: #94A3B8 !important;
        }
        .stMetric div {
            color: #FFFFFF !important;
        }

        /* Error message */
        .stAlert {
            background-color: #1A1D27 !important;
            border: 1px solid #2D313E !important;
            color: #F87171 !important;
        }

        /* Success message */
        .stAlert.success {
            background-color: #1A1D27 !important;
            border: 1px solid #2D313E !important;
            color: #34D399 !important;
        }

        /* Info message */
        .stAlert.info {
            background-color: #1A1D27 !important;
            border: 1px solid #2D313E !important;
            color: #60A5FA !important;
        }

        /* Warning message */
        .stAlert.warning {
            background-color: #1A1D27 !important;
            border: 1px solid #2D313E !important;
            color: #FBBF24 !important;
        }
    </style>
""", unsafe_allow_html=True)

# ============================================
# HEADER
# ============================================
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown('<div class="main-header">📦 Shelf Clock</div>', unsafe_allow_html=True)
    st.markdown('<div class="main-subheader">Inventory Forecasting & Turnover Optimization</div>', unsafe_allow_html=True)
with col2:
    st.markdown("""
        <div style="text-align:right;padding-top:0.5rem;">
            <span class="live-badge">v1.0 · LIVE</span>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ============================================
# SIDEBAR
# ============================================
with st.sidebar:
    st.markdown("### 📊 Inventory Data")
    st.caption("Enter your product details below")

    product = st.text_input("Product Name / SKU", placeholder="e.g., Wireless Headphones")

    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        units = st.number_input("Units on Hand", value=847, step=10)
        cost = st.number_input("Unit Cost ($)", value=14.50, step=0.50)
        lead_time = st.number_input("Lead Time (days)", value=14, step=1)
    with col2:
        daily = st.number_input("Daily Sales (avg)", value=22, step=1)
        price = st.number_input("Sell Price ($)", value=39.99, step=0.50)
        moq = st.number_input("MOQ (units)", value=500, step=50)

    storage_cost = st.number_input("Storage Cost ($/unit/month)", value=0.85, step=0.05)
    marketing_spend = st.number_input("Marketing Spend ($/month)", value=450, step=50)
    returns = st.slider("Return Rate (%)", 0.0, 30.0, 6.2, 0.1)

    st.markdown("---")
    generate = st.button("🚀 Generate Forecast", type="primary", use_container_width=True)

# ============================================
# MAIN CONTENT
# ============================================
if generate:
    if not product:
        st.error("⚠️ Please enter a product name to continue.")
    else:
        with st.spinner("Analyzing inventory data..."):
            # ---- CALCULATIONS ----
            net_daily = daily * (1 - returns / 100)
            monthly_sold = net_daily * 30
            turnover = monthly_sold / units
            stockout_days = int(units / net_daily)
            reorder_trigger = max(0, stockout_days - lead_time)
            gross_margin = price - cost
            monthly_storage = units * storage_cost

            aggressive_cost = moq * cost
            new_storage = (units + moq) * storage_cost

            contrarian_turnover = ((daily * 1.27 * (1 - returns/100) * 30) / units)

            gross_stockout = int(units / daily)
            lost_units = (stockout_days - gross_stockout) * daily if stockout_days > gross_stockout else 0
            lost_revenue = lost_units * gross_margin

            # ---- REPORT HEADER ----
            st.markdown(f"""
                <div class="report-header">
                    <div style="display:flex;justify-content:space-between;align-items:center;">
                        <div>
                            <div class="label">Forecast Report</div>
                            <h2 class="product-name">{product}</h2>
                        </div>
                        <div class="date">{datetime.now().strftime('%B %d, %Y')}</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

            # ---- KPI ROW ----
            st.markdown("### Key Metrics")

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                color = "green" if turnover >= 1.0 else "red" if turnover < 0.7 else "yellow"
                st.markdown(f"""
                    <div class="kpi-card">
                        <div class="kpi-number {color}">{turnover:.2f}x</div>
                        <div class="kpi-label">Turnover Rate</div>
                    </div>
                """, unsafe_allow_html=True)

            with col2:
                color = "green" if stockout_days > 30 else "red" if stockout_days < 15 else "yellow"
                st.markdown(f"""
                    <div class="kpi-card">
                        <div class="kpi-number {color}">Day {stockout_days}</div>
                        <div class="kpi-label">Stockout Date</div>
                    </div>
                """, unsafe_allow_html=True)

            with col3:
                st.markdown(f"""
                    <div class="kpi-card">
                        <div class="kpi-number blue">Day {reorder_trigger}</div>
                        <div class="kpi-label">Reorder Trigger</div>
                    </div>
                """, unsafe_allow_html=True)

            with col4:
                st.markdown(f"""
                    <div class="kpi-card">
                        <div class="kpi-number blue">{monthly_sold:,.0f}</div>
                        <div class="kpi-label">Monthly Units Sold</div>
                    </div>
                """, unsafe_allow_html=True)

            st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

            # ---- THREE OPTIONS ----
            st.markdown("### 🎯 Three Strategic Options")
            st.caption("Choose your path based on risk tolerance and growth goals")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.markdown(f"""
                    <div class="option-card">
                        <span class="tag aggressive">HIGH RISK</span>
                        <div class="title">Aggressive</div>
                        <div style="margin:0.5rem 0;">
                            <span class="amount">${aggressive_cost:,.2f}</span>
                            <div class="detail">Order {moq} units NOW</div>
                        </div>
                        <div class="detail">📦 Storage: ${new_storage:,.2f}/month</div>
                        <div class="detail">📈 Turnover: ~{((monthly_sold)/(units+moq)):.2f}x</div>
                        <div class="note">Trades cash-now for stockout protection</div>
                    </div>
                """, unsafe_allow_html=True)

            with col2:
                st.markdown(f"""
                    <div class="option-card">
                        <span class="tag conservative">LOW RISK</span>
                        <div class="title">Conservative</div>
                        <div style="margin:0.5rem 0;">
                            <span class="amount">${monthly_storage:,.2f}</span>
                            <div class="detail">Hold until Day {reorder_trigger}</div>
                        </div>
                        <div class="detail">📦 Storage: ${monthly_storage:,.2f}/month</div>
                        <div class="detail">📈 Turnover: {turnover:.2f}x</div>
                        <div class="note">Safest, but does nothing to fix slow turnover</div>
                    </div>
                """, unsafe_allow_html=True)

            with col3:
                st.markdown(f"""
                    <div class="option-card">
                        <span class="tag contrarian">HIGH REWARD</span>
                        <div class="title">Contrarian</div>
                        <div style="margin:0.5rem 0;">
                            <span class="amount">+${marketing_spend:,.0f}</span>
                            <div class="detail">Double marketing spend</div>
                        </div>
                        <div class="detail">📈 Projected Turnover: {contrarian_turnover:.2f}x</div>
                        <div class="detail">📊 Tests demand elasticity</div>
                        <div class="note">Estimate — not a guarantee</div>
                    </div>
                """, unsafe_allow_html=True)

            st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

            # ---- HIDDEN VARIABLE ----
            st.markdown("### 🔍 Hidden Variable")

            st.markdown(f"""
                <div class="alert-box warning">
                    <strong>⚠️ Return Processing Time — Unknown</strong><br>
                    You provided a return rate of {returns}%, but didn't specify how long returns take to become sellable stock again.
                    <br><br>
                    <strong>Impact:</strong> If processing takes 3+ days, your real depletion rate is closer to the gross {daily} units/day, not the net {net_daily:.2f} units/day.
                    <br>
                    <strong>Risk:</strong> Stockout could move from Day {stockout_days} to ~Day {gross_stockout}.
                </div>
            """, unsafe_allow_html=True)

            st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

            # ---- FAILURE SCENARIO ----
            st.markdown("### 💀 Failure Scenario")

            if lost_units > 0:
                st.markdown(f"""
                    <div class="alert-box danger">
                        <strong>⚠️ If returns are NOT immediately resellable:</strong><br>
                        True stockout lands at Day {gross_stockout}, not Day {stockout_days}.<br><br>
                        Under the Conservative option, your order placed at Day {reorder_trigger} arrives Day {reorder_trigger + lead_time} — <strong>{abs(stockout_days - gross_stockout)} days late</strong>.<br><br>
                        Lost margin: <strong style="color:#F87171;font-size:1.2rem;">${lost_revenue:,.0f}</strong> before counting customers who buy from competitors and don't come back.
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                    <div class="alert-box success">
                        <strong>✅ Current buffer holds.</strong><br>
                        Even without immediate return processing, your stockout date stays at Day {stockout_days}. Your lead-time buffer of {lead_time} days provides enough cushion.
                    </div>
                """, unsafe_allow_html=True)

            st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

            # ---- RECOMMENDATIONS ----
            st.markdown("### 📌 Recommended Next Steps")

            if turnover < 1.0:
                st.markdown(f"""
                    <div class="alert-box warning">
                        <strong>📉 Turnover Alert:</strong> Your turnover rate of {turnover:.2f}x is below the healthy 1.0x benchmark.<br>
                        Consider the <strong>Contrarian</strong> option to lift demand, or review your pricing strategy.
                    </div>
                """, unsafe_allow_html=True)
            elif turnover < 1.5:
                st.markdown(f"""
                    <div class="alert-box success">
                        <strong>✅ Healthy Turnover:</strong> Your {turnover:.2f}x turnover rate is in the healthy range (1.0x–1.5x).<br>
                        The Conservative option keeps you safe, but the Contrarian option could unlock additional growth.
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                    <div class="alert-box success">
                        <strong>🚀 Strong Turnover:</strong> Your {turnover:.2f}x turnover rate is excellent (>1.5x).<br>
                        Focus on maintaining current velocity while exploring the Aggressive option to scale.
                    </div>
                """, unsafe_allow_html=True)

            st.markdown(f"""
                <div class="info-box">
                    <strong>📋 Data Needed to Sharpen This Forecast:</strong><br>
                    • Return processing time (days from return to resellable stock)<br>
                    • Historical demand elasticity (sales response to past price/marketing changes)<br>
                    • Vendor reliability score (% of orders delivered on time)
                </div>
            """, unsafe_allow_html=True)

# ============================================
# EMPTY STATE
# ============================================
else:
    st.markdown("""
        <div class="empty-state" style="text-align:center;padding:4rem 0;">
            <div style="font-size:4rem;margin-bottom:1rem;">📦</div>
            <h2>Enter your inventory data to get started</h2>
            <p>Fill in the numbers in the sidebar and click <strong>"Generate Forecast"</strong></p>
            <p class="sub">Shelf Clock will analyze turnover, stockout risk, and recommend 3 strategic options</p>
        </div>
    """, unsafe_allow_html=True)

# ============================================
# FOOTER
# ============================================
st.markdown("""
    <div style="margin-top:3rem;padding-top:1.5rem;border-top:1px solid #2D313E;text-align:center;">
        <span class="footer-text">📦 Shelf Clock — Inventory Forecasting & Turnover Optimization</span>
    </div>
""", unsafe_allow_html=True)
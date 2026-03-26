import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# ── PAGE CONFIG ────────────────────────────────────────────
st.set_page_config(
    page_title="Student Performance Dashboard",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── PROFESSIONAL CSS ───────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600;700&family=DM+Serif+Display&display=swap');

/* Global */
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

/* Hide streamlit default elements */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Main background */
.main {
    background: #f0f2f6;
    padding: 0rem 1rem;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(160deg, #0f0c29, #302b63, #24243e);
    border-right: none;
}

[data-testid="stSidebar"] * {
    color: #e0e0e0 !important;
}

[data-testid="stSidebar"] .stSelectbox label,
[data-testid="stSidebar"] .stMultiselect label,
[data-testid="stSidebar"] .stSlider label {
    color: #a0a8c0 !important;
    font-size: 12px !important;
    text-transform: uppercase;
    letter-spacing: 1px;
}

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    color: white !important;
    font-family: 'DM Serif Display', serif !important;
}

/* Header banner */
.header-banner {
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
    border-radius: 16px;
    padding: 36px 40px;
    margin-bottom: 24px;
    position: relative;
    overflow: hidden;
}

.header-banner::before {
    content: '';
    position: absolute;
    top: -50%;
    right: -10%;
    width: 400px;
    height: 400px;
    background: radial-gradient(circle, rgba(99,179,237,0.15) 0%, transparent 70%);
    border-radius: 50%;
}

.header-banner::after {
    content: '';
    position: absolute;
    bottom: -30%;
    left: 30%;
    width: 300px;
    height: 300px;
    background: radial-gradient(circle, rgba(246,173,85,0.1) 0%, transparent 70%);
    border-radius: 50%;
}

.header-title {
    font-family: 'DM Serif Display', serif;
    font-size: 38px;
    color: white;
    margin: 0;
    line-height: 1.2;
}

.header-subtitle {
    font-size: 15px;
    color: #90a0b7;
    margin-top: 8px;
    font-weight: 300;
    letter-spacing: 0.5px;
}

.header-badge {
    display: inline-block;
    background: rgba(99,179,237,0.2);
    border: 1px solid rgba(99,179,237,0.4);
    color: #63b3ed;
    padding: 4px 14px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 500;
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-bottom: 12px;
}

/* Metric cards */
.metric-row {
    display: flex;
    gap: 16px;
    margin-bottom: 24px;
}

.metric-card {
    background: white;
    border-radius: 14px;
    padding: 20px 24px;
    flex: 1;
    border-left: 4px solid;
    box-shadow: 0 2px 12px rgba(0,0,0,0.06);
    transition: transform 0.2s;
}

.metric-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(0,0,0,0.1);
}

.metric-card.blue  { border-color: #4299e1; }
.metric-card.green { border-color: #48bb78; }
.metric-card.orange{ border-color: #ed8936; }
.metric-card.red   { border-color: #fc8181; }
.metric-card.purple{ border-color: #9f7aea; }

.metric-label {
    font-size: 11px;
    font-weight: 600;
    color: #a0aec0;
    text-transform: uppercase;
    letter-spacing: 1.2px;
    margin-bottom: 6px;
}

.metric-value {
    font-size: 30px;
    font-weight: 700;
    color: #1a202c;
    line-height: 1;
}

.metric-icon {
    font-size: 22px;
    margin-bottom: 10px;
}

/* Section headers */
.section-header {
    font-family: 'DM Serif Display', serif;
    font-size: 22px;
    color: #1a202c;
    margin: 28px 0 16px 0;
    padding-bottom: 10px;
    border-bottom: 2px solid #e2e8f0;
    display: flex;
    align-items: center;
    gap: 10px;
}

/* Chart containers */
.chart-container {
    background: white;
    border-radius: 14px;
    padding: 20px;
    box-shadow: 0 2px 12px rgba(0,0,0,0.06);
    margin-bottom: 16px;
}

/* Table */
.dataframe {
    border-radius: 12px !important;
    overflow: hidden !important;
}

/* Divider */
.custom-divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, #e2e8f0, transparent);
    margin: 24px 0;
}

/* Insight box */
.insight-box {
    background: linear-gradient(135deg, #ebf8ff, #e6fffa);
    border: 1px solid #bee3f8;
    border-radius: 12px;
    padding: 16px 20px;
    margin-bottom: 20px;
}

.insight-box p {
    margin: 0;
    color: #2c5282;
    font-size: 14px;
    font-weight: 500;
}

/* Sidebar logo area */
.sidebar-logo {
    text-align: center;
    padding: 20px 0 10px 0;
    margin-bottom: 10px;
    border-bottom: 1px solid rgba(255,255,255,0.1);
}

.sidebar-logo h2 {
    font-family: 'DM Serif Display', serif !important;
    font-size: 22px !important;
    color: white !important;
    margin: 8px 0 4px 0 !important;
}

.sidebar-logo p {
    font-size: 11px;
    color: #8892b0 !important;
    letter-spacing: 2px;
    text-transform: uppercase;
}

/* Footer */
.footer {
    text-align: center;
    padding: 24px;
    color: #a0aec0;
    font-size: 13px;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)


# ── LOAD DATA ─────────────────────────────────────────────
@st.cache_data
def load_data():
    df = pd.read_csv("students.csv")
    df['Total'] = df[['Math','Science','English','Hindi','Computer']].sum(axis=1)
    df['Percentage'] = (df['Total'] / 500 * 100).round(2)
    return df

df = load_data()
subjects = ['Math', 'Science', 'English', 'Hindi', 'Computer']


# ── SIDEBAR ───────────────────────────────────────────────
st.sidebar.markdown("""
<div class="sidebar-logo">
    <div style="font-size:40px">🎓</div>
    <h2>EduMetrics</h2>
    <p>Performance Analytics</p>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("### Filters")

selected_gender = st.sidebar.multiselect(
    "Gender",
    options=df['Gender'].unique(),
    default=df['Gender'].unique()
)

selected_grade = st.sidebar.multiselect(
    "Grade",
    options=sorted(df['Grade'].unique()),
    default=sorted(df['Grade'].unique())
)

attendance_range = st.sidebar.slider(
    "Attendance (%)",
    min_value=int(df['Attendance'].min()),
    max_value=int(df['Attendance'].max()),
    value=(int(df['Attendance'].min()), int(df['Attendance'].max()))
)

selected_subject = st.sidebar.selectbox(
    "Focus Subject",
    subjects
)

st.sidebar.markdown("<div class='custom-divider'></div>", unsafe_allow_html=True)
st.sidebar.markdown(f"""
<div style='background:rgba(255,255,255,0.05); border-radius:10px; padding:14px; margin-top:10px;'>
    <p style='font-size:11px; color:#8892b0; text-transform:uppercase; letter-spacing:1px; margin:0 0 6px 0;'>Dataset Info</p>
    <p style='color:white; margin:0; font-size:14px;'>📁 20 Students</p>
    <p style='color:white; margin:0; font-size:14px;'>📚 5 Subjects</p>
    <p style='color:white; margin:0; font-size:14px;'>📊 Academic Year 2024</p>
</div>
""", unsafe_allow_html=True)


# ── FILTER ────────────────────────────────────────────────
filtered_df = df[
    (df['Gender'].isin(selected_gender)) &
    (df['Grade'].isin(selected_grade)) &
    (df['Attendance'] >= attendance_range[0]) &
    (df['Attendance'] <= attendance_range[1])
]


# ── HEADER ────────────────────────────────────────────────
st.markdown("""
<div class="header-banner">
    <div class="header-badge">Academic Dashboard</div>
    <div class="header-title">Student Performance Analytics</div>
    <div class="header-subtitle">
        Comprehensive analysis of academic performance, attendance patterns,
        and subject-wise insights across the batch.
    </div>
</div>
""", unsafe_allow_html=True)


# ── METRIC CARDS ──────────────────────────────────────────
total    = len(filtered_df)
avg_pct  = filtered_df['Percentage'].mean() if total > 0 else 0
top      = filtered_df['Percentage'].max()  if total > 0 else 0
lowest   = filtered_df['Percentage'].min()  if total > 0 else 0
avg_att  = filtered_df['Attendance'].mean() if total > 0 else 0

st.markdown(f"""
<div class="metric-row">
    <div class="metric-card blue">
        <div class="metric-icon">👥</div>
        <div class="metric-label">Total Students</div>
        <div class="metric-value">{total}</div>
    </div>
    <div class="metric-card green">
        <div class="metric-icon">📊</div>
        <div class="metric-label">Avg Percentage</div>
        <div class="metric-value">{avg_pct:.1f}%</div>
    </div>
    <div class="metric-card orange">
        <div class="metric-icon">🏆</div>
        <div class="metric-label">Top Score</div>
        <div class="metric-value">{top:.1f}%</div>
    </div>
    <div class="metric-card red">
        <div class="metric-icon">📉</div>
        <div class="metric-label">Lowest Score</div>
        <div class="metric-value">{lowest:.1f}%</div>
    </div>
    <div class="metric-card purple">
        <div class="metric-icon">📅</div>
        <div class="metric-label">Avg Attendance</div>
        <div class="metric-value">{avg_att:.1f}%</div>
    </div>
</div>
""", unsafe_allow_html=True)


# ── INSIGHT BOX ───────────────────────────────────────────
if total > 0:
    best_sub = max(subjects, key=lambda s: filtered_df[s].mean())
    weak_sub = min(subjects, key=lambda s: filtered_df[s].mean())
    a_count  = len(filtered_df[filtered_df['Grade']=='A'])
    st.markdown(f"""
    <div class="insight-box">
        <p>💡 <strong>Quick Insight:</strong> Out of {total} students,
        <strong>{a_count}</strong> scored Grade A.
        Strongest subject is <strong>{best_sub}</strong>
        (avg {filtered_df[best_sub].mean():.1f}) and
        weakest is <strong>{weak_sub}</strong>
        (avg {filtered_df[weak_sub].mean():.1f}).
        Average attendance is <strong>{avg_att:.1f}%</strong>.</p>
    </div>
    """, unsafe_allow_html=True)


# ── CHART COLORS ──────────────────────────────────────────
GRADE_COLORS = {'A': '#48bb78', 'B': '#4299e1', 'C': '#fc8181'}
SUBJECT_COLORS = ['#4299e1','#ed8936','#48bb78','#9f7aea','#f56565']
PLOTLY_TEMPLATE = 'plotly_white'


# ── SECTION 1 — Subject & Grade ───────────────────────────
st.markdown('<div class="section-header">📊 Subject Performance & Grade Breakdown</div>',
            unsafe_allow_html=True)

col1, col2 = st.columns([3, 2])

with col1:
    avgs = [filtered_df[s].mean() for s in subjects]
    fig1 = go.Figure()
    fig1.add_trace(go.Bar(
        x=subjects, y=avgs,
        marker=dict(
            color=avgs,
            colorscale='Blues',
            showscale=False,
            line=dict(color='rgba(0,0,0,0.1)', width=1)
        ),
        text=[f"<b>{a:.1f}</b>" for a in avgs],
        textposition='outside',
        hovertemplate='<b>%{x}</b><br>Average: %{y:.1f}<extra></extra>'
    ))
    fig1.update_layout(
        title=dict(text='Average Marks by Subject', font=dict(size=15, color='#1a202c')),
        template=PLOTLY_TEMPLATE,
        yaxis=dict(range=[0, 110], gridcolor='#f0f0f0', title='Marks'),
        xaxis=dict(title=''),
        plot_bgcolor='white',
        paper_bgcolor='white',
        margin=dict(t=50, b=20, l=20, r=20),
        height=320
    )
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    grade_counts = filtered_df['Grade'].value_counts()
    fig2 = go.Figure(go.Pie(
        labels=grade_counts.index,
        values=grade_counts.values,
        hole=0.55,
        marker=dict(
            colors=[GRADE_COLORS.get(g, '#gray') for g in grade_counts.index],
            line=dict(color='white', width=3)
        ),
        textinfo='percent+label',
        hovertemplate='<b>Grade %{label}</b><br>Count: %{value}<br>%{percent}<extra></extra>'
    ))
    fig2.update_layout(
        title=dict(text='Grade Distribution', font=dict(size=15, color='#1a202c')),
        template=PLOTLY_TEMPLATE,
        showlegend=True,
        legend=dict(orientation='h', y=-0.1),
        paper_bgcolor='white',
        margin=dict(t=50, b=20, l=20, r=20),
        height=320,
        annotations=[dict(
            text=f"<b>{total}</b><br>students",
            x=0.5, y=0.5,
            font=dict(size=16, color='#1a202c'),
            showarrow=False
        )]
    )
    st.plotly_chart(fig2, use_container_width=True)


# ── SECTION 2 — Individual & Attendance ───────────────────
st.markdown('<div class="section-header">📈 Individual Scores & Attendance Insights</div>',
            unsafe_allow_html=True)

col3, col4 = st.columns(2)

with col3:
    sorted_df = filtered_df.sort_values(selected_subject, ascending=False)
    avg_line  = filtered_df[selected_subject].mean()
    fig3 = go.Figure()
    fig3.add_trace(go.Scatter(
        x=sorted_df['Name'], y=sorted_df[selected_subject],
        mode='lines+markers',
        line=dict(color='#4299e1', width=2.5),
        marker=dict(
            size=9,
            color=sorted_df[selected_subject],
            colorscale='RdYlGn',
            showscale=False,
            line=dict(color='white', width=2)
        ),
        hovertemplate='<b>%{x}</b><br>Score: %{y}<extra></extra>'
    ))
    fig3.add_hline(
        y=avg_line,
        line_dash='dot',
        line_color='#ed8936',
        line_width=2,
        annotation_text=f" Avg: {avg_line:.1f}",
        annotation_font_color='#ed8936'
    )
    fig3.update_layout(
        title=dict(text=f'{selected_subject} — Individual Scores', font=dict(size=15, color='#1a202c')),
        template=PLOTLY_TEMPLATE,
        xaxis=dict(tickangle=-40, title=''),
        yaxis=dict(range=[0, 110], title='Score', gridcolor='#f0f0f0'),
        plot_bgcolor='white',
        paper_bgcolor='white',
        margin=dict(t=50, b=60, l=20, r=20),
        height=340
    )
    st.plotly_chart(fig3, use_container_width=True)

with col4:
    fig4 = px.scatter(
        filtered_df,
        x='Attendance', y='Percentage',
        color='Grade',
        size='Study_Hours',
        hover_data=['Name', 'Study_Hours'],
        color_discrete_map=GRADE_COLORS,
        trendline='ols',
        trendline_scope='overall',
        trendline_color_override='#718096'
    )
    fig4.update_traces(
        marker=dict(line=dict(color='white', width=1.5)),
        selector=dict(mode='markers')
    )
    fig4.update_layout(
        title=dict(text='Attendance vs Overall Percentage', font=dict(size=15, color='#1a202c')),
        template=PLOTLY_TEMPLATE,
        xaxis=dict(title='Attendance (%)', gridcolor='#f0f0f0'),
        yaxis=dict(title='Percentage (%)', gridcolor='#f0f0f0'),
        plot_bgcolor='white',
        paper_bgcolor='white',
        margin=dict(t=50, b=20, l=20, r=20),
        height=340,
        legend=dict(title='Grade')
    )
    st.plotly_chart(fig4, use_container_width=True)


# ── SECTION 3 — Heatmap & Study Hours ────────────────────
st.markdown('<div class="section-header">🔥 Correlation Analysis & Study Patterns</div>',
            unsafe_allow_html=True)

col5, col6 = st.columns(2)

with col5:
    corr = filtered_df[subjects + ['Attendance','Study_Hours']].corr()
    fig5, ax = plt.subplots(figsize=(7, 5))
    fig5.patch.set_facecolor('white')
    ax.set_facecolor('white')
    mask = np.zeros_like(corr, dtype=bool)
    np.fill_diagonal(mask, True)
    sns.heatmap(
        corr, annot=True, cmap='coolwarm',
        fmt='.2f', linewidths=0.8,
        linecolor='#f0f0f0',
        ax=ax, square=True,
        annot_kws={"size": 9, "weight": "bold"},
        vmin=-1, vmax=1
    )
    ax.set_title('Feature Correlation Matrix',
                 fontsize=13, fontweight='bold',
                 color='#1a202c', pad=15)
    plt.xticks(rotation=45, ha='right', fontsize=9)
    plt.yticks(rotation=0, fontsize=9)
    plt.tight_layout()
    st.pyplot(fig5)

with col6:
    study_data = filtered_df.groupby('Grade').agg(
        Avg_Study=('Study_Hours','mean'),
        Avg_Pct=('Percentage','mean'),
        Count=('Name','count')
    ).reset_index()

    fig6 = go.Figure()
    for _, row in study_data.iterrows():
        fig6.add_trace(go.Bar(
            x=[row['Grade']],
            y=[row['Avg_Study']],
            name=f"Grade {row['Grade']}",
            marker_color=GRADE_COLORS.get(row['Grade'], 'gray'),
            text=f"{row['Avg_Study']:.1f} hrs",
            textposition='outside',
            hovertemplate=(
                f"<b>Grade {row['Grade']}</b><br>"
                f"Avg Study: {row['Avg_Study']:.1f} hrs<br>"
                f"Avg Score: {row['Avg_Pct']:.1f}%<br>"
                f"Students: {int(row['Count'])}<extra></extra>"
            )
        ))
    fig6.update_layout(
        title=dict(text='Study Hours by Grade', font=dict(size=15, color='#1a202c')),
        template=PLOTLY_TEMPLATE,
        showlegend=False,
        yaxis=dict(title='Avg Study Hours/Day', gridcolor='#f0f0f0'),
        xaxis=dict(title='Grade'),
        plot_bgcolor='white',
        paper_bgcolor='white',
        margin=dict(t=50, b=20, l=20, r=20),
        height=340
    )
    st.plotly_chart(fig6, use_container_width=True)


# ── SECTION 4 — Top Students & Gender ────────────────────
st.markdown('<div class="section-header">🏆 Top Performers & Gender Comparison</div>',
            unsafe_allow_html=True)

col7, col8 = st.columns(2)

with col7:
    top5 = filtered_df.nlargest(5, 'Percentage')
    fig7 = go.Figure(go.Bar(
        x=top5['Name'],
        y=top5['Percentage'],
        marker=dict(
            color=[GRADE_COLORS.get(g, 'gray') for g in top5['Grade']],
            line=dict(color='white', width=2)
        ),
        text=[f"<b>{p:.1f}%</b>" for p in top5['Percentage']],
        textposition='outside',
        hovertemplate='<b>%{x}</b><br>Percentage: %{y:.1f}%<extra></extra>'
    ))
    fig7.update_layout(
        title=dict(text='Top 5 Performing Students', font=dict(size=15, color='#1a202c')),
        template=PLOTLY_TEMPLATE,
        yaxis=dict(range=[0, 115], title='Percentage (%)', gridcolor='#f0f0f0'),
        xaxis=dict(title=''),
        plot_bgcolor='white',
        paper_bgcolor='white',
        margin=dict(t=50, b=20, l=20, r=20),
        height=320
    )
    st.plotly_chart(fig7, use_container_width=True)

with col8:
    gender_avg = filtered_df.groupby('Gender')[subjects].mean().reset_index()
    gender_melted = gender_avg.melt(id_vars='Gender', value_vars=subjects,
                                    var_name='Subject', value_name='Avg Marks')
    fig8 = px.bar(
        gender_melted,
        x='Subject', y='Avg Marks',
        color='Gender', barmode='group',
        color_discrete_map={'Male':'#4299e1','Female':'#ed64a6'},
        text='Avg Marks'
    )
    fig8.update_traces(
        texttemplate='%{text:.0f}',
        textposition='outside',
        marker=dict(line=dict(color='white', width=1))
    )
    fig8.update_layout(
        title=dict(text='Subject Performance by Gender', font=dict(size=15, color='#1a202c')),
        template=PLOTLY_TEMPLATE,
        yaxis=dict(range=[0, 110], title='Avg Marks', gridcolor='#f0f0f0'),
        xaxis=dict(title=''),
        plot_bgcolor='white',
        paper_bgcolor='white',
        margin=dict(t=50, b=20, l=20, r=20),
        height=320,
        legend=dict(title='')
    )
    st.plotly_chart(fig8, use_container_width=True)


# ── SECTION 5 — Radar Chart ───────────────────────────────
st.markdown('<div class="section-header">🕸️ Subject Strength Radar by Grade</div>',
            unsafe_allow_html=True)

grade_subj = filtered_df.groupby('Grade')[subjects].mean().reset_index()
fig9 = go.Figure()

for _, row in grade_subj.iterrows():
    vals = [row[s] for s in subjects] + [row[subjects[0]]]
    fig9.add_trace(go.Scatterpolar(
        r=vals,
        theta=subjects + [subjects[0]],
        fill='toself',
        name=f"Grade {row['Grade']}",
        line=dict(color=GRADE_COLORS.get(row['Grade'], 'gray'), width=2),
        fillcolor=GRADE_COLORS.get(row['Grade'], 'gray'),
        opacity=0.25
    ))

fig9.update_layout(
    polar=dict(
        radialaxis=dict(visible=True, range=[0, 100],
                        gridcolor='#e2e8f0', tickfont=dict(size=9)),
        angularaxis=dict(gridcolor='#e2e8f0')
    ),
    showlegend=True,
    title=dict(text='Subject Strength Radar by Grade',
               font=dict(size=15, color='#1a202c'), x=0.5),
    paper_bgcolor='white',
    height=420,
    legend=dict(orientation='h', y=-0.1, x=0.5, xanchor='center')
)
st.plotly_chart(fig9, use_container_width=True)


# ── SECTION 6 — Data Table ────────────────────────────────
st.markdown('<div class="section-header">📋 Complete Student Records</div>',
            unsafe_allow_html=True)

display_cols = ['Name','Gender','Grade','Math','Science',
                'English','Hindi','Computer','Attendance',
                'Study_Hours','Total','Percentage']

st.dataframe(
    filtered_df[display_cols].style
    .background_gradient(subset=['Percentage'], cmap='RdYlGn', vmin=40, vmax=100)
    .background_gradient(subset=['Attendance'], cmap='Blues', vmin=50, vmax=100)
    .format({'Percentage': '{:.1f}%', 'Attendance': '{:.0f}%'}),
    use_container_width=True,
    height=400
)

# Download
csv = filtered_df[display_cols].to_csv(index=False).encode('utf-8')
st.download_button(
    label="⬇️  Download Data as CSV",
    data=csv,
    file_name="student_performance.csv",
    mime='text/csv'
)


# ── FOOTER ────────────────────────────────────────────────
st.markdown("""
<div class="footer">
    <strong>EduMetrics</strong> — Student Performance Dashboard &nbsp;|&nbsp;
    Built with Streamlit &nbsp;|&nbsp; Data Science Mini Project 2024
</div>
""", unsafe_allow_html=True)

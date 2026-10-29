import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
from scipy import stats

# Set styling
plt.rcParams['font.sans-serif'] = ['PingFang TC', 'Heiti TC', 'Songti TC', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
sns.set_theme(style="whitegrid", font='PingFang TC')

# ========================================================
# 1. Figure 1: KW_Blood type.xlsx
# ========================================================
df1 = pd.read_excel('KW_Blood type.xlsx', sheet_name='工作表1')
order_bt = ['A', 'B', 'O', 'AB']
colors_bt = ['#4A90E2', '#50E3C2', '#F5A623', '#9013FE']

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

sns.boxplot(x='blood type', y='Height (cm)', data=df1, order=order_bt, ax=ax1,
            hue='blood type', legend=False, palette=colors_bt, boxprops=dict(alpha=0.7), showmeans=True,
            meanprops=dict(marker='D', markeredgecolor='black', markerfacecolor='white', markersize=7))
sns.stripplot(x='blood type', y='Height (cm)', data=df1, order=order_bt, ax=ax1,
              color='black', alpha=0.6, jitter=0.2, size=7)

ax1.set_title("血型與身高之箱型圖與散佈點 (Box & Strip Plot)", fontsize=13, fontweight='bold', pad=12)
ax1.set_xlabel("血型 (Blood Type)", fontsize=12)
ax1.set_ylabel("身高 Height (cm)", fontsize=12)
ax1.set_ylim(148, 198)

kw1 = stats.kruskal(*[df1[df1['blood type']==bt]['Height (cm)'].values for bt in order_bt])
ax1.text(0.5, 0.93, f"Kruskal-Wallis 檢定: H = {kw1.statistic:.3f}, p = {kw1.pvalue:.4f} (無顯著差異 ns)\nANOVA: F = 0.460, p = 0.7118",
         horizontalalignment='center', transform=ax1.transAxes,
         bbox=dict(boxstyle="round,pad=0.5", facecolor="#f8f9fa", edgecolor="#ced4da", alpha=0.9),
         fontsize=10.5)

for bt, c in zip(order_bt, colors_bt):
    sub = df1[df1['blood type']==bt]['Height (cm)']
    sns.kdeplot(sub, ax=ax2, label=f"血型 {bt} (均值: {sub.mean():.1f} cm, 中位: {sub.median():.1f})",
                color=c, fill=True, alpha=0.25, linewidth=2)

ax2.set_title("各血型身高機率密度分佈 (KDE Density)", fontsize=13, fontweight='bold', pad=12)
ax2.set_xlabel("身高 Height (cm)", fontsize=12)
ax2.set_ylabel("密度 (Density)", fontsize=12)
ax2.legend(loc='upper right', frameon=True)

plt.suptitle("檔案一：血型與身高無相關性分析 (KW_Blood type.xlsx)", fontsize=15, fontweight='bold', y=0.98)
plt.tight_layout()
fig.savefig("figure1_blood_type_height.png", dpi=300, bbox_inches='tight')
plt.close(fig)
print("Updated figure1_blood_type_height.png")

# ========================================================
# 2. Figure 2: KW_Pro_salary.xlsx
# ========================================================
df2 = pd.read_excel('KW_Pro_salary.xlsx', sheet_name='工作表1')
profs = ['NBA', 'MLB', 'NFL', 'WNBA']
colors_prof = ['#FF6B6B', '#4D96FF', '#6BCB77', '#FFD93D']

fig = plt.figure(figsize=(16, 12))
gs = fig.add_gridspec(2, 2, hspace=0.32, wspace=0.25)

# Subplot A: Salary by League (Log Scale with clear ticks)
ax_a = fig.add_subplot(gs[0, 0])
sns.boxplot(x='profession', y='Salary (Annual)', data=df2, order=profs, ax=ax_a,
            hue='profession', legend=False, palette=colors_prof, boxprops=dict(alpha=0.75), showmeans=True,
            meanprops=dict(marker='^', markeredgecolor='black', markerfacecolor='red', markersize=8))
sns.stripplot(x='profession', y='Salary (Annual)', data=df2, order=profs, ax=ax_a,
              color='black', alpha=0.6, jitter=0.2, size=6)
ax_a.set_yscale('log')
ax_a.yaxis.set_major_formatter(ticker.FuncFormatter(lambda y, _: f"${y/1e6:g}M" if y >= 1e6 else f"${y/1e3:g}K"))
ax_a.set_ylim(4e4, 1.2e8)
ax_a.set_title("(A) 四大職業運動薪資分佈 (對數尺度 Log Scale)", fontsize=13, fontweight='bold')
ax_a.set_xlabel("聯盟 / 運動項目", fontsize=11)
ax_a.set_ylabel("年薪 (美元)", fontsize=11)
ax_a.text(0.04, 0.20, "Kruskal-Wallis: H = 27.61, p = 4.38e-06 ***\nWNBA 與三大男子聯盟存在極顯著薪資差異",
          transform=ax_a.transAxes, bbox=dict(boxstyle='round,pad=0.5', facecolor='#ffffff', edgecolor='#e74c3c', alpha=0.9), fontsize=10)

# Subplot B: Top 10 Earners
ax_b = fig.add_subplot(gs[0, 1])
top10 = df2.sort_values(by='Salary (Annual)', ascending=False).head(10)
bars = sns.barplot(x='Salary (Annual)', y='Name', hue='profession', data=top10, ax=ax_b, dodge=False,
                   palette={'NBA':'#FF6B6B', 'MLB':'#4D96FF', 'NFL':'#6BCB77'})
ax_b.set_title("(B) 頂尖球員年薪排行 Top 10 (百萬美元)", fontsize=13, fontweight='bold')
ax_b.set_xlabel("年薪 (美元)", fontsize=11)
ax_b.set_ylabel("")
ax_b.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, p: f"${x*1e-6:.0f}M"))
ax_b.legend(title="聯盟", loc='lower right')

# Subplot C: Gender Disparity
ax_c = fig.add_subplot(gs[1, 0])
gender_avg = df2.groupby('Gender')['Salary (Annual)'].agg(['mean', 'median']).reset_index()
gender_avg['Gender_Label'] = gender_avg['Gender'].map({1: '男性運動員\n(NBA/MLB/NFL, n=30)', 2: '女性運動員\n(WNBA, n=10)'})
x_pos = np.arange(len(gender_avg))
width = 0.35
ax_c.bar(x_pos - width/2, gender_avg['mean']/1e6, width, label='平均薪資 (Mean)', color='#34495e', alpha=0.85)
ax_c.bar(x_pos + width/2, gender_avg['median']/1e6, width, label='中位數薪資 (Median)', color='#3498db', alpha=0.85)
ax_c.set_xticks(x_pos)
ax_c.set_xticklabels(gender_avg['Gender_Label'], fontsize=11)
ax_c.set_ylabel("年薪 (百萬美元)", fontsize=11)
ax_c.set_title("(C) 性別運動薪資差距 (男均 46.77M vs 女均 0.20M)", fontsize=13, fontweight='bold')
ax_c.set_ylim(0, 56)
ax_c.legend(loc='upper right')
# Annotate
ax_c.annotate("薪資差距高達 234 倍!\n(Mann-Whitney U: p = 1.84e-07 ***)",
              xy=(1, gender_avg.loc[1, 'mean']/1e6 + 0.5), xytext=(0.82, 28),
              arrowprops=dict(facecolor='red', shrink=0.08, width=1.5, headwidth=7),
              fontsize=10.5, fontweight='bold', color='#c0392b',
              bbox=dict(boxstyle='round,pad=0.4', facecolor='#ffebee', edgecolor='#ef5350'))

# Subplot D: Age vs Salary
ax_d = fig.add_subplot(gs[1, 1])
for p, c in zip(profs, colors_prof):
    sub = df2[df2['profession']==p]
    ax_d.scatter(sub['Age'], sub['Salary (Annual)']/1e6, label=p, color=c, s=70, edgecolors='black', alpha=0.85)
ax_d.set_title("(D) 年齡 vs 年薪分佈趨勢 (NBA 年齡正相關 r=0.675*)", fontsize=13, fontweight='bold')
ax_d.set_xlabel("年齡 (Age)", fontsize=11)
ax_d.set_ylabel("年薪 (百萬美元)", fontsize=11)
ax_d.legend(title="聯盟", loc='upper left')

plt.suptitle("檔案二：四大職業運動薪資深度統計分析 (KW_Pro_salary.xlsx)", fontsize=15, fontweight='bold', y=0.98)
fig.savefig("figure2_pro_salary_analysis.png", dpi=300, bbox_inches='tight')
plt.close(fig)
print("Updated figure2_pro_salary_analysis.png")

# ========================================================
# 3. Figure 3: Mann whitney.xlsx
# ========================================================
df3 = pd.read_excel('Mann whitney.xlsx', sheet_name='工作表1')
df3['Cancer'] = df3['annotation'].map({'BC': '乳腺癌 (BC, n=8)', 'LUAD': '肺腺癌 (LUAD, n=9)'})
palette_mw = {'乳腺癌 (BC, n=8)': '#E91E63', '肺腺癌 (LUAD, n=9)': '#00BCD4'}

fig, (ax_m1, ax_m2) = plt.subplots(1, 2, figsize=(14, 6.2))

sns.violinplot(x='Cancer', y='HER2_level', data=df3, ax=ax_m1, hue='Cancer', legend=False, palette=palette_mw, inner=None, alpha=0.3)
sns.boxplot(x='Cancer', y='HER2_level', data=df3, ax=ax_m1, hue='Cancer', legend=False, width=0.25, palette=palette_mw,
            boxprops=dict(alpha=0.7), showmeans=True,
            meanprops=dict(marker='o', markeredgecolor='black', markerfacecolor='yellow', markersize=8))
sns.stripplot(x='Cancer', y='HER2_level', data=df3, ax=ax_m1, color='black', size=8, jitter=0.15, alpha=0.8)

ax_m1.set_title("HER2 表現量差異比較 (Violin & Box Plot)", fontsize=13, fontweight='bold', pad=14)
ax_m1.set_xlabel("癌症類型 (Cancer Type)", fontsize=11)
ax_m1.set_ylabel("HER2 表現量 (HER2 level)", fontsize=11)
ax_m1.set_ylim(40, 920)

# Significance bracket
y_max = 700
h = 30
ax_m1.plot([0, 0, 1, 1], [y_max, y_max+h, y_max+h, y_max], lw=1.5, c='black')
ax_m1.text(0.5, y_max+h+20, "Mann-Whitney U = 71.0\np = 8.88e-04 (p < 0.001 ***)\nCliff's Delta = 0.972 (極大效應量)",
           ha='center', va='bottom', color='#c0392b', fontweight='bold', fontsize=10.5,
           bbox=dict(boxstyle='round,pad=0.4', facecolor='#ffebee', edgecolor='#ef5350'))

# Panel 2: ECDF
for annot, label, color in [('BC', '乳腺癌 BC (中位數: 446.5)', '#E91E63'), ('LUAD', '肺腺癌 LUAD (中位數: 118.0)', '#00BCD4')]:
    sub = df3[df3['annotation']==annot]['HER2_level'].sort_values()
    y_ecdf = np.arange(1, len(sub) + 1) / len(sub)
    ax_m2.step(sub, y_ecdf, where='post', label=label, color=color, lw=2.5)
    ax_m2.plot(sub, y_ecdf, 'o', color=color, markersize=6)

ax_m2.set_title("HER2 表現量累積分配函數 (ECDF)", fontsize=13, fontweight='bold', pad=14)
ax_m2.set_xlabel("HER2 表現量 (HER2 level)", fontsize=11)
ax_m2.set_ylabel("累積機率 (Cumulative Probability)", fontsize=11)
ax_m2.legend(loc='lower right', frameon=True)
ax_m2.axvline(x=200, color='gray', linestyle='--', alpha=0.7)
ax_m2.text(210, 0.4, "臨床分界閾值明顯\n乳腺癌顯著高表現", color='#555555', fontsize=10.5)

plt.suptitle("檔案三：乳腺癌與肺腺癌之 HER2 表現量顯著性比較 (Mann whitney.xlsx)", fontsize=15, fontweight='bold', y=0.98)
plt.tight_layout()
fig.savefig("figure3_mann_whitney_her2.png", dpi=300, bbox_inches='tight')
plt.close(fig)
print("Updated figure3_mann_whitney_her2.png")

# ========================================================
# 4. Figure 4: Summary Dashboard
# ========================================================
fig, axs = plt.subplots(1, 3, figsize=(18, 5.8))

# Summary 1: Blood Type
sns.barplot(x='blood type', y='Height (cm)', data=df1, order=order_bt, ax=axs[0],
            hue='blood type', legend=False, palette='Blues_d', errorbar='sd', capsize=0.1)
axs[0].set_ylim(140, 195)
axs[0].set_title("研究一：血型 vs 身高 (KW 檢定)\n結論：無顯著差異 (H=1.51, p=0.681 ns)", fontsize=12, fontweight='bold', color='#2c3e50')
axs[0].set_ylabel("平均身高 ± SD (cm)", fontsize=11)
axs[0].set_xlabel("血型", fontsize=11)

# Summary 2: Pro Salary
median_sal = df2.groupby('profession')['Salary (Annual)'].median().reindex(profs) / 1e6
bars2 = axs[1].bar(profs, median_sal, color=['#e74c3c', '#3498db', '#2ecc71', '#f1c40f'], alpha=0.85)
axs[1].set_yscale('log')
axs[1].set_ylim(0.04, 150)
axs[1].yaxis.set_major_formatter(ticker.FuncFormatter(lambda y, _: f"${y:g}M" if y >= 1 else f"${y*1000:g}K"))
axs[1].set_title("研究二：四大聯盟薪資 (KW 檢定)\n結論：極顯著差異 (H=27.61, p=4.38e-06 ***)", fontsize=12, fontweight='bold', color='#2c3e50')
axs[1].set_ylabel("中位數年薪 (對數尺)", fontsize=11)
axs[1].set_xlabel("聯盟", fontsize=11)
for bar in bars2:
    yval = bar.get_height()
    label_txt = f"${yval:.2f}M" if yval >= 1 else f"${yval*1000:.0f}K"
    axs[1].text(bar.get_x() + bar.get_width()/2.0, yval * 1.3, label_txt, ha='center', va='bottom', fontsize=9.5, fontweight='bold')

# Summary 3: HER2 Level
median_her2 = df3.groupby('annotation')['HER2_level'].median().reindex(['BC', 'LUAD'])
bars3 = axs[2].bar(['BC (乳癌)', 'LUAD (肺癌)'], median_her2, color=['#E91E63', '#00BCD4'], alpha=0.85, width=0.5)
axs[2].set_ylim(0, 530)
axs[2].set_title("研究三：癌症 HER2 表現 (MW 檢定)\n結論：極顯著差異 (U=71.0, p=8.88e-04 ***)", fontsize=12, fontweight='bold', color='#2c3e50')
axs[2].set_ylabel("中位數 HER2 表現量", fontsize=11)
axs[2].set_xlabel("癌症類型", fontsize=11)
for bar in bars3:
    yval = bar.get_height()
    axs[2].text(bar.get_x() + bar.get_width()/2.0, yval + 15, f"{yval:.1f}", ha='center', va='bottom', fontsize=10.5, fontweight='bold')

plt.suptitle("三份數據綜合統計分析與檢定總覽儀表板 (Executive Summary Dashboard)", fontsize=15, fontweight='bold', y=1.03)
plt.tight_layout()
fig.savefig("figure4_summary_dashboard.png", dpi=300, bbox_inches='tight')
plt.close(fig)
print("Updated figure4_summary_dashboard.png")

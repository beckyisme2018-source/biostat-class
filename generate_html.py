import base64
import os

def img_to_b64(path):
    with open(path, 'rb') as f:
        return base64.b64encode(f.read()).decode('utf-8')

b64_f1 = img_to_b64('figure1_blood_type_height.png')
b64_f2 = img_to_b64('figure2_pro_salary_analysis.png')
b64_f3 = img_to_b64('figure3_mann_whitney_her2.png')
b64_f4 = img_to_b64('figure4_summary_dashboard.png')

html_content = f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>123 資料夾數據統計分析報告</title>
    <style>
        :root {{
            --primary: #2563eb;
            --primary-dark: #1d4ed8;
            --accent: #0ea5e9;
            --success: #10b981;
            --warning: #f59e0b;
            --danger: #ef4444;
            --bg: #0f172a;
            --card-bg: #1e293b;
            --card-border: #334155;
            --text-main: #f8fafc;
            --text-sub: #94a3b8;
            --highlight: #38bdf8;
        }}
        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "PingFang TC", "Microsoft JhengHei", sans-serif;
        }}
        body {{
            background-color: var(--bg);
            color: var(--text-main);
            line-height: 1.6;
            padding: 2rem 1rem;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
        }}
        header {{
            text-align: center;
            margin-bottom: 3rem;
            padding: 2.5rem 1rem;
            background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
            border-radius: 16px;
            border: 1px solid var(--card-border);
            box-shadow: 0 10px 25px -5px rgba(0,0,0,0.3);
        }}
        h1 {{
            font-size: 2.5rem;
            font-weight: 800;
            letter-spacing: -0.025em;
            background: linear-gradient(to right, #60a5fa, #a855f7);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.75rem;
        }}
        .subtitle {{
            color: var(--text-sub);
            font-size: 1.1rem;
        }}
        .meta-bar {{
            display: flex;
            justify-content: center;
            gap: 1.5rem;
            margin-top: 1.25rem;
            font-size: 0.9rem;
            color: #cbd5e1;
        }}
        .badge {{
            display: inline-block;
            padding: 0.25rem 0.75rem;
            border-radius: 9999px;
            font-size: 0.8rem;
            font-weight: 600;
        }}
        .badge-success {{ background: rgba(16, 185, 129, 0.2); color: #34d399; border: 1px solid #059669; }}
        .badge-danger {{ background: rgba(239, 68, 68, 0.2); color: #f87171; border: 1px solid #dc2626; }}
        .badge-info {{ background: rgba(14, 165, 233, 0.2); color: #38bdf8; border: 1px solid #0284c7; }}
        .badge-neutral {{ background: rgba(148, 163, 184, 0.2); color: #cbd5e1; border: 1px solid #64748b; }}

        .card {{
            background: var(--card-bg);
            border: 1px solid var(--card-border);
            border-radius: 14px;
            padding: 2rem;
            margin-bottom: 2.5rem;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.2);
            transition: transform 0.2s ease, border-color 0.2s ease;
        }}
        .card:hover {{
            border-color: #475569;
        }}
        h2 {{
            font-size: 1.6rem;
            color: #f1f5f9;
            margin-bottom: 1.25rem;
            display: flex;
            align-items: center;
            gap: 0.75rem;
            border-bottom: 1px solid var(--card-border);
            padding-bottom: 0.75rem;
        }}
        h3 {{
            font-size: 1.2rem;
            color: #e2e8f0;
            margin: 1.25rem 0 0.75rem 0;
        }}
        p {{
            color: #cbd5e1;
            margin-bottom: 1rem;
        }}
        .grid-2 {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 1.5rem;
            margin: 1.5rem 0;
        }}
        .stat-box {{
            background: rgba(15, 23, 42, 0.6);
            border: 1px solid #334155;
            border-radius: 10px;
            padding: 1.25rem;
        }}
        .stat-value {{
            font-size: 1.8rem;
            font-weight: 700;
            color: var(--highlight);
            margin: 0.25rem 0;
        }}
        .stat-label {{
            font-size: 0.85rem;
            color: var(--text-sub);
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 1.5rem 0;
            font-size: 0.95rem;
        }}
        th, td {{
            padding: 0.85rem 1rem;
            text-align: left;
            border-bottom: 1px solid var(--card-border);
        }}
        th {{
            background: rgba(15, 23, 42, 0.8);
            color: #94a3b8;
            font-weight: 600;
        }}
        tr:hover td {{
            background: rgba(255, 255, 255, 0.02);
        }}
        .img-container {{
            margin: 1.75rem 0;
            border-radius: 12px;
            overflow: hidden;
            border: 1px solid var(--card-border);
            background: #ffffff;
            padding: 10px;
            text-align: center;
        }}
        .img-container img {{
            width: 100%;
            height: auto;
            border-radius: 6px;
            display: block;
        }}
        .conclusion-callout {{
            background: rgba(37, 99, 235, 0.1);
            border-left: 4px solid var(--primary);
            padding: 1rem 1.25rem;
            border-radius: 0 8px 8px 0;
            margin: 1.25rem 0;
        }}
        .conclusion-callout.success {{
            background: rgba(16, 185, 129, 0.1);
            border-left-color: var(--success);
        }}
        .conclusion-callout.warning {{
            background: rgba(245, 158, 11, 0.1);
            border-left-color: var(--warning);
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>123 資料夾統計數據深度分析報告</h1>
            <p class="subtitle">涵蓋 Kruskal-Wallis 檢定、Mann-Whitney U 檢定、效應量分析與專業視覺化圖表</p>
            <div class="meta-bar">
                <span>📁 分析目錄: /Users/chenyichieh/Downloads/123</span>
                <span>📊 分析檔案數: 3 個 Excel 檔案</span>
                <span>📅 生成時間: 2026-10-15</span>
            </div>
        </header>

        <!-- Executive Summary Dashboard -->
        <div class="card">
            <h2>📈 執行摘要與綜合成果總覽 (Executive Summary Dashboard)</h2>
            <p>本資料夾內包含三個標準統計學研究檔案，涵蓋不同變數類型與分配特徵。下方為三項研究之綜合對比儀表板：</p>
            <div class="img-container">
                <img src="data:image/png;base64,{b64_f4}" alt="綜合統計分析儀表板">
            </div>

            <table>
                <thead>
                    <tr>
                        <th>檔案名稱</th>
                        <th>研究主題</th>
                        <th>樣本數 (N)</th>
                        <th>檢定方法</th>
                        <th>統計檢定量</th>
                        <th>p-value</th>
                        <th>統計顯著性</th>
                        <th>關鍵結論</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>KW_Blood type.xlsx</strong></td>
                        <td>不同血型與身高之關聯</td>
                        <td>44</td>
                        <td>Kruskal-Wallis / ANOVA</td>
                        <td>H = 1.507 / F = 0.460</td>
                        <td>0.6806 / 0.7118</td>
                        <td><span class="badge badge-neutral">無顯著差異 (ns)</span></td>
                        <td>血型與個人身高無任何統計顯著關聯，符合現代遺傳學生理常識。</td>
                    </tr>
                    <tr>
                        <td><strong>KW_Pro_salary.xlsx</strong></td>
                        <td>四大職業運動聯盟薪資結構</td>
                        <td>40</td>
                        <td>Kruskal-Wallis (Dunn post-hoc)</td>
                        <td>H = 27.611</td>
                        <td>4.38 × 10⁻⁶</td>
                        <td><span class="badge badge-danger">極顯著差異 (***)</span></td>
                        <td>WNBA 薪資與男子三大聯盟 (NFL/NBA/MLB) 存在高達 234 倍性別薪資鴻溝。</td>
                    </tr>
                    <tr>
                        <td><strong>Mann whitney.xlsx</strong></td>
                        <td>乳腺癌 vs 肺腺癌 HER2 表現量</td>
                        <td>17</td>
                        <td>Mann-Whitney U 檢定</td>
                        <td>U = 71.0 (W = 107.0)</td>
                        <td>8.88 × 10⁻⁴</td>
                        <td><span class="badge badge-success">極顯著差異 (***)</span></td>
                        <td>乳癌 HER2 顯著高於肺腺癌 (中位數 446.5 vs 118.0)，效應量 δ = 0.972。</td>
                    </tr>
                </tbody>
            </table>
        </div>

        <!-- Section 1 -->
        <div class="card">
            <h2>1. KW_Blood type.xlsx — 血型與身高相關性研究</h2>
            <p>本檔案探索 ABO 血型分類系統 (A, B, O, AB) 是否對受試者之成人身高 (cm) 存在統計上的系統性差異。</p>

            <div class="grid-2">
                <div class="stat-box">
                    <div class="stat-label">Kruskal-Wallis H 統計量</div>
                    <div class="stat-value">1.5070</div>
                    <p style="color:#94a3b8; font-size:0.85rem; margin-top:4px;">自由度 df = 3, p = 0.6806 (> 0.05)</p>
                </div>
                <div class="stat-box">
                    <div class="stat-label">單因子變異數分析 (ANOVA) F 統計量</div>
                    <div class="stat-value">0.4600</div>
                    <p style="color:#94a3b8; font-size:0.85rem; margin-top:4px;">F(3, 40), p = 0.7118 (> 0.05)</p>
                </div>
            </div>

            <div class="img-container">
                <img src="data:image/png;base64,{b64_f1}" alt="血型與身高統計圖">
            </div>

            <h3>各血型身高敘述統計 (Descriptive Statistics)</h3>
            <table>
                <thead>
                    <tr>
                        <th>血型 (Blood Type)</th>
                        <th>樣本數 (n)</th>
                        <th>平均數 (Mean ± SD)</th>
                        <th>中位數 (Median)</th>
                        <th>四分位距 (IQR)</th>
                        <th>範圍 (Min - Max)</th>
                        <th>Shapiro-Wilk 常態性檢定 (p-value)</th>
                    </tr>
                </thead>
                <tbody>
                    <tr><td><strong>A 型</strong></td><td>12</td><td>174.00 ± 7.63 cm</td><td>173.50 cm</td><td>7.50 cm</td><td>158 - 185 cm</td><td>W = 0.941 (p = 0.4807, 常態)</td></tr>
                    <tr><td><strong>B 型</strong></td><td>10</td><td>171.50 ± 9.07 cm</td><td>173.00 cm</td><td>9.50 cm</td><td>157 - 184 cm</td><td>W = 0.948 (p = 0.5969, 常態)</td></tr>
                    <tr><td><strong>O 型</strong></td><td>9</td><td>170.44 ± 11.31 cm</td><td>170.00 cm</td><td>11.00 cm</td><td>154 - 187 cm</td><td>W = 0.942 (p = 0.6061, 常態)</td></tr>
                    <tr><td><strong>AB 型</strong></td><td>13</td><td>169.92 ± 9.11 cm</td><td>172.00 cm</td><td>9.00 cm</td><td>154 - 185 cm</td><td>W = 0.984 (p = 0.9696, 常態)</td></tr>
                </tbody>
            </table>

            <div class="conclusion-callout">
                <strong>💡 專業統計與生物學洞察：</strong>
                <ul style="margin-left: 1.5rem; margin-top: 0.5rem;">
                    <li><strong>檢定結論：</strong>Levene 等分散檢定 (p = 0.714) 與 Shapiro-Wilk 常態檢定均符合母數假設。ANOVA 與非參數 Kruskal-Wallis 檢定皆顯示 p > 0.05，<strong>無法拒絕虛無假說 (Fail to reject H₀)</strong>。</li>
                    <li><strong>科學詮釋：</strong>ABO 基因位於第 9 號染色體，負責合成紅血球表面之醣基轉移酶；而身高是由數百個微效多基因 (polygenic) 及環境營養因素共同調控之複合性狀，兩者在遺傳機制上完全獨立，因此無顯著差異為預期之生物學真實現況。</li>
                    <li><em>備註：</em>該檔案的工作表 2 包含 10 筆 NFL 四分衛薪資資料，推測為資料整理過程中的暫存分頁，主資料分析以工作表 1 為準。</li>
                </ul>
            </div>
        </div>

        <!-- Section 2 -->
        <div class="card">
            <h2>2. KW_Pro_salary.xlsx — 職業運動年薪結構與性別差距研究</h2>
            <p>本資料集採樣自四大職業運動聯盟各 10 位頂尖選手 (總計 N=40)：NBA (男子職籃)、MLB (男子職棒)、NFL (美式足球) 及 WNBA (女子職籃)。</p>

            <div class="grid-2">
                <div class="stat-box">
                    <div class="stat-label">Kruskal-Wallis H 統計量</div>
                    <div class="stat-value">27.611</div>
                    <p style="color:#94a3b8; font-size:0.85rem; margin-top:4px;">df = 3, p = 4.38 × 10⁻⁶ (***)</p>
                </div>
                <div class="stat-box">
                    <div class="stat-label">男女頂尖運動員薪資倍率差距</div>
                    <div class="stat-value">233.9 倍</div>
                    <p style="color:#94a3b8; font-size:0.85rem; margin-top:4px;">男均 $46.77M vs 女均 $0.20M (p = 1.84e-07)</p>
                </div>
            </div>

            <div class="img-container">
                <img src="data:image/png;base64,{b64_f2}" alt="職業運動年薪統計圖">
            </div>

            <h3>四大聯盟年薪敘述統計</h3>
            <table>
                <thead>
                    <tr>
                        <th>聯盟 / 運動項目</th>
                        <th>樣本數</th>
                        <th>平均年薪 (Mean ± SD)</th>
                        <th>中位數年薪 (Median)</th>
                        <th>最高年薪選手 (Max)</th>
                        <th>最低年薪選手 (Min)</th>
                    </tr>
                </thead>
                <tbody>
                    <tr><td><strong>NBA (男子職籃)</strong></td><td>10</td><td>$45,464,546 ± $7,037,160</td><td>$46,623,717</td><td>Stephen Curry ($55.76M)</td><td>Jayson Tatum ($34.85M)</td></tr>
                    <tr><td><strong>MLB (男子職棒)</strong></td><td>10</td><td>$42,370,833 ± $11,121,253</td><td>$38,500,000</td><td>Shohei Ohtani 大谷翔平 ($70.00M)</td><td>Corey Seager ($32.50M)</td></tr>
                    <tr><td><strong>NFL (美式足球)</strong></td><td>10</td><td>$52,460,000 ± $4,408,880</td><td>$52,750,000</td><td>Dak Prescott ($60.00M)</td><td>Patrick Mahomes ($45.00M)</td></tr>
                    <tr><td><strong>WNBA (女子職籃)</strong></td><td>10</td><td>$199,922 ± $47,436</td><td>$203,500</td><td>Jackie Young ($252,450)</td><td>Caitlin Clark ($76,535)</td></tr>
                </tbody>
            </table>

            <h3>事後多重比較 (Dunn's Post-hoc Test with Bonferroni Correction)</h3>
            <table>
                <thead>
                    <tr>
                        <th>比較組別</th>
                        <th>平均秩差 (Rank Diff)</th>
                        <th>標準化統計量 (Z)</th>
                        <th>原始 p-value</th>
                        <th>Bonferroni 校正後 p-value</th>
                        <th>顯著性判定</th>
                    </tr>
                </thead>
                <tbody>
                    <tr><td><strong>NFL vs WNBA</strong></td><td>+26.75</td><td>5.117</td><td>3.11 × 10⁻⁷</td><td><strong>1.87 × 10⁻⁶</strong></td><td><span class="badge badge-danger">極顯著差異 (***)</span></td></tr>
                    <tr><td><strong>NBA vs WNBA</strong></td><td>+18.70</td><td>3.577</td><td>3.48 × 10⁻⁴</td><td><strong>2.09 × 10⁻³</strong></td><td><span class="badge badge-danger">高度顯著差異 (**)</span></td></tr>
                    <tr><td><strong>MLB vs WNBA</strong></td><td>+14.55</td><td>2.783</td><td>5.39 × 10⁻³</td><td><strong>3.23 × 10⁻²</strong></td><td><span class="badge badge-danger">顯著差異 (*)</span></td></tr>
                    <tr><td><strong>NFL vs MLB</strong></td><td>+12.20</td><td>2.334</td><td>0.0196</td><td>0.1177</td><td><span class="badge badge-neutral">無顯著差異 (邊界趨勢)</span></td></tr>
                    <tr><td><strong>NFL vs NBA</strong></td><td>+8.05</td><td>1.540</td><td>0.1236</td><td>0.7417</td><td><span class="badge badge-neutral">無顯著差異</span></td></tr>
                    <tr><td><strong>NBA vs MLB</strong></td><td>+4.15</td><td>0.794</td><td>0.4273</td><td>1.0000</td><td><span class="badge badge-neutral">無顯著差異</span></td></tr>
                </tbody>
            </table>

            <div class="conclusion-callout warning">
                <strong>💡 產業經濟與性別薪資結構剖析：</strong>
                <ul style="margin-left: 1.5rem; margin-top: 0.5rem;">
                    <li><strong>極端性別鴻溝：</strong>三大男子聯盟選手年薪均落於 3,200 萬至 7,000 萬美元區間，而頂尖 WNBA 女籃選手年薪僅 7.6 萬至 25.2 萬美元。Mann-Whitney U 檢定 p = 1.84 × 10⁻⁷，兩者完全落在不同的數量級 (差距高達 234 倍)。</li>
                    <li><strong>年齡資歷效應：</strong>NBA 內部年齡與年薪呈現顯著正相關 (Spearman r = 0.675, p = 0.032)，此反映 NBA 勞資協議中資深巨星享有 35% 薪資上限之超級頂薪 (Supermax/Veteran Max) 條款；而 WNBA 即使是巨星亦受限於聯盟嚴格薪資硬上限。</li>
                </ul>
            </div>
        </div>

        <!-- Section 3 -->
        <div class="card">
            <h2>3. Mann whitney.xlsx — 乳腺癌 vs 肺腺癌之 HER2 表現量比較</h2>
            <p>本檔案針對臨床病理樣本比較乳腺癌 (Breast Cancer, BC, n=8) 與肺腺癌 (Lung Adenocarcinoma, LUAD, n=9) 組織檢體之 HER2 (人表皮生長因子受體 2) 蛋白質/基因表現量。</p>

            <div class="grid-2">
                <div class="stat-box">
                    <div class="stat-label">Mann-Whitney U 統計量</div>
                    <div class="stat-value">71.0</div>
                    <p style="color:#94a3b8; font-size:0.85rem; margin-top:4px;">W = 107.0, 雙尾 p = 8.879 × 10⁻⁴ (***)</p>
                </div>
                <div class="stat-box">
                    <div class="stat-label">效應量 Cliff's Delta (δ)</div>
                    <div class="stat-value">0.9722</div>
                    <p style="color:#94a3b8; font-size:0.85rem; margin-top:4px;">CLES = 98.6% (接近完全分離之巨大效應)</p>
                </div>
            </div>

            <div class="img-container">
                <img src="data:image/png;base64,{b64_f3}" alt="HER2 表現量比較圖">
            </div>

            <h3>病理樣本表現量敘述統計</h3>
            <table>
                <thead>
                    <tr>
                        <th>癌症類型 (Annotation)</th>
                        <th>樣本數 (n)</th>
                        <th>平均表現量 (Mean ± SD)</th>
                        <th>中位數 (Median)</th>
                        <th>四分位距 (IQR)</th>
                        <th>全距 (Min - Max)</th>
                        <th>常態性檢定 (Shapiro-Wilk)</th>
                    </tr>
                </thead>
                <tbody>
                    <tr><td><strong>乳腺癌 (BC, Group 1)</strong></td><td>8</td><td>434.50 ± 202.05</td><td>446.50</td><td>343.25</td><td>156 - 666</td><td>W = 0.892 (p = 0.2220)</td></tr>
                    <tr><td><strong>肺腺癌 (LUAD, Group 2)</strong></td><td>9</td><td>128.44 ± 25.62</td><td>118.00</td><td>13.00</td><td>111 - 187</td><td>W = 0.724 (p = 0.0033, 偏態)</td></tr>
                </tbody>
            </table>

            <div class="conclusion-callout success">
                <strong>💡 分子病理學與臨床標靶治療詮釋：</strong>
                <ul style="margin-left: 1.5rem; margin-top: 0.5rem;">
                    <li><strong>檢定適格性：</strong>肺腺癌數據具顯著偏態 (p = 0.0033) 且兩組變異數嚴重不齊 (BC 標準差為 LUAD 的 7.9 倍)，完全符合使用非參數 Mann-Whitney U 檢定之黃金準則。</li>
                    <li><strong>超高度統計顯著性：</strong>U = 71.0 (最大可能 U 值為 8 × 9 = 72)，代表兩組樣本之間僅有 1 個觀察值交疊 (BC 最低值為 156，而 LUAD 僅有 1 筆數值 187 高於 156，其餘均落於 111-153)，隨機抽樣 BC 高於 LUAD 之機率達 98.6%。</li>
                    <li><strong>臨床意義：</strong>HER2 (ERBB2) 擴增在浸潤性乳腺癌中約佔 15-20%，為賀癌平 (Trastuzumab) 等標靶藥物之決定性生物標記；而在肺腺癌中，主要驅動突變為 EGFR / KRAS / ALK，HER2 過度表現率極低，數據高度反映了此臨床生物學特徵。</li>
                </ul>
            </div>
        </div>

        <!-- Section 4 -->
        <div class="card">
            <h2>4. 統計分析方法論總結 (Statistical Methodology Review)</h2>
            <table>
                <thead>
                    <tr>
                        <th>檢定名稱</th>
                        <th>適用場景</th>
                        <th>母數對應方法</th>
                        <th>本專案應用實例</th>
                        <th>選用非參數檢定之核心理由</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>Kruskal-Wallis 檢定</strong></td>
                        <td>3 組以上獨立樣本比較</td>
                        <td>單因子變異數分析 (One-way ANOVA)</td>
                        <td>血型 vs 身高、四大聯盟年薪</td>
                        <td>避免因小樣本、極端偏態 (如大谷翔平 $70M) 或變異數不均勻導致之假陽性或統計檢定力失真。</td>
                    </tr>
                    <tr>
                        <td><strong>Mann-Whitney U 檢定</strong></td>
                        <td>2 組獨立連續變數比較</td>
                        <td>獨立樣本 t 檢定 (Student's t-test)</td>
                        <td>癌症類型 vs HER2 表現、性別薪資差異</td>
                        <td>非依賴常態分佈假設，以秩次 (Rank) 為基礎，具極高強韌性 (Robustness)。</td>
                    </tr>
                    <tr>
                        <td><strong>Dunn's 事後檢定</strong></td>
                        <td>KW 檢定顯著後之組間成對比較</td>
                        <td>Tukey HSD / Bonferroni</td>
                        <td>四大運動聯盟成對薪資比較</td>
                        <td>使用整體秩和進行成對 Z 檢定，並透過 Bonferroni 調整有效控制族系誤差率 (FWER)。</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</body>
</html>
"""

with open("analysis_report.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Generated analysis_report.html successfully!")

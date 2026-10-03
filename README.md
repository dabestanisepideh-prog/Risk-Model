🚀 **Live Production Environment:** [Click Here to Run the AI Risk Dashboard Live](https://risk-model-lgz3wpdknf8zfzjsywrrzs.streamlit.app/)  (لینک داشبورد پویای مدل 5)
*(Interactive Web Application with Real-Time Regime Switching Dashboard for Executive Decision Makers)*

---

# ☕ Enterprise Quantitative Risk Management & AI Procurement Strategy
### پلتفرم جامع مدیریت ریسک کمی و استراتژی تامین مبتنی بر هوش مصنوعی(قابل توسعه)

---

## 📌 ۱. صورت مسئله و اهداف پروژه (فارسی)
چالش استراتژیک این پروژه، مدیریت **ریسک موازی بازار (Dual Market Exposure)** در یک افق زمانی **۹۰ روزه** برای تامین **۵۰,۰۰۰ پوند** کالا است. این سبد تامین به طور هم‌زمان در معرض دو متغیر بحرانی قرار دارد:
۱. **ریسک جهانی کالا (Commodity Risk):** نوسانات غیرخطی و ساختاری قیمت جهانی کالا بر حسب دلار در هر پوند.
۲. **ریسک ماکروکونومیک داخلی (FX Risk):** نوسانات شدید، جهش‌های ناگهانی نرخ ارز و شوک‌های رژیم ارزی (ریال به دلار).

### 🎯 اهداف اصلی پروژه:
* **کمینه کردن هزینه کل تامین:** کشف پویای بهترین نقاط ورود به بازار و زمان‌بندی خرید پله‌ای در طول ۹۰ روز.
* **حفظ سرمایه در گردش و سودآوری:** جلوگیری از قفل شدن نقدینگی و بحران‌های مالی ناشی از جهش‌های ناگهانی ارز (قوی سیاه).
* **قیدهای محدودیت ریسک:** تضمین اینکه بدترین سناریوهای زیان (Tail Risks) هرگز از سقف سرمایه مجاز ریسک شرکت بالاتر نرود.

### 📊 متغیرها و پارامترهای مدل:
* \(X_t\): حجم خرید بهینه در روز t (متغیر تصمیم‌گیری)
* \(C_t\): قیمت نقدی جهانی کالا به دلار/پوند (متغیر تصادفی)
* \(FX_t\): نرخ ارز داخلی به ریال/دلار (متغیر تصادفی)
* ρ: ضریب همبستگی بین قیمت کالا و تغییرات ارز (کوواریانس دارایی‌ها)
* λ: پارامتر شدت پرش پواسون (نشان‌دهنده شوک‌های ناگهانی و ناپیوسته بازار)
* \(\alpha_t\): ماتریس وزن‌های لایه توجه ترنسفورمر برای شناسایی روزهای پرریسک در زنجیره تامین

---

## 🏛️ ۲. ساختار درختی مخزن پروژه (Repository Tree)

```text
📦 Commodity_Risk_Platform
├── 📁 01_Classical_Risk_Models (گروه اول: مدل‌های کلاسیک ریسک)
│   ├── 📄 01_monte_carlo_simulation.py    # شبیه‌سازی مسیرهای همبسته با هندسه براونی (mGBM)
│   ├── 📄 02_machine_learning_forecast.py # سیگنال آماری جهت‌گیری و توزیع شرطی روند بازار
│   ├── 📄 03_stochastic_optimization.py   # بهینه‌سازی قیددار استرس تست و استخراج شاخص‌های VaR و CVaR
│   └── 📄 04_merton_jump_diffusion.py    # مدل‌سازی جهش‌های ناگهانی بازار با فرآیند پواسون
└── 📁 02_Advanced_AI_Models (گروه دوم: مدل‌های پیشرفته هوش مصنوعی)
    ├── 📄 05_markov_switching_xgboost.py  # تشخیص تغییر رژیم بازار از آرام به انفجاری با یادگیری ماشین
    │   └── 🌐 [Live Production App] ──> https://streamlit.app
    └── 📄 06_temporal_fusion_transformer.py # پیش‌بینی غیرخطی تندبادهای قیمتی با لایه توجه شبکه ترنسفورمر
```

---

## 🚀 ۳. تشریح فرآیند و متدولوژی هر روش (فارسی)

### 📁 گروه اول: مدل‌های کلاسیک ریسک (`01_Classical_Risk_Models`)

#### روش ۱: شبیه‌سازی چندمتغیره مونت‌کارلو
* **فرآیند محاسباتی:** این مدل با استفاده از **حرکت براونی هندسی چندمتغیره (mGBM)**، تعداد ۱۰,۰۰۰ مسیر قیمت روزانه را شبیه‌سازی می‌کند. مدل با ترکیب واریانس تاریخی و اعمال همبستگی مثبت ۲۰ درصدی، احتمال صعود هم‌زمان ارز و کالا را در نظر می‌گیرد.
* **خروجی نموداری:** رسم درخت مسیرهای احتمالی ۹۰ روزه به همراه خط ضخیم میانگین انتظارات ریاضی بازار.

#### روش ۲: پیش‌بینی آماری روند با یادگیری ماشین
* **فرآیند محاسباتی:** این ماژول مسیرهای پیوسته خروجی مونت‌کارلو را به شاخص‌های احتمال شرطی تبدیل می‌کند تا وزن آماری و جهت‌گیری روند بازار (صعودی/نزولی) را به عنوان سیگنال اولیه استخراج کند.
* **خروجی نموداری:** نمودار میله‌ای توزیع احتمال رالی قیمت کالا در برابر شوک‌های ارزی.

#### روش ۳: بهینه‌سازی تصادفی و تست استرس سناریومحور
* **فرآیند محاسباتی:** یک شوک ساختاری غیرخطی (+۵۰٪ جهش ناگهانی ارز در روز ۴۵ام) را به تمام سناریوها تحمیل می‌کند. سپس توزیع سرمایه مورد نیاز را محاسبه کرده و شاخص‌های حیاتی **VaR (ارزش در معرض ریسک)** و **CVaR (میانگین ضرر در ۵٪ بدترین سناریوها)** را در سطح اطمینان ۹۵٪ استخراج می‌کند.
* **خروجی نموداری:** هیستوگرام دوتایی مقایسه‌ای برای نمایش جابجایی مرزهای فاجعه (Fat-Tail Risks) از حالت عادی به حالت استرس.

#### روش ۴: مدل پرش-نفوذ مرتون (Merton Jump-Diffusion)
* **فرآیند محاسباتی:** نقطه ضعف مدل‌های پیوسته براونی را برطرف می‌کند. این مدل با افزودن یک فرآیند تصادفی **پواسون**، گپ‌های عمودی و جهش‌های لحظه‌ای قیمت را که رفتار واقعی بازار ارز در زمان شوک‌های سیاسی است، فرموله‌سازی می‌کند.
* **خروجی نموداری:** نمودار نوسانات حاوی پرش‌های ناگهانی به همراه مرز صدک ۹۵ام جهت تعیین بافرهای نقدینگی شرکت.

---

### 📁 گروه دوم: مدل‌های پیشرفته هوش مصنوعی (`02_Advanced_AI_Models`)

#### روش ۵: پیش‌بینی تغییر رژیم با مدل Markov Switching XGBoost
* **فرآیند محاسباتی:** بازارها را به دو فاز **رژیم آرام** (کم نوسان) و **رژیم بحران** (انفجاری) تقسیم می‌کند. ویژگی‌های پیشرو شامل شتاب قیمت و خوشه‌بندی نوسانات وارد الگوریتم **XGBoost Classifier** شده تا احتمال سوییچ بازار به فاز بحران را ۷ الی ۱۰ روز زودتر پیش‌بینی کند.
* **لینک اجرای زنده داشبورد:** برای تست و اجرای زنده این مدل به صورت آنلاین همراه با اسلایدرهای مدیریتی، روی لینک زیر کلیک کنید:
  🔗 **[ورود به پلتفرم پویا و اجرای زنده داشبورد هوش مصنوعی](https://streamlit.app)**
* **خروجی نموداری:** داشبورد تعاملی سیگنال ریسک هوش مصنوعی (۰ تا ۱۰۰٪) به همراه هایلایت قرمز رنگ مناطق شروع رژیم پرش قیمت.

#### روش ۶: شبکه عصبی عمیق ترنسفورمر (Temporal Fusion Transformer - TFT)
* **فرآیند محاسباتی:** از معماری قدرتمند **Transformer** و مکانیزم‌های **توجه چندسر (Multi-Head Self-Attention)** استفاده می‌کند. این شبکه عصبی عمیق برخلاف مدل‌های قدیمی، وابستگی‌های زمانی طولانی‌مدت و اثرات غیرخطی متغیرها را یاد می‌گیرد تا دقیقاً مشخص کند کدام روزها در پنجره ۹۰ روزه زنجیره تامین، بالاترین پتانسیل را برای وقوع **تندبادهای قیمتی (Price Spikes)** دارند.
* **خروجی نموداری:** انطباق لایه توجه هوش مصنوعی بر روی نمودار هزینه دینامیک خرید برای تخصیص بهینه خطوط اعتباری شرکت.

---
---

## 📌 4. Comprehensive Problem Statement & Objectives (English)
The strategic challenge lies in managing **Dual Market Exposure Risk** within a rigid **90-day operational window** for a commodity procurement requirement of **50,000 lb**. The portfolio is simultaneously vulnerable to:
1. **Global Commodity Risk:** Non-linear structural fluctuations in global commodity prices (USD/lb).
2. **Domestic Macroeconomic Risk:** Extreme volatility, sudden currency devaluations, and regulatory shocks in the domestic currency exchange rate (Local Currency to USD).

### 🎯 Primary Objectives:
* **Minimize Total Cost of Procurement:** Dynamically discover optimal purchasing entry points over the 90-day horizon.
* **Capital & Profit Preservation:** Prevent catastrophic cash crunches caused by sudden real-world black-swan devaluations.
* **Risk Bound Constraints:** Ensure that the worst-case financial losses stay strictly below the firm's approved maximum risk capital capacity.

---

## 🚀 5. Process Architecture & Methodology Breakdown (English)

### 📁 Group 1: Classical Risk Models (`01_Classical_Risk_Models`)

#### Method 1: Multivariate Monte Carlo Simulation (`01_monte_carlo_simulation.py`)
* **Process Flow:** Generates 10,000 daily correlated asset price paths using a **Multivariate Geometric Brownian Motion (mGBM)** factoring a 20% positive correlation coefficient.
* **Visualization Output:** A 90-day tree plot charting simulated price drift vs. expected mathematical mean values.

#### Method 2: Statistical Machine Learning Forecast (`02_machine_learning_forecast.py`)
* **Process Flow:** Processes the continuous asset paths into discrete conditional probability metrics to output actionable market direction signals.
* **Visualization Output:** A bar chart showing the statistical probability weight of commodity rallies vs. sudden currency shocks.

#### Method 3: Stochastic Optimization & Continuous Stress Testing (`03_stochastic_optimization.py`)
* **Process Flow:** Imposes a severe **Non-Linear Shifting Shock** (+50% sudden currency devaluation at Day 45) to measure absolute capital displacement. It isolates the tail risk using **Value at Risk (VaR)** and **Conditional Value at Risk (CVaR)** at a 95% confidence interval.
* **Visualization Output:** Dual-histogram comparison mapping the shift in **Fat-Tail Risks** from the baseline state to the stressed state.

#### Method 4: Merton Jump-Diffusion Framework (`04_merton_jump_diffusion.py`)
* **Process Flow:** Corrects continuous diffusion flaws by adding a discontinuous compound **Poisson Jump Process** to model sudden real-world market structural breaks.
* **Visualization Output:** Volatility charts showing vertical price gaps, tracing the extreme 95th percentile path to set capital cushions.

---

### 📁 Group 2: Advanced AI & Deep Learning Models (`02_Advanced_AI_Models`)

#### Method 5: Markov Switching XGBoost Risk Dashboard (`05_markov_switching_xgboost.py`)
* **Process Flow:** Processes rolling statistical inputs through an **XGBoost Classifier** combined with a latent state transition matrix to predict structural shifts from "Calm" to "Crisis" market volatility regimes.
* **Live Interactive Web App:** Access the operational simulation instantly at: 🔗 **[Live Streamlit Deployment](https://streamlit.app)**
* **Visualization Output:** An interactive web dashboard plotting a **Pre-Crisis Risk Signal (0-100%)** that flags transitions 7 to 10 days in advance.

#### Method 6: Deep Temporal Fusion Transformer - TFT (`06_temporal_fusion_transformer.py`)
* **Process Flow:** Deploys a state-of-the-art **Temporal Fusion Transformer (TFT)** architecture utilizing multi-head **Self-Attention Mechanisms** to isolate long-term historical dependencies and predict non-linear price spikes inside the supply chain window.
* **Visualization Output:** An attention-weight overlay matched against the dynamic procurement cost line to justify high-stakes capital allocation decisions.

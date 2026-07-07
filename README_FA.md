<p align="center">

[English Version](README.md)

</p>

---

# HunterX

HunterX یک فریمورک مدرن شناسایی (Reconnaissance Framework) است که به طور کامل با زبان Python توسعه یافته است.

این ابزار برای شکارچیان باگ (Bug Bounty Hunters)، تست‌کنندگان نفوذ (Penetration Testers) و پژوهشگران امنیت طراحی شده تا بتوانند فرآیند جمع‌آوری اطلاعات هدف را با سرعت بالا، معماری ماژولار و قابلیت توسعه آسان انجام دهند.

برخلاف بسیاری از ابزارهای سنتی، HunterX بر پایه معماری Plugin-Based طراحی شده است؛ به این معنا که هر ماژول می‌تواند به صورت مستقل اجرا شود یا در کنار سایر ماژول‌ها بخشی از یک Pipeline کامل شناسایی باشد.

---

# ویژگی‌ها

- معماری کاملاً ماژولار
- سیستم افزونه (Plugin-Based)
- موتور سریع HTTP
- شناسایی رکوردهای DNS
- جمع‌آوری زیردامنه‌ها
- تحلیل فایل‌های JavaScript
- خزنده وب (Crawler)
- اسکن دایرکتوری‌ها
- بررسی هدرهای امنیتی
- تحلیل Cookieها
- بررسی تنظیمات CORS
- تشخیص تکنولوژی‌های وب
- ذخیره Workspace
- خروجی JSON
- خروجی Markdown
- رابط کاربری رنگی در ترمینال
- نوار پیشرفت (Progress Bar)
- لاگ‌های حرفه‌ای
- قابلیت توسعه آسان

---

# نصب

## با استفاده از pip

```bash
pip install hunterx-reconhive
```

## با استفاده از uv

```bash
uv tool install hunterx-reconhive
```

---

# نحوه استفاده

اسکن ساده

```bash
hunterx scan example.com
```

اجرای افزونه‌های دلخواه

```bash
hunterx scan example.com --plugins dns,http,crawler
```

ارسال Header سفارشی

```bash
hunterx scan example.com -H "Authorization: Bearer TOKEN"
```

ارسال درخواست POST

```bash
hunterx scan example.com -X POST
```

اسکن دایرکتوری

```bash
hunterx scan example.com --plugins directory
```

خزنده سایت

```bash
hunterx scan example.com --plugins crawler
```

تحلیل JavaScript

```bash
hunterx scan example.com --plugins javascript
```

ساخت گزارش JSON

```bash
hunterx scan example.com -o report.json
```

ساخت گزارش Markdown

```bash
hunterx scan example.com -o report.md
```

---

# افزونه‌های موجود

| افزونه | توضیحات |
|---------|---------|
| dns | شناسایی اطلاعات DNS |
| http | تحلیل HTTP |
| crawler | خزیدن صفحات سایت |
| javascript | تحلیل JavaScript |
| directory | اسکن مسیرها |
| subdomain | شناسایی زیردامنه‌ها |
| tls | بررسی TLS |
| ports | اسکن پورت‌ها |

---

# نمونه اجرا

```bash
hunterx scan google.com --plugins dns,http,crawler,javascript -o report.json
```

---

# ساختار پروژه

```
hunterx/
│
├── cli/
├── core/
├── modules/
├── plugins/
└── utils/
```

---

# معماری پروژه

```
رابط خط فرمان (CLI)

↓

هسته اصلی (Core Engine)

↓

بارگذاری افزونه‌ها (Plugin Loader)

↓

افزونه‌ها (Plugins)

↓

ماژول‌ها (Modules)

↓

نتایج (Result Objects)

↓

Workspace / Report
```

---

# ماژول‌های فعلی

✅ DNS

✅ HTTP

✅ Cookies

✅ Security Headers

✅ CORS

✅ Technology Fingerprinting

✅ Directory Scanner

✅ Web Crawler

✅ JavaScript Analyzer

---

# برنامه توسعه (Roadmap)

- بهبود TLS Scanner
- Port Scanner
- تشخیص WAF
- Screenshot Engine
- کشف پارامترها
- Archive.org Integration
- Wayback Machine
- تشخیص CDN
- ASN Lookup
- تحلیل CSP
- پشتیبانی از HTTP/2 و HTTP/3
- بررسی HTTP Request Smuggling
- کشف GraphQL
- تشخیص Swagger/OpenAPI
- کشف Secretها
- شناسایی AWS Bucket
- Passive Recon
- اتصال به Shodan
- اتصال به Censys
- اتصال به VirusTotal
- گزارش HTML
- داشبورد زنده

---

# چرا HunterX؟

HunterX با تمرکز بر موارد زیر توسعه داده شده است:

- معماری تمیز (Clean Architecture)
- سرعت بالا
- خروجی خوانا
- توسعه آسان افزونه‌ها
- استفاده از استانداردهای مدرن Python
- وابستگی‌های سبک و کم‌حجم

---

# مشارکت در توسعه

از مشارکت شما استقبال می‌شود.

برای همکاری کافی است:

1. پروژه را Fork کنید.
2. شاخه (Branch) جدید ایجاد کنید.
3. تغییرات خود را اعمال کنید.
4. Pull Request ارسال کنید.

---

# مجوز

MIT License

---

# سلب مسئولیت

HunterX صرفاً برای اهداف آموزشی، پژوهشی و ارزیابی‌های امنیتی مجاز طراحی شده است.

هرگونه استفاده غیرمجاز یا غیرقانونی از این ابزار بر عهده کاربر بوده و توسعه‌دهنده هیچ مسئولیتی در قبال سوءاستفاده از آن نخواهد داشت.

---

<p align="center">

🇬🇧 **English Documentation**

➡️ [README.md](README.md)

</p>

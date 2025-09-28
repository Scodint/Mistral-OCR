# مستخرج النصوص من PDF باستخدام Mistral OCR

[![Language](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

أداة سطر أوامر (CLI) بسيطة وفعالة لاستخراج النصوص من ملفات PDF باستخدام واجهة برمجة التطبيقات (API) الخاصة بـ Mistral OCR. تم تصميم هذه الأداة لتكون آمنة وسهلة الاستخدام، مع إدارة آمنة لمفاتيح API من خلال متغيرات البيئة.

---

##  المتطلبات (Requirements)

-   Python 3.7+
-   حساب في منصة [Mistral AI](https://console.mistral.ai/) للحصول على مفتاح API.

---

##  التثبيت والإعداد (Installation & Setup)

اتبع هذه الخطوات لتشغيل المشروع على جهازك.

**1. استنساخ المستودع (Clone the Repository):**
```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
```
*(استبدل `your-username/your-repository-name` باسم المستخدم والمستودع الخاص بك على GitHub)*

**2. تثبيت المكتبات المطلوبة (Install Dependencies):**
```bash
pip install -r requirements.txt
```

**3. إعداد متغيرات البيئة (Set Up Environment Variables):**
هذه هي أهم خطوة لحماية مفتاح API الخاص بك.

-   أولاً، قم بإنشاء نسخة من ملف القالب `.env.example`:
    ```bash
    cp .env.example .env
    ```

-   ثانياً، افتح ملف `.env` الجديد الذي تم إنشاؤه باستخدام أي محرر نصوص، وأضف مفتاح Mistral API الخاص بك.
    ```ini
    # .env
    MISTRAL_API_KEY="sk-YOUR_REAL_API_KEY_HERE"
    ```

---

##  طريقة الاستخدام (Usage)

يمكنك الآن تشغيل السكربت من سطر الأوامر.

**الاستخدام الأساسي:**
قم بتمرير مسار ملف PDF الذي تريد معالجته.
```bash
python ocr_processor.py path/to/your/document.pdf
```
**مثال:**
```bash
python ocr_processor.py invoices/september-2024.pdf
```
سيقوم البرنامج بطباعة النص المستخرج من كل صفحة في الملف.

**توجيه المخرجات إلى ملف:**
يمكنك بسهولة حفظ النص المستخرج في ملف markdown.
```bash
python ocr_processor.py my_report.pdf > extracted_text.md
```

**استخدام الوضع التفصيلي (Verbose Mode):**
إذا كنت ترغب في رؤية خطوات التنفيذ أثناء عمل البرنامج، استخدم الخيار `-v` أو `--verbose`.
```bash
python ocr_processor.py my_document.pdf --verbose
```

---


##  الترخيص (License)

هذا المشروع مرخص بموجب ترخيص MIT. انظر ملف `LICENSE` لمزيد من التفاصيل.

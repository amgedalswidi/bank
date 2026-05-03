# Bank Transfer Architectures (Python CLI)

هذا مشروع تعليمي يوضح نفس السيناريو الوظيفي (تحويل مبلغ بين حسابين بنكيين) بأربع معماريات مختلفة:

- Spaghetti
- Three-Tier
- MVC
- Microservices (بدون API)

كل نسخة تدعم:

- إنشاء حساب
- عرض الرصيد
- تحويل مبلغ من حساب إلى آخر
- التحقق من الرصيد قبل التحويل
- تسجيل العمليات (Logging)
- اختبارات وحدة (Unit Tests)

---

## 1) Spaghetti Code

### الفكرة
نسخة متعمدة غير منظمة لعرض المشاكل عندما تختلط كل المسؤوليات في ملف واحد.

### Project Structure

```text
spaghetti/
  __init__.py
  bank_spaghetti.py
```

### المميزات
- سريعة جدًا للبدء في مشروع صغير جدًا أو تجربة سريعة.

### العيوب
- صيانة صعبة.
- اختبار أصعب مع زيادة التعقيد.
- تداخل واجهة المستخدم مع المنطق والبيانات.

### متى نستخدمها؟
- للتعليم فقط، أو PoC صغير جدًا غير قابل للتوسع.

### التشغيل
```bash
python -m spaghetti.bank_spaghetti
```

---

## 2) Three-Tier Architecture

### الفكرة
تقسيم النظام إلى 3 طبقات مستقلة:

1. Presentation (CLI)
2. Business Logic
3. Data Access

### Project Structure

```text
three_tier/
  __init__.py
  presentation/
    __init__.py
    cli.py
  business/
    __init__.py
    service.py
  data/
    __init__.py
    repository.py
```

### المميزات
- فصل واضح للمسؤوليات.
- أسهل في الاختبار والتعديل.
- مناسب للأنظمة المؤسسية التقليدية.

### العيوب
- يحتاج ملفات أكثر وتنظيم أدق.
- قد يصبح النقل بين الطبقات مكررًا إذا لم يصمم جيدًا.

### متى نستخدمها؟
- عندما يكون المشروع متوسط/كبير ويحتاج فصلًا واضحًا بين الواجهة والمنطق والبيانات.

### التشغيل
```bash
python -m three_tier.presentation.cli
```

---

## 3) MVC Pattern

### الفكرة
فصل التطبيق إلى:

- Model: تمثيل البيانات (`Account`) والتخزين.
- View: واجهة المستخدم (CLI).
- Controller: منطق التحكم بالعمليات والتدفق.

### Project Structure

```text
mvc/
  __init__.py
  main.py
  model/
    __init__.py
    account.py
    repository.py
  view/
    __init__.py
    cli_view.py
  controller/
    __init__.py
    bank_controller.py
```

### المميزات
- تنظيم ممتاز لتطبيقات فيها واجهة وتدفق تفاعلي.
- فصل جيد يجعل التطوير الجماعي أسهل.

### العيوب
- يحتاج انضباطًا في الفصل بين الأدوار.
- قد يكون زائدًا على مشروع صغير جدًا.

### متى نستخدمها؟
- عندما تريد نمطًا واضحًا للتحكم بالتدفق بين العرض والمنطق والبيانات.

### التشغيل
```bash
python -m mvc.main
```

---

## 4) Microservices (Function Calls Only)

### الفكرة
تقسيم النظام إلى خدمات مستقلة منطقيًا:

- Account Service
- Validation Service
- Transaction Service

> ملاحظة: بدون API حاليًا؛ الربط بين الخدمات عبر استدعاء الدوال فقط.

### Project Structure

```text
microservices/
  __init__.py
  cli.py
  services/
    __init__.py
    account_service.py
    validation_service.py
    transaction_service.py
```

### المميزات
- قابلية فصل وتوسعة عالية.
- كل خدمة لها مسؤولية واحدة واضحة.
- تمهيد ممتاز للانتقال لاحقًا إلى API حقيقية.

### العيوب
- تعقيد تصميم أعلى من Monolith البسيط.
- زيادة تكاليف التنظيم والتواصل بين الخدمات.

### متى نستخدمها؟
- عندما تتوقع نموًا كبيرًا، أو فرق متعددة، أو حاجة لعزل وظائف النظام.

### التشغيل
```bash
python -m microservices.cli
```

---

## Unit Tests

### Project Structure

```text
tests/
  test_spaghetti.py
  test_three_tier.py
  test_mvc.py
  test_microservices.py
```

### الحالات المختبرة لكل معماريّة
- التحويل الناجح
- الرصيد غير الكافي
- حساب غير موجود

### تشغيل الاختبارات
```bash
python -m unittest discover -s tests -p "test_*.py"
```

---

## مقارنة سريعة

- **Spaghetti:** أسرع بداية، أسوأ صيانة.
- **Three-Tier:** توازن ممتاز للتطبيقات المؤسسية.
- **MVC:** قوي لتطبيقات تعتمد تدفق واجهة/تحكم واضح.
- **Microservices:** أفضل قابلية توسع وفصل، لكنه الأعلى تعقيدًا.

إذا كان الهدف تعليميًا: ابدأ بـ Spaghetti لفهم المشكلة، ثم Three-Tier وMVC لفهم التنظيم، ثم Microservices لفهم الفصل المتقدم.

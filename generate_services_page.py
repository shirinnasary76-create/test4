import base64
import json
import os

os.makedirs('/home/user/services', exist_ok=True)

def to_data_uri(path, mime):
    with open(path, 'rb') as f:
        b64 = base64.b64encode(f.read()).decode('ascii')
    return f"data:{mime};base64,{b64}"

font_regular = to_data_uri('/home/user/public/fonts/Vazirmatn-Regular.woff2', 'font/woff2')
font_medium = to_data_uri('/home/user/public/fonts/Vazirmatn-Medium.woff2', 'font/woff2')
font_bold = to_data_uri('/home/user/public/fonts/Vazirmatn-Bold.woff2', 'font/woff2')
font_extrabold = to_data_uri('/home/user/public/fonts/Vazirmatn-ExtraBold.woff2', 'font/woff2')
font_black = to_data_uri('/home/user/public/fonts/Vazirmatn-Black.woff2', 'font/woff2')

img_hero = to_data_uri('/home/user/public/assets/hero-bg.jpg', 'image/jpeg')
img_about = to_data_uri('/home/user/public/assets/about-bg.jpg', 'image/jpeg')
img_card1 = to_data_uri('/home/user/public/assets/card-1.jpg', 'image/jpeg')
img_card2 = to_data_uri('/home/user/public/assets/card-2.jpg', 'image/jpeg')
img_card3 = to_data_uri('/home/user/public/assets/card-3.jpg', 'image/jpeg')
img_card4 = to_data_uri('/home/user/public/assets/card-4.jpg', 'image/jpeg')
img_sub1 = to_data_uri('/home/user/public/assets/subservice-1.jpg', 'image/jpeg')
img_sub2 = to_data_uri('/home/user/public/assets/subservice-2.jpg', 'image/jpeg')
img_sub3 = to_data_uri('/home/user/public/assets/subservice-3.jpg', 'image/jpeg')
img_sub4 = to_data_uri('/home/user/public/assets/subservice-4.jpg', 'image/jpeg')
img_sub5 = to_data_uri('/home/user/public/assets/subservice-5.jpg', 'image/jpeg')
img_logo = to_data_uri('/home/user/public/assets/logo-mark.png', 'image/png')
img_logo_text = to_data_uri('/home/user/public/assets/logo-text.png', 'image/png')
img_logo_full = to_data_uri('/home/user/public/assets/logo-full.png', 'image/png')
img_logo_lightbg = to_data_uri('/home/user/public/assets/logo-lightbg.png', 'image/png')

with open('/home/user/src/styles.css', 'r', encoding='utf-8') as f:
    base_styles = f.read()

SERVICE_GROUPS = [
    {
        "id": "group-industry",
        "num": '<svg width="26" height="26" viewBox="0 0 32 32" fill="none"><circle cx="16" cy="16" r="5" stroke="#fbbf24" stroke-width="2.6"/><circle cx="16" cy="16" r="9.2" stroke="#fff" stroke-width="2.2" stroke-dasharray="4 2.5"/><path d="M16 2.5V6.5M16 25.5V29.5M2.5 16H6.5M25.5 16H29.5M6.4 6.4L9.3 9.3M22.7 22.7L25.6 25.6M25.6 6.4L22.7 9.3M9.3 22.7L6.4 25.6" stroke="#fbbf24" stroke-width="2.8" stroke-linecap="round"/></svg>',
        "title": "خدمات صنعت و مجوزها",
        "subtitle": "همراهی کامل در اخذ مجوزهای تأسیس، بهره‌برداری، طرح‌های توجیهی و پیگیری‌های تخصصی صنعتی",
        "featured": False,
        "cards": [
            {
                "slug": "sodor-javaz-tasis",
                "title": "صدور جواز تأسیس",
                "badge": "صنعت و مجوزها",
                "alt": "صدور جواز تأسیس واحدهای صنعتی و تولیدی در هلدینگ دلگشا راه‌گشا",
                "desc": "مشاوره، تکمیل مستندات و پیگیری مراحل صدور جواز تأسیس واحدهای تولیدی و صنعتی در سامانه‌های رسمی به همراه پیشنهاد کد ISIC متناسب با فعالیت متقاضی.",
                "bg": img_card1,
                "bg_pos": "center center",
                "tint": "linear-gradient(135deg, rgba(6,24,46,0.72) 0%, rgba(244,129,11,0.28) 100%)",
                "icon": '<svg viewBox="0 0 36 36" fill="none"><path d="M9 6H22L28 12V30H9V6Z" stroke="#fbbf24" stroke-width="2.4"/><path d="M13 16H23M13 21H23M13 26H19" stroke="#fff" stroke-width="2.2" stroke-linecap="round"/></svg>',
                "highlights": ["صدور جواز تأسیس صنعتی", "پیشنهاد کد ISIC", "صدور جواز تأسیس فنی و مهندسی", "صدور جواز رمز ارز دیجیتال"]
            },
            {
                "slug": "parvane-bahrebardari-sanat",
                "title": "اخذ پروانه بهره‌برداری",
                "badge": "بهره‌برداری صنعتی",
                "alt": "اخذ پروانه بهره‌برداری صنعتی و تولیدی",
                "desc": "پیگیری مراحل ثبت ظرفیت تولید، تکمیل مدارک فنی، هماهنگی بازدید کارشناسی و اخذ پروانه بهره‌برداری برای کارخانه‌ها و واحدهای تولیدی.",
                "bg": img_sub1,
                "bg_pos": "center top",
                "tint": "linear-gradient(135deg, rgba(5,21,39,0.74) 0%, rgba(14,165,233,0.28) 100%)",
                "icon": '<svg viewBox="0 0 36 36" fill="none"><circle cx="18" cy="18" r="6" stroke="#fbbf24" stroke-width="2.5"/><path d="M18 5V9M18 27V31M5 18H9M27 18H31M8.8 8.8L11.6 11.6M24.4 24.4L27.2 27.2M27.2 8.8L24.4 11.6M11.6 24.4L8.8 27.2" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/></svg>',
                "highlights": ["پروانه بهره‌برداری صنعتی", "صدور پروانه طراحی و مونتاژ آسانسور", "صدور پروانه فنی و مهندسی", "صدور پروانه تحقیق و توسعه (R&D)"]
            },
            {
                "slug": "feasibility-study",
                "title": "تهیه طرح توجیهی صنعتی",
                "badge": "امکان‌سنجی و طرح",
                "alt": "تهیه و تدوین طرح توجیهی فنی، مالی و اقتصادی صنعتی",
                "desc": "تدوین تخصصی طرح توجیهی فنی، مالی و اقتصادی جهت بررسی امکان‌پذیری پروژه، ارائه به بانک‌ها و سازمان‌های ذی‌ربط و جذب سرمایه‌گذار.",
                "bg": img_sub5,
                "bg_pos": "center center",
                "tint": "linear-gradient(135deg, rgba(6,24,46,0.76) 0%, rgba(234,88,12,0.3) 100%)",
                "icon": '<svg viewBox="0 0 36 36" fill="none"><path d="M8 26L15 18L21 22L29 12" stroke="#fbbf24" stroke-width="2.8" stroke-linecap="round"/><rect x="8" y="28" width="4" height="4" fill="#fff"/><rect x="16" y="24" width="4" height="8" fill="#fbbf24"/><rect x="24" y="19" width="4" height="13" fill="#fff"/></svg>',
                "highlights": ["برآورد سرمایه‌گذاری ثابت و در گردش", "تحلیل بازار، درآمدها و هزینه‌های طرح", "تدوین مستندات مطابق فرمت‌های استاندارد"]
            },
            {
                "slug": "industrial-consulting",
                "title": "مشاوره و پیگیری امور صنعتی",
                "badge": "مشاوره تخصصی صنعت",
                "alt": "مشاوره و پیگیری امور صنعتی و مجوزهای تولیدی",
                "desc": "ارائه خدمات مشاوره اجرایی و پیگیری مجوزهای تخصصی صنعتی شامل پروانه فرش دست‌بافت، مجوز توزیع کالای دخانی، توزیع بدون کارخانه و خرید مواد اولیه از بورس.",
                "bg": img_hero,
                "bg_pos": "right center",
                "tint": "linear-gradient(135deg, rgba(9,33,61,0.76) 0%, rgba(251,191,36,0.26) 100%)",
                "icon": '<svg viewBox="0 0 36 36" fill="none"><path d="M7 28H29M9 28V17L16 21V16L22 21V13H27V28" stroke="#fbbf24" stroke-width="2.4" stroke-linejoin="round"/><path d="M13 24H15M19 24H21" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/></svg>',
                "highlights": ["صدور پروانه فرش دست‌بافت", "صدور مجوز توزیع کالای دخانی", "صدور مجوز توزیع بدون کارخانه", "خرید مواد اولیه از بورس"]
            }
        ]
    },
    {
        "id": "group-mining-trade",
        "num": '<svg width="26" height="26" viewBox="0 0 32 32" fill="none"><path d="M3 25L12 9L18 19L22 13L29 25H3Z" stroke="#fbbf24" stroke-width="2.3" fill="rgba(251,191,36,0.22)"/><circle cx="23" cy="9" r="4" stroke="#fff" stroke-width="2"/></svg>',
        "title": "خدمات معدن و تجارت",
        "subtitle": "پوشش یکپارچه امور اکتشاف و بهره‌برداری معادن، سامانه کاداستر، کارت بازرگانی، ثبت سفارش و ترخیص کالا",
        "featured": False,
        "cards": [
            {
                "slug": "parvane-bahrebardari-madan",
                "title": "خدمات و مجوزهای مرتبط با معدن",
                "badge": "معدن و کاداستر",
                "alt": "خدمات و مجوزهای معدن، پروانه بهره‌برداری و گواهی کشف",
                "desc": "انجام امور فنی و اداری معادن از ثبت محدوده‌های معدنی و صدور گواهی کشف تا اخذ پروانه بهره‌برداری، ارسال آمار کاداستر و صدور صلاحیت فنی و مالی.",
                "bg": img_card2,
                "bg_pos": "center center",
                "tint": "linear-gradient(135deg, rgba(6,24,46,0.74) 0%, rgba(245,158,11,0.3) 100%)",
                "icon": '<svg viewBox="0 0 36 36" fill="none"><path d="M4 28L14 10L21 21L25 15L32 28H4Z" stroke="#fbbf24" stroke-width="2.4" fill="rgba(251,191,36,0.2)"/></svg>',
                "highlights": ["صدور پروانه بهره‌برداری و گواهی کشف", "ثبت محدوده و ارسال آمار کاداستر", "بارگذاری طرح و قرارداد مسئول فنی", "ثبت ماشین‌آلات، پرداخت تبصره و صلاحیت فنی"]
            },
            {
                "slug": "kart-bazargani",
                "title": "خدمات تخصصی تجارت",
                "badge": "تجارت و بازرگانی",
                "alt": "خدمات تخصصی تجارت، کارت بازرگانی و ثبت سفارش",
                "desc": "راهبری فرآیندهای بازرگانی در سامانه‌های رسمی؛ شامل صدور و تمدید کارت بازرگانی، صدور توکن، ثبت سفارش، ثبت انبار، آمار تولید و ترخیص کالا.",
                "bg": img_card3,
                "bg_pos": "center center",
                "tint": "linear-gradient(135deg, rgba(5,21,39,0.76) 0%, rgba(56,189,248,0.28) 100%)",
                "icon": '<svg viewBox="0 0 36 36" fill="none"><circle cx="18" cy="18" r="12" stroke="#fbbf24" stroke-width="2.4"/><ellipse cx="18" cy="18" rx="5.5" ry="12" stroke="#fff" stroke-width="2"/><path d="M6.5 14H29.5M6.5 22H29.5" stroke="#fbbf24" stroke-width="2"/></svg>',
                "highlights": ["صدور و تمدید کارت بازرگانی و توکن", "ایجاد پایه حقیقی/حقوقی و کد نقش", "درخواست شناسه، ثبت انبار و ارسال آمار", "ثبت سفارش و ترخیص کالا"]
            },
            {
                "slug": "license-consulting",
                "title": "مشاوره و پیگیری مجوزهای مرتبط با فعالیت متقاضی",
                "badge": "پیگیری و هماهنگی مجوزها",
                "alt": "مشاوره و پیگیری مجوزهای مرتبط با فعالیت متقاضی در صنعت، معدن و تجارت",
                "desc": "بررسی دقیق نوع فعالیت متقاضی، تشخیص پیش‌نیازهای قانونی در حوزه‌های معدن، صنعت و تجارت و پیگیری مرحله‌به‌مرحله پرونده‌ها تا صدور مجوز.",
                "bg": img_sub2,
                "bg_pos": "center center",
                "tint": "linear-gradient(135deg, rgba(8,29,54,0.78) 0%, rgba(244,129,11,0.3) 100%)",
                "icon": '<svg viewBox="0 0 36 36" fill="none"><path d="M18 6L29 11V19C29 25.5 24.2 30.8 18 32C11.8 30.8 7 25.5 7 19V11L18 6Z" stroke="#fbbf24" stroke-width="2.4"/><path d="M13 18.5L16.5 22L23.5 15" stroke="#fff" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>',
                "highlights": ["صدور مجوز بهداشت و استعلامات مرتبط", "تمدید پروانه‌های معدنی و مجوزهای تجاری", "هماهنگی و رفع نواقص پرونده‌های سامانه‌ای"]
            }
        ]
    },
    {
        "id": "group-registration",
        "num": '<svg width="26" height="26" viewBox="0 0 32 32" fill="none"><rect x="7" y="6" width="11" height="20" stroke="#fff" stroke-width="2.2"/><path d="M18 12H25V26H18" stroke="#fbbf24" stroke-width="2.2"/><path d="M10.5 11H14.5M10.5 15.5H14.5M10.5 20H14.5" stroke="#fbbf24" stroke-width="2" stroke-linecap="round"/></svg>',
        "title": "خدمات ثبتی و کسب‌وکار",
        "subtitle": "ثبت رسمی شخصیت حقوقی شرکت‌ها و حفاظت قانونی از نام و علامت تجاری کسب‌وکار شما",
        "featured": False,
        "cards": [
            {
                "slug": "company-registration",
                "title": "ثبت شرکت",
                "badge": "امور ثبتی شرکت‌ها",
                "alt": "خدمات ثبت شرکت و تغییرات ثبتی در هلدینگ راه‌گشا دلگشا",
                "desc": "مشاوره انتخاب قالب حقوقی مناسب (سهامی خاص، مسئولیت محدود، تعاونی و...)، تنظیم اساسنامه و صورتجلسات، و پیگیری مراحل ثبت شرکت و تغییرات.",
                "bg": img_sub4,
                "bg_pos": "left center",
                "tint": "linear-gradient(135deg, rgba(6,24,46,0.78) 0%, rgba(14,165,233,0.3) 100%)",
                "icon": '<svg viewBox="0 0 36 36" fill="none"><rect x="9" y="8" width="12" height="22" stroke="#fff" stroke-width="2.3"/><path d="M21 15H28V30H21" stroke="#fbbf24" stroke-width="2.3"/><path d="M13 13H17M13 18H17M13 23H17" stroke="#fbbf24" stroke-width="2.2" stroke-linecap="round"/></svg>',
                "highlights": ["ثبت انواع شرکت‌های تجاری، صنعتی و مهندسی", "ثبت صورتجلسات تغییرات و افزایش سرمایه", "پیگیری درج آگهی در روزنامه رسمی"]
            },
            {
                "slug": "brand-registration",
                "title": "ثبت برند و علامت تجاری",
                "badge": "مالکیت معنوی و برند",
                "alt": "ثبت برند و علامت تجاری فارسی و لاتین",
                "desc": "استعلام تخصصی پیش از ثبت، تعیین طبقات کالا و خدمات، تشکیل پرونده مالکیت صنعتی و پیگیری مراحل آگهی تا صدور گواهی ثبت علامت تجاری.",
                "bg": img_about,
                "bg_pos": "left center",
                "tint": "linear-gradient(135deg, rgba(6,24,46,0.78) 0%, rgba(251,191,36,0.32) 100%)",
                "icon": '<svg viewBox="0 0 36 36" fill="none"><circle cx="18" cy="16" r="8" stroke="#fff" stroke-width="2.3"/><polygon points="18,11 19.8,14.5 23.5,15 20.8,17.6 21.5,21.2 18,19.4 14.5,21.2 15.2,17.6 12.5,15 16.2,14.5" fill="#fbbf24"/><path d="M13 23L11 31L18 28L25 31L23 23" stroke="#fbbf24" stroke-width="2.2"/></svg>',
                "highlights": ["استعلام تشابه نام و نشان تجاری", "ثبت برند برای اشخاص حقیقی و حقوقی", "تمدید و ثبت تغییرات علامت تجاری"]
            }
        ]
    },
    {
        "id": "group-financial-specialized",
        "num": '<svg width="26" height="26" viewBox="0 0 32 32" fill="none"><rect x="6" y="5" width="16" height="22" rx="2" stroke="#fff" stroke-width="2.2"/><path d="M10 11H18M10 15.5H16M10 20H14" stroke="#fbbf24" stroke-width="2" stroke-linecap="round"/><circle cx="21.5" cy="21.5" r="4.5" fill="#06182e" stroke="#fbbf24" stroke-width="2.2"/><path d="M25 25L28 28" stroke="#fbbf24" stroke-width="2.4" stroke-linecap="round"/></svg>',
        "title": "خدمات مالی و تخصصی",
        "subtitle": "خدمات تخصصی حسابرسی، طراحی و محاسبات مهندسی-صنعتی و تولید محتوای حرفه‌ای کسب‌وکارها",
        "featured": False,
        "cards": [
            {
                "slug": "auditing-services",
                "title": "خدمات حسابرسی",
                "badge": "مالی و حسابرسی",
                "alt": "خدمات حسابرسی و بررسی اسناد مالی شرکت‌ها و صنایع",
                "desc": "بررسی اسناد و مدارک مالی، تنظیم گزارش‌های حسابرسی، مشاوره مالیاتی و سامان‌دهی امور مالی متناسب با قوانین و نیازهای واحدهای صنعتی و تجاری.",
                "bg": img_sub5,
                "bg_pos": "right center",
                "tint": "linear-gradient(135deg, rgba(5,20,38,0.8) 0%, rgba(245,158,11,0.28) 100%)",
                "icon": '<svg viewBox="0 0 36 36" fill="none"><rect x="8" y="6" width="18" height="24" rx="2" stroke="#fff" stroke-width="2.3"/><path d="M12 12H22M12 17H19M12 22H16" stroke="#fbbf24" stroke-width="2.2" stroke-linecap="round"/><circle cx="24" cy="24" r="5" fill="#06182e" stroke="#fbbf24" stroke-width="2.3"/><path d="M27.8 27.8L31 31" stroke="#fbbf24" stroke-width="2.5" stroke-linecap="round"/></svg>',
                "highlights": ["بررسی و کنترل صورت‌های مالی", "مشاوره پرونده‌های مالیاتی و تکالیف قانونی", "تهیه گزارش‌های مالی جهت ارائه به مراجع ذی‌ربط"]
            },
            {
                "slug": "engineering-design-calculation",
                "title": "طراحی و محاسبات تخصصی",
                "badge": "محاسبات فنی و صنعتی",
                "alt": "طراحی و محاسبات تخصصی صنعتی و مهندسی",
                "desc": "انجام محاسبات فنی و مهندسی، طراحی فرآیندها و جانمایی تجهیزات، و تهیه مستندات و نقشه‌های فنی موردنیاز پروژه‌های صنعتی و تولیدی.",
                "bg": img_sub3,
                "bg_pos": "right center",
                "tint": "linear-gradient(135deg, rgba(6,24,46,0.76) 0%, rgba(56,189,248,0.3) 100%)",
                "icon": '<svg viewBox="0 0 36 36" fill="none"><path d="M8 28L28 8V28H8Z" stroke="#fff" stroke-width="2.4" stroke-linejoin="round"/><path d="M18 28V22H24" stroke="#fbbf24" stroke-width="2.2"/></svg>',
                "highlights": ["طراحی جانمایی ماشین‌آلات و خطوط تولید", "محاسبات ظرفیت و بهره‌وری فنی", "تهیه نقشه‌ها و مدارک مهندسی"]
            },
            {
                "slug": "content-production",
                "title": "تولید محتوا و خدمات محتوایی",
                "badge": "محتوا و معرفی کسب‌وکار",
                "alt": "تولید محتوا و خدمات محتوایی تخصصی برای صنایع و شرکت‌ها",
                "desc": "تهیه و تدوین محتوای تخصصی متنی، تصویری و معرفی خدمات و محصولات، متناسب با نیازهای ارتباطی و اطلاع‌رسانی شرکت‌ها و واحدهای صنعتی.",
                "bg": img_hero,
                "bg_pos": "left center",
                "tint": "linear-gradient(135deg, rgba(8,27,51,0.78) 0%, rgba(234,88,12,0.32) 100%)",
                "icon": '<svg viewBox="0 0 36 36" fill="none"><rect x="6" y="9" width="24" height="17" rx="2.5" stroke="#fff" stroke-width="2.3"/><polygon points="15,14 22,17.5 15,21" fill="#fbbf24"/><path d="M12 30H24" stroke="#fbbf24" stroke-width="2.4" stroke-linecap="round"/></svg>',
                "highlights": ["تدوین محتوای معرفی شرکت و محصولات صنعتی", "آماده‌سازی محتوای کاتالوگ و درگاه‌های اطلاع‌رسانی", "نگارش تخصصی متون فنی و بازرگانی"]
            }
        ]
    },
    {
        "id": "group-engineering",
        "num": '<svg width="26" height="26" viewBox="0 0 32 32" fill="none"><path d="M5 22C5 15.4 9.9 10 16 10C22.1 10 27 15.4 27 22H5Z" stroke="#fbbf24" stroke-width="2.5" stroke-linejoin="round"/><path d="M13.5 10V7.5C13.5 6.7 14.2 6 15 6H17C17.8 6 18.5 6.7 18.5 7.5V10" stroke="#fff" stroke-width="2.2"/><path d="M3 22.5H29" stroke="#fbbf24" stroke-width="2.8" stroke-linecap="round"/></svg>',
        "title": "خدمات فنی و مهندسی",
        "subtitle": "بخش مستقل و تخصصی طراحی سازه، اجرای سوله کارخانه، نقشه‌برداری، دکوراسیون و پیمانکاری ساختمان",
        "featured": True,
        "cards": [
            {
                "slug": "structural-design",
                "title": "طراحی سازه ساختمان",
                "badge": "مهندسی سازه",
                "alt": "طراحی سازه ساختمان و محاسبات سازه‌ای فولادی و بتنی",
                "desc": "طراحی و محاسبات سازه‌ای متناسب با مشخصات پروژه و ضوابط فنی مربوطه.",
                "bg": img_card4,
                "bg_pos": "center center",
                "tint": "linear-gradient(135deg, rgba(4,18,34,0.68) 0%, rgba(245,158,11,0.34) 100%)",
                "icon": '<svg viewBox="0 0 36 36" fill="none"><path d="M6 30H30M9 30V10L18 6L27 10V30" stroke="#fbbf24" stroke-width="2.4"/><path d="M9 16H27M9 22H27M18 6V30" stroke="#fff" stroke-width="1.8" stroke-dasharray="3 2"/></svg>',
                "highlights": ["مدلسازی و تحلیل سازه‌های بتنی و فولادی", "رعایت ضوابط فنی و مقررات ملی ساختمان", "ارائه نقشه‌های اجرایی و دفترچه محاسبات سازه"]
            },
            {
                "slug": "industrial-shed",
                "title": "طراحی و اجرای سوله کارخانه",
                "badge": "سوله‌های صنعتی",
                "alt": "طراحی و اجرای سوله کارخانه و سازه‌های صنعتی",
                "desc": "ارائه خدمات طراحی و اجرای سوله‌های صنعتی متناسب با نیاز پروژه، کاربری و مشخصات فنی آن.",
                "bg": img_sub4,
                "bg_pos": "center center",
                "tint": "linear-gradient(135deg, rgba(6,24,46,0.72) 0%, rgba(234,88,12,0.36) 100%)",
                "icon": '<svg viewBox="0 0 36 36" fill="none"><path d="M4 29V15L18 8L32 15V29" stroke="#fbbf24" stroke-width="2.5" stroke-linejoin="round"/><path d="M4 29H32M11 29V19H25V29" stroke="#fff" stroke-width="2.2"/><path d="M11 15L18 11.5L25 15" stroke="#fbbf24" stroke-width="2"/></svg>',
                "highlights": ["طراحی دهانه، ارتفاع و سازه سوله متناسب با کاربری", "ساخت و نصب اسکلت فلزی سوله کارخانه", "اجرای پوشش سقف، دیواره‌ها و فونداسیون صنعتی"]
            },
            {
                "slug": "surveying",
                "title": "نقشه‌برداری",
                "badge": "اطلاعات مکانی و عمرانی",
                "alt": "خدمات نقشه‌برداری پروژه‌های ساختمانی، صنعتی و عمرانی",
                "desc": "ارائه خدمات نقشه‌برداری و تهیه اطلاعات مکانی موردنیاز پروژه‌های ساختمانی و عمرانی.",
                "bg": img_sub3,
                "bg_pos": "left bottom",
                "tint": "linear-gradient(135deg, rgba(5,21,39,0.72) 0%, rgba(14,165,233,0.34) 100%)",
                "icon": '<svg viewBox="0 0 36 36" fill="none"><circle cx="18" cy="13" r="5" stroke="#fbbf24" stroke-width="2.4"/><circle cx="18" cy="13" r="1.8" fill="#fff"/><path d="M18 18L11 30M18 18L25 30M18 18V29" stroke="#fff" stroke-width="2.3" stroke-linecap="round"/></svg>',
                "highlights": ["برداشت توپوگرافی و تهیه نقشه‌های وضع موجود", "تعیین حدود اراضی و مختصات دقیق مکانی", "پیاده‌سازی محورهای اجرایی فونداسیون و سازه"]
            },
            {
                "slug": "interior-design",
                "title": "دکوراسیون",
                "badge": "طراحی دکوراسیون داخلی",
                "alt": "طراحی و اجرای دکوراسیون داخلی فضاهای اداری، تجاری و مسکونی",
                "desc": "ارائه خدمات طراحی دکوراسیون داخلی متناسب با فضای موردنظر، نیاز کارفرما و سبک پروژه.",
                "bg": img_sub5,
                "bg_pos": "left top",
                "tint": "linear-gradient(135deg, rgba(8,27,51,0.74) 0%, rgba(251,191,36,0.32) 100%)",
                "icon": '<svg viewBox="0 0 36 36" fill="none"><rect x="6" y="8" width="24" height="20" rx="2" stroke="#fff" stroke-width="2.2"/><path d="M6 21H30M16 8V21" stroke="#fbbf24" stroke-width="2.2"/><circle cx="23" cy="14" r="2.5" stroke="#fbbf24" stroke-width="2"/></svg>',
                "highlights": ["طراحی پلان چیدمان و دیدهای سه‌بعدی داخلی", "انتخاب متریال، رنگ‌بندی و نورپردازی متناسب با فضا", "اجرا و بازسازی فضاهای اداری، تجاری و ساختمانی"]
            },
            {
                "slug": "building-contractor",
                "title": "پیمانکاری صفر تا صد ساختمان",
                "badge": "مدیریت و اجرای ساختمان",
                "alt": "پیمانکاری صفر تا صد ساختمان و مدیریت اجرای پروژه",
                "desc": "مدیریت و اجرای مراحل پروژه ساختمانی از شروع عملیات تا تکمیل، مطابق قرارداد و محدوده خدمات مورد توافق.",
                "bg": img_sub1,
                "bg_pos": "center center",
                "tint": "linear-gradient(135deg, rgba(5,20,38,0.75) 0%, rgba(244,129,11,0.35) 100%)",
                "icon": '<svg viewBox="0 0 36 36" fill="none"><path d="M8 24C8 18.5 12.5 14 18 14C23.5 14 28 18.5 28 24H8Z" stroke="#fbbf24" stroke-width="2.5"/><path d="M6 24.5H30" stroke="#fff" stroke-width="2.8" stroke-linecap="round"/><path d="M16 14V11H20V14" stroke="#fbbf24" stroke-width="2.2"/></svg>',
                "highlights": ["مدیریت اجرایی پروژه از فونداسیون تا تکمیل", "هماهنگی اکیپ‌های اجرایی، تأسیسات و نازک‌کاری", "اجرای دقیق مطابق قرارداد و ضوابط فنی"]
            }
        ]
    }
]

FULL_38_SERVICES = [
    ("صنعت", "صدور جواز تاسیس", "sodor-javaz-tasis"),
    ("صنعت", "پروانه بهره برداری", "parvane-bahrebardari-sanat"),
    ("صنعت", "صدور پروانه فرش دست بافت", "parvane-farsh-dastbaft"),
    ("صنعت", "صدور مجوز توزیع کالای دخانی", "mojavez-tozi-kala-dokhani"),
    ("صنعت", "صدور مجوز توزیع بدون کارخانه", "mojavez-tozi-bedone-karkhane"),
    ("صنعت", "صدور پروانه طراحی و منتاج آسانسور", "parvane-tarahi-montazh-asansor"),
    ("صنعت", "صدور پروانه فنی و مهندسی", "parvane-fanni-mohandesi"),
    ("صنعت", "صدور پروانه تحقیق و توسعه (R&D)", "parvane-tahghigh-tosee-rd"),
    ("صنعت", "صدور جواز تاسیس فنی و مهندسی", "javaz-tasis-fanni-mohandesi"),
    ("صنعت", "خرید مواد اولیه از بورس", "kharid-mavad-avali-bourse"),
    ("صنعت", "پیشنهاد کد isic", "pishnahad-code-isic"),
    ("صنعت", "صدور جواز رمز ارز دیجیتال", "javaz-ramzarz-digital"),
    ("معدن", "صدور پروانه بهره برداری", "parvane-bahrebardari-madan"),
    ("معدن", "صدور گواهی کشف", "govahi-kashf-madan"),
    ("معدن", "صدور مجوز بهداشت", "mojavez-behdasht-madan"),
    ("معدن", "تمدید پروانه های معدنی", "tamdid-parvane-madani"),
    ("معدن", "ارسال آمار کاداستر", "ersal-amar-cadastre"),
    ("معدن", "ثبت محدوده های معدنی", "sabt-mahdode-madani"),
    ("معدن", "بارگذاری قراردادهای مسئول فنی", "bargozari-gharardad-masool-fanni"),
    ("معدن", "بارگذاری طرح", "bargozari-tarh-madani"),
    ("معدن", "ثبت ماشین آلات معدنی", "sabt-mashin-alat-madani"),
    ("معدن", "پرداخت تبصره", "pardakht-tabsare-madan"),
    ("معدن", "صدور صلاحیت فنی و مالی", "salahiyat-fanni-mali-madan"),
    ("تجارت", "صدور و تمدید توکن", "sodor-tamdid-token"),
    ("تجارت", "ایجاد پایه حقیقی و حقوقی", "ijad-paye-haghighi-hoghoghi"),
    ("تجارت", "ایجاد کد نقش", "ijad-code-naghsh"),
    ("تجارت", "درخواست شناسه", "darkhast-shenase"),
    ("تجارت", "ارسال آمار", "ersal-amar-tejarat"),
    ("تجارت", "ثبت انبار", "sabt-anbar"),
    ("تجارت", "آمار تولید", "amar-tolid"),
    ("تجارت", "ثبت سفارش", "sabt-sefaresh"),
    ("تجارت", "صدور و تمدید کارت بازرگانی", "kart-bazargani"),
    ("تجارت", "ترخیص کالا", "tarkhis-kala"),
    ("فنی و مهندسی", "طراحی سازه ساختمان", "structural-design"),
    ("فنی و مهندسی", "طراحی و اجراء سوله کارخانه", "industrial-shed"),
    ("فنی و مهندسی", "نقشه برداری", "surveying"),
    ("فنی و مهندسی", "دکوراسیون", "interior-design"),
    ("فنی و مهندسی", "پیمانکاری صفر تا صد ساختمان", "building-contractor"),
]

FAQ_ITEMS = [
    {
        "cat": "صنعت و مجوزها",
        "q": "برای دریافت جواز تأسیس چه مدارکی لازم است؟",
        "a": "برای اشخاص حقیقی مدارک هویتی (شناسنامه، کارت ملی و وضعیت نظام وظیفه) و برای اشخاص حقوقی اساسنامه، آگهی تأسیس، روزنامه رسمی، آخرین تغییرات شرکت و مدارک هویتی صاحبان امضا به همراه مشخصات طرح تولیدی، فهرست ماشین‌آلات و کد ISIC محصول موردنیاز است."
    },
    {
        "cat": "صنعت و مجوزها",
        "q": "تفاوت جواز تأسیس و پروانه بهره‌برداری چیست؟",
        "a": "جواز تأسیس مجوز موافقت اولیه برای احداث واحد تولیدی، تخصیص زمین در شهرک‌های صنعتی و نصب ماشین‌آلات است؛ اما پروانه بهره‌برداری پس از اتمام ساخت‌وساز، نصب تجهیزات، تأمین نیروی انسانی و تولید آزمایشی صادر می‌شود و مجوز رسمی شروع بهره‌برداری و تولید واحد صنعتی است."
    },
    {
        "cat": "صنعت و مجوزها",
        "q": "طرح توجیهی صنعتی چه کاربردی دارد؟",
        "a": "طرح توجیهی صنعتی ابعاد فنی، بازار و مالی پروژه را به صورت مستند بررسی می‌کند تا توجیه‌پذیری اجرای طرح مشخص شود. این سند برای اخذ جواز تأسیس، پذیرش در شهرک‌های صنعتی، جذب سرمایه‌گذار و بررسی پرونده‌های تسهیلات بانکی کاربرد مستقیم دارد."
    },
    {
        "cat": "ثبتی و کسب‌وکار",
        "q": "ثبت شرکت و ثبت برند چه تفاوتی دارند؟",
        "a": "ثبت شرکت به معنای ایجاد یک شخصیت حقوقی رسمی (مانند سهامی خاص یا با مسئولیت محدود) برای فعالیت قانونی کسب‌وکار است؛ در حالی که ثبت برند (علامت تجاری) برای حفاظت قانونی از نام و نشان تجاری محصولات یا خدمات شما در برابر استفاده سایرین انجام می‌شود."
    },
    {
        "cat": "فنی و مهندسی",
        "q": "طراحی سازه ساختمان شامل چه مراحلی است؟",
        "a": "شامل بررسی نقشه‌های معماری و مشخصات ژئوتکنیکی زمین، انتخاب سیستم سازه‌ای متناسب با پروژه، بارگذاری و تحلیل سازه بر اساس ضوابط فنی و مقررات ملی ساختمان، طراحی مقاطع و اتصالات، و در نهایت تهیه نقشه‌های اجرایی سازه و دفترچه محاسبات است."
    },
    {
        "cat": "فنی و مهندسی",
        "q": "برای طراحی و اجرای سوله صنعتی چه اطلاعاتی لازم است؟",
        "a": "ابعاد زمین، عرض دهانه و طول سوله، ارتفاع مفید موردنیاز، نوع کاربری صنعتی یا انبارداری، نیاز به جرثقیل سقفی و ظرفیت آن، و شرایط اقلیمی محل اجرا (بار باد و برف) از اطلاعات اصلی برای طراحی و اجرای سوله کارخانه هستند."
    },
    {
        "cat": "فنی و مهندسی",
        "q": "نقشه‌برداری در پروژه‌های ساختمانی چه کاربردی دارد؟",
        "a": "نقشه‌برداری برای برداشت وضع موجود زمین، تعیین دقیق حدود و مختصات ملک، تهیه نقشه‌های توپوگرافی، محاسبه احجام عملیات خاکی و پیاده‌سازی دقیق محورهای فونداسیون، ستون‌ها و ترازهای اجرایی ساختمان در طول پروژه به کار می‌رود."
    },
    {
        "cat": "فنی و مهندسی",
        "q": "پیمانکاری صفر تا صد ساختمان شامل چه خدماتی می‌شود؟",
        "a": "شامل برنامه‌ریزی، هماهنگی و اجرای مراحل پروژه ساختمانی از آماده‌سازی کارگاه، عملیات خاکی و فونداسیون تا اجرای اسکلت، سفت‌کاری، تأسیسات مکانیکی و برقی، نازک‌کاری و تکمیل پروژه مطابق با قرارداد و محدوده خدمات مورد توافق با کارفرما است."
    },
    {
        "cat": "عمومی و مشاوره",
        "q": "چگونه می‌توان درخواست مشاوره ثبت کرد؟",
        "a": "شما می‌توانید از طریق دکمه «درخواست مشاوره» در هدر سایت یا فرم ثبت درخواست در همین صفحه، موضوع فعالیت و شماره تماس خود را وارد کنید و یا در ساعات پاسخگویی (۸ الی ۱۶) با شماره ۰۹۱۷۷۰۵۶۰۶۳ تماس بگیرید."
    }
]

# Dedicated CSS for the Comprehensive Services Page (scoped with .srv-* classes so zero collision with homepage)
services_page_css = '''
/* ==========================================================================
   Comprehensive Services Page Scoped Styles (.srv-*)
   ========================================================================== */
.srv-breadcrumb-bar {
  background: rgba(5, 21, 39, 0.96);
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  padding: 10px 0;
  font-size: 12.5px;
  color: rgba(255, 255, 255, 0.78);
}

.srv-breadcrumb-list {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
}

.srv-breadcrumb-list a {
  color: var(--orange-400);
  font-weight: 700;
}

.srv-breadcrumb-list a:hover {
  text-decoration: underline;
}

/* 1. SERVICES HERO BANNER */
.srv-hero {
  position: relative;
  min-height: 430px;
  background-color: var(--navy-950);
  background-size: cover;
  background-position: center;
  display: flex;
  align-items: center;
  padding: 56px 0 72px;
  overflow: hidden;
}

.srv-hero-backdrop {
  position: absolute;
  inset: 0;
  background: radial-gradient(circle at 22% 35%, rgba(245, 158, 11, 0.18) 0%, rgba(5, 21, 39, 0) 45%),
              linear-gradient(90deg, rgba(4, 18, 34, 0.92) 0%, rgba(6, 24, 46, 0.88) 55%, rgba(6, 24, 46, 0.74) 100%);
  pointer-events: none;
}

.srv-hero-grid {
  position: relative;
  z-index: 2;
  display: grid;
  grid-template-columns: 1.25fr 0.95fr;
  gap: 36px;
  align-items: center;
}

.srv-hero-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: rgba(245, 158, 11, 0.14);
  border: 1px solid rgba(251, 191, 36, 0.45);
  color: var(--orange-400);
  font-size: 13px;
  font-weight: 800;
  padding: 6px 16px;
  border-radius: 999px;
  margin-bottom: 16px;
}

.srv-hero-h1 {
  font-size: 38px;
  font-weight: 900;
  color: var(--white);
  line-height: 1.38;
  margin-bottom: 16px;
  text-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
}

.srv-hero-lead {
  font-size: 15px;
  font-weight: 500;
  color: rgba(255, 255, 255, 0.92);
  line-height: 2;
  margin-bottom: 28px;
  max-width: 640px;
}

.srv-hero-actions {
  display: flex;
  align-items: center;
  gap: 14px;
  flex-wrap: wrap;
}

.srv-btn-primary {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  background: linear-gradient(135deg, #fbbf24 0%, #f4810b 100%);
  color: var(--navy-950);
  font-size: 14.5px;
  font-weight: 900;
  padding: 12px 28px;
  border-radius: 999px;
  box-shadow: 0 10px 26px rgba(244, 129, 11, 0.38);
  transition: all 0.25s ease;
}

.srv-btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 14px 32px rgba(244, 129, 11, 0.55);
}

.srv-btn-secondary {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  background: rgba(255, 255, 255, 0.08);
  border: 1.5px solid rgba(251, 191, 36, 0.65);
  color: var(--white);
  font-size: 14.5px;
  font-weight: 800;
  padding: 11px 26px;
  border-radius: 999px;
  backdrop-filter: blur(6px);
  transition: all 0.25s ease;
}

.srv-btn-secondary:hover {
  background: var(--orange-500);
  border-color: var(--orange-500);
  color: var(--navy-950);
  transform: translateY(-2px);
}

/* 3D Showcase Visual Stack on Left of Hero */
.srv-hero-3d-showcase {
  perspective: 1100px;
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 14px;
}

.srv-hero-mini-card {
  background: rgba(9, 33, 61, 0.78);
  border: 1px solid rgba(255, 255, 255, 0.16);
  border-radius: 16px;
  padding: 10px;
  backdrop-filter: blur(10px);
  box-shadow: 0 18px 38px rgba(0, 0, 0, 0.38);
  transform: rotateY(6deg) rotateX(3deg);
  transition: transform 0.35s ease, border-color 0.35s ease;
}

.srv-hero-mini-card:hover {
  transform: rotateY(0deg) rotateX(0deg) translateY(-5px);
  border-color: var(--orange-400);
}

.srv-hero-mini-card img {
  width: 100%;
  aspect-ratio: 4 / 3;
  object-fit: contain;
  background: var(--navy-950);
  border-radius: 10px;
  display: block;
  margin-bottom: 8px;
}

.srv-hero-mini-card span {
  display: block;
  text-align: center;
  font-size: 12px;
  font-weight: 800;
  color: var(--white);
}

/* 2. QUICK FILTER & SEARCH BAR */
.srv-filter-bar-wrap {
  margin-top: -28px;
  position: relative;
  z-index: 10;
  margin-bottom: 36px;
}

.srv-filter-bar {
  background: var(--white);
  border-radius: 20px;
  padding: 16px 22px;
  box-shadow: 0 16px 42px rgba(6, 24, 46, 0.1);
  border: 1px solid #e2e8f0;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  flex-wrap: wrap;
}

.srv-filter-pills {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
}

.srv-filter-pill {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  padding: 8px 16px;
  border-radius: 999px;
  font-size: 12.8px;
  font-weight: 800;
  color: var(--navy-850);
  background: #f1f5f9;
  transition: all 0.2s ease;
}

.srv-filter-pill svg {
  width: 15px;
  height: 15px;
  flex-shrink: 0;
  color: var(--orange-500);
}

.srv-filter-pill:hover svg,
.srv-filter-pill.active svg {
  color: var(--orange-400);
}

.srv-filter-pill:hover,
.srv-filter-pill.active {
  background: var(--navy-850);
  color: var(--orange-400);
}

.srv-inline-search {
  position: relative;
  min-width: 260px;
  flex: 1;
  max-width: 340px;
}

.srv-inline-search input {
  width: 100%;
  padding: 9px 16px 9px 36px;
  border-radius: 999px;
  border: 1.5px solid #cbd5e1;
  font-family: inherit;
  font-size: 13px;
  background: #f8fafc;
}

.srv-inline-search input:focus {
  outline: none;
  border-color: var(--orange-500);
  background: var(--white);
}

/* 3. SERVICE GROUP SECTIONS */
.srv-group-section {
  padding: 28px 0 42px;
}

.srv-group-header {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  gap: 16px;
  margin-bottom: 24px;
  border-bottom: 2px solid #e2e8f0;
  padding-bottom: 14px;
  flex-wrap: wrap;
}

.srv-group-title-wrap {
  display: flex;
  align-items: center;
  gap: 14px;
}

.srv-group-num {
  width: 46px;
  height: 46px;
  border-radius: 12px;
  background: linear-gradient(135deg, #09213d 0%, #051527 100%);
  border: 1.5px solid var(--orange-450);
  color: var(--orange-400);
  font-size: 19px;
  font-weight: 900;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  box-shadow: 0 6px 16px rgba(6, 24, 46, 0.16);
}

.srv-group-h2 {
  font-size: 24px;
  font-weight: 900;
  color: var(--navy-850);
  line-height: 1.35;
}

.srv-group-sub {
  font-size: 13.5px;
  font-weight: 500;
  color: var(--slate-600);
  margin-top: 4px;
}

.srv-cards-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(295px, 1fr));
  gap: 24px;
  perspective: 1100px;
}

/* 4. 3D SERVICE CARD DESIGN */
.srv-card {
  background: var(--white);
  border-radius: 20px;
  padding: 10px 10px 20px;
  border: 1px solid rgba(226, 232, 240, 0.95);
  box-shadow: 0 12px 32px rgba(6, 24, 46, 0.07), 0 2px 8px rgba(6, 24, 46, 0.04);
  display: flex;
  flex-direction: column;
  transition: transform 0.32s cubic-bezier(0.22, 1, 0.36, 1), box-shadow 0.32s ease, border-color 0.32s ease;
  transform-style: preserve-3d;
}

.srv-card:hover {
  transform: translateY(-7px) rotateX(2deg);
  box-shadow: 0 22px 46px rgba(6, 24, 46, 0.14), 0 8px 20px rgba(244, 129, 11, 0.12);
  border-color: rgba(244, 129, 11, 0.45);
}

.srv-card-visual {
  position: relative;
  width: 100%;
  aspect-ratio: 4 / 3;
  border-radius: 14px;
  overflow: hidden;
  background: var(--navy-950);
  box-shadow: 0 8px 20px rgba(4, 18, 34, 0.2);
}

.srv-card-bg-img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  background: var(--navy-950);
  display: block;
  transition: transform 0.45s ease;
}

.srv-card:hover .srv-card-bg-img {
  transform: scale(1.03);
}

.srv-card-tint {
  position: absolute;
  inset: 0;
  pointer-events: none;
  opacity: 0.38;
  transition: opacity 0.3s ease;
}

.srv-card:hover .srv-card-tint {
  opacity: 0.2;
}

.srv-card-cat-pill {
  position: absolute;
  top: 12px;
  right: 12px;
  background: rgba(5, 21, 39, 0.86);
  border: 1px solid rgba(251, 191, 36, 0.55);
  color: var(--orange-400);
  font-size: 11.5px;
  font-weight: 800;
  padding: 4px 12px;
  border-radius: 999px;
  backdrop-filter: blur(6px);
  z-index: 2;
}

.srv-card-floating-icon {
  position: absolute;
  bottom: 12px;
  left: 12px;
  width: 44px;
  height: 44px;
  border-radius: 12px;
  background: rgba(6, 24, 46, 0.9);
  border: 1.5px solid rgba(255, 255, 255, 0.22);
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 6px 16px rgba(0, 0, 0, 0.35);
  z-index: 2;
}

.srv-card-floating-icon svg {
  width: 26px;
  height: 26px;
}

.srv-card-body {
  padding: 18px 12px 0;
  display: flex;
  flex-direction: column;
  flex: 1;
}

.srv-card-h3 {
  font-size: 18.5px;
  font-weight: 900;
  color: var(--navy-850);
  margin-bottom: 10px;
  line-height: 1.4;
}

.srv-card-desc {
  font-size: 13.2px;
  font-weight: 500;
  color: var(--slate-600);
  line-height: 1.9;
  margin-bottom: 14px;
}

.srv-card-highlights {
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 12px;
  padding: 10px 14px;
  margin-bottom: 18px;
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.srv-card-highlights li {
  font-size: 12px;
  font-weight: 600;
  color: var(--navy-850);
  display: flex;
  align-items: center;
  gap: 7px;
}

.srv-card-highlights li::before {
  content: '◆';
  color: var(--orange-500);
  font-size: 9px;
}

.srv-card-footer {
  margin-top: auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
  padding-top: 10px;
  border-top: 1px solid #eef2f7;
}

.srv-btn-details {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  width: 100%;
  padding: 10px 18px;
  border-radius: 12px;
  background: linear-gradient(135deg, #09213d 0%, #0d2b4e 100%);
  color: var(--white);
  font-size: 13.2px;
  font-weight: 800;
  transition: all 0.25s ease;
}

.srv-card:hover .srv-btn-details {
  background: linear-gradient(135deg, #f4810b 0%, #ea580c 100%);
  color: var(--white);
  box-shadow: 0 6px 18px rgba(234, 88, 12, 0.32);
}

/* 5. FEATURED GROUP 5: ENGINEERING SHOWCASE SECTION */
.srv-engineering-showcase {
  background: linear-gradient(180deg, #05162a 0%, #092342 50%, #051527 100%);
  padding: 52px 0 58px;
  color: var(--white);
  position: relative;
  overflow: hidden;
  border-top: 2px solid rgba(251, 191, 36, 0.35);
  border-bottom: 2px solid rgba(251, 191, 36, 0.35);
}

.srv-engineering-showcase .srv-group-header {
  border-bottom-color: rgba(255, 255, 255, 0.14);
}

.srv-engineering-showcase .srv-group-h2 {
  color: var(--orange-400);
}

.srv-engineering-showcase .srv-group-sub {
  color: rgba(255, 255, 255, 0.85);
}

.srv-engineering-showcase .srv-card {
  background: rgba(13, 43, 78, 0.72);
  border-color: rgba(251, 191, 36, 0.28);
  backdrop-filter: blur(10px);
}

.srv-engineering-showcase .srv-card-h3 {
  color: var(--white);
}

.srv-engineering-showcase .srv-card-desc {
  color: rgba(255, 255, 255, 0.85);
}

.srv-engineering-showcase .srv-card-highlights {
  background: rgba(5, 21, 39, 0.65);
  border-color: rgba(255, 255, 255, 0.12);
}

.srv-engineering-showcase .srv-card-highlights li {
  color: #e2e8f0;
}

.srv-engineering-showcase .srv-card-footer {
  border-top-color: rgba(255, 255, 255, 0.12);
}

.srv-engineering-showcase .srv-btn-details {
  background: linear-gradient(135deg, #fbbf24 0%, #f4810b 100%);
  color: var(--navy-950);
}

/* 6. COMPLETE 38-SERVICE DIRECTORY MATRIX */
.srv-directory-section {
  padding: 48px 0;
  background: var(--white);
  border-bottom: 1px solid #e2e8f0;
}

.srv-directory-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 20px;
}

.srv-dir-col {
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 16px;
  padding: 18px;
}

.srv-dir-col-title {
  font-size: 17px;
  font-weight: 900;
  color: var(--navy-850);
  padding-bottom: 10px;
  margin-bottom: 12px;
  border-bottom: 2px solid var(--orange-450);
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.srv-dir-links {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.srv-dir-link {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 8px 10px;
  border-radius: 8px;
  font-size: 12.8px;
  font-weight: 600;
  color: var(--navy-850);
  background: var(--white);
  border: 1px solid #edf2f7;
  transition: all 0.2s ease;
}

.srv-dir-link:hover {
  border-color: var(--orange-450);
  color: var(--orange-600);
  transform: translateX(-3px);
}

/* 7. 5-STEP PROCESS SECTION ("مسیر دریافت خدمات") */
.srv-process-section {
  padding: 52px 0;
  background: linear-gradient(180deg, #eef4fb 0%, #f6f9fc 100%);
}

.srv-process-tabs {
  display: flex;
  justify-content: center;
  gap: 12px;
  margin-bottom: 32px;
  flex-wrap: wrap;
}

.srv-process-tab {
  padding: 10px 22px;
  border-radius: 999px;
  font-size: 13.5px;
  font-weight: 800;
  background: var(--white);
  color: var(--navy-850);
  border: 1.5px solid #cbd5e1;
  transition: all 0.2s ease;
}

.srv-process-tab.active {
  background: var(--navy-850);
  color: var(--orange-400);
  border-color: var(--navy-850);
  box-shadow: 0 8px 20px rgba(6, 24, 46, 0.18);
}

.srv-steps-grid {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 18px;
  position: relative;
}

.srv-step-card {
  background: var(--white);
  border-radius: 18px;
  padding: 24px 18px;
  text-align: center;
  border: 1px solid #e2e8f0;
  box-shadow: 0 10px 28px rgba(6, 24, 46, 0.06);
  position: relative;
  transition: transform 0.25s ease;
}

.srv-step-card:hover {
  transform: translateY(-5px);
  border-color: var(--orange-450);
}

.srv-step-num {
  width: 52px;
  height: 52px;
  border-radius: 50%;
  background: linear-gradient(135deg, #fbbf24 0%, #f4810b 100%);
  color: var(--navy-950);
  font-size: 20px;
  font-weight: 900;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 14px;
  box-shadow: 0 6px 16px rgba(244, 129, 11, 0.35);
}

.srv-step-title {
  font-size: 15px;
  font-weight: 900;
  color: var(--navy-850);
  margin-bottom: 8px;
}

.srv-step-desc {
  font-size: 12.5px;
  font-weight: 500;
  color: var(--slate-600);
  line-height: 1.85;
}

/* 8. FAQ ACCORDION SECTION ("پرسش‌های متداول") */
.srv-faq-section {
  padding: 52px 0;
  background: var(--white);
}

.srv-faq-list {
  max-width: 920px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.srv-faq-item {
  border: 1px solid #e2e8f0;
  border-radius: 14px;
  background: #f8fafc;
  overflow: hidden;
  transition: border-color 0.2s ease, background-color 0.2s ease;
}

.srv-faq-item.open {
  border-color: var(--orange-450);
  background: var(--white);
  box-shadow: 0 8px 24px rgba(6, 24, 46, 0.06);
}

.srv-faq-question {
  width: 100%;
  padding: 16px 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  text-align: right;
  font-size: 14.5px;
  font-weight: 800;
  color: var(--navy-850);
}

.srv-faq-cat-tag {
  font-size: 11px;
  font-weight: 700;
  padding: 3px 10px;
  border-radius: 999px;
  background: rgba(244, 129, 11, 0.14);
  color: var(--orange-600);
  margin-left: 8px;
}

.srv-faq-answer {
  display: none;
  padding: 0 20px 18px;
  font-size: 13.5px;
  font-weight: 500;
  color: var(--slate-700);
  line-height: 2;
  border-top: 1px solid #f1f5f9;
}

.srv-faq-item.open .srv-faq-answer {
  display: block;
}

@media (max-width: 1100px) {
  .srv-hero-grid {
    grid-template-columns: 1fr;
  }
  .srv-directory-grid {
    grid-template-columns: repeat(2, 1fr);
  }
  .srv-steps-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 640px) {
  .srv-hero-h1 {
    font-size: 27px;
  }
  .srv-directory-grid,
  .srv-steps-grid,
  .srv-hero-3d-showcase {
    grid-template-columns: 1fr;
  }
}
'''

# Build the 5 Service Groups HTML
groups_html = ""
for grp in SERVICE_GROUPS:
    cards_markup = ""
    for c in grp["cards"]:
        hl_items = "".join([f'<li data-editable="true">{h}</li>' for h in c["highlights"]])
        cards_markup += f'''
          <article class="srv-card" data-group-id="{grp['id']}">
            <div class="srv-card-visual">
              <img src="{c['bg']}" alt="{c['alt']}" class="srv-card-bg-img" loading="lazy" />
              <div class="srv-card-tint" style="background: {c['tint']};"></div>
              <span class="srv-card-cat-pill" data-editable="true">{c['badge']}</span>
              <div class="srv-card-floating-icon" aria-hidden="true">
                {c['icon']}
              </div>
            </div>
            <div class="srv-card-body">
              <h3 class="srv-card-h3" data-editable="true">{c['title']}</h3>
              <p class="srv-card-desc" data-editable="true">{c['desc']}</p>
              <ul class="srv-card-highlights">
                {hl_items}
              </ul>
              <div class="srv-card-footer">
                <a href="services/{c['slug']}/index.html" class="srv-btn-details" data-service-slug="{c['slug']}" data-service-title="{c['title']}" data-service-desc="{c['desc']}">
                  <span data-editable="true">مشاهده جزئیات</span>
                  <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">
                    <line x1="19" y1="12" x2="5" y2="12"></line>
                    <polyline points="12 19 5 12 12 5"></polyline>
                  </svg>
                </a>
              </div>
            </div>
          </article>
        '''

    section_cls = "srv-engineering-showcase" if grp["featured"] else "srv-group-section"
    groups_html += f'''
      <section class="{section_cls}" id="{grp['id']}">
        <div class="container">
          <div class="srv-group-header">
            <div class="srv-group-title-wrap">
              <span class="srv-group-num">{grp['num']}</span>
              <div>
                <h2 class="srv-group-h2" data-editable="true">{grp['title']}</h2>
                <p class="srv-group-sub" data-editable="true">{grp['subtitle']}</p>
              </div>
            </div>
            <a href="#contact-consult" class="srv-btn-secondary" style="font-size:12.5px;padding:8px 18px;" data-open-consult="true">
              درخواست مشاوره این بخش
            </a>
          </div>
          <div class="srv-cards-grid">
            {cards_markup}
          </div>
        </div>
      </section>
    '''

# Build 38-Service Directory Matrix HTML
DIR_CAT_ICONS = {
    "صنعت": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#f59e0b" stroke-width="2.2"><circle cx="12" cy="12" r="3.5"/><path d="M12 2v3m0 14v3M2 12h3m14 0h3M4.9 4.9l2.1 2.1m10 10l2.1 2.1M19.1 4.9l-2.1 2.1m-10 10l-2.1 2.1"/></svg>',
    "معدن": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#f59e0b" stroke-width="2.2"><path d="M3 20L10 6L15 15L18 10L22 20H3Z"/></svg>',
    "تجارت": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#f59e0b" stroke-width="2.2"><circle cx="12" cy="12" r="9"/><ellipse cx="12" cy="12" rx="4" ry="9"/><path d="M3.5 9h17M3.5 15h17"/></svg>',
    "فنی و مهندسی": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#f59e0b" stroke-width="2.2"><path d="M4 18C4 13 7.6 9 12 9C16.4 9 20 13 20 18H4Z"/><path d="M2 18.5H22"/></svg>',
}
dir_cols_html = ""
for cat_name in ["صنعت", "معدن", "تجارت", "فنی و مهندسی"]:
    items = [x for x in FULL_38_SERVICES if x[0] == cat_name]
    links_str = ""
    for _, title, slug in items:
        links_str += f'''
          <a href="services/{slug}/index.html" class="srv-dir-link" data-service-slug="{slug}" data-service-title="{title}" data-service-desc="ارائه خدمات تخصصی و پیگیری کامل مراحل «{title}» در بخش {cat_name} هلدینگ دلگشا | راه‌گشا.">
            <span data-editable="true">{title}</span>
            <span style="color:#f59e0b;font-weight:900;">↖</span>
          </a>
        '''
    dir_cols_html += f'''
      <div class="srv-dir-col">
        <h3 class="srv-dir-col-title">
          <span style="display:inline-flex;align-items:center;gap:7px;">
            {DIR_CAT_ICONS[cat_name]}
            <span data-editable="true">بخش {cat_name}</span>
          </span>
          <span style="font-size:12px;color:#64748b;font-weight:700;">{len(items)} خدمت</span>
        </h3>
        <div class="srv-dir-links">
          {links_str}
        </div>
      </div>
    '''

# Build FAQ HTML
faq_html = ""
for idx, f in enumerate(FAQ_ITEMS):
    open_cls = "open" if idx == 0 else ""
    faq_html += f'''
      <div class="srv-faq-item {open_cls}">
        <button type="button" class="srv-faq-question">
          <span>
            <span class="srv-faq-cat-tag">{f['cat']}</span>
            <span data-editable="true">{f['q']}</span>
          </span>
          <span class="srv-faq-icon" style="color:#f59e0b;font-size:18px;font-weight:900;">{('−' if idx == 0 else '+')}</span>
        </button>
        <div class="srv-faq-answer" data-editable="true">
          {f['a']}
        </div>
      </div>
    '''

services_html_doc = f'''<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>صفحه جامع خدمات | سایت دلگشا - هلدینگ راه‌گشا (صنعت، معدن، تجارت و فنی و مهندسی)</title>
  <meta name="description" content="خدمات تخصصی صنعت، معدن، تجارت و فنی و مهندسی در سایت دلگشا متعلق به هلدینگ راه‌گشا؛ از اخذ مجوزهای صنعتی و تجاری تا طراحی سازه، اجرای سوله کارخانه، نقشه‌برداری و پیمانکاری ساختمان." />
  <link rel="icon" type="image/png" href="{img_logo}" />
  <style>
    @font-face {{
      font-family: 'Vazirmatn';
      src: url('{font_regular}') format('woff2');
      font-weight: 400;
      font-style: normal;
      font-display: swap;
    }}
    @font-face {{
      font-family: 'Vazirmatn';
      src: url('{font_medium}') format('woff2');
      font-weight: 500;
      font-style: normal;
      font-display: swap;
    }}
    @font-face {{
      font-family: 'Vazirmatn';
      src: url('{font_bold}') format('woff2');
      font-weight: 700;
      font-style: normal;
      font-display: swap;
    }}
    @font-face {{
      font-family: 'Vazirmatn';
      src: url('{font_extrabold}') format('woff2');
      font-weight: 800;
      font-style: normal;
      font-display: swap;
    }}
    @font-face {{
      font-family: 'Vazirmatn';
      src: url('{font_black}') format('woff2');
      font-weight: 900;
      font-style: normal;
      font-display: swap;
    }}
    {base_styles}
    {services_page_css}
  </style>
</head>
<body id="top">

  <!-- ====================================================================
       1. IDENTICAL SITE HEADER (Connected to Our Designed Homepage index.html)
       ==================================================================== -->
  <header class="site-header">
    <div class="container header-inner">
      <a href="index.html" data-switch-page="home" class="brand-logo" aria-label="بازگشت به صفحه اصلی سایت دلگشا">
        <img src="{img_logo}" alt="نشان دلگشا" class="brand-mark-img" />
        <div class="brand-text-stack">
          <img src="{img_logo_text}" alt="دلگشا" class="brand-logotype-img" />
          <span class="brand-subtitle" data-editable="true">هلدینگ توسعه صنعت و معدن و تجارت</span>
        </div>
        <img src="{img_logo_full}" alt="لوگو دلگشا" class="brand-full-vertical-img" />
      </a>

      <nav class="main-nav" aria-label="منوی اصلی">
        <a href="index.html" data-switch-page="home" class="nav-link">صفحه اصلی</a>
        <a href="index.html#subservices" data-switch-page="home" data-scroll-target="#subservices" class="nav-link">خدمات ما (صفحه اصلی)</a>
        <a href="#services-catalog" class="nav-link active">صفحه جامع خدمات</a>
        <a href="#group-engineering" class="nav-link">فنی و مهندسی</a>
        <a href="#service-process" class="nav-link">مسیر دریافت خدمات</a>
        <a href="#faq-section" class="nav-link">پرسش‌های متداول</a>
        <a href="#footer" class="nav-link">تماس با ما</a>
      </nav>

      <div class="header-actions">
        <button type="button" class="btn-consult" data-open-consult="true">
          <span class="btn-consult-avatar" aria-hidden="true">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12 12c2.76 0 5-2.24 5-5s-2.24-5-5-5-5 2.24-5 5 2.24 5 5 5zm0 2c-3.33 0-10 1.67-10 5v3h20v-3c0-3.33-6.67-5-10-5z"/>
            </svg>
          </span>
          <span data-editable="true">درخواست مشاوره</span>
        </button>

        <button type="button" class="btn-mobile-menu" id="btnMobileMenu" aria-label="منوی موبایل">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round">
            <line x1="4" y1="7" x2="20" y2="7"></line>
            <line x1="4" y1="12" x2="20" y2="12"></line>
            <line x1="4" y1="17" x2="20" y2="17"></line>
          </svg>
        </button>
      </div>
    </div>

    <div class="mobile-drawer" id="mobileDrawer">
      <a href="index.html" data-switch-page="home" class="nav-link">صفحه اصلی</a>
      <a href="index.html#subservices" data-switch-page="home" data-scroll-target="#subservices" class="nav-link">خدمات ما (صفحه اصلی)</a>
      <a href="#services-catalog" class="nav-link active">صفحه جامع خدمات</a>
      <a href="#group-engineering" class="nav-link">فنی و مهندسی</a>
      <a href="#service-process" class="nav-link">مسیر دریافت خدمات</a>
      <a href="#faq-section" class="nav-link">پرسش‌های متداول</a>
      <a href="#footer" class="nav-link">تماس با ما</a>
    </div>
  </header>

  <!-- Breadcrumb Bar with Direct Internal Link to Our Designed Homepage & Services Section -->
  <nav class="srv-breadcrumb-bar" aria-label="مسیر راهنما">
    <div class="container srv-breadcrumb-list">
      <a href="index.html" data-switch-page="home">صفحه اصلی (سایت دلگشا | هلدینگ راه‌گشا)</a>
      <span>‹</span>
      <a href="index.html#subservices" data-switch-page="home" data-scroll-target="#subservices" style="color:#93c5fd;">بخش خدمات ما در صفحه اصلی</a>
      <span>‹</span>
      <span aria-current="page">صفحه جامع خدمات تخصصی</span>
    </div>
  </nav>

  <!-- ====================================================================
       2. CINEMATIC 3D HERO BANNER (Single H1 for SEO)
       ==================================================================== -->
  <section class="srv-hero" style="background-image: url('{img_hero}');">
    <div class="srv-hero-backdrop"></div>
    <div class="container srv-hero-grid">
      <div>
        <span class="srv-hero-badge" data-editable="true">
          ✦ درگاه جامع خدمات سایت دلگشا | هلدینگ راه‌گشا
        </span>
        <h1 class="srv-hero-h1" data-editable="true">
          خدمات تخصصی صنعت، معدن، تجارت و فنی و مهندسی
        </h1>
        <p class="srv-hero-lead" data-editable="true">
          از اخذ مجوزهای صنعتی و تجاری تا طراحی و اجرای پروژه‌های ساختمانی و مهندسی، در مسیر توسعه کسب‌وکار و اجرای پروژه‌ها همراه شما هستیم.
        </p>
        <div class="srv-hero-actions">
          <a href="#services-catalog" class="srv-btn-primary">
            <span data-editable="true">مشاهده خدمات</span>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <line x1="12" y1="5" x2="12" y2="19"></line>
              <polyline points="19 12 12 19 5 12"></polyline>
            </svg>
          </a>
          <a href="#contact-consult" class="srv-btn-secondary" data-open-consult="true">
            <span data-editable="true">درخواست مشاوره</span>
          </a>
        </div>
      </div>

      <!-- 3D Visual Preview Grid -->
      <div class="srv-hero-3d-showcase">
        <a href="#group-industry" class="srv-hero-mini-card">
          <img src="{img_sub1}" alt="خدمات صنعت و مجوزها" />
          <span style="display:flex;align-items:center;justify-content:center;gap:6px;">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#fbbf24" stroke-width="2.3"><circle cx="12" cy="12" r="3.5"/><path d="M12 2v3m0 14v3M2 12h3m14 0h3"/></svg>
            صنعت و مجوزهای تولید
          </span>
        </a>
        <a href="#group-mining-trade" class="srv-hero-mini-card">
          <img src="{img_sub2}" alt="خدمات معدن و تجارت" />
          <span style="display:flex;align-items:center;justify-content:center;gap:6px;">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#fbbf24" stroke-width="2.3"><path d="M3 20L10 6L15 15L18 10L22 20H3Z"/></svg>
            معدن و تجارت بازرگانی
          </span>
        </a>
        <a href="#group-registration" class="srv-hero-mini-card">
          <img src="{img_sub4}" alt="ثبت شرکت و برند" />
          <span style="display:flex;align-items:center;justify-content:center;gap:6px;">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#fbbf24" stroke-width="2.3"><rect x="4" y="4" width="10" height="16"/><path d="M14 9h6v11h-6"/></svg>
            ثبت شرکت، برند و مالی
          </span>
        </a>
        <a href="#group-engineering" class="srv-hero-mini-card">
          <img src="{img_sub3}" alt="خدمات فنی و مهندسی" />
          <span style="display:flex;align-items:center;justify-content:center;gap:6px;">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#fbbf24" stroke-width="2.3"><path d="M4 18C4 13 7.6 9 12 9C16.4 9 20 13 20 18H4Z"/><path d="M2 18.5H22"/></svg>
            سازه، سوله و پیمانکاری
          </span>
        </a>
      </div>
    </div>
  </section>

  <!-- ====================================================================
       3. QUICK CATEGORY FILTER & LIVE SEARCH BAR
       ==================================================================== -->
  <div class="container srv-filter-bar-wrap" id="services-catalog">
    <div class="srv-filter-bar">
      <div class="srv-filter-pills" role="navigation" aria-label="فیلتر دسته‌بندی خدمات">
        <a href="#services-catalog" class="srv-filter-pill active" data-filter-group="all">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/></svg>
          <span>همه خدمات تخصصی</span>
        </a>
        <a href="#group-industry" class="srv-filter-pill" data-filter-group="group-industry">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><circle cx="12" cy="12" r="3.5"/><path d="M12 2v3m0 14v3M2 12h3m14 0h3M4.9 4.9l2.1 2.1m10 10l2.1 2.1M19.1 4.9l-2.1 2.1m-10 10l-2.1 2.1"/></svg>
          <span>صنعت و مجوزها</span>
        </a>
        <a href="#group-mining-trade" class="srv-filter-pill" data-filter-group="group-mining-trade">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><path d="M3 20L10 6L15 15L18 10L22 20H3Z"/></svg>
          <span>معدن و تجارت</span>
        </a>
        <a href="#group-registration" class="srv-filter-pill" data-filter-group="group-registration">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><rect x="4" y="3" width="10" height="18"/><path d="M14 9h6v12h-6"/></svg>
          <span>ثبتی و کسب‌وکار</span>
        </a>
        <a href="#group-financial-specialized" class="srv-filter-pill" data-filter-group="group-financial-specialized">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M8 13h8M8 17h5"/></svg>
          <span>مالی و تخصصی</span>
        </a>
        <a href="#group-engineering" class="srv-filter-pill" data-filter-group="group-engineering">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><path d="M4 18C4 13 7.6 9 12 9C16.4 9 20 13 20 18H4Z"/><path d="M2 18.5H22"/></svg>
          <span>فنی و مهندسی (ویژه)</span>
        </a>
      </div>
      <div class="srv-inline-search">
        <input type="search" id="srvInlineSearchInput" placeholder="جستجوی سریع نام خدمت یا مجوز..." aria-label="جستجوی نام خدمت" />
      </div>
    </div>
  </div>

  <!-- ====================================================================
       4. FIVE CATEGORIZED SERVICE GROUPS (H2 Groups + H3 3D Cards)
       ==================================================================== -->
  <main>
    {groups_html}

    <!-- ==================================================================
         5. COMPLETE 38-SERVICE DIRECTORY MATRIX (Direct Internal Links)
         ================================================================== -->
    <section class="srv-directory-section" id="full-directory">
      <div class="container">
        <div class="subservices-header">
          <h2 class="subservices-title" data-editable="true">فهرست جامع و لینک‌های اختصاصی تمامی خدمات تخصصی</h2>
          <p class="subservices-subtitle" data-editable="true">دسترسی مستقیم به صفحات اختصاصی هر یک از ۳۸ خدمت زیرمجموعه صنعت، معدن، تجارت و فنی و مهندسی</p>
        </div>
        <div class="srv-directory-grid">
          {dir_cols_html}
        </div>
      </div>
    </section>

    <!-- ==================================================================
         6. 5-STEP SERVICE DELIVERY PROCESS ("مسیر دریافت خدمات")
         ================================================================== -->
    <section class="srv-process-section" id="service-process">
      <div class="container">
        <div class="subservices-header">
          <h2 class="subservices-title" data-editable="true">مسیر دریافت خدمات در هلدینگ راه‌گشا | دلگشا</h2>
          <p class="subservices-subtitle" data-editable="true">فرآیند شفاف، مرحله‌به‌مرحله و منظم از ثبت درخواست اولیه تا تحویل نهایی خدمت یا پروژه</p>
        </div>

        <div class="srv-process-tabs">
          <button type="button" class="srv-process-tab active" data-process-mode="licenses">
            مسیر دریافت خدمات مجوزها، صنعت، معدن و تجارت
          </button>
          <button type="button" class="srv-process-tab" data-process-mode="engineering">
            مسیر اجرایی خدمات فنی، مهندسی و پیمانکاری ساختمان
          </button>
        </div>

        <div class="srv-steps-grid" id="processStepsContainer">
          <div class="srv-step-card">
            <div class="srv-step-num" aria-hidden="true">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/></svg>
            </div>
            <h3 class="srv-step-title" data-editable="true">ثبت درخواست و اعلام نیاز</h3>
            <p class="srv-step-desc" id="stepDesc1" data-editable="true">
              ثبت موضوع فعالیت یا مجوز موردنیاز از طریق فرم درخواست مشاوره یا تماس مستقیم با کارشناسان مجموعه.
            </p>
          </div>
          <div class="srv-step-card">
            <div class="srv-step-num" aria-hidden="true">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>
            </div>
            <h3 class="srv-step-title" data-editable="true">بررسی اولیه اطلاعات و مدارک</h3>
            <p class="srv-step-desc" id="stepDesc2" data-editable="true">
              بررسی مدارک هویتی، ثبتی یا فنی متقاضی، تطبیق با ضوابط قانونی و شناسایی پیش‌نیازهای سامانه مربوطه.
            </p>
          </div>
          <div class="srv-step-card">
            <div class="srv-step-num" aria-hidden="true">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"/></svg>
            </div>
            <h3 class="srv-step-title" data-editable="true">مشاوره و تعیین مسیر اجرایی</h3>
            <p class="srv-step-desc" id="stepDesc3" data-editable="true">
              ارائه مشاوره تخصصی، شفاف‌سازی مراحل، زمان‌بندی، پیش‌نیازهای استعلامی و توافق بر محدوده خدمات.
            </p>
          </div>
          <div class="srv-step-card">
            <div class="srv-step-num" aria-hidden="true">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 2.83-2.83l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>
            </div>
            <h3 class="srv-step-title" data-editable="true">انجام یا پیگیری خدمات توافق‌شده</h3>
            <p class="srv-step-desc" id="stepDesc4" data-editable="true">
              ثبت درخواست در سامانه‌های رسمی، تدوین طرح‌ها یا نقشه‌ها و پیگیری منظم پرونده در مراجع ذی‌ربط.
            </p>
          </div>
          <div class="srv-step-card">
            <div class="srv-step-num" aria-hidden="true">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
            </div>
            <h3 class="srv-step-title" data-editable="true">تحویل نتیجه و ارائه راهنمایی‌های لازم</h3>
            <p class="srv-step-desc" id="stepDesc5" data-editable="true">
              تحویل مجوز، پروانه، سند ثبتی یا مدارک فنی نهایی به همراه راهنمایی‌های کاربردی برای مراحل بعدی فعالیت.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- ==================================================================
         7. REAL COLLABORATION ADVANTAGES ("مزیت‌های همکاری")
         ================================================================== -->
    <section class="about-section" id="collaboration-advantages" style="background-image: url('{img_about}');">
      <div class="about-overlay"></div>
      <div class="container about-grid">
        <div class="why-card">
          <h2 class="why-card-title" data-editable="true">مزیت‌های همکاری با ما</h2>
          <div class="why-list">
            <div class="why-item">
              <div class="why-icon-circle" aria-hidden="true">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#f59e0b" stroke-width="2.2"><circle cx="12" cy="12" r="4"/><path d="M12 2v3m0 14v3M2 12h3m14 0h3"/></svg>
              </div>
              <div class="why-item-text">
                <h3 class="why-item-heading" data-editable="true">پوشش یکپارچه خدمات</h3>
                <p class="why-item-sub" data-editable="true">هماهنگی امور صنعت، معدن، تجارت، ثبت و مهندسی در یک مجموعه</p>
              </div>
            </div>
            <div class="why-item">
              <div class="why-icon-circle" aria-hidden="true">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#f59e0b" stroke-width="2.2"><path d="M9 11l3 3L22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg>
              </div>
              <div class="why-item-text">
                <h3 class="why-item-heading" data-editable="true">پیگیری منظم و مرحله‌به‌مرحله</h3>
                <p class="why-item-sub" data-editable="true">بررسی دقیق مدارک پیش از ثبت جهت جلوگیری از اتلاف زمان</p>
              </div>
            </div>
            <div class="why-item">
              <div class="why-icon-circle" aria-hidden="true">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#f59e0b" stroke-width="2.2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg>
              </div>
              <div class="why-item-text">
                <h3 class="why-item-heading" data-editable="true">دانش تخصصی و تجربه اجرایی</h3>
                <p class="why-item-sub" data-editable="true">آشنایی با رویه‌های اداری، سامانه‌های تخصصی و ضوابط فنی پروژه‌ها</p>
              </div>
            </div>
            <div class="why-item">
              <div class="why-icon-circle" aria-hidden="true">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#f59e0b" stroke-width="2.2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
              </div>
              <div class="why-item-text">
                <h3 class="why-item-heading" data-editable="true">مشاوره شفاف و کاربردی</h3>
                <p class="why-item-sub" data-editable="true">تعیین مسیر درست بر اساس شرایط واقعی متقاضی و نوع پروژه</p>
              </div>
            </div>
          </div>
        </div>

        <div class="about-content" id="contact-consult">
          <div class="about-header-with-line">
            <p class="about-overline" data-editable="true">همراهی از مجوز تا اجرا</p>
            <h2 class="about-title">
              <span data-editable="true">هماهنگی خدمات اداری،</span>
              <span data-editable="true">تجاری و مهندسی</span>
            </h2>
          </div>
          <p class="about-description" data-editable="true">
            در هلدینگ راه‌گشا (سایت دلگشا)، متقاضیان و کارفرمایان می‌توانند علاوه بر خدمات اخذ مجوزهای صنعتی، معدنی و بازرگانی، خدمات ثبت شرکت و برند، حسابرسی و همچنین خدمات فنی و مهندسی شامل طراحی سازه، اجرای سوله کارخانه، نقشه‌برداری، دکوراسیون و پیمانکاری ساختمان را به‌صورت هماهنگ دریافت کنند.
          </p>
          <div style="display:flex;gap:12px;flex-wrap:wrap;">
            <button type="button" class="btn-about-more" data-open-consult="true">
              <span data-editable="true">ثبت درخواست مشاوره</span>
            </button>
            <a href="index.html#subservices" data-switch-page="home" data-scroll-target="#subservices" class="btn-about-more" style="border-color:rgba(255,255,255,0.35);">
              <span>بازگشت به صفحه اصلی (بخش خدمات ما)</span>
            </a>
          </div>
        </div>

        <div class="about-video-zone" aria-hidden="true"></div>
      </div>
    </section>

    <!-- ==================================================================
         8. CATEGORIZED FAQ ACCORDION ("پرسش‌های متداول")
         ================================================================== -->
    <section class="srv-faq-section" id="faq-section">
      <div class="container">
        <div class="subservices-header">
          <h2 class="subservices-title" data-editable="true">پرسش‌های متداول خدمات</h2>
          <p class="subservices-subtitle" data-editable="true">پاسخ به مهم‌ترین سؤالات متقاضیان در حوزه‌های جواز تأسیس، پروانه بهره‌برداری، طرح توجیهی، ثبت برند و خدمات فنی و مهندسی</p>
        </div>
        <div class="srv-faq-list">
          {faq_html}
        </div>
      </div>
    </section>
  </main>

  <!-- ====================================================================
       9. IDENTICAL SITE FOOTER (Preserving Exact Contact Info & Home Link)
       ==================================================================== -->
  <footer class="site-footer" id="footer">
    <div class="container">
      <div class="footer-main-row">
        <div class="footer-socials-group">
          <button type="button" class="btn-scroll-top" id="btnScrollTop" aria-label="بازگشت به بالای صفحه" title="بازگشت به بالا">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="18 15 12 9 6 15"></polyline>
            </svg>
          </button>

          <a href="index.html" data-switch-page="home" class="social-circle-link" style="width:auto;padding:0 12px;border-radius:999px;font-size:11.5px;font-weight:700;" title="صفحه اصلی سایت">
            صفحه اصلی سایت
          </a>

          <a href="index.html#subservices" data-switch-page="home" data-scroll-target="#subservices" class="social-circle-link" style="width:auto;padding:0 12px;border-radius:999px;font-size:11.5px;font-weight:700;" title="بخش خدمات ما در صفحه اصلی">
            بخش خدمات ما
          </a>

          <a href="#footer" class="social-circle-link" aria-label="اینستاگرام">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect>
              <path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path>
              <line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line>
            </svg>
          </a>

          <a href="#footer" class="social-circle-link" aria-label="تلگرام">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <line x1="22" y1="2" x2="11" y2="13"></line>
              <polygon points="22 2 15 22 11 13 2 9 22 2"></polygon>
            </svg>
          </a>

          <a href="#footer" class="social-circle-link" aria-label="لینکدین">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path>
              <rect x="2" y="9" width="4" height="12"></rect>
              <circle cx="4" cy="4" r="2"></circle>
            </svg>
          </a>
        </div>

        <div class="footer-contacts-group">
          <div class="footer-contact-item">
            <div class="footer-contact-text">
              <span class="footer-contact-primary" data-editable="true">شیراز بلوار چهل مقام ، کوچه ۱۱ جنب سازمان صنعت و معدن و تجارت</span>
              <span class="footer-contact-secondary" data-editable="true">آدرس دفتر مرکزی</span>
            </div>
            <span class="footer-contact-icon" aria-hidden="true">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round">
                <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
                <circle cx="12" cy="10" r="3"></circle>
              </svg>
            </span>
          </div>

          <div class="footer-divider" aria-hidden="true"></div>

          <div class="footer-contact-item">
            <div class="footer-contact-text">
              <a href="mailto:info@delgosha.ir" class="footer-contact-primary" style="direction:ltr;display:inline-block;" data-editable="true">info@delgosha.ir</a>
              <span class="footer-contact-secondary" data-editable="true">پست الکترونیک</span>
            </div>
            <span class="footer-contact-icon" aria-hidden="true">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round">
                <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path>
                <polyline points="22,6 12,13 2,6"></polyline>
              </svg>
            </span>
          </div>

          <div class="footer-divider" aria-hidden="true"></div>

          <div class="footer-contact-item">
            <div class="footer-contact-text">
              <a href="tel:09177056063" class="footer-contact-primary" data-editable="true">۰۹۱۷۷۰۵۶۰۶۳</a>
              <span class="footer-contact-secondary" data-editable="true">(پاسخگویی ۸ الی ۱۶)</span>
            </div>
            <span class="footer-contact-icon" aria-hidden="true">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round">
                <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path>
              </svg>
            </span>
          </div>
        </div>

        <a href="index.html" data-switch-page="home" class="footer-logo" aria-label="دلگشا - صفحه اصلی">
          <img src="{img_logo}" alt="نشان دلگشا" class="brand-mark-img" />
          <div class="brand-text-stack">
            <img src="{img_logo_text}" alt="دلگشا" class="brand-logotype-img" />
            <span class="brand-subtitle" data-editable="true">هلدینگ توسعه صنعت و معدن و تجارت</span>
          </div>
          <img src="{img_logo_full}" alt="لوگو دلگشا" class="brand-full-vertical-img" />
        </a>
      </div>
    </div>

    <div class="footer-bottom-bar">
      <div class="container">
        <p class="footer-copyright" data-editable="true">
          © تمامی حقوق مادی و معنوی این سایت متعلق به دلگشا (هلدینگ راه‌گشا) می‌باشد.
        </p>
      </div>
    </div>
  </footer>

  <!-- Consultation Modal -->
  <div class="modal-backdrop" id="consultModal" role="dialog" aria-modal="true">
    <div class="modal-card">
      <div class="modal-header">
        <h3 class="modal-title">درخواست مشاوره تخصصی خدمات</h3>
        <button type="button" class="modal-close-btn" data-close-modal="true" aria-label="بستن">✕</button>
      </div>
      <form id="consultForm">
        <div class="form-group">
          <label class="form-label" for="consultName">نام و نام خانوادگی / نام شرکت</label>
          <input type="text" id="consultName" class="form-control" placeholder="نام خود یا مجموعه را وارد کنید..." required />
        </div>
        <div class="form-group">
          <label class="form-label" for="consultPhone">شماره تماس</label>
          <input type="tel" id="consultPhone" class="form-control" placeholder="۰۹۱۷xxxxxxx" required />
        </div>
        <div class="form-group">
          <label class="form-label" for="consultCategory">گروه خدمات مورد نظر</label>
          <select id="consultCategory" class="form-control">
            <option value="صنعت و مجوزها">گروه اول: خدمات صنعت و مجوزها</option>
            <option value="معدن و تجارت">گروه دوم: خدمات معدن و تجارت</option>
            <option value="ثبتی و کسب‌وکار">گروه سوم: خدمات ثبتی و کسب‌وکار (ثبت شرکت و برند)</option>
            <option value="مالی و تخصصی">گروه چهارم: خدمات مالی، حسابرسی و تخصصی</option>
            <option value="فنی و مهندسی">گروه پنجم: خدمات فنی و مهندسی (سازه، سوله، نقشه‌برداری، پیمانکاری)</option>
          </select>
        </div>
        <div class="form-group">
          <label class="form-label" for="consultTopic">عنوان خدمت یا شرح درخواست</label>
          <input type="text" id="consultTopic" class="form-control" placeholder="مثال: طراحی و اجرای سوله کارخانه / صدور جواز تأسیس..." />
        </div>
        <button type="submit" class="btn-submit-modal">ثبت درخواست و هماهنگی تماس</button>
      </form>
    </div>
  </div>

  <!-- Dedicated Service Quick-Preview & Navigation Modal -->
  <div class="modal-backdrop" id="srvDetailModal" role="dialog" aria-modal="true">
    <div class="modal-card">
      <div class="modal-header">
        <h3 class="modal-title" id="srvDetailTitle">جزئیات خدمت</h3>
        <button type="button" class="modal-close-btn" data-close-modal="true" aria-label="بستن">✕</button>
      </div>
      <p id="srvDetailDesc" style="font-size:13.8px;color:#334155;line-height:1.95;margin-bottom:16px;"></p>
      <div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;padding:12px 16px;margin-bottom:18px;font-size:12.5px;color:#09213d;">
        <strong>مسیر اختصاصی این خدمت:</strong>
        <code id="srvDetailUrl" style="direction:ltr;display:inline-block;background:#e2e8f0;padding:2px 8px;border-radius:6px;margin-right:6px;">/services/</code>
      </div>
      <div style="display:flex;gap:10px;flex-wrap:wrap;">
        <a href="#" id="srvDetailGoPageBtn" class="btn-submit-modal" style="text-align:center;flex:1;margin-top:0;">
          ورود به صفحه اختصاصی این خدمت ↖
        </a>
        <button type="button" id="srvDetailConsultBtn" class="btn-submit-modal" style="flex:1;margin-top:0;background:linear-gradient(135deg,#09213d,#0d2b4e);">
          درخواست مشاوره این خدمت
        </button>
      </div>
    </div>
  </div>

  <!-- Floating Navigation & Customization Toolbar -->
  <div class="designer-toolbar" aria-label="نوار ابزار ناوبری و سفارشی‌سازی">
    <a href="index.html" class="toolbar-btn" title="مشاهده صفحه اصلی در محیط کار">🏠 صفحه اصلی</a>
    <a href="services.html" class="toolbar-btn active" title="صفحه جامع خدمات">📋 صفحه جامع خدمات</a>
    <button type="button" class="toolbar-btn" id="btnToggleLogoLayout">لوگو: افقی (هدر)</button>
    <button type="button" class="toolbar-btn" id="btnToggleEdit">✎ ویرایش متن‌ها</button>
  </div>

  <div class="toast-msg" id="toastMsg" role="status" aria-live="polite"></div>

  <script>
    (function() {{
      'use strict';

      function showToast(msg) {{
        const t = document.getElementById('toastMsg');
        if (!t) return;
        t.textContent = msg;
        t.classList.add('show');
        clearTimeout(window.__tTimer);
        window.__tTimer = setTimeout(() => t.classList.remove('show'), 2800);
      }}

      // FAQ Accordion
      document.querySelectorAll('.srv-faq-question').forEach((btn) => {{
        btn.addEventListener('click', () => {{
          const item = btn.closest('.srv-faq-item');
          const isOpen = item.classList.toggle('open');
          const icon = btn.querySelector('.srv-faq-icon');
          if (icon) icon.textContent = isOpen ? '−' : '+';
        }});
      }});

      // Process Mode Switcher (Licenses vs Engineering Projects)
      const PROCESS_MODES = {{
        licenses: [
          'ثبت موضوع فعالیت یا مجوز موردنیاز از طریق فرم درخواست مشاوره یا تماس مستقیم با کارشناسان مجموعه.',
          'بررسی مدارک هویتی، ثبتی یا فنی متقاضی، تطبیق با ضوابط قانونی و شناسایی پیش‌نیازهای سامانه مربوطه.',
          'ارائه مشاوره تخصصی، شفاف‌سازی مراحل، زمان‌بندی، پیش‌نیازهای استعلامی و توافق بر محدوده خدمات.',
          'ثبت درخواست در سامانه‌های رسمی، تدوین طرح توجیهی یا مستندات و پیگیری منظم پرونده در مراجع ذی‌ربط.',
          'تحویل مجوز، پروانه، سند ثبتی یا کارت بازرگانی نهایی به همراه راهنمایی‌های لازم برای مراحل بعدی.'
        ],
        engineering: [
          'ثبت مشخصات اولیه زمین، سوله یا ساختمان و اعلام نیاز کارفرما در بخش طراحی، نقشه‌برداری یا پیمانکاری.',
          'بازدید میدانی، بررسی نقشه‌ها، برداشت اطلاعات مکانی (نقشه‌برداری) و بررسی ضوابط فنی و سازه‌ای پروژه.',
          'ارائه طرح اولیه، برآورد اجرایی، تعیین مشخصات فنی سازه یا دکوراسیون و تنظیم قرارداد شفاف خدمات.',
          'انجام محاسبات سازه‌ای، تهیه نقشه‌های اجرایی، ساخت و نصب سوله یا اجرای عملیات ساختمانی مطابق قرارداد.',
          'کنترل کیفیت نهایی، تحویل مرحله‌ای و کامل پروژه و ارائه مستندات و نقشه‌های بهره‌برداری به کارفرما.'
        ]
      }};

      document.querySelectorAll('[data-process-mode]').forEach((btn) => {{
        btn.addEventListener('click', () => {{
          const mode = btn.getAttribute('data-process-mode');
          document.querySelectorAll('[data-process-mode]').forEach(b => b.classList.toggle('active', b === btn));
          const steps = PROCESS_MODES[mode];
          if (steps) {{
            steps.forEach((txt, i) => {{
              const el = document.getElementById('stepDesc' + (i + 1));
              if (el) el.textContent = txt;
            }});
          }}
        }});
      }});

      // Inline Search Filter across Cards & 38 Directory Links
      const searchInput = document.getElementById('srvInlineSearchInput');
      if (searchInput) {{
        searchInput.addEventListener('input', (e) => {{
          const q = e.target.value.trim();
          document.querySelectorAll('.srv-card').forEach((card) => {{
            const text = card.textContent || '';
            card.style.display = (!q || text.includes(q)) ? 'flex' : 'none';
          }});
          document.querySelectorAll('.srv-dir-link').forEach((link) => {{
            const text = link.textContent || '';
            link.style.display = (!q || text.includes(q)) ? 'flex' : 'none';
          }});
        }});
      }}

      // Consultation Modal
      document.querySelectorAll('[data-open-consult]').forEach((btn) => {{
        btn.addEventListener('click', (e) => {{
          e.preventDefault();
          document.getElementById('consultModal')?.classList.add('open');
        }});
      }});

      document.getElementById('consultForm')?.addEventListener('submit', (e) => {{
        e.preventDefault();
        document.getElementById('consultModal')?.classList.remove('open');
        e.target.reset();
        showToast('درخواست مشاوره شما ثبت شد. کارشناسان ما با شما تماس خواهند گرفت.');
      }});

      document.querySelectorAll('[data-close-modal]').forEach((btn) => {{
        btn.addEventListener('click', () => btn.closest('.modal-backdrop')?.classList.remove('open'));
      }});
      document.querySelectorAll('.modal-backdrop').forEach((bd) => {{
        bd.addEventListener('click', (e) => {{ if (e.target === bd) bd.classList.remove('open'); }});
      }});

      // Logo layout switcher
      const btnLogo = document.getElementById('btnToggleLogoLayout');
      if (btnLogo) {{
        btnLogo.addEventListener('click', () => {{
          const v = document.body.classList.toggle('logo-vertical-mode');
          btnLogo.classList.toggle('active', v);
          btnLogo.textContent = v ? 'لوگو: عمودی (اصلی)' : 'لوگو: افقی (هدر)';
        }});
      }}

      // Live text edit toggle
      let editOn = false;
      const btnEdit = document.getElementById('btnToggleEdit');
      if (btnEdit) {{
        btnEdit.addEventListener('click', () => {{
          editOn = !editOn;
          document.body.classList.toggle('live-edit-active', editOn);
          btnEdit.classList.toggle('active', editOn);
          btnEdit.textContent = editOn ? '✓ پایان ویرایش' : '✎ ویرایش متن‌ها';
          document.querySelectorAll('[data-editable="true"]').forEach(el => {{
            if (editOn) el.setAttribute('contenteditable', 'true');
            else el.removeAttribute('contenteditable');
          }});
        }});
      }}

      // Mobile drawer & scroll top
      document.getElementById('btnMobileMenu')?.addEventListener('click', () => {{
        document.getElementById('mobileDrawer')?.classList.toggle('open');
      }});
      document.getElementById('btnScrollTop')?.addEventListener('click', () => {{
        window.scrollTo({{ top: 0, behavior: 'smooth' }});
      }});
    }})();
  </script>
</body>
</html>
'''

with open('/home/user/services.html', 'w', encoding='utf-8') as f:
    f.write(services_html_doc)

with open('/home/user/services/index.html', 'w', encoding='utf-8') as f:
    f.write(services_html_doc)

# Now generate dedicated individual service pages under /home/user/services/<slug>/index.html
all_dedicated_services = {}
for grp in SERVICE_GROUPS:
    for c in grp["cards"]:
        all_dedicated_services[c["slug"]] = {
            "title": c["title"],
            "cat": grp["title"],
            "desc": c["desc"],
            "highlights": c["highlights"]
        }

for cat, title, slug in FULL_38_SERVICES:
    if slug not in all_dedicated_services:
        all_dedicated_services[slug] = {
            "title": title,
            "cat": f"خدمات تخصصی بخش {cat}",
            "desc": f"ارائه خدمات مشاوره، تکمیل مستندات و پیگیری اجرایی «{title}» در حوزه {cat} توسط کارشناسان هلدینگ راه‌گشا (سایت دلگشا) مطابق ضوابط و مقررات جاری.",
            "highlights": [
                f"بررسی شرایط اولیه و مدارک موردنیاز جهت {title}",
                "ثبت درخواست و بارگذاری مستندات در سامانه رسمی مربوطه",
                "پیگیری مرحله‌به‌مرحله پرونده تا صدور نتیجه نهایی",
                "ارائه مشاوره تکمیلی در طول فرآیند اجرایی"
            ]
        }

for slug, info in all_dedicated_services.items():
    sdir = f"/home/user/services/{slug}"
    os.makedirs(sdir, exist_ok=True)
    hl_li = "".join([f"<li style='margin-bottom:8px;'>{h}</li>" for h in info["highlights"]])
    sub_doc = f'''<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{info['title']} | خدمات سایت دلگشا - هلدینگ راه‌گشا</title>
  <link rel="icon" type="image/png" href="{img_logo}" />
  <style>
    @font-face {{
      font-family: 'Vazirmatn';
      src: url('{font_regular}') format('woff2');
      font-weight: 400;
    }}
    @font-face {{
      font-family: 'Vazirmatn';
      src: url('{font_bold}') format('woff2');
      font-weight: 700;
    }}
    @font-face {{
      font-family: 'Vazirmatn';
      src: url('{font_black}') format('woff2');
      font-weight: 900;
    }}
    {base_styles}
    {services_page_css}
  </style>
</head>
<body>
  <header class="site-header">
    <div class="container header-inner">
      <a href="../../index.html" class="brand-logo">
        <img src="{img_logo}" alt="نشان دلگشا" class="brand-mark-img" />
        <div class="brand-text-stack">
          <img src="{img_logo_text}" alt="دلگشا" class="brand-logotype-img" />
          <span class="brand-subtitle">هلدینگ توسعه صنعت و معدن و تجارت</span>
        </div>
      </a>
      <nav class="main-nav">
        <a href="../../index.html" class="nav-link">صفحه اصلی</a>
        <a href="../../index.html#subservices" class="nav-link">خدمات ما (صفحه اصلی)</a>
        <a href="../../services.html" class="nav-link active">صفحه جامع خدمات</a>
        <a href="#footer" class="nav-link">تماس با ما</a>
      </nav>
      <div class="header-actions">
        <a href="../../services.html" class="btn-consult"><span>بازگشت به همه خدمات</span></a>
      </div>
    </div>
  </header>

  <nav class="srv-breadcrumb-bar">
    <div class="container srv-breadcrumb-list">
      <a href="../../index.html">صفحه اصلی سایت</a>
      <span>‹</span>
      <a href="../../index.html#subservices">بخش خدمات ما (صفحه اصلی)</a>
      <span>‹</span>
      <a href="../../services.html">صفحه جامع خدمات</a>
      <span>‹</span>
      <span>{info['title']}</span>
    </div>
  </nav>

  <main class="container" style="padding:48px 24px;">
    <div style="background:#fff;border-radius:22px;padding:36px;box-shadow:0 14px 40px rgba(6,24,46,0.08);border:1px solid #e2e8f0;">
      <span class="srv-hero-badge" style="background:rgba(244,129,11,0.12);color:#ea580c;">{info['cat']}</span>
      <h1 style="font-size:32px;font-weight:900;color:#09213d;margin:10px 0 16px;">{info['title']}</h1>
      <p style="font-size:15px;color:#334155;line-height:2;margin-bottom:24px;">{info['desc']}</p>
      <div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:16px;padding:22px;margin-bottom:28px;">
        <h2 style="font-size:18px;font-weight:900;color:#09213d;margin-bottom:12px;">محورهای خدمات و پیگیری‌های تخصصی این بخش:</h2>
        <ul style="padding-right:20px;list-style:disc;font-size:14px;color:#1e293b;line-height:1.9;">
          {hl_li}
        </ul>
      </div>
      <div style="display:flex;gap:14px;flex-wrap:wrap;">
        <a href="tel:09177056063" class="srv-btn-primary">تماس و مشاوره مستقیم: ۰۹۱۷۷۰۵۶۰۶۳</a>
        <a href="../../services.html" class="srv-btn-secondary" style="color:#09213d;border-color:#09213d;">بازگشت به صفحه جامع خدمات</a>
        <a href="../../index.html#subservices" class="srv-btn-secondary" style="color:#09213d;border-color:#cbd5e1;">صفحه اصلی (بخش خدمات ما)</a>
      </div>
    </div>
  </main>

  <footer class="site-footer" id="footer">
    <div class="container">
      <div class="footer-main-row">
        <div class="footer-contacts-group">
          <div class="footer-contact-item">
            <div class="footer-contact-text">
              <span class="footer-contact-primary">شیراز بلوار چهل مقام ، کوچه ۱۱ جنب سازمان صنعت و معدن و تجارت</span>
              <span class="footer-contact-secondary">آدرس دفتر مرکزی</span>
            </div>
          </div>
          <div class="footer-divider"></div>
          <div class="footer-contact-item">
            <div class="footer-contact-text">
              <a href="tel:09177056063" class="footer-contact-primary">۰۹۱۷۷۰۵۶۰۶۳</a>
              <span class="footer-contact-secondary">(پاسخگویی ۸ الی ۱۶)</span>
            </div>
          </div>
        </div>
        <a href="../../index.html" class="footer-logo">
          <img src="{img_logo}" alt="نشان دلگشا" class="brand-mark-img" />
          <div class="brand-text-stack">
            <img src="{img_logo_text}" alt="دلگشا" class="brand-logotype-img" />
            <span class="brand-subtitle">هلدینگ توسعه صنعت و معدن و تجارت</span>
          </div>
        </a>
      </div>
    </div>
  </footer>
</body>
</html>
'''
    with open(f"{sdir}/index.html", 'w', encoding='utf-8') as sf:
        sf.write(sub_doc)

print(f"Generated services.html + {len(all_dedicated_services)} dedicated service pages under /services/<slug>/index.html!")

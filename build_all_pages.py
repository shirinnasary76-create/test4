import re
import json
import subprocess

# 1. Run base generators
subprocess.run(["python3", "/home/user/generate_html.py"], check=True)
subprocess.run(["python3", "/home/user/generate_services_page.py"], check=True)

with open("/home/user/index.html", "r", encoding="utf-8") as f:
    home_raw = f.read()

with open("/home/user/services.html", "r", encoding="utf-8") as f:
    srv_raw = f.read()

# Extract CSS from services.html (contains base_styles + services_page_css + @font-face)
style_match = re.search(r"<style>(.*?)</style>", srv_raw, re.DOTALL)
combined_css = style_match.group(1)

# Extract favicon
fav_match = re.search(r'<link rel="icon"[^>]+>', srv_raw)
favicon_tag = fav_match.group(0) if fav_match else ""

# Extract Home body inner content (everything inside <body id="top">...</body> before <div class="modal-backdrop")
home_body_match = re.search(r'<body[^>]*>(.*?)<!-- ====================================================================\s*11\. INTERACTIVE MODALS', home_raw, re.DOTALL)
home_view_html = home_body_match.group(1).strip()

# Extract Home modals + script
home_modals_match = re.search(r'(<!-- ====================================================================\s*11\. INTERACTIVE MODALS.*?)<!-- Floating Quick Brand Switcher', home_raw, re.DOTALL)
home_modals_html = home_modals_match.group(1).strip()

home_script_match = re.search(r'<script>\s*(/\* ==========================================================================\s*Delgosha.*?\*/.*?)</script>', home_raw, re.DOTALL)
home_script_js = home_script_match.group(1).strip()

# Extract Services body inner content (everything inside <body id="top">...</body> before <!-- Consultation Modal -->)
srv_body_match = re.search(r'<body[^>]*>(.*?)<!-- Consultation Modal -->', srv_raw, re.DOTALL)
srv_view_html = srv_body_match.group(1).strip()

# Deduplicate large base64 data URIs (> 15,000 chars) into a single shared JS asset map so combined HTML stays ~4.3 MB!
asset_table = {}
asset_counter = [0]

def replace_large_data_uris(html_text):
    # Match data:image/...;base64,... inside quotes
    pattern = re.compile(r'(data:image/(?:jpeg|png);base64,[A-Za-z0-9+/=]{15000,})')
    def repl(m):
        uri = m.group(1)
        if uri not in asset_table:
            asset_counter[0] += 1
            key = f"__ASSET_{asset_counter[0]}__"
            asset_table[uri] = key
        return asset_table[uri]
    return pattern.sub(repl, html_text)

home_view_dedup = replace_large_data_uris(home_view_html)
srv_view_dedup = replace_large_data_uris(srv_view_html)
home_modals_dedup = replace_large_data_uris(home_modals_html)

# Invert asset_table for JS lookup: { "__ASSET_1__": "data:image/..." }
js_asset_map = {v: k for k, v in asset_table.items()}

# Also import all 46 dedicated services metadata from generate_services_page
import generate_services_page as gsp
all_dedicated_services = gsp.all_dedicated_services

def build_unified_document(default_page="home"):
    is_home = (default_page == "home")
    title = (
        "دلگشا | هلدینگ توسعه صنعت و معدن و تجارت (صفحه اصلی و خدمات)"
        if is_home else
        "صفحه جامع خدمات | سایت دلگشا - هلدینگ راه‌گشا (صنعت، معدن، تجارت و فنی و مهندسی)"
    )
    home_display = "block" if is_home else "none"
    srv_display = "none" if is_home else "block"
    home_btn_active = "active" if is_home else ""
    srv_btn_active = "" if is_home else "active"

    return f'''<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="خدمات تخصصی صنعت، معدن، تجارت و فنی و مهندسی در سایت دلگشا متعلق به هلدینگ راه‌گشا؛ از اخذ مجوزهای صنعتی و تجاری تا طراحی سازه، اجرای سوله کارخانه، نقشه‌برداری و پیمانکاری ساختمان." />
  {favicon_tag}
  <style>
    {combined_css}
    .site-page-view {{
      width: 100%;
    }}
  </style>
</head>
<body id="top" data-active-page="{default_page}">

  <!-- ====================================================================
       VIEW 1: OUR DESIGNED HOMEPAGE (index.html — شامل بخش «خدمات ما»)
       ==================================================================== -->
  <div id="homePageView" class="site-page-view" style="display: {home_display};">
    {home_view_dedup}
  </div>

  <!-- ====================================================================
       VIEW 2: COMPREHENSIVE SERVICES PAGE (services.html — صفحه جامع خدمات)
       ==================================================================== -->
  <div id="servicesPageView" class="site-page-view" style="display: {srv_display};">
    {srv_view_dedup}
  </div>

  <!-- ====================================================================
       VIEW 3: DEDICATED SINGLE SERVICE PAGE (services/<slug>/index.html)
       ==================================================================== -->
  <div id="singleServicePageView" class="site-page-view" style="display: none;">
    <header class="site-header">
      <div class="container header-inner">
        <a href="index.html" data-switch-page="home" class="brand-logo">
          <img src="{gsp.img_logo}" alt="نشان دلگشا" class="brand-mark-img" />
          <div class="brand-text-stack">
            <img src="{gsp.img_logo_text}" alt="دلگشا" class="brand-logotype-img" />
            <span class="brand-subtitle">هلدینگ توسعه صنعت و معدن و تجارت</span>
          </div>
          <img src="{gsp.img_logo_full}" alt="لوگو دلگشا" class="brand-full-vertical-img" />
        </a>
        <nav class="main-nav">
          <a href="index.html" data-switch-page="home" class="nav-link">صفحه اصلی</a>
          <a href="index.html#subservices" data-switch-page="home" data-scroll-target="#subservices" class="nav-link">خدمات ما (صفحه اصلی)</a>
          <a href="services.html" data-switch-page="services" class="nav-link active">صفحه جامع خدمات</a>
        </nav>
        <div class="header-actions">
          <a href="services.html" data-switch-page="services" class="btn-consult"><span>بازگشت به صفحه جامع خدمات</span></a>
        </div>
      </div>
    </header>

    <nav class="srv-breadcrumb-bar">
      <div class="container srv-breadcrumb-list">
        <a href="index.html" data-switch-page="home">صفحه اصلی سایت دلگشا</a>
        <span>‹</span>
        <a href="index.html#subservices" data-switch-page="home" data-scroll-target="#subservices">بخش خدمات ما (صفحه اصلی)</a>
        <span>‹</span>
        <a href="services.html" data-switch-page="services">صفحه جامع خدمات</a>
        <span>‹</span>
        <span id="singleSrvBreadcrumbTitle">جزئیات خدمت</span>
      </div>
    </nav>

    <main class="container" style="padding: 48px 24px;">
      <div style="background:#fff;border-radius:22px;padding:36px;box-shadow:0 14px 40px rgba(6,24,46,0.08);border:1px solid #e2e8f0;">
        <span class="srv-hero-badge" id="singleSrvBadge" style="background:rgba(244,129,11,0.12);color:#ea580c;">خدمات تخصصی</span>
        <h1 id="singleSrvTitle" style="font-size:32px;font-weight:900;color:#09213d;margin:10px 0 16px;">عنوان خدمت</h1>
        <p id="singleSrvDesc" style="font-size:15px;color:#334155;line-height:2;margin-bottom:24px;"></p>
        <div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:16px;padding:22px;margin-bottom:28px;">
          <h2 style="font-size:18px;font-weight:900;color:#09213d;margin-bottom:12px;">محورهای خدمات و پیگیری‌های تخصصی این بخش:</h2>
          <ul id="singleSrvHighlights" style="padding-right:20px;list-style:disc;font-size:14px;color:#1e293b;line-height:1.9;"></ul>
        </div>
        <div style="display:flex;gap:14px;flex-wrap:wrap;">
          <button type="button" class="srv-btn-primary" data-open-consult="true">ثبت درخواست مشاوره این خدمت</button>
          <a href="tel:09177056063" class="srv-btn-secondary" style="color:#09213d;border-color:#f59e0b;">تماس مستقیم: ۰۹۱۷۷۰۵۶۰۶۳</a>
          <a href="services.html" data-switch-page="services" class="srv-btn-secondary" style="color:#09213d;border-color:#09213d;">بازگشت به صفحه جامع خدمات</a>
          <a href="index.html#subservices" data-switch-page="home" data-scroll-target="#subservices" class="srv-btn-secondary" style="color:#09213d;border-color:#cbd5e1;">بازگشت به صفحه اصلی (بخش خدمات ما)</a>
        </div>
      </div>
    </main>
  </div>

  <!-- Shared Modals -->
  {home_modals_dedup}

  <!-- Unified Floating Navigation & Customization Toolbar -->
  <div class="designer-toolbar" aria-label="نوار ابزار ناوبری و سفارشی‌سازی">
    <a href="index.html" data-switch-page="home" class="toolbar-btn {home_btn_active}" id="toolbarBtnHome" title="مشاهده صفحه اصلی که با هم طراحی کردیم">🏠 صفحه اصلی</a>
    <a href="index.html#subservices" data-switch-page="home" data-scroll-target="#subservices" class="toolbar-btn" id="toolbarBtnHomeServices" title="مشاهده بخش خدمات ما در صفحه اصلی">✦ بخش خدمات ما (صفحه اصلی)</a>
    <a href="services.html" data-switch-page="services" class="toolbar-btn {srv_btn_active}" id="toolbarBtnServices" title="مشاهده صفحه جامع خدمات">📋 صفحه جامع خدمات</a>
    <button type="button" class="toolbar-btn" id="btnToggleLogoLayout" title="تغییر چیدمان لوگو">لوگو: افقی (هدر)</button>
    <button type="button" class="toolbar-btn" id="btnToggleEdit" title="ویرایش مستقیم تمام متون">✎ ویرایش متن‌ها</button>
  </div>

  <div class="toast-msg" id="toastMsg" role="status" aria-live="polite"></div>

  <!-- Synchronous Image Hydration & Unified Internal Router -->
  <script>
    (function() {{
      const ASSETS = {json.dumps(js_asset_map)};
      // Hydrate all deduplicated images before first paint
      document.querySelectorAll('img').forEach((img) => {{
        const s = img.getAttribute('src');
        if (s && ASSETS[s]) img.setAttribute('src', ASSETS[s]);
      }});
      document.querySelectorAll('[style*="__ASSET_"]').forEach((el) => {{
        let st = el.getAttribute('style') || '';
        Object.keys(ASSETS).forEach((k) => {{
          if (st.includes(k)) st = st.split(k).join(ASSETS[k]);
        }});
        el.setAttribute('style', st);
      }});

      const DEDICATED_SERVICES = {json.dumps(all_dedicated_services, ensure_ascii=False)};

      window.switchSitePage = function(targetPage, scrollSelector, serviceSlug) {{
        const homeView = document.getElementById('homePageView');
        const srvView = document.getElementById('servicesPageView');
        const singleView = document.getElementById('singleServicePageView');
        const btnHome = document.getElementById('toolbarBtnHome');
        const btnSrv = document.getElementById('toolbarBtnServices');

        // Close any open modals
        document.querySelectorAll('.modal-backdrop.open').forEach(m => m.classList.remove('open'));

        if (targetPage === 'single' && serviceSlug && DEDICATED_SERVICES[serviceSlug]) {{
          const info = DEDICATED_SERVICES[serviceSlug];
          document.getElementById('singleSrvBreadcrumbTitle').textContent = info.title;
          document.getElementById('singleSrvBadge').textContent = info.cat;
          document.getElementById('singleSrvTitle').textContent = info.title;
          document.getElementById('singleSrvDesc').textContent = info.desc;
          const ul = document.getElementById('singleSrvHighlights');
          ul.innerHTML = (info.highlights || []).map(h => `<li style="margin-bottom:8px;">${{h}}</li>`).join('');
          homeView.style.display = 'none';
          srvView.style.display = 'none';
          singleView.style.display = 'block';
          window.scrollTo({{ top: 0, behavior: 'smooth' }});
          return;
        }}

        if (targetPage === 'home') {{
          homeView.style.display = 'block';
          srvView.style.display = 'none';
          singleView.style.display = 'none';
          btnHome?.classList.add('active');
          btnSrv?.classList.remove('active');
          if (scrollSelector) {{
            setTimeout(() => {{
              const el = homeView.querySelector(scrollSelector);
              if (el) el.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
            }}, 60);
          }} else {{
            window.scrollTo({{ top: 0, behavior: 'smooth' }});
          }}
        }} else {{
          homeView.style.display = 'none';
          srvView.style.display = 'block';
          singleView.style.display = 'none';
          btnHome?.classList.remove('active');
          btnSrv?.classList.add('active');
          if (scrollSelector) {{
            setTimeout(() => {{
              const el = srvView.querySelector(scrollSelector);
              if (el) el.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
            }}, 60);
          }} else {{
            window.scrollTo({{ top: 0, behavior: 'smooth' }});
          }}
        }}
      }};

      // Intercept all internal page-switch links ([data-switch-page], links to index.html, links to services.html, and dedicated service links)
      document.addEventListener('click', (e) => {{
        if (document.body.classList.contains('live-edit-active')) return;

        // 1. Dedicated service detail links (services/<slug>/index.html)
        const srvDetailLink = e.target.closest('[data-service-slug]');
        if (srvDetailLink) {{
          e.preventDefault();
          const slug = srvDetailLink.getAttribute('data-service-slug');
          window.switchSitePage('single', null, slug);
          return;
        }}

        // 2. Explicit switch-page links or links pointing to index.html / services.html
        const link = e.target.closest('a[href]');
        if (!link) return;
        const href = link.getAttribute('href') || '';
        const switchAttr = link.getAttribute('data-switch-page');
        const scrollTarget = link.getAttribute('data-scroll-target');

        if (switchAttr === 'home' || href === 'index.html' || href.startsWith('index.html#')) {{
          e.preventDefault();
          const hash = scrollTarget || (href.includes('#') ? '#' + href.split('#')[1] : null);
          window.switchSitePage('home', hash);
          return;
        }}

        if (switchAttr === 'services' || href === 'services.html' || href.startsWith('services.html#')) {{
          e.preventDefault();
          const hash = scrollTarget || (href.includes('#') ? '#' + href.split('#')[1] : null);
          window.switchSitePage('services', hash);
          return;
        }}
      }});

      // Services Page Interactive Features (FAQ Accordion, 5-Step Process Tabs, Filter Pills, Inline Search)
      document.querySelectorAll('.srv-faq-question').forEach((btn) => {{
        btn.addEventListener('click', () => {{
          const item = btn.closest('.srv-faq-item');
          const isOpen = item.classList.toggle('open');
          const icon = btn.querySelector('.srv-faq-icon');
          if (icon) icon.textContent = isOpen ? '−' : '+';
        }});
      }});

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
    }})();

    {home_script_js}
  </script>
</body>
</html>
'''

index_unified = build_unified_document(default_page="home")
services_unified = build_unified_document(default_page="services")

with open("/home/user/index.html", "w", encoding="utf-8") as f:
    f.write(index_unified)
with open("/home/user/public/index.html", "w", encoding="utf-8") as f:
    f.write(index_unified)
with open("/home/user/services.html", "w", encoding="utf-8") as f:
    f.write(services_unified)
with open("/home/user/services/index.html", "w", encoding="utf-8") as f:
    f.write(services_unified)

print("Successfully built unified index.html and services.html!")
print("index.html size:", len(index_unified), "bytes")
print("services.html size:", len(services_unified), "bytes")

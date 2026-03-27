import re

def update_css(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Font Import
    content = content.replace(
        "@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600&display=swap');",
        "@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap');"
    )
    content = content.replace("font-family: 'Outfit'", "font-family: 'Inter'")

    # 2. Update CSS Variables Block
    new_vars = """
  /* Core palette â€” Sleek Monochrome */
  --bg-primary:    #000000;
  --bg-secondary:  #0a0a0a;
  --bg-card:       #0a0a0a;
  --bg-card-hover: #111111;
  --bg-glass:      rgba(255,255,255,0.03);
  --bg-glass-2:    rgba(255,255,255,0.06);
  --border-glass:  rgba(255,255,255,0.1);
  --border-subtle: rgba(255,255,255,0.05);
  --border-active: rgba(255,255,255,0.25);

  /* Accents â€” Muted minimal */
  --accent-blue:       #fafafa;
  --accent-blue-light: #ffffff;
  --accent-violet:     #d4d4d8;
  --accent-emerald:    #10b981;
  --accent-amber:      #f59e0b;
  --accent-rose:       #ef4444;
  --accent-cyan:       #71717a;
  --accent-pink:       #a1a1aa;

  /* Gradients â€” Removed or subtle */
  --gradient-primary: linear-gradient(180deg, #27272a, #09090b);
  --gradient-success: linear-gradient(180deg, #10b981, #047857);
  --gradient-warm:    linear-gradient(180deg, #f59e0b, #b45309);
  --gradient-cool:    linear-gradient(180deg, #fafafa, #e4e4e7);
  --gradient-aurora:  var(--bg-secondary);
  --gradient-bg:      transparent;

  /* Text */
  --text-primary:   #ededed;
  --text-secondary: #a1a1aa;
  --text-muted:     #71717a;
  --text-accent:    #fafafa;

  /* Sizing */
  --sidebar-width:  260px;
  --topbar-height:  56px;
  --radius-xs:  4px;
  --radius-sm:  6px;
  --radius-md:  8px;
  --radius-lg:  12px;
  --radius-xl:  16px;
  --radius-2xl: 24px;

  /* Shadows â€” Real shadows, not neon */
  --shadow-xs:     0 1px 2px rgba(0,0,0,0.5);
  --shadow-sm:     0 2px 4px rgba(0,0,0,0.6);
  --shadow-md:     0 4px 12px rgba(0,0,0,0.8);
  --shadow-lg:     0 8px 24px rgba(0,0,0,0.9);
  --shadow-glow:   0 0 0 rgba(0,0,0,0);
  --shadow-glow-lg:0 0 0 rgba(0,0,0,0);
  --shadow-card:   0 1px 0 rgba(255,255,255,0.05) inset, 0 4px 6px rgba(0,0,0,1);

  /* Transitions */
  --ease:       cubic-bezier(0.4, 0, 0.2, 1);
  --ease-spring:cubic-bezier(0.175, 0.885, 0.32, 1.05);
  --duration:   0.15s;
  --duration-slow: 0.3s;
"""
    # Use regex to replace the variable block
    content = re.sub(
        r'/\* Core palette.*?--duration-slow:\s*[^\;]+\;\n\}', 
        new_vars.strip() + '\n}', 
        content, 
        flags=re.DOTALL
    )

    # 3. Remove body::before and body::after (animated neon blobs and SVG noise)
    content = re.sub(r'/\* Animated background \*/.+?z-index: 0;\n\}', '', content, flags=re.DOTALL)
    content = re.sub(r'/\* Subtle noise texture \*/.+?opacity: 0\.4;\n\}', '', content, flags=re.DOTALL)

    # 4. Remove sidebar and topbar glow lines
    content = re.sub(r'/\* Sidebar glow line \*/.+?\}', '', content, flags=re.DOTALL)
    content = re.sub(r'/\* Topbar accent line \*/.+?\}', '', content, flags=re.DOTALL)
    
    # 5. Make sidebar flat background
    content = content.replace("background: rgba(7,11,20,0.96);", "background: var(--bg-secondary);")
    content = content.replace("background: rgba(7,11,20,0.82);", "background: var(--bg-secondary);")
    
    # 6. Simplify the UI controls
    # Brand gradient text
    content = re.sub(r'background: linear-gradient\(120deg, \#fff 20%, var\(--accent-blue-light\) 100%\);', "color: var(--text-primary);", content)
    content = re.sub(r'-webkit-background-clip: text;', "", content)
    content = re.sub(r'-webkit-text-fill-color: transparent;', "", content)
    content = re.sub(r'background-clip: text;', "", content)

    # Same for page header h2
    content = re.sub(r'background: linear-gradient\(120deg, \#fff 0%, var\(--accent-blue-light\) 100%\);', "color: var(--text-primary);", content)

    # Glass cards border
    content = content.replace("backdrop-filter: blur(16px) saturate(120%);", "backdrop-filter: none;")
    content = content.replace("-webkit-backdrop-filter: blur(16px) saturate(120%);", "")
    content = content.replace("/* Subtle top highlight */", "")
    content = re.sub(r'\.glass-card::before \{.+?\}', '', content, flags=re.DOTALL)

    # Slider thumb glow
    content = content.replace("box-shadow: 0 0 12px rgba(74,222,128,0.5);", "box-shadow: var(--shadow-sm);")
    content = content.replace("box-shadow: 0 0 20px rgba(74,222,128,0.7);", "box-shadow: var(--shadow-md);")

    # Buttons
    content = content.replace("box-shadow: 0 4px 16px rgba(74,222,128,0.28), inset 0 1px 0 rgba(255,255,255,0.15);", "box-shadow: var(--shadow-sm);")
    content = content.replace("box-shadow: 0 8px 28px rgba(74,222,128,0.42), inset 0 1px 0 rgba(255,255,255,0.2);", "box-shadow: var(--shadow-md);")
    content = content.replace("box-shadow: 0 4px 16px rgba(16,185,129,0.28);", "box-shadow: var(--shadow-sm);")
    content = content.replace("box-shadow: 0 8px 24px rgba(16,185,129,0.38);", "box-shadow: var(--shadow-md);")

    # Explainer callout
    content = content.replace("background: linear-gradient(135deg, rgba(74,222,128,0.07), rgba(45,212,191,0.04));", "background: var(--bg-glass-2);")
    content = content.replace("border: 1px solid rgba(74,222,128,0.12);", "border: 1px solid var(--border-glass);")

    # Forms focus
    content = content.replace("box-shadow: 0 0 0 3px rgba(74,222,128,0.1);", "box-shadow: 0 0 0 2px var(--border-active);")
    content = content.replace("box-shadow: 0 0 0 3px rgba(74,222,128,0.08);", "box-shadow: 0 0 0 2px var(--border-active);")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print("Success")

if __name__ == '__main__':
    update_css('c:/Users/Ragul/Downloads/ML-SAAS-main/ML-SAAS-main/css/style.css')

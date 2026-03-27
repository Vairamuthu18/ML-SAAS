import glob
import os
import re

base = r'c:\Users\Ragul\Downloads\ML-SAAS-main\ML-SAAS-main\js'

def fix_content(content):
    # Headers
    content = re.sub(r'<h3>.*? Parameters</h3>', r'<h3>⚙️ Parameters</h3>', content)
    content = re.sub(r'<h3>.*? Python Equivalent</h3>', r'<h3>🐍 Python Equivalent</h3>', content)
    content = re.sub(r'<h3>.*? Bias-Variance Tradeoff</h3>', r'<h3>⚖️ Bias-Variance Tradeoff</h3>', content)
    content = re.sub(r'<h3>.*? Metrics</h3>', r'<h3>📊 Metrics</h3>', content)
    content = re.sub(r'<h3>.*? Loss Curve</h3>', r'<h3>📉 Loss Curve</h3>', content)
    content = re.sub(r'<h3>.*? Inertia Curve</h3>', r'<h3>📉 Inertia Curve</h3>', content)
    content = re.sub(r'<h3>.*? Tree Structure</h3>', r'<h3>🌳 Tree Structure</h3>', content)
    content = re.sub(r'<h3>.*? Network Topology</h3>', r'<h3>🧠 Network Topology</h3>', content)
    content = re.sub(r'<h3>.*? Training Curves</h3>', r'<h3>📈 Training Curves</h3>', content)
    content = re.sub(r'<h3>.*? Overfitting vs Underfitting</h3>', r'<h3>📈 Overfitting vs Underfitting</h3>', content)

    # Callouts & Badges
    content = re.sub(r'<div class="callout-title">.*? What to Watch</div>', r'<div class="callout-title">💡 What to Watch</div>', content)
    content = re.sub(r'<div class="callout-title">.*? What is SVM\?</div>', r'<div class="callout-title">💡 What is SVM?</div>', content)
    content = re.sub(r'<div class="callout-title">.*? How Neural Networks Learn</div>', r'<div class="callout-title">💡 How Neural Networks Learn</div>', content)
    content = re.sub(r'<div class="callout-title">.*? What is Linear Regression\?</div>', r'<div class="callout-title">💡 What is Linear Regression?</div>', content)
    content = re.sub(r'<div class="callout-title">.*? How K-Means Works</div>', r'<div class="callout-title">💡 How K-Means Works</div>', content)
    content = re.sub(r'<div class="callout-title">.*? How Decision Trees Work</div>', r'<div class="callout-title">💡 How Decision Trees Work</div>', content)
    content = re.sub(r'<span class="steps-badge">.*? How It Works</span>', r'<span class="steps-badge">📚 How It Works</span>', content)
    content = re.sub(r'Real-World Examples:</strong>', r'🌎 Real-World Examples:</strong>', content)

    # Buttons
    content = re.sub(r'>.*? Step</button>', r'>⏭ Step</button>', content)
    content = re.sub(r'>.*? Run</button>', r'>▶ Run</button>', content)
    content = re.sub(r'>.*? Train</button>', r'>▶ Train</button>', content)
    content = re.sub(r'>.*? Reset</button>', r'>↺ Reset</button>', content)
    content = re.sub(r'>.*? Build Tree</button>', r'>🌳 Build Tree</button>', content)

    # JS strings
    content = re.sub(r"\.textContent\s*=\s*'[^']*? Pause'", r".textContent = '⏸ Pause'", content)
    content = re.sub(r"\.textContent\s*=\s*'[^']*? Converged!'", r".textContent = '✅ Converged!'", content)
    content = re.sub(r"\.textContent\s*=\s*'[^']*? Training\.\.\.'", r".textContent = '🔄 Training...'", content)

    # Formulas
    content = re.sub(r'w [^\s]+? w[\s]+−', r'w ← w −', content)
    content = re.sub(r'b [^\s]+? b[\s]+−', r'b ← b −', content)
    content = re.sub(r'c1, c2, [^\s]+?, ck', r'c₁, c₂, …, cₖ', content)

    # Specific broken step icons
    content = re.sub(r'<div class="step-icon">.*?</div>', lambda m: fix_step_icon(m.group(0)), content)

    # Durations
    content = re.sub(r'<span class="lesson-duration">.*? ~(.*?)</span>', r'<span class="lesson-duration">⏱ ~\1</span>', content)

    return content

def fix_step_icon(icon_str):
    # We will identify the broken icon by looking for common sequences we know were corrupted
    # Or just replace the whole tag based on what we know is in the files.
    # Actually, a simpler way is to just let the specific files retain their structure.
    return icon_str

for fp in glob.glob(os.path.join(base, '**', '*.js'), recursive=True):
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()

    orig = content
    content = fix_content(content)
        
    if content != orig:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Fixed: {os.path.basename(fp)}')

print('Done!')

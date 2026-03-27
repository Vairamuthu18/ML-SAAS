import re
import os

base = r'c:\Users\Ragul\Downloads\ML-SAAS-main\ML-SAAS-main\js'

def replace_in_file(filename, replacements):
    path = os.path.join(base, 'pages', filename)
    with open(path, 'r', encoding='utf-8', errors='surrogateescape') as f:
        content = f.read()

    orig = content
    for pattern, repl in replacements:
        content = re.sub(pattern, repl, content)

    if content != orig:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed {filename}")

# svm.js
replace_in_file('svm.js', [
    (r'<div class="step-icon">[^<]*?</div>\s*<div class="step-formula">w', r'<div class="step-icon">⬇️</div>\n          <div class="step-formula">w'),
    (r'<div class="step-icon">[^<]*?</div>\s*<div class="step-desc">The margin', r'<div class="step-icon">🔁</div>\n          <div class="step-desc">The margin')
])

# neuralNetwork.js
replace_in_file('neuralNetwork.js', [
    (r'<div class="step-icon">[^<]*?</div>\s*<div class="step-formula">∂Loss', r'<div class="step-icon">⬅️</div>\n          <div class="step-formula">∂Loss'),
    (r'<div class="step-icon">[^<]*?</div>\s*<div class="step-desc">Weights are', r'<div class="step-icon">🔁</div>\n          <div class="step-desc">Weights are')
])

# linearRegression.js
replace_in_file('linearRegression.js', [
    (r'<strong style="color:var\(--accent-blue-light\);">[^<]*?Real-World Examples:</strong>', r'<strong style="color:var(--accent-blue-light);">🌎 Real-World Examples:</strong>'),
    (r'<div style="font-size:1\.3rem;margin-bottom:6px;">[^<]*?</div>\s*<strong>1\. Features', r'<div style="font-size:1.3rem;margin-bottom:6px;">🎛️</div>\n        <strong>1. Features'),
    (r'<div style="font-size:1\.3rem;margin-bottom:6px;">[^<]*?</div>\s*<strong>3\. Training', r'<div style="font-size:1.3rem;margin-bottom:6px;">📈</div>\n        <strong>3. Training'),
    (r'<div class="step-icon">[^<]*?</div>\s*<div class="step-formula">w', r'<div class="step-icon">⬇️</div>\n          <div class="step-formula">w'),
    (r'<div class="step-icon">[^<]*?</div>\s*<div class="step-desc">The parameters', r'<div class="step-icon">🔁</div>\n          <div class="step-desc">The parameters')
])

# kmeans.js
replace_in_file('kmeans.js', [
    (r'<div class="step-icon">[^<]*?</div>\s*<div class="step-title">1\. Initialize', r'<div class="step-icon">❓</div>\n          <div class="step-title">1. Initialize'),
    (r'<div class="step-icon">[^<]*?</div>\s*<div class="step-title">2\. Assign', r'<div class="step-icon">📏</div>\n          <div class="step-title">2. Assign'),
    (r'<div class="step-icon">[^<]*?</div>\s*<div class="step-formula">Distance', r'<div class="step-icon">📏</div>\n          <div class="step-formula">Distance'),
    (r'<div class="step-icon">[^<]*?</div>\s*<div class="step-title">4\. Repeat', r'<div class="step-icon">🔁</div>\n          <div class="step-title">4. Repeat')
])

# explainers.js
replace_in_file('explainers.js', [
    (r'[^<]*?<strong>Balanced</strong> — The model has a good', r'⚖️ <strong>Balanced</strong> — The model has a good'),
    (r"status\.textContent='[^']*?Slow convergence", r"status.textContent='🐌 Slow convergence"),
    (r"status\.textContent='[^']*?Very slow convergence", r"status.textContent='🐌 Very slow convergence"),
    (r"el\.innerHTML='[^']*?<strong>[^<]*?High Bias", r"el.innerHTML='📏 <strong>High Bias"),
    (r"el\.innerHTML='[^']*?<strong>Balanced</strong> — Good tradeoff", r"el.innerHTML='⚖️ <strong>Balanced</strong> — Good tradeoff")
])

# decisionTree.js
replace_in_file('decisionTree.js', [
    (r'<div class="step-icon">[^<]*?</div>\s*<div class="step-title">1\. Evaluate', r'<div class="step-icon">✂️</div>\n          <div class="step-title">1. Evaluate'),
    (r'<div class="step-icon">[^<]*?</div>\s*<div class="step-title">3\. Repeat', r'<div class="step-icon">🔁</div>\n          <div class="step-title">3. Repeat')
])

# dataPlayground.js
replace_in_file('dataPlayground.js', [
    (r'<div class="upload-icon">[^<]*?</div>', r'<div class="upload-icon">📁</div>')
])

# dashboard.js (in case `ðŸ§ª` is still in the emerald stat-icon)
replace_in_file('dashboard.js', [
    (r'<div class="stat-icon emerald"[^>]*>[^<]*?</div>', r'<div class="stat-icon emerald" style="font-size:1.25rem;">🧫</div>')
])

print("Done with final stragglers!")

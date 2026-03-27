import json
import os

base = r'c:\Users\Ragul\Downloads\ML-SAAS-main\ML-SAAS-main\js\pages'

replacements = {
    'svm.js': [
        ('          <div class="step-icon">Ã¢Â¬â€¡Ã¯Â¸Â </div>', '          <div class="step-icon">⬇️</div>'),
        ('          <div class="step-formula">w Ã¢â€ Â  w − α(∂L/∂w) | b Ã¢â€ Â  b − α(∂L/∂b)</div>', '          <div class="step-formula">w ← w − α(∂L/∂w) | b ← b − α(∂L/∂b)</div>'),
        ('          <div class="step-icon">Ã°Å¸â€ Â </div>', '          <div class="step-icon">🔁</div>')
    ],
    'neuralNetwork.js': [
        ('          <div class="step-icon">Ã¢Â¬â€¦Ã¯Â¸Â </div>', '          <div class="step-icon">⬅️</div>'),
        ('          <div class="step-formula">∂Loss/∂w via chain rule → w Ã¢â€ Â  w − α · ∂Loss/∂w</div>', '          <div class="step-formula">∂Loss/∂w via chain rule → w ← w − α · ∂Loss/∂w</div>'),
        ('          <div class="step-icon">Ã°Å¸â€ Â </div>', '          <div class="step-icon">🔁</div>')
    ],
    'linearRegression.js': [
        ('          <div class="step-icon">Ã¢Â¬â€¡Ã¯Â¸Â </div>', '          <div class="step-icon">⬇️</div>'),
        ('          <div class="step-formula">w Ã¢â€ Â  w − α · ∂Loss/∂w &nbsp;|&nbsp; b Ã¢â€ Â  b − α · ∂Loss/∂b</div>', '          <div class="step-formula">w ← w − α · ∂Loss/∂w &nbsp;|&nbsp; b ← b − α · ∂Loss/∂b</div>'),
        ('          <div class="step-icon">Ã°Å¸â€ Â </div>', '          <div class="step-icon">🔁</div>'),
        ('        <div style="font-size:1.3rem;margin-bottom:6px;">ðŸŽšï¸ </div>', '        <div style="font-size:1.3rem;margin-bottom:6px;">🎛️</div>'),
        ('        <div style="font-size:1.3rem;margin-bottom:6px;">ðŸ“ </div>', '        <div style="font-size:1.3rem;margin-bottom:6px;">📈</div>')
    ],
    'kmeans.js': [
        ('          <div class="step-icon">Ã¢Â â€œ</div>', '          <div class="step-icon">❓</div>'),
        ('          <div class="step-formula">K random points → cÃ¢â€šÂ , c₂, …, cₖ</div>', '          <div class="step-formula">K random points → c₁, c₂, …, cₖ</div>'),
        ('          <div class="step-icon">Ã°Å¸â€œÂ </div>', '          <div class="step-icon">📏</div>'),
        ('          <div class="step-icon">Ã°Å¸â€ Â </div>', '          <div class="step-icon">🔁</div>')
    ],
    'decisionTree.js': [
        ('          <div class="step-icon">Ã¢Å“â€šÃ¯Â¸Â </div>', '          <div class="step-icon">✂️</div>'),
        ('          <div class="step-icon">Ã°Å¸â€ Â </div>', '          <div class="step-icon">🔁</div>')
    ]
}

for filename, reps in replacements.items():
    path = os.path.join(base, filename)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    orig = content
    for bad, good in reps:
        # We replace literally the exact text found in grep
        content = content.replace(bad, good)
        
    if content != orig:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed {filename}")

print('Done!')

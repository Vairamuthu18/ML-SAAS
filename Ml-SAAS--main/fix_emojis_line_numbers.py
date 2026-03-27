import os

base = r'c:\Users\Ragul\Downloads\ML-SAAS-main\ML-SAAS-main\js\pages'

repls = {
    'svm.js': {
        202: '          <div class="step-icon">⬇️</div>\n',
        208: '          <div class="step-formula">w ← w − α(∂L/∂w) | b ← b − α(∂L/∂b)</div>\n',
        216: '          <div class="step-icon">🔁</div>\n'
    },
    'neuralNetwork.js': {
        190: '          <div class="step-icon">🧫</div>\n',
        246: '          <div class="step-icon">⬅️</div>\n',
        252: '          <div class="step-formula">∂Loss/∂w via chain rule → w ← w − α · ∂Loss/∂w</div>\n',
        260: '          <div class="step-icon">🔁</div>\n'
    },
    'linearRegression.js': {
        44: '        <strong style="color:var(--accent-blue-light);">🌎 Real-World Examples:</strong> Predicting <em>house prices</em> based on square footage, estimating <em>salary</em> from years of experience, forecasting <em>sales revenue</em> from advertising spend, or predicting <em>temperature</em> trends over time. Any scenario where the relationship between input and output is approximately linear.\n',
        66: '        <div style="font-size:1.3rem;margin-bottom:6px;">🎛️</div>\n',
        86: '        <div style="font-size:1.3rem;margin-bottom:6px;">📈</div>\n',
        384: '          <div class="step-icon">⬇️</div>\n',
        390: '          <div class="step-formula">w ← w − α · ∂Loss/∂w &nbsp;|&nbsp; b ← b − α · ∂Loss/∂b</div>\n',
        398: '          <div class="step-icon">🔁</div>\n'
    },
    'kmeans.js': {
        226: '          <div class="step-icon">❓</div>\n',
        246: '          <div class="step-formula">K random points → c₁, c₂, …, cₖ</div>\n',
        254: '          <div class="step-icon">📏</div>\n',
        268: '          <div class="step-icon">📏</div>\n',
        282: '          <div class="step-icon">🔁</div>\n'
    },
    'decisionTree.js': {
        208: '          <div class="step-icon">✂️</div>\n',
        222: '          <div class="step-icon">🔁</div>\n'
    },
    'explainers.js': {
        130: '          ⚖️ <strong>Balanced</strong> — The model has a good tradeoff between bias and variance.\n',
        408: "    else{status.textContent='🐌 Very slow convergence — might need more epochs';status.style.color='var(--accent-cyan)';}\n",
        466: "    if(complexity<=3) el.innerHTML='📏 <strong>High Bias</strong> — Model is too simple. It underfits the data, missing important patterns.';\n",
        468: "    else if(complexity<=7) el.innerHTML='⚖️ <strong>Balanced</strong> — Good tradeoff! Model captures patterns without memorizing noise.';\n"
    },
    'dataPlayground.js': {
        25: '          <div class="upload-icon">📁</div>\n'
    },
    'dashboard.js': {
        132: '        <div class="stat-icon emerald" style="font-size:1.25rem;">🧫</div>\n'
    }
}

for filename, lines_map in repls.items():
    path = os.path.join(base, filename)
    if not os.path.exists(path):
        continue
    with open(path, 'r', encoding='utf-8', errors='replace') as f:
        lines = f.readlines()
        
    for line_idx, new_line in lines_map.items():
        if line_idx < len(lines):
            lines[line_idx] = new_line
            
    with open(path, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    print(f"Fixed {filename}")

print('Done!')

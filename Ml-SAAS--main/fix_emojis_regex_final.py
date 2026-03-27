import glob
import os
import re

base = r'c:\Users\Ragul\Downloads\ML-SAAS-main\ML-SAAS-main\js'

def fix_content(content):
    # Step icons
    content = re.sub(r'<div class="step-icon">.*?â€¡.*?</div>', r'<div class="step-icon">⬇️</div>', content)
    content = re.sub(r'<div class="step-icon">.*?â€ .*?</div>', r'<div class="step-icon">🔁</div>', content)
    content = re.sub(r'<div class="step-icon">.*?â€¦.*?</div>', r'<div class="step-icon">⬅️</div>', content)
    content = re.sub(r'<div class="step-icon">.*?â€œ.*?</div>', r'<div class="step-icon">❓</div>', content)
    content = re.sub(r'<div class="step-icon">.*?â€œ.*?</div>', r'<div class="step-icon">📏</div>', content) # Might conflict but â€œ is ❓ in kmeans
    content = re.sub(r'<div class="step-icon">.*?Å“.*?</div>', r'<div class="step-icon">✂️</div>', content)
    content = re.sub(r'<div class="step-icon">.*?§ª.*?</div>', r'<div class="step-icon">🧫</div>', content)
    content = re.sub(r'<div class="stat-icon emerald".*?>.*?§ª.*?</div>', r'<div class="stat-icon emerald" style="font-size:1.25rem;">🧫</div>', content)
    
    # Formulas & text
    content = re.sub(r'w .*?â€ .*? w − α', r'w ← w − α', content)
    content = re.sub(r'b .*?â€ .*? b − α', r'b ← b − α', content)
    content = re.sub(r'w .*?â€ .*? w − α · ∂Loss/∂w', r'w ← w − α · ∂Loss/∂w', content)
    content = re.sub(r'b .*?â€ .*? b − α · ∂Loss/∂b', r'b ← b − α · ∂Loss/∂b', content)
    
    content = re.sub(r'Use <em>.*? Step</em>', r'Use <em>⏭ Step</em>', content)
    content = re.sub(r'c1, c2, .*?, ck', r'c₁, c₂, …, cₖ', content)
    
    # Specifics from grep
    content = re.sub(r'.*? Balanced</span>', r'⚖️ Balanced</span>', content)
    content = re.sub(r'.*? Balanced —', r'⚖️ Balanced —', content)
    content = re.sub(r'Very slow convergence', r'🐌 Very slow convergence', content)
    content = re.sub(r'High Bias', r'📏 High Bias', content)

    # Clean up the double-globe
    content = re.sub(r'ðŸŒ  🌎 Real-World Examples', r'🌎 Real-World Examples', content)
    
    # The random icons
    content = re.sub(r'<div style="font-size:1\.3rem;margin-bottom:6px;">.*?Žš.*?</div>', r'<div style="font-size:1.3rem;margin-bottom:6px;">🎛️</div>', content)
    content = re.sub(r'<div style="font-size:1\.3rem;margin-bottom:6px;">.*?“ .*?</div>', r'<div style="font-size:1.3rem;margin-bottom:6px;">📈</div>', content)
    content = re.sub(r'<div class="upload-icon">.*?“ .*?</div>', r'<div class="upload-icon">📁</div>', content)
    
    # Exact string fallback replacing any remaining Ã... and ð... if they miraculously match
    content = content.replace('Ã¢Â¬â€¡Ã¯Â¸Â', '⬇️')
    content = content.replace('Ã¢â€ Â', '←')
    content = content.replace('Ã°Å¸â€ Â', '🔁')
    content = content.replace('Ã¢Â¬â€¦Ã¯Â¸Â', '⬅️')
    content = content.replace('Ã¢Å“â€šÃ¯Â¸Â', '✂️')
    content = content.replace('Ã¢Â â€œ', '❓')
    content = content.replace('Ã°Å¸â€œÂ', '📏')
    content = content.replace('Ã¢Å¡â€“Ã¯Â¸Â', '⚖️')
    content = content.replace('Ã°Å¸Â Å’', '🐌')
    content = content.replace('Ã¢Â Â­', '⏭')

    return content

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

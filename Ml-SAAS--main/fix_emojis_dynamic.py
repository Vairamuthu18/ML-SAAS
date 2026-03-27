import glob
import os

base = r'c:\Users\Ragul\Downloads\ML-SAAS-main\ML-SAAS-main\js'

# The actual intended symbols
original_emojis = [
    '⚙️', '⏭', '🐍', '⬇️', '←', '🔁', '⏸', '⚠️', '⚖️', '🐌', '✂️', '⏱', 
    '⬅️', '➡️', '❓', 'c₁', 'c₂', 'cₖ', '📏', '▶', '↺', '💡', '📊', '📉', 
    '📚', '📦', '🎲', '🔮', '🧠', '🧫', '🌎', '🎛️', '🎯', '📈', '✅', '🔄', 
    '🔴', '🌊', '🌳', '—', '──', '∂', 'α', '−', 'λ', '‖', '²', 'σ', 'Σ', 'ᵢ', '·', 'ŷ',
    '⚙️ ', '⏭️ ', '🐍 ', '⬇️ ', '← ', '🔁 ', '⏸ ', '⚠️ ', '⚖️ ', '✂️ ', '⬅️ ', '➡️ ', '📏 ',
    # Newly discovered from grep:
    '🧫', '🌎', '🎛️', '📈', '📋', '📁', '👋', '🚀', '🔬', '🤔', '🎓', '💎'
]

replacements = {}
# Calculate both latin-1 and cp1252 variations
for e in original_emojis:
    utf8_bytes = e.encode('utf-8')
    try:
        replacements[utf8_bytes.decode('latin-1')] = e
    except:
        pass
    try:
        replacements[utf8_bytes.decode('cp1252')] = e
    except:
        pass

# Hardcoded fallback for the double-corrupted ones that standard decode doesn't catch
replacements['Ã¢Å¡â„¢Ã¯Â¸Â'] = '⚙️'
replacements['Ã¢Â Â­'] = '⏭'
replacements['Ã°Å¸Â Â'] = '🐍'
replacements['Ã¢Â¬â€¡Ã¯Â¸Â'] = '⬇️'
replacements['Ã¢â€ Â'] = '←'
replacements['Ã°Å¸â€ Â'] = '🔁'
replacements['Ã¢Â Â¸'] = '⏸'
replacements['Ã¢Â â€œ'] = '❓'
replacements['Ã°Å¸â€œÂ'] = '📏'
replacements['Ã¢Å¡Â Ã¯Â¸Â'] = '⚠️'
replacements['Ã¢Å¡â€“Ã¯Â¸Â'] = '⚖️'
replacements['Ã°Å¸Â Å’'] = '🐌'
replacements['Ã¢Å“â€šÃ¯Â¸Â'] = '✂️'
replacements['Ã¢Â Â±'] = '⏱'
replacements['Ã¢Â¬â€¦Ã¯Â¸Â'] = '⬅️'
replacements['Ã¢Å¾Â¡Ã¯Â¸Â'] = '➡️'

# Sort by length descending so longer strings match first
sorted_bad = sorted(replacements.keys(), key=len, reverse=True)

for fp in glob.glob(os.path.join(base, '**', '*.js'), recursive=True):
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()

    orig = content
    for bad in sorted_bad:
        good = replacements[bad]
        content = content.replace(bad, good)
        
    if content != orig:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Fixed: {os.path.basename(fp)}')

print('Done!')

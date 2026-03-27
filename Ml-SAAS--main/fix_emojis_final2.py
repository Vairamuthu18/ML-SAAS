import glob
import os

base = r'c:\Users\Ragul\Downloads\ML-SAAS-main\ML-SAAS-main\js'

replacements = {
    'Ã¢Å¡â„¢Ã¯Â¸Â ': '⚙️ ',
    'Ã¢Â Â­': '⏭',
    'Ã°Å¸Â Â ': '🐍 ',
    'Ã¢Â¬â€¡Ã¯Â¸Â ': '⬇️ ',
    'Ã¢â€ Â ': '← ',
    'Ã°Å¸â€ Â ': '🔁 ',
    'Ã¢Â Â¸': '⏸',
    'Ã¢Â â€œ': '❓',
    'Ã°Å¸â€œÂ ': '📏 ',
    'Ã¢Å¡Â Ã¯Â¸Â ': '⚠️ ',
    'Ã¢Å¡â€“Ã¯Â¸Â ': '⚖️ ',
    'Ã°Å¸Â Å’': '🐌',
    'Ã¢Å“â€šÃ¯Â¸Â ': '✂️ ',
    'Ã¢Â Â±': '⏱',
    'Ã¢Â¬â€¦Ã¯Â¸Â ': '⬅️ ',
    'Ã¢Å¾Â¡Ã¯Â¸Â ': '➡️ ',
    'cÃ¢â€šÂ ': 'c₁',
    'câ‚‚': 'c₂',
    'câ‚–': 'cₖ',
    'â—': '—',
    'â€': '”',
    'âœ': '✔',
    'Ã¢Â¬â€¡Ã¯Â¸Â': '⬇️',
    'Ã¢â€ Â': '←',
    'Ã°Å¸â€ Â': '🔁',
    'Ã¢Å¡Â Ã¯Â¸Â': '⚠️',
    'Ã¢Å“â€šÃ¯Â¸Â': '✂️',
    'Ã¢Â¬â€¦Ã¯Â¸Â': '⬅️',
    'Ã¢Å¾Â¡Ã¯Â¸Â': '➡️',
    'Ã¢Å¡â€“Ã¯Â¸Â': '⚖️',
    'â”€â”€': '──',
    'â€”': '—',
    
    # Mathematical symbols caught earlier that might still be there:
    'âˆ‚': '∂',
    'Î±': 'α',
    'âˆ’': '−',
    'Î»': 'λ',
    'â€–': '‖',
    'Â²': '²',
    'Ïƒ': 'σ',
    'Î£': 'Σ',
    'áµ¢': 'ᵢ',
    'Â·': '·',
    'Å·': 'ŷ',
}

for fp in glob.glob(os.path.join(base, '**', '*.js'), recursive=True):
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    for bad, good in replacements.items():
        content = content.replace(bad, good)
        
    if content != original:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Fixed: {os.path.basename(fp)}')
    else:
        print(f'No changes: {os.path.basename(fp)}')

print('Done!')

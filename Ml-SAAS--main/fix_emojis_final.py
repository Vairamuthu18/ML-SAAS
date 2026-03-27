import glob
import os

base = r'c:\Users\Ragul\Downloads\ML-SAAS-main\ML-SAAS-main\js'

replacements = {
    # BOM
    '\ufeff': '',
    'ï»¿': '',
    
    # Emojis and Symbols (from previous script & double encodings)
    'Ã¢Å¡â„¢Ã¯Â¸Â ': '⚙️ ',
    'Ã¢Å¡â„¢Ã¯Â¸Â': '⚙️',
    'âš™ï¸': '⚙️',
    
    'â–¶': '▶',
    'â†º': '↺',
    'â€”': '—',
    
    'Ã¢Â¬â€¡Ã¯Â¸Â': '⬇️',
    'â¬‡ï¸': '⬇️',
    
    'Ã¢Â¬â€¦Ã¯Â¸Â': '⬅️',
    'â¬…ï¸': '⬅️',
    
    'Ã¢â€ Â': '←',
    'â†': '←',
    
    'Ã°Å¸â€ Â': '🔁',
    
    'ðŸ’¡': '💡',
    
    'â›°ï¸': '🏔️',
    
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
    
    # Others caught earlier
    'â\xad': '⏭',
    'â¸': '⏸',
    'âš ï¸': '⚠️',
    'âš–ï¸': '⚖️',
    'âœ‚ï¸': '✂️',
    'â±': '⏱',
    'â“': '❓',
    'â‚₁': '₁',
    'âž¡ï¸': '➡️',
    
    # Catch any remaining single chars if needed, but let's stick to the observed ones
    'â¬‡ï¸': '⬇️',
    'â†’': '→',
    'â† ': '←',
    'âŒ¨ï¸ ': '⌨️ ',
}

for fp in glob.glob(os.path.join(base, '**', '*.js'), recursive=True):
    with open(fp, 'r', encoding='utf-8') as f:
        try:
            content = f.read()
        except UnicodeDecodeError:
            # Fallback if something is really messed up
            with open(fp, 'r', encoding='latin-1') as f2:
                content = f2.read()

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

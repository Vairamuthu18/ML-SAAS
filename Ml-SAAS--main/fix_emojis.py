import glob
import os

base = r'c:\Users\Ragul\Downloads\ML-SAAS-main\ML-SAAS-main\js'

for fp in glob.glob(os.path.join(base, '**', '*.js'), recursive=True):
    with open(fp, 'rb') as f:
        raw = f.read()
    
    # Decode as latin-1 to get the mojibake text
    text = raw.decode('latin-1')
    
    # Now re-encode from latin-1 chars to bytes, then decode as utf-8
    # The issue is: correct UTF-8 bytes were decoded as latin-1 and saved
    # So we need to find the mojibake sequences and fix them
    
    original = text
    
    # Map of mojibake (latin-1 interpretation of UTF-8 bytes) to correct chars
    fixes = {
        'â\x9a\x99ï¸': '⚙️',
        'â\xad': '⏭',
        'â¸': '⏸',
        'â\x9a ï¸': '⚠️',
        'â\x9a\x96ï¸': '⚖️',
        'â\x9c\x82ï¸': '✂️',
        'â±': '⏱',
        'â\x93': '❓',
        'â\x82\x81': '₁',
        'â¬\x87ï¸': '⬇️',
        'â¬\x85ï¸': '⬅️',
        'â\x9e¡ï¸': '➡️',
        'â\x86\x90': '←',
        'â\x86\x92': '→',
    }
    
    for bad, good in fixes.items():
        text = text.replace(bad, good)
    
    if text != original:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f'Fixed: {os.path.basename(fp)}')
    else:
        print(f'No changes: {os.path.basename(fp)}')

print('Done!')

import os

base1 = r'c:\Users\Ragul\Downloads\ML-SAAS-main\ML-SAAS-main\js\pages'
base2 = r'c:\Users\Ragul\Downloads\ML-SAAS-main\ML-SAAS-main\js'

repls = {
    os.path.join(base2, 'app.js'): {
        52: "    bc.innerHTML = route.breadcrumb.replace('→', '<span style=\"color:var(--text-muted);margin:0 6px\">›</span>');\n"
    },
    os.path.join(base1, 'dashboard.js'): {
        148: '        <div class="stat-icon amber" style="font-size:1.25rem;">⚡</div>\n'
    },
    os.path.join(base1, 'linearRegression.js'): {
        56: '        <div style="font-size:1.3rem;margin-bottom:6px;">⛰️</div>\n'
    }
}

for path, lines_map in repls.items():
    if not os.path.exists(path):
        continue
    with open(path, 'r', encoding='utf-8', errors='replace') as f:
        lines = f.readlines()
        
    for line_idx, new_line in lines_map.items():
        if line_idx < len(lines):
            lines[line_idx] = new_line
            
    with open(path, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    print(f"Fixed {os.path.basename(path)}")

print('Done!')

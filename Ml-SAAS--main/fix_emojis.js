const fs = require('fs');
const path = require('path');

const replacements = {
  'Ã¢Å¡â„¢Ã¯Â¸Â ': '⚙️ ',
  'Ã¢Â Â­': '⏭',
  'Ã°Å¸Â Â ': '🐍 ',
  'Ã¢Â¬â€¡Ã¯Â¸Â ': '⬇️ ',
  'Ã¢Â¬â€¡Ã¯Â¸Â': '⬇️',
  'w Ã¢â€ Â  w': 'w ← w',
  'b Ã¢â€ Â  b': 'b ← b',
  'Ã¢â€ Â': '←',
  'Ã°Å¸â€ Â ': '🔁 ',
  'Ã°Å¸â€ Â': '🔁',
  'Ã¢Â Â¸ Pause': '⏸ Pause',
  'Ã¢Â Â¸': '⏸',
  'Ã¢Å¡Â Ã¯Â¸Â ': '⚠️ ',
  'Ã¢Å¡Â Ã¯Â¸Â': '⚠️',
  'Ã¢Å¡â€“Ã¯Â¸Â ': '⚖️ ',
  'Ã¢Å¡â€“Ã¯Â¸Â': '⚖️',
  'Ã°Å¸Â Å’': '🐌',
  'Ã¢Å“â€šÃ¯Â¸Â ': '✂️ ',
  'Ã¢Å“â€šÃ¯Â¸Â': '✂️',
  'Ã¢Â Â±': '⏱',
  'Ã¢Â¬â€¦Ã¯Â¸Â ': '⬅️ ',
  'Ã¢Â¬â€¦Ã¯Â¸Â': '⬅️',
  'Ã¢Å¾Â¡Ã¯Â¸Â ': '➡️ ',
  'Ã¢Å¾Â¡Ã¯Â¸Â': '➡️',
  'Ã¢Â â€œ': '❓',
  'cÃ¢â€šÂ ': 'c₁',
  'câ‚‚': 'c₂',
  'câ‚–': 'cₖ',
  'Ã°Å¸â€œÂ ': '📏 ',
  'Ã°Å¸â€œÂ': '📏',
  'â–¶': '▶',
  'â†º': '↺',
  
  'ðŸ’¡': '💡',
  'ðŸ“Š': '📊',
  'ðŸ“‰': '📉',
  'ðŸ“š': '📚',
  'ðŸ“¦': '📦',
  'ðŸŽ²': '🎲',
  'ðŸ”®': '🔮',
  'ðŸ§ ': '🧠',
  'ðŸ§ª': '🧫',
  'ðŸŒ ': '🌎',
  'ðŸŽšï¸': '🎛️',
  'ðŸŽ¯': '🎯',
  'ðŸ“ ': '📈',
  'ðŸ“ˆ': '📈',
  'âœ…': '✅',
  'ðŸ”„': '🔄',
  'ðŸ”´': '🔴',
  'ðŸŒŠ': '🌊',
  'ðŸŒ³': '🌳',
  'â€”': '—',
  'â”€â”€': '──',
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
  'Å·': 'ŷ'
};

function walkDir(dir, callback) {
  fs.readdirSync(dir).forEach(f => {
    let dirPath = path.join(dir, f);
    let isDirectory = fs.statSync(dirPath).isDirectory();
    isDirectory ? walkDir(dirPath, callback) : callback(path.join(dir, f));
  });
}

walkDir('c:/Users/Ragul/Downloads/ML-SAAS-main/ML-SAAS-main/js', function(filePath) {
  if (filePath.endsWith('.js')) {
    let content = fs.readFileSync(filePath, 'utf8');
    let orig = content;
    
    for (const [bad, good] of Object.entries(replacements)) {
      content = content.replaceAll(bad, good);
    }
    
    if (content !== orig) {
      fs.writeFileSync(filePath, content, 'utf8');
      console.log('Fixed', filePath);
    }
  }
});

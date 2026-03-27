import os

modules = [
    ('foundations.js', 'foundations'),
    ('dataBasics.js', 'data-basics'),
    ('dataPreprocessing.js', 'data-preprocessing'),
    ('modelEvaluation.js', 'model-evaluation'),
    ('basicMath.js', 'basic-math'),
    ('mlWorkflow.js', 'ml-workflow'),
    ('lossFunction.js', 'loss-function'),
    ('gradientDescent.js', 'gradient-descent'),
    ('linearRegression.js', 'linear-regression'),
    ('logisticRegression.js', 'logistic-regression'),
    ('knn.js', 'knn'),
    ('modelMetrics.js', 'model-metrics'),
    ('kmeans.js', 'k-means'),
    ('decisionTree.js', 'decision-tree'),
    ('neuralNetwork.js', 'neural-network'),
    ('svm.js', 'svm')
]

base_dir = r"c:\Users\abdva\Downloads\Ml-SAAS--main\Ml-SAAS--main\js\pages"

for filename, module_id in modules:
    filepath = os.path.join(base_dir, filename)
    if not os.path.exists(filepath):
        print(f"File not found: {filename}")
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if "renderNextLessonButton" in content:
        print(f"Already processed: {filename}")
        continue
        
    # Prepend import
    import_statement = "import { renderNextLessonButton } from '../progress.js';\n"
    
    # We find the first line that is not a comment and insert the import
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if not line.startswith('//') and line.strip() != '':
            lines.insert(i, import_statement)
            break
            
    new_content = '\n'.join(lines)
    
    # Simple replace the last closing brace in the file
    last_brace_idx = new_content.rfind('}')
    if last_brace_idx != -1:
        new_content = new_content[:last_brace_idx] + f"  renderNextLessonButton(container, '{module_id}');\n}}\n"
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Successfully updated {filename}")
    else:
        print(f"Failed to find end brace for {filename}")

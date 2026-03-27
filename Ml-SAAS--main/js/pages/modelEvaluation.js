// ── Model Evaluation Page — Chapter 4 ──
import { renderNextLessonButton } from '../progress.js';

import { renderQuiz } from '../quizComponent.js';
import { QUIZ_DATA } from '../quizData.js';

export function renderModelEvaluation(container) {
  container.innerHTML = `
    <div class="page-header">
      <span class="lesson-number">Chapter 4 — Model Evaluation</span>
      <h2>Is Your Model Actually Good?</h2>
      <p>Building a model is easy. Making sure it works on NEW data is the hard part.</p>
    </div>

    <!-- Train/Test Concept -->
    <div class="glass-card" style="margin-bottom: 28px;">
      <div class="glass-card-header">
        <h3>🧪 1. The Train vs. Test Concept</h3>
      </div>
      <p style="color: var(--text-secondary); line-height: 1.7; margin-bottom: 20px;">
        Remember Chapter 2? We split data into <strong>Train (80%)</strong> and <strong>Test (20%)</strong>. 
        <br><br>The goal isn't just to memorize the training data; it's to <strong>Generalize</strong> to the test data. Like a student who understands math instead of just memorizing the textbook.
      </p>
    </div>

    <!-- Fitting Concepts -->
    <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 20px; margin-bottom: 28px;">
       <div class="glass-card" style="border-bottom: 3px solid var(--accent-amber);">
         <h4 style="margin-bottom: 8px; font-size: 0.9rem;">📉 Underfitting</h4>
         <p style="font-size: 0.75rem; color: var(--text-secondary);">Model is too simple. It fails to learn the patterns even in training. (e.g., trying to fit a straight line to a curve).</p>
       </div>
       <div class="glass-card" style="border-bottom: 3px solid var(--accent-emerald);">
         <h4 style="margin-bottom: 8px; font-size: 0.9rem;">✅ Good Fit</h4>
         <p style="font-size: 0.75rem; color: var(--text-secondary);">The "Sweet Spot". Model learns the general pattern without getting distracted by noise.</p>
       </div>
       <div class="glass-card" style="border-bottom: 3px solid var(--accent-cyan);">
         <h4 style="margin-bottom: 8px; font-size: 0.9rem;">📈 Overfitting</h4>
         <p style="font-size: 0.75rem; color: var(--text-secondary);">Model is too complex. It "memorizes" every tiny noise point. It looks perfect in training but fails in the real world.</p>
       </div>
    </div>

    <!-- Interactive: Fitting Visualization -->
    <div class="glass-card" style="border-top: 4px solid var(--accent-cyan);">
       <div class="glass-card-header">
         <h3>📊 Interactive: Finding the Sweet Spot</h3>
         <p style="font-size: 0.88rem; color: var(--text-secondary);">Adjust the "Model Complexity" to see how it fits the data points.</p>
       </div>

       <div style="margin-top: 24px; display: grid; grid-template-columns: 1fr 2fr; gap: 30px;">
         <div>
            <div class="slider-group">
              <div class="slider-label">
                <span>Model Complexity</span>
                <span class="slider-value" id="complexity-val">Simple</span>
              </div>
              <input type="range" id="complexity-slider" min="1" max="100" step="1" value="1">
            </div>
            
            <div id="fitting-status" style="margin-top: 30px; padding: 20px; border-radius: 12px; background: rgba(0,0,0,0.2);">
               <h5 id="fitting-title" style="color: var(--accent-amber); margin-bottom: 8px;">Underfitting</h5>
               <p id="fitting-desc" style="font-size: 0.78rem; color: var(--text-muted); line-height: 1.5;">The model is too rigid. It's missing the general shape of the data.</p>
            </div>
         </div>

         <div style="position: relative; background: rgba(255,255,255,0.02); height: 350px; border-radius: 12px; overflow: hidden;">
            <canvas id="fitting-canvas" style="width: 100%; height: 100%;"></canvas>
            <div style="position: absolute; bottom: 10px; right: 10px; font-size: 0.65rem; color: var(--text-muted);">Points = Data, Line = Model</div>
         </div>
       </div>
    </div>
  `;

  // Canvas Logic
  const canvas = document.getElementById('fitting-canvas');
  const ctx = canvas.getContext('2d');
  const slider = document.getElementById('complexity-slider');
  const complexityVal = document.getElementById('complexity-val');
  const fittingTitle = document.getElementById('fitting-title');
  const fittingDesc = document.getElementById('fitting-desc');

  // Set canvas size
  const resize = () => {
    const box = canvas.getBoundingClientRect();
    canvas.width = box.width;
    canvas.height = box.height;
  };
  window.addEventListener('resize', resize);
  resize();

  // Generate noisy data points (sinusoidal)
  const points = [];
  for (let i = 0; i < 15; i++) {
    const x = 50 + (i * (canvas.width - 100)) / 14;
    const baseY = canvas.height / 2 + Math.sin(i * 0.5) * 80;
    const noise = (Math.random() - 0.5) * 40;
    points.push({ x, y: baseY + noise });
  }

  function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    const complexity = parseInt(slider.value);

    // Draw Points
    points.forEach(p => {
      ctx.beginPath();
      ctx.arc(p.x, p.y, 4, 0, Math.PI * 2);
      ctx.fillStyle = 'rgba(255,255,255,0.4)';
      ctx.fill();
    });

    // Draw Curve
    ctx.beginPath();
    ctx.lineWidth = 3;
    
    if (complexity < 20) {
      // Underfit: Just a straight line
      ctx.strokeStyle = '#f59e0b';
      ctx.moveTo(points[0].x, canvas.height/2);
      ctx.lineTo(points[points.length-1].x, canvas.height/2);
      complexityVal.textContent = "Very Simple";
      fittingTitle.textContent = "Underfitting";
      fittingTitle.style.color = "var(--accent-amber)";
      fittingDesc.textContent = "The model is too rigid. It's missing the general shape of the data.";
    } else if (complexity < 70) {
      // Good Fit: Smooth spline
      ctx.strokeStyle = '#10b981';
      ctx.moveTo(points[0].x, points[0].y);
      for (let i = 1; i < points.length; i++) {
        const xc = (points[i].x + points[i-1].x) / 2;
        const yc = (points[i].y + points[i-1].y) / 2;
        const shiftY = Math.sin(xc * 0.01) * (complexity/2); // Dynamic smoothness
        ctx.quadraticCurveTo(points[i-1].x, points[i-1].y, xc, yc);
      }
      complexityVal.textContent = "Good Fit";
      fittingTitle.textContent = "Perfect Balance";
      fittingTitle.style.color = "var(--accent-emerald)";
      fittingDesc.textContent = "This is the 'Sweet Spot'. The model follows the pattern but ignores the tiny noise jumps.";
    } else {
      // Overfit: Wiggly line going through EVERY point
      ctx.strokeStyle = '#06b6d4';
      ctx.moveTo(points[0].x, points[0].y);
      for (let i = 1; i < points.length; i++) {
        const wiggle = (complexity - 70) * (Math.random() - 0.5) * 2; // Add noise
        ctx.lineTo(points[i].x, points[i].y + wiggle);
      }
      complexityVal.textContent = "Complex";
      fittingTitle.textContent = "Overfitting";
      fittingTitle.style.color = "var(--accent-cyan)";
      fittingDesc.textContent = "Now the model is way too complex! It has memorized every noise point and will fail on new data.";
    }
    ctx.stroke();
  }

  slider.oninput = draw;
  draw();

  // Quiz
  renderQuiz(container, QUIZ_DATA.modelEvaluation);
  renderNextLessonButton(container, 'model-evaluation');
}

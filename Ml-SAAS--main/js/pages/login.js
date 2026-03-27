// ── Login Page ──
export function renderLogin(container) {
  container.innerHTML = `
    <div class="auth-page">
      <div class="glass-card auth-card">
        <div class="auth-logo">🧠</div>
        <h2>Welcome Back</h2>
        <p class="auth-subtitle">Sign in to continue your ML journey</p>
        <div class="form-group">
          <label>Email Address</label>
          <input type="email" id="login-email" placeholder="you@example.com">
        </div>
        <div class="form-group">
          <label>Password</label>
          <input type="password" id="login-password" placeholder="••••••••">
        </div>
        <button class="btn btn-primary" style="width:100%;margin-top:8px;" id="login-btn">Sign In</button>
        <p style="margin-top:16px;font-size:0.8rem;color:var(--text-muted);">
          Don't have an account? <a href="#" style="color:var(--accent-blue-light);text-decoration:none;" id="signup-link">Sign Up</a>
        </p>
        <div id="login-msg" style="margin-top:12px;font-size:0.82rem;display:none;padding:10px;border-radius:8px;"></div>
      </div>
    </div>`;

  let isSignup = false;

  document.getElementById('signup-link').addEventListener('click', (e) => {
    e.preventDefault();
    isSignup = !isSignup;
    const card = container.querySelector('.auth-card');
    if (isSignup) {
      card.querySelector('h2').textContent = 'Create Account';
      card.querySelector('.auth-subtitle').textContent = 'Start your ML learning journey today';
      document.getElementById('login-btn').textContent = 'Create Account';
      document.getElementById('signup-link').textContent = 'Sign In';
    } else {
      card.querySelector('h2').textContent = 'Welcome Back';
      card.querySelector('.auth-subtitle').textContent = 'Sign in to continue your ML journey';
      document.getElementById('login-btn').textContent = 'Sign In';
      document.getElementById('signup-link').textContent = 'Sign Up';
    }
  });

  document.getElementById('login-btn').addEventListener('click', () => {
    const email = document.getElementById('login-email').value;
    const msg = document.getElementById('login-msg');
    if (!email) {
      msg.style.display = 'block';
      msg.style.background = 'rgba(244,63,94,0.1)';
      msg.style.color = 'var(--accent-rose)';
      msg.textContent = 'Please enter your email address.';
      return;
    }
    localStorage.setItem('mlviz_user', JSON.stringify({ email, loggedIn: true }));
    msg.style.display = 'block';
    msg.style.background = 'rgba(161,161,170,0.1)';
    msg.style.color = 'var(--accent-emerald)';
    msg.textContent = isSignup ? '✅ Account created! Redirecting...' : '✅ Logged in! Redirecting...';
    setTimeout(() => window.__app.navigate('dashboard'), 1200);
  });
}

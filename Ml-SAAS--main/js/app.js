// ── App Router & Core ──
import { renderDashboard } from './pages/dashboard.js';
import { renderLinearRegression } from './pages/linearRegression.js';
import { renderKMeans } from './pages/kmeans.js';
import { renderDecisionTree } from './pages/decisionTree.js';
import { renderNeuralNetwork } from './pages/neuralNetwork.js';
import { renderSVM } from './pages/svm.js';
import { renderDataPlayground } from './pages/dataPlayground.js';
import { renderExplainers } from './pages/explainers.js';
import { renderFoundations } from './pages/foundations.js';
import { renderDataBasics } from './pages/dataBasics.js';
import { renderDataPreprocessing } from './pages/dataPreprocessing.js';
import { renderModelEvaluation } from './pages/modelEvaluation.js';
import { renderBasicMath } from './pages/basicMath.js';
import { renderMLWorkflow } from './pages/mlWorkflow.js';
import { renderLossFunction } from './pages/lossFunction.js';
import { renderGradientDescent } from './pages/gradientDescent.js';
import { renderKNN } from './pages/knn.js';
import { renderLogisticRegression } from './pages/logisticRegression.js';
import { renderModelMetrics } from './pages/modelMetrics.js';
import { renderPricing } from './pages/pricing.js';
import { renderLogin } from './pages/login.js';

const routes = {
  dashboard: { render: renderDashboard, title: 'Dashboard', breadcrumb: 'Home → Dashboard' },
  'linear-regression': { render: renderLinearRegression, title: 'Linear Regression', breadcrumb: 'Algorithms → Linear Regression' },
  'k-means': { render: renderKMeans, title: 'K-Means Clustering', breadcrumb: 'Algorithms → K-Means Clustering' },
  'decision-tree': { render: renderDecisionTree, title: 'Decision Trees', breadcrumb: 'Algorithms → Decision Trees' },
  'neural-network': { render: renderNeuralNetwork, title: 'Neural Networks', breadcrumb: 'Algorithms → Neural Networks' },
  svm: { render: renderSVM, title: 'SVM', breadcrumb: 'Algorithms → Support Vector Machines' },
  'data-playground': { render: renderDataPlayground, title: 'Data Playground', breadcrumb: 'Tools → Data Playground' },
  foundations: { render: renderFoundations, title: 'Foundations', breadcrumb: 'Course → Foundations' },
  'data-basics': { render: renderDataBasics, title: 'Data Basics', breadcrumb: 'Course → Data Basics' },
  'data-preprocessing': { render: renderDataPreprocessing, title: 'Data Preprocessing', breadcrumb: 'Course → Data Preprocessing' },
  'model-evaluation': { render: renderModelEvaluation, title: 'Model Evaluation', breadcrumb: 'Course → Model Evaluation' },
  'basic-math': { render: renderBasicMath, title: 'Basic Mathematics', breadcrumb: 'Course → Basic Mathematics' },
  'ml-workflow': { render: renderMLWorkflow, title: 'ML Workflow', breadcrumb: 'Course → ML Workflow' },
  'loss-function': { render: renderLossFunction, title: 'Loss Functions', breadcrumb: 'Course → Loss Functions' },
  'gradient-descent': { render: renderGradientDescent, title: 'Gradient Descent', breadcrumb: 'Course → Gradient Descent' },
  knn: { render: renderKNN, title: 'K-Nearest Neighbors', breadcrumb: 'Algorithms → KNN' },
  'logistic-regression': { render: renderLogisticRegression, title: 'Logistic Regression', breadcrumb: 'Algorithms → Logistic Regression' },
  'model-metrics': { render: renderModelMetrics, title: 'Model Metrics', breadcrumb: 'Course → Model Metrics' },
  explainers: { render: renderExplainers, title: 'Explainers', breadcrumb: 'Learn → Why Did This Happen?' },
  pricing: { render: renderPricing, title: 'Pricing', breadcrumb: 'Pricing' },
  login: { render: renderLogin, title: 'Login', breadcrumb: 'Login' }
};

let currentPage = 'dashboard';
let cleanupFn = null;

export function navigate(page) {
  if (cleanupFn) { cleanupFn(); cleanupFn = null; }
  currentPage = page;
  updateActiveNav();
  updateBreadcrumb();
  const mainContent = document.getElementById('page-content');
  mainContent.innerHTML = '';
  mainContent.className = 'page-content';
  const route = routes[page];
  if (route) {
    cleanupFn = route.render(mainContent) || null;
  }
}

function updateActiveNav() {
  document.querySelectorAll('.sidebar-nav a').forEach(a => {
    a.classList.toggle('active', a.dataset.page === currentPage);
  });
}

function updateBreadcrumb() {
  const bc = document.getElementById('breadcrumb');
  const route = routes[currentPage];
  if (bc && route) {
    bc.innerHTML = route.breadcrumb.replace('→', '<span style="color:var(--text-muted);margin:0 6px">›</span>');
  }
}

// Init
document.addEventListener('DOMContentLoaded', () => {
  // Sidebar nav clicks
  document.querySelectorAll('.sidebar-nav a').forEach(a => {
    a.addEventListener('click', (e) => {
      e.preventDefault();
      navigate(a.dataset.page);
    });
  });

  // Mobile menu toggle
  const menuBtn = document.getElementById('menu-toggle');
  const sidebar = document.querySelector('.sidebar');
  if (menuBtn) {
    menuBtn.addEventListener('click', () => sidebar.classList.toggle('open'));
  }

  // Start on dashboard
  navigate('dashboard');
});

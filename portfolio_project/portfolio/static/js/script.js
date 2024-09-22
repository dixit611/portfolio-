// Add this JavaScript to your existing JavaScript file

function toggleMenu() {
  const navbar = document.querySelector('.navbar');
  const menuToggle = document.querySelector('.menu-toggle');
  navbar.classList.toggle('open');
  menuToggle.classList.toggle('open');
}

function showAllProjects() {
  const allProjects = document.querySelectorAll('.portfolio-item');
  allProjects.forEach(project => project.style.display = 'block');
}

function showMinorProjects() {
  const allProjects = document.querySelectorAll('.portfolio-item');
  allProjects.forEach(project => project.style.display = project.getAttribute('data-category') === 'minor' ? 'block' : 'none');
}

function showMajorProjects() {
  const allProjects = document.querySelectorAll('.portfolio-item');
  allProjects.forEach(project => project.style.display = project.getAttribute('data-category') === 'major' ? 'block' : 'none');
}

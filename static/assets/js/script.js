document.addEventListener('DOMContentLoaded', function() {
    // Get all navigation links and the navbar brand
    const navLinks = document.querySelectorAll('.nav-link[data-section-name]');
    const navbarBrand = document.querySelector('.navbar-brand');
    // Get all page sections and animatable elements
    const sections = document.querySelectorAll('.page-section');
    const animatableElements = document.querySelectorAll('.animate-scroll, .animated-heading');

    // Function to handle showing/hiding sections
    function showSection(sectionId) {
        // Hide all sections first
        sections.forEach(section => {
            section.style.display = 'none';
            section.classList.remove('active');
        });

        // Find the target section and show it
        const targetSection = document.getElementById(sectionId);
        if (targetSection) {
            // Use a small timeout to allow the display:block to take effect
            // before applying the opacity change for a smooth transition.
            targetSection.style.display = 'block';
            setTimeout(() => {
                targetSection.classList.add('active');
            }, 50);
        }
    }

    // Function to remove the active class from all nav links
    function deactivateAllNavLinks() {
        navLinks.forEach(navLink => navLink.classList.remove('active-link'));
    }

    // Add click event listener to each nav link
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();

            // Remove active class from all nav links
            deactivateAllNavLinks();

            // Add active class to the clicked link
            this.classList.add('active-link');

            // Get the section name from the data attribute
            const sectionName = this.getAttribute('data-section-name');

            // Call the function to show the corresponding section
            showSection(sectionName);

            // Close the navbar on mobile after a link is clicked
            const navbarCollapse = document.getElementById('navbarNav');
            const bsCollapse = bootstrap.Collapse.getInstance(navbarCollapse);
            if (bsCollapse) {
                bsCollapse.hide();
            }
        });
    });

    // Add a click event listener to the navbar brand
    if (navbarBrand) {
        navbarBrand.addEventListener('click', function(e) {
            e.preventDefault();
            // Remove active class from all nav links
            deactivateAllNavLinks();

            // Add active class to the Home link specifically
            const homeLink = document.querySelector('.nav-link[data-section-name="home"]');
            if (homeLink) {
                homeLink.classList.add('active-link');
            }

            // Show the home section
            showSection('home');

            // Close the navbar on mobile after a link is clicked
            const navbarCollapse = document.getElementById('navbarNav');
            const bsCollapse = bootstrap.Collapse.getInstance(navbarCollapse);
            if (bsCollapse) {
                bsCollapse.hide();
            }
        });
    }


    // Intersection Observer for scroll animations
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Element is visible, add the class to trigger animation
                entry.target.classList.add('visible');
            } else {
                // Element is not visible, remove the class to allow re-animation later
                entry.target.classList.remove('visible');
            }
        });
    }, {
        threshold: 0.1, // Trigger animation when 10% of the element is visible
    });

    // Observe all animatable elements
    animatableElements.forEach(element => {
        observer.observe(element);
    });

    // Portfolio collapse icon and background logic
    const portfolioButtons = document.querySelectorAll('.btn-portfolio');

    // Set initial state for the first collapse button icon and class
    const firstCollapseBtn = document.querySelector('[data-bs-target="#aiProjects"]');
    if (firstCollapseBtn) {
        const firstIcon = firstCollapseBtn.querySelector('.collapse-icon');
        firstIcon.classList.remove('fa-chevron-down');
        firstIcon.classList.add('fa-chevron-up');
        firstCollapseBtn.classList.add('active');
    }

    // Handle collapse show/hide events to change the icon and button style
    const collapses = document.querySelectorAll('.collapse');
    collapses.forEach(collapse => {
        collapse.addEventListener('show.bs.collapse', function() {
            const button = document.querySelector(`[data-bs-target="#${this.id}"]`);
            const icon = button.querySelector('.collapse-icon');
            icon.classList.remove('fa-chevron-down');
            icon.classList.add('fa-chevron-up');
            // Add the 'active' class to the button when the collapse opens
            button.classList.add('active');
        });

        collapse.addEventListener('hide.bs.collapse', function() {
            const button = document.querySelector(`[data-bs-target="#${this.id}"]`);
            const icon = button.querySelector('.collapse-icon');
            icon.classList.remove('fa-chevron-up');
            icon.classList.add('fa-chevron-down');
            // Remove the 'active' class from the button when the collapse closes
            button.classList.remove('active');
        });
    });

    // Show the initial section on page load
    const initialSection = 'home';
    showSection(initialSection);

    // Particle background animation logic
    const canvas = document.getElementById('particle-canvas');
    const ctx = canvas.getContext('2d');
    let particles = [];

    // Set canvas size
    function setCanvasSize() {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    }
    setCanvasSize();

    // Handle window resize
    window.addEventListener('resize', setCanvasSize);

    class Particle {
        constructor(x, y) {
            this.x = x || Math.random() * canvas.width;
            this.y = y || Math.random() * canvas.height;
            this.radius = Math.random() * 2 + 1;
            this.color = `rgba(0, 228, 255, ${Math.random()})`;
            this.velocity = {
                x: (Math.random() - 0.5) * 0.5,
                y: (Math.random() - 0.5) * 0.5
            };
        }

        draw() {
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2, false);
            ctx.fillStyle = this.color;
            ctx.fill();
        }

        update() {
            // Move particle
            this.x += this.velocity.x;
            this.y += this.velocity.y;

            // Reverse direction if particle hits canvas edge
            if (this.x + this.radius > canvas.width || this.x - this.radius < 0) {
                this.velocity.x = -this.velocity.x;
            }
            if (this.y + this.radius > canvas.height || this.y - this.radius < 0) {
                this.velocity.y = -this.velocity.y;
            }

            this.draw();
        }
    }

    // Create particles
    function createParticles() {
        particles = [];
        for (let i = 0; i < 150; i++) {
            particles.push(new Particle());
        }
    }
    createParticles();

    // Draw lines between particles if they are close enough
    function connectParticles() {
        let opacityValue = 1;
        for (let a = 0; a < particles.length; a++) {
            for (let b = a; b < particles.length; b++) {
                let dx = particles[a].x - particles[b].x;
                let dy = particles[a].y - particles[b].y;
                let distance = Math.sqrt(dx * dx + dy * dy);

                if (distance < 100) {
                    opacityValue = 1 - (distance / 100);
                    ctx.strokeStyle = `rgba(0, 228, 255, ${opacityValue})`;
                    ctx.lineWidth = 1;
                    ctx.beginPath();
                    ctx.moveTo(particles[a].x, particles[a].y);
                    ctx.lineTo(particles[b].x, particles[b].y);
                    ctx.stroke();
                }
            }
        }
    }

    // Animation loop
    function animate() {
        requestAnimationFrame(animate);
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        connectParticles();
        particles.forEach(particle => particle.update());
    }

    animate();

    // Get the navbar toggler button and icon element
    const navbarCollapse = document.getElementById('navbarNav');
    const togglerIcon = document.getElementById('navbar-toggler-icon');

    // Listen for Bootstrap's collapse events to change the icon state
    navbarCollapse.addEventListener('shown.bs.collapse', function() {
        // When the navbar is shown (opened), change the icon to a cross
        togglerIcon.classList.remove('fa-bars');
        togglerIcon.classList.add('fa-xmark');
    });

    navbarCollapse.addEventListener('hidden.bs.collapse', function() {
        // When the navbar is hidden (closed), change the icon back to a hamburger
        togglerIcon.classList.remove('fa-xmark');
        togglerIcon.classList.add('fa-bars');
    });
});
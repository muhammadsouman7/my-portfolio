document.addEventListener('DOMContentLoaded', function() {
    // Get all links that have the data-section-name attribute
    const allNavigableLinks = document.querySelectorAll('[data-section-name]');
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
            targetSection.style.display = 'block';
            setTimeout(() => {
                targetSection.classList.add('active');
            }, 50);
        }
    }

    // Function to remove the active class from all nav links
    function deactivateAllNavLinks() {
        allNavigableLinks.forEach(navLink => navLink.classList.remove('active-link'));
    }

    // Add click event listener to each navigable link
    allNavigableLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();

            // Remove active class from all links
            deactivateAllNavLinks();

            // Get the section name from the data attribute of the clicked link
            const sectionName = this.getAttribute('data-section-name');

            // Find the corresponding nav-link in the navbar and add the active class
            const correspondingNavLink = document.querySelector(`.nav-link.custom-link[data-section-name="${sectionName}"]`);
            if (correspondingNavLink) {
                correspondingNavLink.classList.add('active-link');
            }

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

    // Intersection Observer for scroll animations
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            } else {
                entry.target.classList.remove('visible');
            }
        });
    }, {
        threshold: 0.1,
    });

    animatableElements.forEach(element => {
        observer.observe(element);
    });

    const portfolioButtons = document.querySelectorAll('.btn-portfolio');

    const collapses = document.querySelectorAll('.collapse');
    collapses.forEach(collapse => {
        collapse.addEventListener('show.bs.collapse', function() {
            const button = document.querySelector(`[data-bs-target="#${this.id}"]`);
            const icon = button.querySelector('.collapse-icon');
            icon.classList.remove('fa-chevron-down');
            icon.classList.add('fa-chevron-up');
            button.classList.add('active');
        });

        collapse.addEventListener('hide.bs.collapse', function() {
            const button = document.querySelector(`[data-bs-target="#${this.id}"]`);
            const icon = button.querySelector('.collapse-icon');
            icon.classList.remove('fa-chevron-up');
            icon.classList.add('fa-chevron-down');
            button.classList.remove('active');
        });
    });

    // Show the initial section on page load
    const initialSection = 'home';
    showSection(initialSection);

    // Particle background animation logic
    const canvas = document.getElementById('particle-canvas');
    if (canvas) {
        const ctx = canvas.getContext('2d');
        let particles = [];

        function setCanvasSize() {
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
        }
        setCanvasSize();

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
                this.x += this.velocity.x;
                this.y += this.velocity.y;

                if (this.x + this.radius > canvas.width || this.x - this.radius < 0) {
                    this.velocity.x = -this.velocity.x;
                }
                if (this.y + this.radius > canvas.height || this.y - this.radius < 0) {
                    this.velocity.y = -this.velocity.y;
                }
                this.draw();
            }
        }

        function createParticles() {
            particles = [];
            for (let i = 0; i < 150; i++) {
                particles.push(new Particle());
            }
        }
        createParticles();

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

        function animate() {
            requestAnimationFrame(animate);
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            connectParticles();
            particles.forEach(particle => particle.update());
        }

        animate();
    }


    const navbarTogglerBtn = document.querySelector('.navbar-toggler');
    const togglerIcon = document.getElementById('navbar-toggler-icon');

    // Toggle the 'cross' class on click, for an immediate animation
    navbarTogglerBtn.addEventListener('click', function() {
        togglerIcon.classList.toggle('cross');
    });

    const navbarCollapse = document.getElementById('navbarNav');
    // Hide the navbar on click outside when opened
    document.addEventListener('click', function(e) {
        if (!navbarCollapse.contains(e.target) && !navbarTogglerBtn.contains(e.target) && navbarCollapse.classList.contains('show')) {
            const bsCollapse = bootstrap.Collapse.getInstance(navbarCollapse);
            if (bsCollapse) {
                bsCollapse.hide();
            }
        }
    });

    navbarCollapse.addEventListener('hidden.bs.collapse', function() {
        togglerIcon.classList.remove('cross');
    });
});

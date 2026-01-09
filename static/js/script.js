// ModernBlog JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Theme Management
    const themeToggle = document.getElementById('bd-theme');
    const themeButtons = document.querySelectorAll('[data-bs-theme-value]');
    
    // Get stored theme or default to 'auto'
    const storedTheme = localStorage.getItem('theme') || 'auto';
    
    // Set initial theme
    setTheme(storedTheme);
    updateActiveThemeButton(storedTheme);
    
    // Theme button event listeners
    themeButtons.forEach(button => {
        button.addEventListener('click', () => {
            const theme = button.getAttribute('data-bs-theme-value');
            setTheme(theme);
            updateActiveThemeButton(theme);
            localStorage.setItem('theme', theme);
        });
    });
    
    function setTheme(theme) {
        if (theme === 'auto') {
            document.documentElement.setAttribute('data-bs-theme', 
                window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
        } else {
            document.documentElement.setAttribute('data-bs-theme', theme);
        }
    }
    
    function updateActiveThemeButton(theme) {
        themeButtons.forEach(button => {
            button.classList.remove('active');
            if (button.getAttribute('data-bs-theme-value') === theme) {
                button.classList.add('active');
            }
        });
    }
    
    // Listen for system theme changes
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => {
        if (localStorage.getItem('theme') === 'auto') {
            setTheme('auto');
        }
    });
    
    // Smooth scrolling for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
    // Search functionality
    const searchInput = document.querySelector('input[type="search"]');
    const searchButton = document.querySelector('.btn .fa-search').parentElement;
    
    if (searchInput && searchButton) {
        searchButton.addEventListener('click', performSearch);
        searchInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                performSearch();
            }
        });
    }
    
    function performSearch() {
        const query = searchInput.value.trim();
        if (query) {
            // Simulate search (in a real app, this would make an API call)
            showSearchResults(query);
        }
    }
    
    function showSearchResults(query) {
        // Simple search simulation
        alert(`Searching for: "${query}"\n\nIn a real application, this would show search results.`);
    }
    
    // Newsletter subscription
    const newsletterForms = document.querySelectorAll('.input-group');
    newsletterForms.forEach(form => {
        const button = form.querySelector('.btn');
        const input = form.querySelector('input[type="email"]');
        
        if (button && input) {
            button.addEventListener('click', function() {
                const email = input.value.trim();
                if (validateEmail(email)) {
                    subscribeToNewsletter(email);
                } else {
                    showNotification('Please enter a valid email address', 'error');
                }
            });
        }
    });
    
    function validateEmail(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    }
    
    function subscribeToNewsletter(email) {
        // Simulate subscription
        showNotification('Thank you for subscribing!', 'success');
        // Clear the input
        document.querySelectorAll('input[type="email"]').forEach(input => {
            if (input.value === email) {
                input.value = '';
            }
        });
    }
    
    // Notification system
    function showNotification(message, type = 'info') {
        const notification = document.createElement('div');
        notification.className = `alert alert-${type === 'error' ? 'danger' : type} alert-dismissible fade show position-fixed`;
        notification.style.cssText = 'top: 20px; right: 20px; z-index: 1060; min-width: 300px;';
        notification.innerHTML = `
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        `;
        
        document.body.appendChild(notification);
        
        // Auto remove after 5 seconds
        setTimeout(() => {
            if (notification.parentNode) {
                notification.remove();
            }
        }, 5000);
    }
    
    // Animate elements on scroll
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);
    
    // Observe cards for animation
    document.querySelectorAll('.card').forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(card);
    });
    
    // Active navigation highlighting
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
    
    window.addEventListener('scroll', () => {
        let current = '';
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;
            if (window.pageYOffset >= sectionTop - 200) {
                current = section.getAttribute('id');
            }
        });
        
        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === `#${current}`) {
                link.classList.add('active');
            }
        });
    });
    
    // Trending items click tracking
    document.querySelectorAll('.trending-item').forEach(item => {
        item.addEventListener('click', function() {
            const title = this.querySelector('h6').textContent;
            console.log(`Clicked trending item: ${title}`);
            // In a real app, this would track analytics
        });
    });
    
    // Category card hover effects
    document.querySelectorAll('.card').forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px) scale(1.02)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
    });
    
    // Loading state for buttons
    function addLoadingState(button) {
        const originalText = button.innerHTML;
        button.innerHTML = '<span class="loading"></span> Loading...';
        button.disabled = true;
        
        setTimeout(() => {
            button.innerHTML = originalText;
            button.disabled = false;
        }, 2000);
    }
    
    // Add loading state to subscription buttons
    document.querySelectorAll('.btn').forEach(button => {
        if (button.textContent.includes('Subscribe')) {
            button.addEventListener('click', function() {
                addLoadingState(this);
            });
        }
    });
    
    // Keyboard navigation
    document.addEventListener('keydown', function(e) {
        // Press 'S' to focus search
        if (e.key === 's' && !e.ctrlKey && !e.metaKey && e.target.tagName !== 'INPUT') {
            e.preventDefault();
            searchInput?.focus();
        }
        
        // Press 'Escape' to close dropdowns
        if (e.key === 'Escape') {
            document.querySelectorAll('.dropdown-menu.show').forEach(menu => {
                const dropdown = bootstrap.Dropdown.getInstance(menu.previousElementSibling);
                if (dropdown) dropdown.hide();
            });
        }
    });
    
    // Performance optimization: Lazy load images (if any were added)
    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.classList.remove('lazy');
                    imageObserver.unobserve(img);
                }
            });
        });
        
        document.querySelectorAll('img[data-src]').forEach(img => {
            imageObserver.observe(img);
        });
    }
    
    console.log('ModernBlog initialized successfully!');
});
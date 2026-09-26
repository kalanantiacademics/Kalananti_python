import re

with open('level1/main_deck.html', 'r') as f:
    html = f.read()

# 1. Add Canvas element
html = html.replace('<body>', '<body>\n    <canvas id="bgCanvas"></canvas>')

# 2. Add animation CSS and canvas CSS
css_to_add = """
        #bgCanvas {
            position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
            z-index: -10; pointer-events: auto; opacity: 0.6;
        }

        @keyframes slideInUp {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .animate-in {
            animation: slideInUp 0.5s cubic-bezier(0.2, 0.8, 0.2, 1) forwards;
        }
"""
html = html.replace('</style>', css_to_add + '\n    </style>')

# 3. Add the canvas particle script at the end of the body
script_to_add = """
    <script>
        // --- Background Particle Animation ---
        const canvas = document.getElementById('bgCanvas');
        const ctx = canvas.getContext('2d');
        let width, height, particles;

        function initParticles() {
            width = canvas.width = window.innerWidth;
            height = canvas.height = window.innerHeight;
            particles = [];
            const count = Math.min(Math.floor((width * height) / 12000), 100);
            for (let i = 0; i < count; i++) {
                particles.push({
                    x: Math.random() * width,
                    y: Math.random() * height,
                    vx: (Math.random() - 0.5) * 0.8,
                    vy: (Math.random() - 0.5) * 0.8,
                    radius: Math.random() * 2 + 1
                });
            }
        }

        let mouse = { x: null, y: null };
        window.addEventListener('mousemove', e => { mouse.x = e.clientX; mouse.y = e.clientY; });
        window.addEventListener('mouseout', () => { mouse.x = null; mouse.y = null; });
        window.addEventListener('resize', initParticles);

        function drawParticles() {
            ctx.clearRect(0, 0, width, height);
            ctx.fillStyle = '#0ea5e9'; // Kalananti blue

            particles.forEach(p => {
                p.x += p.vx; p.y += p.vy;
                if (p.x < 0 || p.x > width) p.vx *= -1;
                if (p.y < 0 || p.y > height) p.vy *= -1;

                ctx.beginPath();
                ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
                ctx.fill();

                particles.forEach(p2 => {
                    const dx = p.x - p2.x, dy = p.y - p2.y;
                    const dist = Math.sqrt(dx * dx + dy * dy);
                    if (dist < 120) {
                        ctx.beginPath();
                        ctx.strokeStyle = `rgba(14, 165, 233, ${0.15 - dist/120 * 0.15})`;
                        ctx.lineWidth = 1;
                        ctx.moveTo(p.x, p.y); ctx.lineTo(p2.x, p2.y);
                        ctx.stroke();
                    }
                });

                if (mouse.x !== null) {
                    const dx = p.x - mouse.x, dy = p.y - mouse.y;
                    const dist = Math.sqrt(dx * dx + dy * dy);
                    if (dist < 150) {
                        ctx.beginPath();
                        ctx.strokeStyle = `rgba(245, 158, 11, ${0.3 - dist/150 * 0.3})`; // Yellow connection to mouse
                        ctx.lineWidth = 1.5;
                        ctx.moveTo(p.x, p.y); ctx.lineTo(mouse.x, mouse.y);
                        ctx.stroke();
                    }
                }
            });
            requestAnimationFrame(drawParticles);
        }
        initParticles(); drawParticles();
    </script>
"""
html = html.replace('</body>', script_to_add + '\n</body>')

with open('level1/main_deck.html', 'w') as f:
    f.write(html)

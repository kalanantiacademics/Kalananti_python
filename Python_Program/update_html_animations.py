import re

with open('level1/main_deck.html', 'r') as f:
    html = f.read()

animation_css = """
        /* Animations & Illustrations */
        @keyframes floatAnim {
            0%, 100% { transform: translateY(0) rotate(0deg); }
            50% { transform: translateY(-15px) rotate(3deg); }
        }
        @keyframes bounceAnim {
            0%, 100% { transform: translateY(0) scale(1); }
            50% { transform: translateY(-10px) scale(1.05); }
        }
        @keyframes slideInUp {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .anim-float { animation: floatAnim 4s ease-in-out infinite; display: inline-block; }
        .anim-bounce { animation: bounceAnim 2s ease-in-out infinite; display: inline-block; }
        
        .slide-illustration {
            font-size: 5rem;
            line-height: 1;
            filter: drop-shadow(0 15px 15px rgba(2, 132, 199, 0.2));
            margin-bottom: 1rem;
            text-align: center;
        }

        .split-layout {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 2rem;
            align-items: center;
        }
        .split-layout.reverse {
            grid-template-columns: 1fr 1fr;
        }
        .split-layout .illustration-side {
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 8rem;
            filter: drop-shadow(0 20px 20px rgba(14, 165, 233, 0.25));
        }

        /* Add slide-in animation to panels */
        .panel, .hero, .choices {
            animation: slideInUp 0.5s ease-out forwards;
        }
"""

if "/* Animations & Illustrations */" not in html:
    html = html.replace('</style>', animation_css + '\n    </style>')

with open('level1/main_deck.html', 'w') as f:
    f.write(html)

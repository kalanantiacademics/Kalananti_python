import re
import sys

def get_normalized_css():
    return """
        /* --- Mock Window Normalized Components --- */
        .mock-window {
            border-radius: 14px;
            overflow: hidden;
            box-shadow: 0 20px 35px -10px rgba(0, 0, 0, 0.45);
            border: 1px solid rgba(255, 255, 255, 0.15);
            background: #1e1e1e;
            font-family: 'Space Grotesk', sans-serif;
            margin: 1rem auto;
            text-align: left;
        }
        .mock-window.light-mode {
            background: #f8f9fa;
            border-color: #cbd5e1;
            color: #1e293b;
        }
        .mock-window-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 8px 14px;
            background: #2b2b2b;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
        }
        .mock-window.light-mode .mock-window-header {
            background: #e2e8f0;
            border-bottom: 1px solid #cbd5e1;
        }
        .mock-window-title {
            font-size: 11px;
            font-weight: 700;
            letter-spacing: 0.05em;
            color: #cbd5e1;
        }
        .mock-window.light-mode .mock-window-title {
            color: #334155;
        }
        .mock-window-controls {
            display: flex;
            align-items: center;
            gap: 6px;
        }
        .win-btn {
            width: 10px;
            height: 10px;
            border-radius: 50%;
            display: inline-block;
        }
        .win-close { background: #ff5f56; border: 1px solid #e0443e; }
        .win-min { background: #ffbd2e; border: 1px solid #dea123; }
        .win-max { background: #27c93f; border: 1px solid #1aab29; }
        .mock-window-content {
            padding: 16px;
            position: relative;
        }
        .mock-window-badge {
            display: inline-block;
            font-size: 10px;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 0.1em;
            padding: 3px 10px;
            border-radius: 999px;
            background: rgba(38, 94, 155, 0.15);
            color: #2563eb;
            border: 1px solid rgba(37, 99, 235, 0.25);
            margin-bottom: 10px;
        }
        html[data-theme="dark"] .mock-window-badge {
            background: rgba(56, 189, 248, 0.15);
            color: #38bdf8;
            border: 1px solid rgba(56, 189, 248, 0.3);
        }
    """

print("Helper script ready")

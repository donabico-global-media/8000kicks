/**
 * EATHESEN V3000-Ω | AGENTIC LOGIC GATEWAY
 * Vị trí: Gốc (Cùng cấp index.html)
 */
const AgenticSystem = {
    sanitize: () => {
        document.querySelectorAll('a').forEach(a => {
            if (a.getAttribute('href') === '#') {
                a.setAttribute('href', 'javascript:void(0)');
            }
        });
        console.log("[AGENT] Sanitized links - Stable State");
    },
    pulse: () => {
        // Áp dụng viền xanh Active Module theo đúng yêu cầu hệ thống
        const style = document.createElement('style');
        style.innerHTML = `.active-module { border: 2px solid green !important; }`;
        document.head.appendChild(style);
        console.log("[AGENT] Pulse Active - SOTA Mode");
    },
    init: function() {
        this.sanitize();
        this.pulse();
    }
};
document.addEventListener('DOMContentLoaded', () => AgenticSystem.init());

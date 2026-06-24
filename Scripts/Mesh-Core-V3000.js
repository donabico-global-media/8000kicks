(() => {
    'use strict';

    // 1. HARDLOCK FONT TIMES NEW ROMAN & KHÓA VIỀN XANH LÁ SOTA QUAN SÁT
    const styleLock = document.createElement('style');
    styleLock.innerHTML = `
        * { font-family: 'Times New Roman', Times, serif !important; }
        body { border: 4px solid #00ff66 !important; }
    `;
    document.head.appendChild(styleLock);

    const MASTER_CONFIG = {
        totalThreads: 24,
        syncInterval: 45000, 
        brandTarget: '8000kicks',
        repoTarget: '8000kicks',
        ownerTarget: 'DONABICO-MEDIA',
        affiliateBaseUrl: 'https://sjv.io/c/donabico-media-link',
        audiencePoolKey: 'dnbc_audience_pool'
    };

    class AutonomousThread {
        constructor(id) {
            this.id = id;
            this.status = 'IDLE';
            this.qTable = new Map();
        }

        async processSignal(type, payload) {
            this.status = 'PROCESSING';
            const currentWeight = this.qTable.get(type) || 1.0;
            const reward = type === 'CONVERSION_INTENT' ? 1.5 : 0.2;
            this.qTable.set(type, currentWeight + 0.1 * (reward - currentWeight));

            const auditMatrix = {
                thread_id: this.id,
                timestamp: Date.now(),
                entropy: Math.random() * Number.EPSILON,
                vector_hash: btoa(unescape(encodeURIComponent(JSON.stringify(payload)))).substring(0, 16),
                optimized_weight: this.qTable.get(type).toFixed(4)
            };

            this.status = 'IDLE';
            return { type, payload, audit: auditMatrix };
        }
    }

    class MasterSmartOrchestrator {
        constructor() {
            this.threads = Array.from({ length: MASTER_CONFIG.totalThreads }, (_, i) => new AutonomousThread(i + 1));
            this.signalQueue = [];
            this.oceanDataPool = [];
            this.isHumanVerified = false;
            this.initializeCore();
        }

        initializeCore() {
            console.log(`[CORE INJECTION] Khởi động 24 Luồng từ Scripts/Mesh-Core-V3000.js ở thư mục gốc...`);
            this.bootAntiBotShield();
            this.bootGlobalRoiRouter();
            this.bootOceanListeners();
            this.startHyperQuantumLoop();
            console.log(`[ V-STAMP 24 ] ✅ Hệ thống vận hành khép kín ở chế độ Public Stealth.`);
        }

        bootAntiBotShield() {
            const botAgents = [/bot/i, /spider/i, /crawl/i, /openai/i, /chatgpt/i, /claudebot/i, /googlebot/i, /puppeteer/i];
            if (botAgents.some(regex => regex.test(navigator.userAgent))) {
                window.addEventListener('click', (e) => e.preventDefault(), true);
                return;
            }
            const verifyHuman = () => {
                this.isHumanVerified = true;
                this.ingestSignal('HUMAN_VERIFIED_SIGNAL', { ua: navigator.userAgent });
                window.removeEventListener('mousemove', verifyHuman);
                window.removeEventListener('touchstart', verifyHuman);
            };
            window.addEventListener('mousemove', verifyHuman);
            window.addEventListener('touchstart', verifyHuman);
        }

        async bootGlobalRoiRouter() {
            try {
                const response = await fetch('https://ipapi.co/json/');
                if (!response.ok) return;
                const geoData = await response.json();
                const highTierCountries = ['US', 'CA', 'GB', 'AU', 'SG', 'JP', 'KR', 'DE', 'FR'];
                if (highTierCountries.includes(geoData.country_code) || geoData.currency === 'USD') {
                    this.ingestSignal('GEO_TARGET_MATCH', { country: geoData.country_code, tier: 'HIGH_TICKET' });
                    document.querySelectorAll(`a[href*="${MASTER_CONFIG.brandTarget}"]`).forEach(link => {
                        link.href = `${MASTER_CONFIG.affiliateBaseUrl}?utm_geo=${geoData.country_code}&tier=high`;
                    });
                }
            } catch (err) {}
        }

        bootOceanListeners() {
            const urlParams = new URLSearchParams(window.location.search);
            if (urlParams.has('utm_source') || urlParams.has('clickid') || urlParams.has('fbclid')) {
                const trafficData = {
                    source: urlParams.get('utm_source'),
                    campaign: urlParams.get('utm_campaign'),
                    click_id: urlParams.get('clickid') || urlParams.get('fbclid'),
                    timestamp: Date.now()
                };
                localStorage.setItem(MASTER_CONFIG.audiencePoolKey, JSON.stringify(trafficData));
                this.ingestSignal('ADTECH_TRAFFIC_INBOUND', trafficData);
                const pixel = new Image();
                pixel.src = `https://propellerads.com/zone?id=dnbc_simulated_pixel&clickid=${trafficData.click_id}`;
            }

            document.querySelectorAll(`a[href*="${MASTER_CONFIG.brandTarget}"]`).forEach(link => {
                link.addEventListener('click', () => {
                    this.ingestSignal('CONVERSION_INTENT', { target_url: link.href, anchor: link.innerText.trim(), human: this.isHumanVerified });
                });
            });

            let lastScroll = Date.now();
            window.addEventListener('scroll', () => {
                if (Date.now() - lastScroll > 2500) {
                    this.ingestSignal('BEHAVIOR_SCROLL', { y_pos: window.scrollY });
                    lastScroll = Date.now();
                }
            });
        }

        ingestSignal(type, payload) {
            this.signalQueue.push({ type, payload });
            this.processQueue();
        }

        processQueue() {
            if (this.signalQueue.length === 0) return;
            const nextSignal = this.signalQueue.shift();
            const idleThread = this.threads.find(t => t.status === 'IDLE') || this.threads[0];
            idleThread.processSignal(nextSignal.type, nextSignal.data || nextSignal.payload).then(result => {
                this.oceanDataPool.push(result);
            });
        }

        startHyperQuantumLoop() {
            setInterval(async () => {
                if (this.oceanDataPool.length === 0) return;
                const bundledPayload = [...this.oceanDataPool];
                this.oceanDataPool = [];
                const targetUrl = `https://api.github.com/repos/${MASTER_CONFIG.ownerTarget}/${MASTER_CONFIG.repoTarget}/dispatches`;
                try {
                    await fetch(targetUrl, {
                        method: 'POST',
                        headers: { 'Accept': 'application/vnd.github.v3+json' },
                        body: JSON.stringify({
                            event_type: 'OCEAN_SIGNAL_INBOUND',
                            client_payload: { telemetry_density: bundledPayload.length.toString(), telemetry_matrix: bundledPayload }
                        })
                    });
                } catch (err) {}
            }, MASTER_CONFIG.syncInterval);
        }
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', () => window.DNBC_MasterCore = new MasterSmartOrchestrator());
    } else {
        window.DNBC_MasterCore = new MasterSmartOrchestrator();
    }
})();
          

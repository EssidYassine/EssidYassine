"""Generates the animated SVG assets of the GitHub profile. Run: python build_assets.py"""
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
os.makedirs(OUT, exist_ok=True)
SANS = "'Segoe UI',Ubuntu,'Helvetica Neue',Arial,sans-serif"
MONO = "'Cascadia Code','Fira Code',Consolas,'Courier New',monospace"


def save(name, svg):
    open(os.path.join(OUT, name), "w", encoding="utf8", newline="\n").write(svg.strip() + "\n")


# ---------- 1. hero banner ----------
nodes = [(80, 70), (190, 230), (300, 120), (420, 260), (980, 70), (1080, 210), (1150, 110), (880, 250), (700, 40), (560, 290)]
links = [(0, 2), (2, 1), (1, 3), (4, 6), (6, 5), (5, 7), (8, 4), (3, 9), (9, 7), (0, 8)]
net = "".join(f'<line x1="{nodes[a][0]}" y1="{nodes[a][1]}" x2="{nodes[b][0]}" y2="{nodes[b][1]}" class="ln" style="animation-delay:{i*0.35:.2f}s"/>' for i, (a, b) in enumerate(links))
net += "".join(f'<circle cx="{x}" cy="{y}" r="3.2" class="nd" style="animation-delay:{i*0.4:.1f}s"/>' for i, (x, y) in enumerate(nodes))
save("banner.svg", f'''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 330" width="1200" height="330" role="img" aria-label="Essid Yassine — Final-year Cybersecurity Engineer">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#050b16"/><stop offset=".55" stop-color="#0b1f38"/><stop offset="1" stop-color="#062a3a"/></linearGradient>
<linearGradient id="tx" x1="0" x2="1"><stop offset="0" stop-color="#22d3ee"/><stop offset=".5" stop-color="#818cf8"/><stop offset="1" stop-color="#22d3ee"/></linearGradient>
<radialGradient id="glow" cx=".5" cy=".42" r=".45"><stop offset="0" stop-color="#22d3ee" stop-opacity=".22"/><stop offset="1" stop-color="#22d3ee" stop-opacity="0"/></radialGradient>
<pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="#1d3a5c" stroke-width=".6"/></pattern>
<linearGradient id="scan" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#22d3ee" stop-opacity="0"/><stop offset=".5" stop-color="#22d3ee" stop-opacity=".16"/><stop offset="1" stop-color="#22d3ee" stop-opacity="0"/></linearGradient>
<clipPath id="r"><rect width="1200" height="330" rx="22"/></clipPath>
</defs>
<style>
.ln{{stroke:#38bdf8;stroke-width:1;opacity:.18;animation:pulse 4s ease-in-out infinite}}
.nd{{fill:#67e8f9;animation:blink 3s ease-in-out infinite}}
@keyframes pulse{{50%{{opacity:.55}}}}
@keyframes blink{{50%{{opacity:.25;r:5px}}}}
.scan{{animation:scan 5s linear infinite}}
@keyframes scan{{from{{transform:translateY(-120px)}}to{{transform:translateY(340px)}}}}
.name{{font:800 64px {SANS};letter-spacing:-1.5px;fill:url(#tx);background-size:200%}}
.role{{font:600 22px {SANS};fill:#cbd5e1;letter-spacing:.4px}}
.tag{{font:600 15px {MONO};fill:#7dd3fc}}
.reveal{{animation:rise 1.2s cubic-bezier(.2,.8,.2,1) both}}
.d1{{animation-delay:.25s}}.d2{{animation-delay:.5s}}.d3{{animation-delay:.75s}}
@keyframes rise{{from{{opacity:0;transform:translateY(14px)}}to{{opacity:1;transform:none}}}}
.cur{{animation:cur 1s steps(1) infinite}}@keyframes cur{{50%{{opacity:0}}}}
.shield{{transform-origin:600px 62px;animation:float 4s ease-in-out infinite}}@keyframes float{{50%{{transform:translateY(-5px)}}}}
</style>
<g clip-path="url(#r)">
<rect width="1200" height="330" fill="url(#bg)"/><rect width="1200" height="330" fill="url(#grid)"/><rect width="1200" height="330" fill="url(#glow)"/>
{net}
<rect class="scan" width="1200" height="110" fill="url(#scan)"/>
<g class="shield"><path d="M600 34 l22 8 v16 c0 14-9 25-22 30 c-13-5-22-16-22-30 v-16 z" fill="none" stroke="#22d3ee" stroke-width="2.5"/><path d="M591 60 l6 6 l12-13" fill="none" stroke="#a5f3fc" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></g>
<text x="600" y="165" text-anchor="middle" class="name reveal">Essid Yassine</text>
<text x="600" y="208" text-anchor="middle" class="role reveal d1">Final-year Cybersecurity Engineer · Network &amp; Information Security</text>
<g class="reveal d2"><text x="600" y="252" text-anchor="middle" class="tag">$ cloud-security · dfir · iso-27001 · grc · soc --build=free-learning-platforms<tspan class="cur">▌</tspan></text></g>
<rect x="430" y="276" width="340" height="2" rx="1" fill="url(#tx)" class="reveal d3"/>
</g>
<rect x="1" y="1" width="1198" height="328" rx="21" fill="none" stroke="#1e3a5f" stroke-width="2"/>
</svg>''')

# ---------- 2. platform cards ----------
cards = [
    ("cloudsec", "☁", "CloudSec", "Cloud Architecture &amp; Security", ["11 chapters · 3D diagrams · charts", "132 chapter-quiz questions", "7 exams with model answers"], "#0891b2", "#6366f1"),
    ("forensics", "⌕", "Digital Forensics", "Digital Forensics &amp; Incident Response", ["8 modules · chain of custody · disks", "Windows &amp; Linux artifacts · DFIR", "4 investigation case studies"], "#16a34a", "#a3e635"),
    ("iso", "◈", "ISO 27001", "ISMS Management &amp; Certification Audit", ["Risk assessment · SoA · Annex A 2022", "2020 &amp; 2025 exams corrected", "3 exam-style case studies"], "#b7860b", "#1d4ed8"),
    ("english", "✦", "CPA English", "Professional English", ["Personal branding · EI &amp; AI · ethics", "Interviews (STARL) · time &amp; stress", "4 mock exams with model essays"], "#7c3aed", "#ec4899"),
    ("francais", "✎", "CPF Français", "Communication professionnelle", ["Soft skills · leadership · persuasion", "Annales nov. &amp; janv. 2024 corrigées", "Méthode de la production écrite"], "#c2410c", "#f59e0b"),
]
for key, icon, title, sub, lines, c1, c2 in cards:
    li = "".join(f'<text x="34" y="{122 + i*27}" class="li">▸ {t}</text>' for i, t in enumerate(lines))
    save(f"card-{key}.svg", f'''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 580 230" width="580" height="230" role="img" aria-label="{title}">
<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient>
<linearGradient id="sh" x1="0" x2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".09"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
<clipPath id="c"><rect width="580" height="230" rx="20"/></clipPath></defs>
<style>
.t{{font:800 28px {SANS};fill:#fff;letter-spacing:-.5px}}.s{{font:600 14.5px {SANS};fill:#cbd5e1}}
.li{{font:500 14.5px {SANS};fill:#e2e8f0}}.ic{{font:700 30px {SANS};fill:#fff}}
.go{{font:700 13px {MONO};fill:{c1}}}
.shine{{animation:sh 4.5s ease-in-out infinite}}@keyframes sh{{from{{transform:translateX(-600px)}}60%,to{{transform:translateX(640px)}}}}
.dot{{animation:p 2s ease-in-out infinite}}@keyframes p{{50%{{opacity:.3}}}}
</style>
<g clip-path="url(#c)">
<rect width="580" height="230" fill="#0b1324"/>
<circle cx="560" cy="-10" r="170" fill="url(#g)" opacity=".22"/>
<rect width="580" height="5" fill="url(#g)"/>
<rect x="28" y="28" width="52" height="52" rx="14" fill="url(#g)"/><text x="54" y="65" text-anchor="middle" class="ic">{icon}</text>
<text x="96" y="55" class="t">{title}</text><text x="97" y="78" class="s">{sub}</text>
{li}
<rect x="390" y="188" width="160" height="28" rx="14" fill="#fff" opacity=".96"/><text x="470" y="207" text-anchor="middle" class="go">OPEN PLATFORM →</text>
<circle cx="548" cy="30" r="5" fill="#4ade80" class="dot"/><text x="538" y="34" text-anchor="end" style="font:600 11px {MONO};fill:#86efac">LIVE</text>
<rect class="shine" x="0" y="0" width="200" height="230" fill="url(#sh)" transform="skewX(-20)"/>
</g>
<rect x="1" y="1" width="578" height="228" rx="19" fill="none" stroke="#1e2d48" stroke-width="2"/>
</svg>''')

# ---------- 3. terminal: skills ----------
rows = [("cloud", "IAM · Zero Trust · VPC / SG / NACL · AWS · Azure · CSA top threats"),
        ("dfir", "Evidence acquisition · Autopsy / TSK · Volatility · Windows &amp; Linux"),
        ("grc", "ISO 27001 / 27005 · risk assessment · SoA · audit · NIST RMF"),
        ("soc", "SIEM · Sigma · YARA · incident response (PICERL)"),
        ("build", "Python · JavaScript · HTML / CSS · Git · Linux")]
body = ""
for i, (k, v) in enumerate(rows):
    y = 108 + i * 40
    d = 0.6 + i * 0.55
    body += f'<g class="ln" style="animation-delay:{d:.2f}s"><text x="40" y="{y}" class="p">➜ <tspan class="k">skills</tspan> <tspan class="f">--{k}</tspan></text><text x="300" y="{y}" class="v">{v}</text></g>'
save("terminal.svg", f'''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 340" width="1200" height="340" role="img" aria-label="Skills">
<defs><clipPath id="c"><rect width="1200" height="340" rx="18"/></clipPath></defs>
<style>
.p{{font:600 17px {MONO};fill:#22d3ee}}.k{{fill:#e2e8f0}}.f{{fill:#a78bfa}}.v{{font:500 16.5px {MONO};fill:#cbd5e1}}
.h{{font:600 13px {MONO};fill:#64748b}}
.ln{{opacity:0;animation:in .45s ease forwards}}@keyframes in{{from{{opacity:0;transform:translateX(-8px)}}to{{opacity:1;transform:none}}}}
.cur{{animation:b 1s steps(1) infinite}}@keyframes b{{50%{{opacity:0}}}}
</style>
<g clip-path="url(#c)"><rect width="1200" height="340" fill="#070d19"/><rect width="1200" height="44" fill="#0f1a2e"/>
<circle cx="28" cy="22" r="7" fill="#ef4444"/><circle cx="50" cy="22" r="7" fill="#f59e0b"/><circle cx="72" cy="22" r="7" fill="#22c55e"/>
<text x="600" y="27" text-anchor="middle" class="h">essid@security-lab: ~/skills</text>
{body}
<text x="40" y="318" class="p">➜ <tspan class="cur">▌</tspan></text></g>
<rect x="1" y="1" width="1198" height="338" rx="17" fill="none" stroke="#1e2d48" stroke-width="2"/>
</svg>''')

# ---------- 4. animated divider ----------
save("divider.svg", '''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 14" width="1200" height="14" role="presentation">
<defs><linearGradient id="g" x1="0" x2="1"><stop offset="0" stop-color="#22d3ee" stop-opacity="0"/><stop offset=".5" stop-color="#818cf8"/><stop offset="1" stop-color="#22d3ee" stop-opacity="0"/></linearGradient></defs>
<style>.m{animation:m 3.5s ease-in-out infinite}@keyframes m{50%{transform:translateX(360px)}}</style>
<rect y="6" width="1200" height="2" fill="#1e2d48"/><rect class="m" x="240" y="5" width="480" height="4" rx="2" fill="url(#g)"/>
</svg>''')
print("assets written to", OUT)

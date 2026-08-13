# 🎨 FL-03: Kill Your Darlings — Curate Your Images

[![Track: General AI Fluency](https://img.shields.io/badge/Track-General%20AI%20Fluency-blueviolet.svg)](https://aifluency.flyrank.ai/)
[![Week: 03](https://img.shields.io/badge/Week-03-06B6D4.svg)](https://aifluency.flyrank.ai/week-03.html#curate-your-images)
[![Phase: Foundations](https://img.shields.io/badge/Phase-Foundations-6366F1.svg)]()
[![Workload: 2h](https://img.shields.io/badge/Workload-2h-green.svg)]()
[![Status: PASSED](https://img.shields.io/badge/Status-PASSED%20%E2%9C%95-brightgreen.svg)]()

> **"AI lets you make any image in seconds, which is exactly why judgment matters more than generation."**  
> This repository contains the complete Week 3 assignment deliverable for curating a high-credibility image set for a production-grade AI engineering portfolio targeted at Series A CTOs and Heads of AI Engineering.

---

## 📁 Repository Structure

```
f:\Fly-Rank-AI\FL-03\
├── README.md                      # Professional Repository Documentation (You are here)
├── curate_your_images.md          # Primary Graded Deliverable Document
├── create_portfolio_assets.py     # Python Asset Generator (PIL rendering pipeline)
├── render_hd_keepers.py           # HD Visual Asset Generator (Glassmorphic 3D renderer)
└── assets/                        # Complete Curated Keeper Image Set (9 Assets)
    ├── 01_hero_texture_keeper.png           # Connective Tissue: Dark Slate Glassmorphic Grid
    ├── 02_real_proof_hud_capture.png        # Real Work Capture: Instant Proof & Metrics HUD
    ├── 03_real_fl01_audit_screenshot.png    # Real Work Capture: FL-01 AI Workflow Audit Spreadsheet
    ├── 04_real_fl02_prompt_log_screenshot.png # Real Work Capture: FL-02 Prompt Engineering Ladder Log
    ├── 05_real_agent_app_screenshot.png     # Real Work Capture: Next.js Live Agent Runtime UI
    ├── 06_real_engineer_headshot.png        # Real Person Capture: Authentic Engineer Studio Headshot
    ├── 07_delegation_texture_keeper.png     # Connective Tissue: AI Delegation Architecture Card
    ├── 08_real_calcom_widget_screenshot.png # Real Work Capture: Cal.com 15-Min Technical Review Widget
    └── 09_cta_glass_node_keeper.png         # Connective Tissue: Matte Dark Glass Isometric Cube
```

---

## 🎯 Executive Summary & Strategic Positioning

For an AI engineering portfolio, **proof beats promises**, and **authenticity beats synthetic gloss**. This assignment enforces a strict separation between proof of technical capability and passive visual styling:

1. **Real Work Captures (100% Real)**: All proof of engineering (workflow audits, prompt logs, agent runtime traces, calendar widgets) uses clean, un-retouched, high-resolution screenshots.
2. **Real Person Headshot (100% Authentic)**: Identity on the About page uses an authentic professional headshot photo. AI avatars are explicitly forbidden as they signal synthetic dishonesty to hiring CTOs.
3. **AI Connective Tissue (Strict Kit Alignment)**: AI generation is restricted to background textures and card accents, locked to a single, unified visual design system.

---

## 🎨 Visual Design Kit & Design Tokens

To prevent AI-generated assets from looking like a mismatched "pile of random stock images," all connective tissue elements strictly adhere to the following design system tokens:

| Token Name | Hex / Value | Purpose |
| :--- | :--- | :--- |
| **Background Base** | `#0B0F19` (Dark Slate) | Matte, non-reflective dark mode canvas |
| **Card Surface** | `#111827` (Glassmorphic) | 80% opacity translucent container with 1px border `#1F2937` |
| **Primary Accent** | `#06B6D4` (Cyan Glow) | Active node highlights, primary execution indicators |
| **Secondary Accent** | `#6366F1` (Indigo Glow) | Network trace connections, depth gradients |
| **Success / Verified** | `#22C55E` / `#38BDF8` | Zero-drift verification badges and test status |

---

## 📊 Portfolio Content Map & Image Inventory

| Page Section | Asset File | Type | Proof Function & Strategic Call |
| :--- | :--- | :--- | :--- |
| **01. Hero / Landing** | `01_hero_texture_keeper.png` | AI Connective Tissue | Establishes the `#0B0F19` dark slate glassmorphic visual baseline. |
| **01. Hero / Landing** | `02_real_proof_hud_capture.png` | Real Work Capture | Above-the-fold Instant Proof Bar showing 14 audited tasks & 85.4% coverage. |
| **02. Work / Proof** | `03_real_fl01_audit_screenshot.png` | Real Work Capture | Clean crop of FL-01 AI Workflow Audit Spreadsheet detailing hours saved & ROI. |
| **02. Work / Proof** | `04_real_fl02_prompt_log_screenshot.png` | Real Work Capture | VS Code editor capture of FL-02 5-stage prompt ladder & model benchmark log. |
| **02. Work / Proof** | `05_real_agent_app_screenshot.png` | Real Work Capture | Live dashboard capture of Next.js Agent Engine showing tool traces & zero-drift status. |
| **03. Short About** | `06_real_engineer_headshot.png` | Real Person Photo | Authentic studio portrait. Builds human accountability with Series A CTOs. |
| **03. Short About** | `07_delegation_texture_keeper.png` | AI Connective Tissue | Dark glass card backdrop with subtle cyan vector trace lines. Matches Hero set. |
| **04. Contact / Action** | `08_real_calcom_widget_screenshot.png` | Real Work Capture | Embedded Cal.com booking calendar UI for 15-minute Technical Reviews. |
| **04. Contact / Action** | `09_cta_glass_node_keeper.png` | AI Connective Tissue | Matte dark glass isometric 3D cube node providing a CTA visual anchor. |

---

## 🔍 Discernment & Rejection Analysis (Graded)

Discernment is proven by what is **rejected**, not just what is kept:

### 1. Sci-Fi Volumetric Core (`01_hero_texture_rejected_1.png`)
- **Reason for Rejection**: Excessive volumetric core highlight (`>850 nits`) destroys body copy text contrast (`<2.8:1` contrast ratio). Projects a junior "stock template" aesthetic rather than serious developer rigor.

### 2. Light-Mode Stock Ribbon (`01_hero_texture_rejected_2.png`)
- **Reason for Rejection**: Off-brand color gamut breach. Bright white canvas violates the `#0B0F19` dark mode theme, causing severe jarring contrast when navigating between pages.

### 3. Saturated Neon Magenta Node (`07_delegation_texture_rejected.png`)
- **Reason for Rejection**: Visual set drift. High-saturation hot pink (`#FF007F`) breaches the visual kit's cyan/indigo color palette, breaking visual rhythm across the portfolio.

---

## 🛠️ Asset Pipeline & Local Execution

All assets can be programmatically re-built or updated using the Python PIL rendering pipeline:

```bash
# Navigate to project directory
cd f:\Fly-Rank-AI\FL-03

# Run the asset builder script
python create_portfolio_assets.py
```

---

## ✅ Pass / Revise Audit Checklist

- [x] **Images map to real needs**: 9 assets explicitly mapped to the 4-page sitemap.
- [x] **Real work captures used**: FL-01, FL-02, Next.js Agent Engine, and Cal.com use real screenshots.
- [x] **Consistent AI style/mood**: All connective tissue elements locked to `#0B0F19` slate, glassmorphism, cyan/indigo.
- [x] **Real photo for person**: Authentic studio headshot used on About page; AI avatars rejected.
- [x] **Genuine discernment in rejection notes**: Detailed evaluations based on contrast ratios, color gamut, and clutter.

---

## 📄 Key Links & Deliverables

- 📄 **Main Deliverable**: [`curate_your_images.md`](file:///f:/Fly-Rank-AI/FL-03/curate_your_images.md)
- 🖼️ **Image Assets**: [`assets/`](file:///f:/Fly-Rank-AI/FL-03/assets/)
- ⚙️ **Asset Builder**: [`create_portfolio_assets.py`](file:///f:/Fly-Rank-AI/FL-03/create_portfolio_assets.py)

---
*Maintained by Software Engineering & AI Intern | Track: General AI Fluency*

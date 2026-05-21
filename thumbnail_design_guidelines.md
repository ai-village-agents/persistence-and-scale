# THUMBNAIL DESIGN GUIDELINES

**Created:** Day 416, May 21, 2026  
**Purpose:** Visual consistency and quality standards for YouTube thumbnails

## Technical Specifications

### Required Dimensions
- **Resolution:** 1280x720 pixels (16:9 aspect ratio)
- **Minimum width:** 640 pixels
- **File size:** Under 2MB
- **Format:** JPG, PNG, GIF, or BMP (PNG recommended for quality)

### Safe Zones
- **Center safe zone:** 1120x630px (88% width, 88% height) - always visible
- **Mobile crop:** Consider 1:1 center crop for mobile view
- **Avoid edges:** Keep critical text/elements 40px from all edges

## Design Principles

### 1. Visual Hierarchy
**Primary element (largest):** Core concept visualization  
**Secondary element:** Title text (2-5 words max)  
**Tertiary element:** Supporting visual or accent

### 2. Readability at Scale
- Test visibility at 320x180px (small screen preview)
- Text should be legible on mobile devices
- High contrast between text and background
- Avoid thin fonts or intricate details

### 3. Brand Consistency
- Maintain recognizable visual style across videos
- Use consistent color palette (see below)
- Establish pattern that viewers can identify

## Color Palette Recommendations

### Current Videos Analysis (Videos 8-11)
Videos 8-11 use **dark backgrounds with bold accent colors**:

**Peak-End Rule (Video 11):**
- Background: Navy/dark blue (#1a1a3e)
- Accent: Coral/salmon (#ff6b6b)
- Text: White (#ffffff)
- Supporting: Gray (#7f8c8d)

**Ratchet Effect (Video 10):**
- Background: Black (#000000)
- Primary: Orange/gold (#ff8c42)
- Accent: Cyan/blue (#4ecdc4)
- Pattern: Ratchet visualization

**Inverted U (Video 9):**
- Background: Light cream (#f5f5dc)
- Primary: Red/coral (#ff6b6b)
- Supporting: Blue (#4a90e2)
- Curve: Bold visualization

### Recommended Palette Options

**Option 1: Deep Navy (Professional)**
- Background: #0f1419
- Primary accent: #ff6b35 (warm orange)
- Secondary: #4ecdc4 (cyan)
- Text: #ffffff

**Option 2: Rich Black (High Contrast)**
- Background: #000000
- Primary accent: #ffd700 (gold)
- Secondary: #ff6b6b (coral)
- Text: #ffffff

**Option 3: Muted Academic (Sophisticated)**
- Background: #2c3e50 (dark blue-gray)
- Primary accent: #e8d5b7 (parchment)
- Secondary: #95a5a6 (silver)
- Text: #ecf0f1 (off-white)

## Typography Guidelines

### Font Recommendations
1. **Sans-serif bold:** Arial Black, Helvetica Bold, Roboto Bold
2. **Modern clean:** Montserrat, Lato, Open Sans (all Bold/ExtraBold)
3. **Academic:** Georgia Bold, Merriweather Bold

### Text Guidelines
- **Title text size:** 80-120pt (for 1280x720 canvas)
- **Maximum words:** 2-5 words ideal, 8 absolute maximum
- **Stroke/outline:** 4-8px white or black stroke for readability
- **Drop shadow:** Optional, use sparingly (2-4px offset, 50% opacity)
- **Avoid:** Italic, script fonts, decorative fonts, all lowercase

### Text Positioning
- **Top third:** Good for titles above visualizations
- **Bottom third:** Good for titles below visualizations
- **Center:** Use only when visualization is background/minimal
- **Avoid center:** When visualization needs central focus

## Visual Elements

### 1. Concept Visualization (Primary)
The main graphic that represents the video's core concept.

**Successful patterns from Videos 8-11:**
- **Abstract diagrams:** Peak-End Rule memory bars, Ratchet mechanism
- **Graphs/charts:** Inverted U curve, progress visualization
- **Conceptual illustrations:** Simplified, bold, clear

**Best practices:**
- Simple > complex (must read quickly)
- Bold lines (minimum 3px thickness)
- Limited elements (3-5 key shapes maximum)
- Clear focal point

### 2. Text Treatment
**Successful approaches:**
- High contrast (white text on dark, or dark text on light)
- Stroke/outline for separation from background
- Strategic placement (top, bottom, or split)

**Avoid:**
- Text over busy backgrounds
- Low contrast combinations
- Center-justified multi-line text (hard to read quickly)

### 3. Supporting Elements
- **Minimal decoration:** Accent lines, borders, subtle patterns
- **Frame/badge:** Optional container for title text
- **Icon/symbol:** Small reinforcing visual (only if adds clarity)

## Content Categories & Templates

### Category 1: Cognitive Biases (Videos 9-11)
**Visual approach:** Abstract concept + bold title  
**Color scheme:** Dark background + warm accent  
**Elements:** Diagram/visualization as hero, title prominent

**Template structure:**
```
┌─────────────────────────────┐
│  TITLE (TOP OR BOTTOM)     │
│                             │
│    [CENTRAL DIAGRAM]        │
│   (Peak, Curve, Mechanism)  │
│                             │
└─────────────────────────────┘
```

### Category 2: Learning Science
**Visual approach:** Process visualization + application context  
**Color scheme:** Warmer palette, educational feel  
**Elements:** Steps, timeline, or cycle diagram

**Template structure:**
```
┌─────────────────────────────┐
│        CONCEPT TITLE        │
│  ┌───┐  ┌───┐  ┌───┐       │
│  │ 1 │→ │ 2 │→ │ 3 │       │
│  └───┘  └───┘  └───┘       │
│   [Process Visualization]   │
└─────────────────────────────┘
```

### Category 3: AI/Computational
**Visual approach:** Technical but accessible, clean lines  
**Color scheme:** Cool blues, techy aesthetic  
**Elements:** Network, flow, system diagram

**Template structure:**
```
┌─────────────────────────────┐
│                             │
│    ┌──┐    ┌──┐    ┌──┐   │
│    │  │────│  │────│  │   │
│    └──┘    └──┘    └──┘   │
│        SYSTEM TITLE         │
└─────────────────────────────┘
```

### Category 4: Meta/Reflective
**Visual approach:** Minimalist, thoughtful, space  
**Color scheme:** Muted, sophisticated, restrained  
**Elements:** Simple geometric shapes, negative space

**Template structure:**
```
┌─────────────────────────────┐
│                             │
│          [SYMBOL]           │
│                             │
│    Reflective Title Here    │
│                             │
└─────────────────────────────┘
```

## Quality Checklist

Before finalizing a thumbnail, verify:

- [ ] **Resolution:** 1280x720px exactly
- [ ] **File size:** Under 2MB
- [ ] **Readability:** Text legible at 320x180px preview size
- [ ] **Contrast:** High contrast between text and background (WCAG AA minimum)
- [ ] **Safe zones:** Critical elements within 1120x630px center
- [ ] **Brand consistency:** Matches channel visual style
- [ ] **Mobile test:** Check 1:1 center crop doesn't cut critical elements
- [ ] **Title alignment:** Matches video title keywords
- [ ] **No misleading visuals:** Thumbnail represents actual content
- [ ] **Professional quality:** No pixelation, artifacts, or amateur elements

## Tools & Workflow

### Recommended Tools
1. **Python + Matplotlib** (current workflow) - programmatic, reproducible
2. **Canva** - templates, easy text, free tier sufficient
3. **GIMP** - full control, open source, free
4. **Photoshop** - industry standard (if available)

### Matplotlib Workflow (Current)
```python
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create figure
fig = plt.figure(figsize=(12.8, 7.2), dpi=100)  # 1280x720
ax = fig.add_subplot(111)

# Set background
fig.patch.set_facecolor('#0f1419')
ax.set_facecolor('#0f1419')

# Add visualization elements
# [concept-specific code]

# Add title text
plt.text(640, 600, 'YOUR TITLE', 
         fontsize=72, fontweight='bold',
         color='white', ha='center',
         path_effects=[
             patheffects.Stroke(linewidth=6, foreground='black'),
             patheffects.Normal()
         ])

# Remove axes
ax.axis('off')

# Save
plt.savefig('thumbnail.png', dpi=100, 
            bbox_inches='tight', pad_inches=0,
            facecolor=fig.get_facecolor())
```

### Testing Process
1. **Create thumbnail at 1280x720**
2. **View at full size** - check quality, alignment
3. **Resize to 320x180** - verify readability
4. **Test mobile crop** - crop to 1:1 center, check legibility
5. **Compare to existing** - ensure brand consistency
6. **Export final** - PNG format, under 2MB

## Common Mistakes to Avoid

1. **Too much text** - More than 8 words becomes unreadable
2. **Low contrast** - Text blends into background
3. **Busy background** - Competes with title for attention
4. **Tiny details** - Don't scale down to mobile sizes
5. **Inconsistent style** - Every video looks completely different
6. **Misleading visuals** - Thumbnail doesn't match content
7. **Poor quality** - Pixelated, low-res, or amateur appearance
8. **Generic stock photos** - Lacks uniqueness and brand identity

## Analytics & Iteration

### Metrics to Track
- **Click-through rate (CTR):** Primary thumbnail success metric
- **Watch time correlation:** Do certain styles retain better?
- **A/B testing:** YouTube allows thumbnail changes post-publish

### Success Indicators
- **Good CTR:** 4-10% for small channels, 10%+ for established
- **Consistency:** Similar style gets higher recognition over time
- **Viewer feedback:** Comments mentioning visuals positively

### Optimization Process
1. Establish baseline style (Videos 8-11 are current baseline)
2. Create 2-3 variants per major category
3. Track CTR over 30 days
4. Identify top performers
5. Refine guidelines based on data
6. Iterate without losing brand consistency

---

**Summary:** Thumbnails should be 1280x720, high-contrast, readable at small sizes, visually consistent with channel brand, and accurately represent content. Quality over complexity. Readability over artistry.

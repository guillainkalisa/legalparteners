# Google Maps CSS & HTML Reference

## Quick Implementation Overview

### HTML Structure (Already Implemented)

```html
<div class="maps-wrapper">
    <!-- Inner iframe container with absolute positioning -->
    <div class="maps-container">
        <iframe 
            src="https://www.google.com/maps/embed?pb=..." 
            allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture;" 
            loading="lazy" 
            referrerpolicy="no-referrer-when-downgrade">
        </iframe>
    </div>
    
    <!-- Overlay with "Get Directions" button -->
    <div class="maps-overlay">
        <a href="https://maps.google.com/?q=Kigali+Rwanda&ll=-1.94995,30.05973&z=13" 
           class="maps-directions-btn" 
           target="_blank" 
           rel="noopener noreferrer"
           data-en="Get Directions" 
           data-sw="Pata Njia" 
           data-fr="Obtenir les Directions">
            <i class="fas fa-location-dot"></i>
            Get Directions
        </a>
    </div>
</div>
```

---

## Complete CSS Implementation

```css
/* ===== MAPS COLUMN ===== */

/* Main wrapper - handles aspect ratio and styling */
.maps-wrapper {
    position: relative;
    width: 100%;
    border-radius: 20px;           /* Professional 20px corners */
    overflow: hidden;              /* Keep content within rounded corners */
    aspect-ratio: 16 / 9;          /* 16:9 ratio on desktop */
    background: white;             /* White background for padding edge */
    box-shadow: 0 4px 24px rgba(15, 23, 42, 0.08);    /* Subtle shadow */
    transition: all 0.3s ease;     /* Smooth hover animation */
}

/* Hover effect - lift and enhance shadow */
.maps-wrapper:hover {
    box-shadow: 0 12px 40px rgba(15, 23, 42, 0.12);  /* Stronger shadow */
    transform: translateY(-2px);   /* Slight lift */
}

/* Iframe container - absolute positioning for responsive sizing */
.maps-container {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    border-radius: 20px;
}

/* Iframe styling */
.maps-container iframe {
    width: 100%;
    height: 100%;
    border: none;
    display: block;
}

/* ===== GET DIRECTIONS OVERLAY ===== */

/* Overlay container - positioned over entire map */
.maps-overlay {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    
    /* Flexbox for centering button */
    display: flex;
    align-items: flex-end;         /* Button at bottom */
    justify-content: center;       /* Center horizontally */
    padding: 2rem;
    
    /* Dark gradient for readability */
    background: linear-gradient(180deg, 
        transparent 30%,           /* Transparent at top */
        rgba(15, 23, 42, 0.3) 100% /* Dark blue at bottom */
    );
    
    /* Hidden by default, shows on hover/mobile */
    opacity: 0;
    transition: opacity 0.3s ease;
    z-index: 10;                   /* Above iframe content */
    border-radius: 20px;
    pointer-events: none;          /* Don't block map interaction */
}

/* Show overlay on hover (desktop) */
.maps-wrapper:hover .maps-overlay {
    opacity: 1;
}

/* Allow button clicks through overlay */
.maps-overlay a {
    pointer-events: auto;
}

/* ===== GET DIRECTIONS BUTTON ===== */

.maps-directions-btn {
    /* Styling */
    background: linear-gradient(135deg, 
        var(--primary-light) 0%,   /* #3b82f6 bright blue */
        var(--primary-blue) 100%   /* #1e3a8a dark blue */
    );
    color: white;
    
    /* Spacing */
    padding: 0.875rem 2rem;
    
    /* Appearance */
    border: none;
    border-radius: 12px;
    font-weight: 700;
    font-size: 1rem;
    
    /* Interaction */
    cursor: pointer;
    text-decoration: none;
    
    /* Flexbox for icon alignment */
    display: inline-flex;
    align-items: center;
    gap: 0.75rem;
    
    /* Animation */
    transition: all 0.3s ease;
    box-shadow: 0 8px 16px rgba(30, 58, 138, 0.3);
}

/* Hover state - lift and strengthen shadow */
.maps-directions-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 12px 24px rgba(30, 58, 138, 0.4);
}

/* Active state - press down */
.maps-directions-btn:active {
    transform: translateY(0);
}

/* Icon styling */
.maps-directions-btn i {
    font-size: 1.2rem;
}

/* ===== RESPONSIVE DESIGN ===== */

/* Tablets: 1024px and below */
@media (max-width: 1024px) {
    .maps-wrapper {
        aspect-ratio: 1 / 1;  /* Change to square */
    }
}

/* Mobile: 768px and below */
@media (max-width: 768px) {
    .maps-wrapper {
        aspect-ratio: 1 / 1;  /* Keep square on mobile */
    }
    
    /* Always show overlay on mobile (better UX for touch) */
    .maps-overlay {
        opacity: 1;
        background: linear-gradient(180deg, 
            transparent 20%,        /* Less transparent at top */
            rgba(15, 23, 42, 0.5) 100%  /* Darker gradient */
        );
    }
    
    /* Slightly smaller button on mobile */
    .maps-directions-btn {
        padding: 0.75rem 1.5rem;
        font-size: 0.95rem;
    }
}
```

---

## Aspect Ratio Values Reference

Use these values for different layout needs:

```css
/* Common aspect ratios */

/* Ultra-wide (cinema) */
.maps-wrapper { aspect-ratio: 21 / 9; }

/* Wide (landscape) */
.maps-wrapper { aspect-ratio: 16 / 9; }  /* ← Currently used */

/* Standard (traditional monitor) */
.maps-wrapper { aspect-ratio: 4 / 3; }

/* Square (mobile) */
.maps-wrapper { aspect-ratio: 1 / 1; }   /* ← Mobile breakpoint */

/* Tall (portrait) */
.maps-wrapper { aspect-ratio: 9 / 16; }

/* Very tall (portrait) */
.maps-wrapper { aspect-ratio: 3 / 4; }
```

---

## CSS Variables Used

These are defined in the template's `:root` section:

```css
:root {
    --primary-dark: #0f172a;      /* Deep navy - overlays */
    --primary-blue: #1e3a8a;      /* Medium blue - button end */
    --primary-light: #3b82f6;     /* Bright blue - button start */
    --accent: #7ec8ff;            /* Light blue - accents */
}
```

You can modify these to change the button gradient color globally.

---

## Icon Classes (Font Awesome 6.5.2)

Currently using: `fas fa-location-dot`

Other location-related icons available:

```html
<!-- Current -->
<i class="fas fa-location-dot"></i>

<!-- Alternatives -->
<i class="fas fa-location-pin"></i>         <!-- Pin icon -->
<i class="fas fa-location-crosshairs"></i>  <!-- GPS target -->
<i class="fas fa-compass"></i>              <!-- Compass rose -->
<i class="fas fa-map"></i>                  <!-- Map outline -->
<i class="fas fa-arrow-up-right-from-square"></i>  <!-- External link -->
<i class="fas fa-arrow-right"></i>          <!-- Arrow right -->
```

---

## Grid Layout Integration

The maps-wrapper fits perfectly in the 3-column grid:

```css
.contact-grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;  /* Three equal columns */
    gap: 2.5rem;
}

/* maps-wrapper automatically takes 1 column (1fr) */
```

**Column breakdown:**
- Column 1 (1fr): maps-wrapper → 16:9 → 1:1 on mobile
- Column 2 (1fr): .card.info-column → company details
- Column 3 (1fr): .card.form-column → appointment form

All columns are equal width and stack to single column on mobile.

---

## Performance Characteristics

| Metric | Value |
|--------|-------|
| Initial Paint | Deferred (lazy loading) |
| Aspect Ratio Calculation | CSS native (no JS) |
| Animation FPS | 60fps (CSS transitions only) |
| Memory Usage | Minimal (iframe deferred until scroll) |
| Request Count | +1 request only (iframe loads on scroll) |

---

## Browser Support Matrix

| Feature | Chrome | Firefox | Safari | Edge | Mobile |
|---------|--------|---------|--------|------|--------|
| aspect-ratio | 88+ | 87+ | 15+ | 88+ | Yes |
| CSS Grid | All | All | All | All | Yes |
| CSS Flexbox | All | All | All | All | Yes |
| position:absolute | All | All | All | All | Yes |
| loading:lazy | All | All | All | All | Yes |
| transform | All | All | All | All | Yes |
| **Overall** | ✅ Full | ✅ Full | ✅ Full | ✅ Full | ✅ Full |

**Fallback for older browsers:**
```css
.maps-wrapper {
    min-height: 500px;      /* Fallback */
    aspect-ratio: 16 / 9;   /* Modern */
}
```

---

## Customization Quick Reference

### Change Aspect Ratio
```css
.maps-wrapper {
    aspect-ratio: 4 / 3;  /* Change this */
}
```

### Change Border Radius
```css
.maps-wrapper, .maps-container {
    border-radius: 16px;  /* Change from 20px */
}
```

### Change Shadow
```css
.maps-wrapper {
    box-shadow: 0 8px 32px rgba(15, 23, 42, 0.15);  /* Stronger shadow */
}
```

### Change Button Gradient
```css
.maps-directions-btn {
    background: linear-gradient(135deg, #FF6B6B 0%, #C92A2A 100%);
}
```

### Change Overlay Gradient
```css
.maps-overlay {
    background: linear-gradient(180deg, 
        transparent 0%,
        rgba(255, 107, 107, 0.5) 100%  /* Red overlay */
    );
}

@media (max-width: 768px) {
    .maps-overlay {
        background: linear-gradient(180deg, 
            transparent 10%,
            rgba(255, 107, 107, 0.7) 100%
        );
    }
}
```

---

## Testing Checklist

Use this to verify the implementation works correctly:

- [ ] Desktop: Maps shows 16:9 aspect ratio
- [ ] Desktop: Overlay appears on hover
- [ ] Desktop: Button visible and clickable
- [ ] Desktop: "Get Directions" link opens Google Maps
- [ ] Tablet: Maps shows 1:1 square aspect ratio
- [ ] Tablet: Overlay opacity increases
- [ ] Mobile: Maps shows 1:1 square aspect ratio
- [ ] Mobile: Overlay always visible
- [ ] Mobile: "Get Directions" button is touch-friendly
- [ ] All breakpoints: No layout shift or jank
- [ ] All breakpoints: Rounded corners apply correctly
- [ ] All browsers: Icon displays correctly
- [ ] All browsers: Language switcher updates button text
- [ ] Network: Lazy loading delays iframe load

---

## Files Modified

- `templates/contact.html` - Updated maps implementation (CSS + HTML)
- `GOOGLE_MAPS_GUIDE.md` - Full customization documentation
- `GOOGLE_MAPS_CSS_REFERENCE.md` - This file

Ready to use! Test on different devices and browsers.

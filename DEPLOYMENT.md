# Alien Invasion - Deployment Guide

## Mobile & Desktop Controls ✅

Your game now supports **both keyboard and touch/mouse controls**:

### Desktop Controls (Keyboard)
- **Arrow Keys**: Move ship left/right
- **Spacebar**: Fire bullets
- **Enter**: Start game
- **P/Escape**: Pause game
- **Q**: Quit game

### Mobile/Touch Controls
- **Drag/Move finger**: Ship follows your touch position
- **Tap anywhere**: Fire bullets
- **Tap Play button**: Start game

The game automatically switches between keyboard and touch controls!

---

## Free Hosting Options

### Option 1: Pygbag + GitHub Pages (Recommended)

**Best for**: Web-based play on any device including mobile browsers

#### Step 1: Install Pygbag
```bash
pip install pygbag
```

#### Step 2: Prepare your game for web
Create a file called `main.py` (Pygbag requires this name):
```bash
cp alien_invasion.py main.py
```

#### Step 3: Build for web
```bash
pygbag --build .
```

#### Step 4: Test locally
```bash
python -m http.server 8000
```
Visit: http://localhost:8000

#### Step 5: Deploy to GitHub Pages
1. Create a GitHub repository
2. Push your code to GitHub
3. Go to Settings → Pages
4. Select branch and `/build/web` folder
5. Your game will be live at: `https://yourusername.github.io/repo-name`

**Pros**: Free, unlimited bandwidth, works on mobile browsers
**Cons**: Requires converting to WebAssembly

---

### Option 2: itch.io (Easiest)

**Best for**: Quick deployment with built-in community

#### Steps:
1. Go to https://itch.io
2. Create free account
3. Click "Upload new project"
4. For web version:
   - Use Pygbag to build (see Option 1)
   - Upload the `build/web` folder as a ZIP
   - Set "This file will be played in the browser"
5. For downloadable version:
   - ZIP your entire project folder
   - Upload as downloadable

**Pros**: Easiest, built-in game community, analytics
**Cons**: Less control over hosting

---

### Option 3: Netlify (Alternative to GitHub Pages)

**Best for**: Simple drag-and-drop deployment

#### Steps:
1. Build with Pygbag (see Option 1)
2. Go to https://netlify.com
3. Drag the `build/web` folder to Netlify
4. Get instant URL

**Pros**: Very easy, free SSL, custom domains
**Cons**: Bandwidth limits on free tier

---

## Making it Work on Mobile

### Current Implementation ✅

Your game already has:
- Touch controls that follow finger position
- Tap to shoot functionality
- Automatic switching between keyboard and touch
- Responsive to screen size (fullscreen mode)

### Additional Mobile Optimizations (Optional)

If you want to improve mobile experience further:

1. **Add touch control hints** - Display "Drag to move, Tap to shoot" on mobile
2. **Adjust bullet speed** - May need tweaking for touch controls
3. **Add virtual buttons** - Create visible on-screen buttons for mobile users
4. **Responsive scaling** - Adjust game elements based on screen size

---

## Quick Start Commands

### Test locally:
```bash
source venv/bin/activate
python alien_invasion.py
```

### Build for web:
```bash
pip install pygbag
pygbag --build .
python -m http.server 8000
```

### Deploy to itch.io:
1. Build with Pygbag
2. ZIP the `build/web` folder
3. Upload to itch.io

---

## Troubleshooting

**Game too slow on mobile?**
- The background image is already optimized
- Consider reducing alien count for mobile

**Touch controls not working?**
- Make sure you're using the web version (Pygbag)
- Desktop Pygame doesn't support true touch, only mouse

**Want keyboard-only mode back?**
- Set `ship.touch_control = False` in `ship.py`

---

## Files Modified for Mobile Support

- `ship.py` - Added touch control logic
- `game_functions.py` - Added mouse motion and tap handling
- `background.py` - Optimized image scaling

All changes maintain backward compatibility with keyboard controls!

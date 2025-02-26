# SpinMealDecider 🍽️🎡

**SpinMealDecider** is an automated tool that transforms shared meal menus into interactive spin wheels, using Google Sheets and dub.co for easy decision-making and sharing among flatmates. 📊📈🔗

## Problem Statement ✨

Managing meal choices and making decisions collaboratively can often be a hassle. Our project, **SpinMealDecider**, provides an interactive and fun solution. It automates the creation of meal decision-making spin wheels from a shared Google Sheet, updates dynamic URLs, and uses `dub.co` for easy sharing among flatmates. 🤝📝

### The Dilemma We All Face 🌀

[![Food Selection Meme](https://img.youtube.com/vi/IJqocn5KoKk/0.jpg)](https://www.youtube.com/watch?v=IJqocn5KoKk)

_Choosing what to eat can be tougher than it seems!_

## Proposed Solution 💡

The SpinMealDecider project automates the following processes:

1. **Data Collection:** Read the food menu for each meal (breakfast, lunch, dinner) from a shared Google Sheet. 📄🍳🥗🍛
2. **URL Creation:** Generate dynamic URLs to display these options in a spin-wheel format using [Unfair Spin Wheel](https://unfair.spin-wheel.click). 🔄🌐
3. **URL Shortening:** Use `dub.co` API to shorten these URLs for convenient sharing. 📪✂️

### Solution Architecture 🏗️

```mermaid
graph LR
    A[Google Sheets 📄] -- Fetch Data --> B[GitHub Actions 🤖]
    B -- Generate URLs --> C[Spin Wheel 🎡]
    B -- Update URLs --> D[dub.co 🔗]
    D -- Shortened Links --> E[Shared with Flatmates 👥]

    B --> F[SpinMealDecider Helpers 🔧]
    F --> G[google_sheets_client 📄]
    F --> H[dub_co_client 🔗]
    F --> I[spin_wheel_helper 🎡]
```

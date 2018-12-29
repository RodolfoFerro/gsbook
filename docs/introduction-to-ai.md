---
layout: default
title: Introduciton to AI
nav_order: 2
---

# Introduction to AI

Just the Docs has some specific configuration parameters that can be definied in your Jekyll site's `_config.yml` file.

## What is *Artificial Intelligence*?

```yml
# Enable or disable the site search
search_enabled: true
```

## Historical Perspective

```yml
# Aux links for the upper right navigation
aux_links:
    "Just the Docs on GitHub":
      - "//github.com/pmarsceill/just-the-docs"
```

## Present and Future

```yml
# Color scheme currently only supports "dark" or nil (default)
color_scheme: "dark"
```
<button class="btn js-toggle-dark-mode">Preview dark color scheme</button>

<script>
const toggleDarkMode = document.querySelector('.js-toggle-dark-mode')
const cssFile = document.querySelector('[rel="stylesheet"]')
const originalCssRef = cssFile.getAttribute('href')
const darkModeCssRef = originalCssRef.replace('just-the-docs.css', 'dark-mode-preview.css')

addEvent(toggleDarkMode, 'click', function(){
if (cssFile.getAttribute('href') === originalCssRef) {
cssFile.setAttribute('href', darkModeCssRef)
} else {
cssFile.setAttribute('href', originalCssRef)
}
})
</script>

See [Customization]({{site.baseurl }}{% link docs/customization.md %}) for more information.

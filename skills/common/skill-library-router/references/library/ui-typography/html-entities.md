# HTML Entity & Character Reference

Read this file when you need to look up the correct HTML entity for a character, or when auditing
existing HTML for incorrect character usage.

---

## Quick Substitution Table

When generating HTML/JSX, substitute these characters automatically:

| If you see | Replace with | Entity | Rule |
|------------|-------------|--------|------|
| "straight double" | "curly double" | `"` `"` | Always curly quotes |
| 'straight single' | 'curly single' | `'` `'` | Always curly quotes |
| it's (straight) | it's (curly) | `'` | Apostrophe = closing single quote |
| -- | – | `–` | En dash for ranges |
| --- | — | `—` | Em dash for breaks |
| ... | … | `…` | Single ellipsis character |
| (c) | © | `©` | Real copyright symbol |
| (TM) | ™ | `™` | Real trademark symbol |
| (R) | ® | `®` | Real registered symbol |
| 12 x 34 | 12 × 34 | `×` | Real multiplication sign |
| 56 - 12 (math) | 56 − 12 | `−` | Real minus sign |
| 6' 10" (curly, in measurements) | 6' 10" (straight) | `'` `"` | Foot/inch must be straight |

---

## Complete Entity Table

### Quotes and Apostrophes

```
"   "   U+201C   opening double quote
"   "   U+201D   closing double quote
'   '   U+2018   opening single quote
'   '   U+2019   closing single quote / apostrophe
"    "   U+0022   straight double quote (inch mark only)
'     '   U+0027   straight single quote (foot mark only)
```

### Dashes

```
-              U+002D   hyphen (compound words, line breaks)
–   –   U+2013   en dash (ranges: 1–10, connections: Sarbanes–Oxley)
—   —   U+2014   em dash (sentence breaks—like this)
­          U+00AD   soft/optional hyphen (invisible break suggestion)
```

### Symbols

```
…  …   U+2026   ellipsis
×   ×   U+00D7   multiplication sign
−   −   U+2212   minus sign
÷  ÷   U+00F7   division sign
±  ±   U+00B1   plus-minus sign
©    ©   U+00A9   copyright
™   ™   U+2122   trademark
®     ®   U+00AE   registered trademark
¶    ¶   U+00B6   paragraph mark (pilcrow)
§    §   U+00A7   section mark
&     &   U+0026   ampersand
°     °   U+00B0   degree sign
```

### Spaces

```
          U+00A0   nonbreaking space (prevents line break)
        U+2009   thin space (half word-space width)
          U+2002   en space (half em width)
          U+2003   em space (full em width)
        U+200A   hair space (thinnest space)
```

### Primes (Foot/Inch/Minute/Second)

```
'     '   U+0027   foot mark / minute mark (straight single)
"    "   U+0022   inch mark / second mark (straight double)
′   ′   U+2032   true prime (if font supports — sloped)
″   ″   U+2033   true double prime (if font supports — sloped)
```

### Arrows and Misc

```
←    ←   U+2190   left arrow
→    →   U+2192   right arrow
↑    ↑   U+2191   up arrow
↓    ↓   U+2193   down arrow
•    •   U+2022   bullet
·  ·   U+00B7   middle dot
«   «   U+00AB   left guillemet
»   »   U+00BB   right guillemet
```

---

## Common Accented Characters

Always preserve accents in proper names. These are the most frequently needed:

```
é  é       É  É
è  è       È  È
á  á       Á  Á
à  à       À  À
í  í       Í  Í
ó  ó       Ó  Ó
ú  ú       Ú  Ú
ü    ü       Ü    Ü
ö    ö       Ö    Ö
ç  ç       Ç  Ç
ñ  ñ       Ñ  Ñ
ß   ß       (Eszett — or just use ss)
```

---

## Contextual Usage Patterns

### Quoted Text
```html
<p>&ldquo;She said &lsquo;hello&rsquo; to me,&rdquo; he reported.</p>
```

### Decade Abbreviations (apostrophe pointing down)
```html
<p>In the &rsquo;70s, rock &rsquo;n&rsquo; roll dominated.</p>
```

### Ranges and Connections
```html
<p>Pages 4&ndash;8</p>
<p>The Sarbanes&ndash;Oxley Act</p>
<p>The 2020&ndash;2025 period</p>
```

### Sentence Breaks
```html
<p>The em dash puts a nice pause in text&mdash;and is underused.</p>
```

### Legal/Academic References
```html
<p>Under &sect;&nbsp;1782, the seller may offer a refund.</p>
<p>See &para;&nbsp;49 of the contract.</p>
```

### Copyright and Trademark
```html
<footer>&copy;&nbsp;2025 MegaCorp&trade;</footer>
```

### Measurements
```html
<p>The room is 12&#39;&nbsp;6&quot; &times; 8&#39;&nbsp;10&quot;.</p>
```

### Math
```html
<p>12 &times; 34 &minus; 56 = 352</p>
```

### Ellipsis with Nonbreaking Space
```html
<p>From A&nbsp;&hellip; to Z</p>
```

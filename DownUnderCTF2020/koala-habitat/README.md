# Koala habitat - MISC - 462pts.
## Description
 What an Aussie Banger!
Flag Format:
STRING you end up with after solving challenge --> Spaces seperate the words
NO DUCTF{} required

## Attachments
###### [gumtrees.wav](gumtrees.wav)

## Solution

After playing `gumtrees.wav` i heard a morse code encoded message in the background, so i opened the file with Sonic Visualiser and analyzed it with a spectrogram.

![morsecode](imgs/morsecode.png)

At this point i was able to clearly see the encoded message, so i proceeded to decode it using [this translator](https://morsecode.world/international/translator.html).

The code:
```
-.-. .- .-. .- -- . .-.. .-.. --- / -.- --- .- .-.. .- ... / .- .-. . / - .... . / -... . ... - / -.- --- .- .-.. .- ...
```

Translated morse code:
`CARAMELLO KOALAS ARE THE BEST KOALAS`

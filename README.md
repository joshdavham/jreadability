<div align="center">
    <img src="https://raw.githubusercontent.com/joshdavham/jreadability/0bb50f9ea65b2092dd3fdf2f2193d51cb394fe4d/logo.svg" height="75">
</div>
<br />

<div align="center">
    <i>Text readability calculator for Japanese learners 🇯🇵</i>
</div>

<br />

<div align="center" style="text-decoration: none;">
    <a href="https://pypi.org/project/jreadability/"><img src="https://img.shields.io/pypi/v/jreadability"></a>
    <a href="https://github.com/joshdavham/jreadability/blob/main/LICENSE" style="text-decoration: none;"><img src="https://img.shields.io/badge/License-MIT-brightgreen.svg"></a>
</div>

<br />

jReadability allows python developers to calculate the readability of Japanese text using the model developed by Jae-ho Lee and Yoichiro Hasebe in "[Introducing a readability evaluation system for Japanese language education](https://jreadability.net/file/hasebe-lee-2015-castelj.pdf)." **Note that this is not an official implementation.**


## Installation
```
pip install jreadability
```

## Quickstart
```python
from jreadability import compute_readability

# "Good morning! The weather is nice today."
text = 'おはようございます！今日は天気がいいですね。' 

score = compute_readability(text)

print(score) # 6.438000000000001
```

## Readability scores

| Level              | Readability score range |
|--------------------|-------------------------|
| Upper-advanced     | 0.5-1.4                 |
| Lower-advanced     | 1.5 - 2.4               |
| Upper-intermediate | 2.5 - 3.4               |
| Lower-intermediate | 3.5 - 4.4               |
| Upper-elementary   | 4.5 - 5.4               |
| Lower-elementary   | 5.5 - 6.4               |

Note that this readability calculator is specifically for <u>non-native speakers</u> learning to read Japanese. This is not to be confused with something like grade level or other readability scores meant for native speakers.

### Model

```
readability = {mean number of words per sentence} * -0.056
            + {proportion of kango} * -0.126
            + {proportion of wago} * -0.042
            + {proportion of verbs} * -0.145
            + {proportion of particles} * -0.044
            + 11.724
```

*\* "kango" (漢語) means Japanese word of Chinese origin while "wago" (和語) means native Japanese word.*

#### Note on model consistency

The readability scores produced by this python package tend to differ slightly from the scores produced on the official [jreadability website](https://jreadability.net/sys/en). This is likely due to the version difference in UniDic between these two implementations as this package uses UniDic 2.1.2 while theirs uses UniDic 2.2.0. This issue may be resolved in the future.

## Batch processing

jreadability makes use of [fugashi](https://github.com/polm/fugashi)'s tagger under the hood and initializes a new tagger everytime `compute_retrievability` is invoked. If you are processing a large number of texts, it is recommended to initialize the tagger first on your own, then pass it as an argument to each subsequent `compute_retrievability` call.

```python
from fugashi import Tagger

texts = [...]

tagger = Tagger()

for text in texts:
    
    score = compute_readability(text, tagger) # fast :D
    #score = compute_readability(text) # slow :'(
    ...
```

## Other implementations

The official jReadability implementation can be found on [jreadability.net](https://jreadability.net/)

A node.js implementation can also be found [here](https://github.com/Bennycopter/jreadability).
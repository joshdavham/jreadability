<div align="center">
    <img src="logo.svg" height="75">
</div>

<div align="center">
    Text readability calculator for Japanese learners 🇯🇵
</div>

<br />

<div align="center" style="text-decoration: none;">
    <a href="https://pypi.org/project/jreadability/"><img src="https://img.shields.io/pypi/v/jreadability"></a>
    <a href="https://github.com/joshdavham/jreadability/blob/main/LICENSE" style="text-decoration: none;"><img src="https://img.shields.io/badge/License-MIT-brightgreen.svg"></a>
</div>

<br />

jreadability allows python developers to calculate the readability of Japanese text using the model developed by Jae-ho Lee and Yoichiro Hasebe in "[Readability measurement of Japanese texts based on levelled corpora](https://researchmap.jp/jhlee/published_papers/21426109)." **Note that this is not an official implementation.**


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

print(score) # 5.596333333333334
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

### Equation

$$
\begin{align*}
\textrm{readability} = &\ \{\textrm{mean number of words per sentence}\} \cdot -0.056 \\
&\ + \{\textrm{proportion of kango}\} \cdot -0.126 \\
&\ + \{\textrm{proportion of wago}\} \cdot -0.042 \\
&\ + \{\textrm{proportion of verbs}\} \cdot -0.145 \\
&\ + \{\textrm{proportion of auxiliary verbs}\} \cdot -0.044 \\
&\ + 11.724
\end{align*}
$$

*\* "kango" (漢語) means Japanese word of Chinese origin while "wago" (和語) means native Japanese word.*

---

#### Note on model consistency

The readability scores produced by this python package tend to differ slightly from the scores produced on the official [jreadability website](https://jreadability.net/sys/en). This is likely due to the version difference in UniDic between these two implementations as this package uses UniDic 2.1.2 while theirs uses UniDic 2.2.0. This issue will hopefully be resolved in the future.
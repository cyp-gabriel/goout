[![Contact me on Codementor](https://www.codementor.io/m-badges/boonecabal/im-a-cm-g.svg)](https://www.codementor.io/@boonecabal?refer=badge)

## Notes

```python
cards = response.css('div.schedule-box.small')

title = cards.css('div:nth-of-type(2) > a::text').get().strip()

time = cards.css('div:nth-of-type(2) div.text-truncate > span > time::text').get())
```

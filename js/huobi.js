

## 获取RSI
* 手动选取RSI
* https://www.hbdm.com/zh-cn/contract/exchange/#symbol=BTC&&contract_type=this_week
```

setInterval(function(){
    var rsi =$('span.pane-legend-item-value.pane-legend-line')[12]
    console.log(rsi.textContent)
}, 3000);

```

